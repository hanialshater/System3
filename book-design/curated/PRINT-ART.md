# Print artwork derivatives

The original 102 assets remain in `assets/art/`. Thirteen covers/openers started
at 1024 × 1536 pixels, or 170.67 PPI at 6 × 9 inches. The separate 1800 × 2700
Chapter 4 opener and the 88 interior crops already met the placed-size target.

The selected restoration is local Real-ESRGAN animevideov3-x2, run through NCNN
on CPU with 256-pixel tiles and 24-pixel overlap. Final pixels blend 40% of the
restoration with 60% Lanczos interpolation of the original. This deliberately
moderates smoothing and reconstructed detail. No face-replacement model,
prompt-based redrawing, typography replacement or additional sharpening is used.
The result is 2048 × 3072 pixels, or 341.33 PPI at trim size, saved losslessly as
an sRGB PNG. This is upscaled artwork, not newly captured high-resolution detail.

The built-in image editor was tested first, but returned 1024 × 1536 with painted
changes. That result was rejected and is not used by the book. The user explicitly
authorized the dedicated local upscaler instead. No artwork is sent to an external
upscaling service by this workflow.

`print-assets.json` selects accepted covers and records their provenance.
`assets/print/processing-record.json` records each source/output hash, dimensions,
model hashes, runtime, settings and round-trip difference. A small round-trip
difference helps identify drift but is not a substitute for visual review.

## Reproduction

Artwork in `assets/art/`, `assets/print/`, and `../paged/assets/` is tracked
with Git LFS. Install Git LFS before cloning or building on a new machine:

```sh
git lfs install
git lfs pull
```

On macOS, install the client with `brew install git-lfs` first. JSON manifests
and build scripts stay in ordinary Git. Generated proofs and previews under
`output/pdf/` stay outside Git; distribute finished PDFs as release assets.

Use a separate Python environment with `../requirements-upscale.txt`. Ordinary
PDF builds need only the saved derivative PNGs and the normal PDF requirements.

The models come from the official [Real-ESRGAN macOS bundle](https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.5.0/realesrgan-ncnn-vulkan-20220424-macos.zip),
linked from the [project README](https://github.com/xinntao/Real-ESRGAN).
Bundle SHA-256:
`e0ad05580abfeb25f8d8fb55aaf7bedf552c375b5b4d9bd3c8d59764d2cc333a`.
The runtime is the [NCNN Python package](https://pypi.org/project/ncnn/).

From the repository root, with that environment activated and the official model
bundle extracted to a temporary directory:

```sh
python book-design/curated/enhance_covers.py \
  --models /path/to/extracted/models \
  --input book-design/curated/assets/art \
  --output tmp/pdfs/print-candidates
```

Review the candidates before selecting them in `print-assets.json`. Keep the
originals. Do not mistake a DPI metadata tag or interpolation alone for recovered
detail. The PDF renderer preserves these PNGs without another JPEG encoding and
checks all source and embedded placements for the 300-PPI target.

## Printer-dependent work

These are RGB print-resolution masters and a 6 × 9 trim-size proof. Printer
selection still determines bleed, cover/spine geometry, binding allowance,
output profile and any PDF/X requirements. Retain the RGB masters and convert
only from the selected printer's specification. A physical proof remains the
final check for paper, contrast and color.
