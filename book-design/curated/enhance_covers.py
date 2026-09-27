"""Conservative local 2x restoration of existing illustrated covers.

Requires the separately installed ncnn runtime and the official Real-ESRGAN
animevideov3-x2 model. No API calls, prompt-based redrawing or face replacement.
Outputs derivatives only; the original artwork is never overwritten.
"""
import argparse
import hashlib
import json
import time
from pathlib import Path

import ncnn
import numpy as np
from PIL import Image, ImageCms


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def upscale(image, net, tile=256, pad=24):
    source = np.asarray(image.convert('RGB'), dtype=np.float32) / 255
    height, width = source.shape[:2]
    output = np.empty((height * 2, width * 2, 3), dtype=np.float32)
    for y in range(0, height, tile):
        for x in range(0, width, tile):
            x1, y1 = min(x + tile, width), min(y + tile, height)
            left, top = max(x - pad, 0), max(y - pad, 0)
            right, bottom = min(x1 + pad, width), min(y1 + pad, height)
            pixels = np.ascontiguousarray(source[top:bottom, left:right].transpose(2, 0, 1))
            with net.create_extractor() as extractor:
                code = extractor.input('data', ncnn.Mat(pixels).clone())
                if code != 0:
                    raise RuntimeError(f'NCNN input failed: {code}')
                code, result = extractor.extract('output')
                if code != 0:
                    raise RuntimeError(f'NCNN output failed: {code}')
                enhanced = np.array(result).transpose(1, 2, 0)
                expected = ((bottom - top) * 2, (right - left) * 2, 3)
                if enhanced.shape != expected:
                    raise RuntimeError(f'Unexpected model shape {enhanced.shape}, expected {expected}')
                output[y*2:y1*2, x*2:x1*2] = enhanced[(y-top)*2:(y1-top)*2, (x-left)*2:(x1-left)*2]
        print(f'  rows {min(y+tile,height)}/{height}', flush=True)
    return Image.fromarray(np.round(np.clip(output, 0, 1) * 255).astype(np.uint8))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--models', type=Path, required=True)
    parser.add_argument('--input', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--strength', type=float, default=0.4)
    parser.add_argument('--threads', type=int, default=4)
    args = parser.parse_args()
    if not 0 <= args.strength <= 1:
        parser.error('strength must be between zero and one')
    param = args.models / 'realesr-animevideov3-x2.param'
    weights = args.models / 'realesr-animevideov3-x2.bin'
    net = ncnn.Net()
    net.opt.use_vulkan_compute = False
    net.opt.num_threads = args.threads
    if net.load_param(str(param)) or net.load_model(str(weights)):
        raise RuntimeError('Cannot load official model')
    args.output.mkdir(parents=True, exist_ok=True)
    files = sorted(args.input.glob('cover-*.png')) if args.input.is_dir() else [args.input]
    profile = ImageCms.ImageCmsProfile(ImageCms.createProfile('sRGB')).tobytes()
    records = []
    for path in files:
        with Image.open(path) as im:
            image = im.convert('RGB')
        if image.width >= 1800 and image.height >= 2700:
            continue
        destination = args.output / path.name
        if destination.resolve() == path.resolve():
            raise RuntimeError('Refusing to overwrite an original')
        start = time.monotonic()
        print(path.name, image.size, flush=True)
        restored = upscale(image, net)
        baseline = image.resize(restored.size, Image.Resampling.LANCZOS)
        # The original interpolation supplies most of the texture and geometry.
        # A mild learned residual improves edge definition without a full redraw.
        final = Image.blend(baseline, restored, args.strength)
        final.save(destination, icc_profile=profile,
                   dpi=(final.width/6, final.height/9), compress_level=6)
        reduced = final.resize(image.size, Image.Resampling.LANCZOS)
        error = float(np.abs(np.asarray(reduced,dtype=float)-np.asarray(image,dtype=float)).mean())
        record = dict(source=str(path), source_sha256=sha(path), source_pixels=list(image.size),
                      output=str(destination), output_sha256=sha(destination), pixels=list(final.size),
                      model='realesr-animevideov3-x2', model_sha256=sha(weights),
                      param_sha256=sha(param), ncnn_version=ncnn.__version__,
                      method='2x NCNN CPU restoration blended with original Lanczos interpolation',
                      restoration_strength=args.strength, tile=256, halo=24,
                      color_profile='sRGB', downsample_mean_absolute_error_255=round(error,4),
                      elapsed_seconds=round(time.monotonic()-start,1))
        records.append(record)
        (args.output/'processing-record.json').write_text(json.dumps(records,indent=2)+'\n')
        print(f'  saved {final.size}; round-trip error {error:.3f}/255; {record["elapsed_seconds"]} sec',flush=True)


if __name__ == '__main__':
    main()
