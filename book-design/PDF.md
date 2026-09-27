# Curated PDF builds

The current manuscript lives in `chapters/`. The supplied curated 6×9 edition is the visual baseline: cream paper, embedded Nimbus Roman at 11.5/15 pt, mirrored margins, illustrated covers and selected interior art. Editing a chapter does **not** start a build.

For the Chapter 5 experiment with flexible text masks, transparent cutouts and immersive edge crops, use the separate [Paged.js proof workflow](paged/README.md). It preserves the original full-image opener and produces a chapter PDF and an interactive mask/spread preview without replacing the full-book output.

## Normal workflow

After manuscript or design edits, ask Codex **“build the book PDF”**, or run these commands from the repository root:

```sh
.venv-pdf/bin/python book-design/pdf.py status
.venv-pdf/bin/python book-design/pdf.py build --preview
```

`status` reads inputs without building. `build` compares the manuscript, renderer, design settings, assets and dependency versions against the last successful build. Unchanged inputs and an intact PDF skip typesetting. `--force` deliberately rebuilds. `--preview` renders contact sheets of every page and larger section samples for review.

The latest successful output is `output/pdf/System3_Curated_6x9.pdf`. Its companion `build-report.json` contains text/layout checks, artwork requiring attention, outstanding visual directions, the included manuscript files and section page numbers. `build-state.json` records input hashes and the output checksum. Generated proofs, previews, temporary files and the Python environment are ignored by Git; manuscript, build code, fonts and reusable artwork belong in Git.

A failed build retains the previous published PDF. Diagnostic output stays in `tmp/pdfs/build-*`. Concurrent builds are refused; editing inputs during a build prevents that candidate from replacing the previous proof.

## One-time setup on a new machine

Use Python 3.11 or newer (the GitHub job uses 3.12):

```sh
git lfs install
git lfs pull
python3 -m venv .venv-pdf
.venv-pdf/bin/python -m pip install -r book-design/requirements-pdf.txt
```

The assets have already been imported. Ordinary builds do not need the Downloads folder, the original placement PDF, page-image ZIP or network access. Font licenses are retained in `book-design/curated/assets/fonts/`.

For a deliberate re-import, first move the existing `assets/` directory aside, then run:

```sh
.venv-pdf/bin/python book-design/curated/import_assets.py \
  /path/to/System3_Curated_Reproduction.zip \
  /path/to/System3_Curated_6x9.pdf
```

Re-importing resets `art.json`, `layout.json` and provenance, so preserve any subsequent art-placement edits. The importer reads selected files; it never executes code from the ZIP. It extracts 88 selected interior crops, 14 covers and fonts. Crops are opaque RGB at 300 dpi, stored as high-quality JPEG; the original supplied archives remain the masters. Chapter 4's composed exercise cover is recovered from the supplied proof. The other covers retain their PNG masters. `provenance.json` records checksums of the supplied inputs.

## Artwork follows passages, not page numbers

`book-design/curated/art.json` associates each illustration with a chapter (or an explicit `section` filename for structural pages) and a unique text passage in `after`. Punctuation/formatting changes are normalized; an exact, unique passage match is required. Artwork follows that passage when pagination changes. A removed or ambiguous anchor omits the image and produces a review entry. There is no proportional or fuzzy placement fallback.

To reconnect an image after editing, inspect the artwork and the chapter, then set its `after` value to a distinctive phrase from the appropriate current passage. Rebuild and inspect the resulting page. Historic `source_page` values identify the original asset and its visual treatment; they never pin it to an output page.

An illustrated cover is reused only while the manuscript title matches its recorded source title. A title change uses a text opening and flags the old cover. Update the cover master and its `source_titles` entry in `provenance.json` together after visual review.

`[VISUAL ...]` and `[DIAGRAM ...]` production directions remain in the manuscript and appear in the report, never in the reading PDF. They are design work still to do, not newly generated images. The legacy inline image references are reported; the curated selection supplies the existing illustrations. A new standalone image needs an explicit art entry and reviewed placement.

Use `build --strict-art` to stop publication of a new proof if existing anchors or covers need attention. This option does not claim that every new visual-design direction has been fulfilled; review those separately in the report.

## Book order and validation

`curated/book-order.json` explicitly lists the complete reading order, including part openings, the science reveal, the institutional-failure interlude, the alternative-ending divider and the evidence appendix. `14-scaffolds.md` is a centered closing interlude, not a fourteenth numbered chapter. Missing, duplicate or unlisted Markdown files cause an error so additions cannot silently disappear.

Footnotes are kept in chapter-specific namespaces and collected at the end. Undefined or duplicate notes fail. The manuscript's known raw-LaTeX page breaks are interpreted as layout, including Chapter 5's reveal; unsupported raw LaTeX fails instead of becoming printed code.

Before replacing the previous proof, the build checks every expected prose/code/note block against extracted text, 6×9 page size, page bounds, live font embedding, bookmarks and artwork/text intersections. These mechanical checks complement visual review; inspect contact sheets and full-size pages around changed passages before sharing a proof. This is a reading edition. Printer-specific bleed, binding and a physical proof remain a separate production pass.

### Print artwork quality

The build also checks both source assets and embedded PDF images at their actual placed size, requiring 300 pixels per inch (with a 1 PPI raster-rounding tolerance). Changing a file's DPI metadata cannot satisfy this check. Results are included in `build-report.json` under `verification.print_quality`.

`curated/print-assets.json` selects reviewed print derivatives for covers; `assets/art/` retains the originals. Upscaled derivatives must record their source dimensions and processing method. More output pixels do not establish that detail was captured at that resolution: inspect faces, lettering and painted texture against the original.

PDF assembly embeds cover PNGs and composited interior art losslessly, avoiding another JPEG generation. Original JPEG interiors remain lossy source assets; lossless embedding does not undo their existing compression.

With no printer selected, these are RGB artwork masters and a trim-size proof. A printer-specific bleed layout, output profile, cover spread/spine and physical proof are still required before claiming press approval. Do not apply an arbitrary CMYK conversion to the masters.

```sh
.venv-pdf/bin/python -m unittest discover -s book-design/curated/tests -v
```

## Manual GitHub build

After these build files and assets are committed and pushed, open **Actions → Build curated book PDF (manual) → Run workflow**, choosing the desired branch. The action installs pinned dependencies, restores a previous proof when available, runs safeguards, builds only when needed, and uploads the PDF, report and previews as one artifact. Optional inputs force rebuilding or require resolved artwork anchors.

The workflow runs only when explicitly dispatched. It has read-only repository permissions and never commits generated files back to `main`. It replaces the previous automatic Pandoc PDF workflow. The older `book-design/render.py` remains available for draft layout experiments; the curated flow above is the full-book build.
