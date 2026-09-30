import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

CURATED=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(CURATED))
from manuscript import prepare, resolve_anchor, latex_break, structural_layout, ordered_paths, reference_entries, validate_references
from print_quality import effective_ppi, cover_path
spec=importlib.util.spec_from_file_location('pdf_build',CURATED.parent/'pdf.py')
build=importlib.util.module_from_spec(spec)
spec.loader.exec_module(build)


class ManuscriptTests(unittest.TestCase):
    def test_author_photo_survives_repaired_markdown_path(self):
        legacy = prepare('![Author](../resources/image0133.png)\n\n*Author*\n\nProse.')
        repaired = prepare('![Author](../book-design/curated/assets/art/photo58.jpg)\n\n*Author*\n\nProse.')
        self.assertEqual(legacy[:3], repaired[:3])
        self.assertEqual(repaired[0].count('PHOTO_PLACEHOLDER'), 1)

    def test_hidden_editorial_notes_and_visual_briefs(self):
        text,notes,directions,images=prepare('Before.\n<!-- DRAFT: never print me. -->\n<!-- [VISUAL: a new image] -->\n<!-- DIAGRAM — another brief -->\nAfter.')
        self.assertNotIn('DRAFT',text)
        self.assertNotIn('VISUAL',text)
        self.assertIn('After.',text)
        self.assertEqual(directions,['[VISUAL: a new image]','DIAGRAM — another brief'])

    def test_actual_structural_pages_preserve_headings(self):
        chapters=CURATED.parents[1]/'chapters'
        text=structural_layout((chapters/'part-3-science-turns-inward.md').read_text())
        self.assertIn('# Part III: Science Turns Inward',text)
        self.assertIn('Who changes the arrangement',text)
        self.assertNotIn('\\LARGE',text)
        with self.assertRaises(ValueError):
            structural_layout('```{=latex}\n\\unknown{prose}\n```')

    def test_book_order_includes_every_source_once(self):
        chapters=CURATED.parents[1]/'chapters'
        paths=ordered_paths(chapters,CURATED/'book-order.json')
        self.assertEqual(set(paths),set(chapters.glob('*.md')))
        names=[p.name for p in paths]
        self.assertLess(names.index('05-the-society-of-agents.md'),names.index('reveal-we-call-it-science.md'))
        self.assertLess(names.index('reveal-we-call-it-science.md'),names.index('06-pattern-language.md'))
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory);(root/'a.md').write_text('A')
            manifest=root/'order.json';manifest.write_text('["a.md", "a.md"]')
            with self.assertRaises(ValueError):ordered_paths(root,manifest)
            manifest.write_text('[]')
            with self.assertRaises(ValueError):ordered_paths(root,manifest)

    def test_editing_anchor_never_moves_art_by_guess(self):
        blocks=[{'raw':'An unchanged paragraph.'},{'raw':'The edited passage.'}]
        self.assertEqual(resolve_anchor(blocks,'unchanged paragraph'),0)
        self.assertIsNone(resolve_anchor(blocks,'old passage'))
        self.assertIsNone(resolve_anchor(blocks+blocks,'unchanged paragraph'))
        self.assertIsNone(resolve_anchor(blocks,''))

    def test_notes_and_design_directions_do_not_leak_into_prose(self):
        raw='''# Title

A sentence.[^one]

> [DIAGRAM — a long direction
> continued here.]

## Notes
[^one]: A source.
    With a qualification.

    A second paragraph.
'''
        text,notes,directions,images=prepare(raw)
        self.assertIn('A sentence.[^one]',text)
        self.assertNotIn('DIAGRAM',text)
        self.assertNotIn('## Notes',text)
        self.assertEqual(notes,[('one','A source. With a qualification. A second paragraph.')])
        self.assertEqual(len(directions),1)

    def test_duplicate_footnotes_fail(self):
        with self.assertRaises(ValueError):prepare('[^a]: First\n[^a]: Second')

    def test_central_references_resolve_without_chapter_definitions(self):
        chapters = CURATED.parents[1] / 'chapters'
        entries = reference_entries((chapters / 'appendix-references.md').read_text())
        self.assertTrue(entries)
        validate_references(chapters.glob('*.md'), entries)
        for path in chapters.glob('*.md'):
            self.assertFalse(prepare(path.read_text())[1], path.name)

    def test_reference_errors_fail_before_rendering(self):
        entry = '1. <a id="ref-05-example"></a>A source. Its qualification.\n'
        entries = reference_entries(entry)
        self.assertEqual(entries['ref-05-example'], (1, 'A source. Its qualification.'))
        with self.assertRaises(ValueError):
            reference_entries(entry + entry)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'chapter.md'
            path.write_text('Claim.[1](appendix-references.md#ref-05-example)')
            validate_references([path], entries)
            path.write_text('Claim.[2](appendix-references.md#ref-05-example)')
            with self.assertRaises(ValueError):validate_references([path], entries)
            path.write_text('Claim.[1](appendix-references.md#ref-05-missing)')
            with self.assertRaises(ValueError):validate_references([path], entries)
            path.write_text('No citation.')
            with self.assertRaises(ValueError):validate_references([path], entries)

    def test_body_verification_ignores_superscript_reference_labels(self):
        from verify import citation_fragments
        self.assertEqual(citation_fragments('First.[12](appendix-references.md#ref-05-source) Next.'), ['First.', ' Next.'])
        self.assertEqual(citation_fragments('First.[^source] Next.'), ['First.', ' Next.'])

    def test_reveal_and_interlude_latex_are_layout_only(self):
        self.assertTrue(latex_break('\\clearpage'))
        self.assertTrue(latex_break('\\clearpage\n\\thispagestyle{empty}\n\\vspace*{\\fill}\n\\begin{center}'))
        self.assertFalse(latex_break('\\end{center}'))
        with self.assertRaises(ValueError):latex_break('\\unknown{missing text}')


class PrintQualityTests(unittest.TestCase):
    def test_resolution_uses_pixels_and_placement_not_dpi_tags(self):
        self.assertAlmostEqual(effective_ppi((1024,1536),[0,0,432,648]),170.6666667)
        self.assertEqual(effective_ppi((1800,2700),[0,0,432,648]),300)
        self.assertLess(effective_ppi((1800,2700),[0,0,864,1296]),300)
        with self.assertRaises(ValueError):effective_ppi((100,100),[0,0,0,10])

    def test_enhanced_cover_is_explicit_and_original_is_fallback(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory)
            self.assertEqual(cover_path(1,root),root/'assets/art/cover-001.png')
            (root/'print-assets.json').write_text(json.dumps({'covers':{'cover-001.png':{'file':'assets/print/cover-001.png'}}}))
            self.assertEqual(cover_path(1,root),root/'assets/print/cover-001.png')
            self.assertEqual(cover_path(4,root),root/'assets/art/cover-004.png')


class FreshnessTests(unittest.TestCase):
    def test_unchanged_and_modified_or_missing_pdf(self):
        with tempfile.TemporaryDirectory() as directory:
            pdf=Path(directory)/'proof.pdf';pdf.write_bytes(b'proof')
            report=pdf.parent/'build-report.json';report.write_text('{}')
            inputs={'fingerprint':'first'}
            state={**inputs,'pdf_sha256':build.digest(pdf),'report_sha256':build.digest(report)}
            self.assertTrue(build.fresh(state,inputs,pdf))
            report.write_text('changed')
            self.assertFalse(build.fresh(state,inputs,pdf))
            report.write_text('{}')
            self.assertFalse(build.fresh(state,{'fingerprint':'edited'},pdf))
            pdf.write_bytes(b'corrupted')
            self.assertFalse(build.fresh(state,inputs,pdf))
            pdf.unlink()
            self.assertFalse(build.fresh(state,inputs,pdf))

    def test_snapshot_tracks_manuscript_asset_and_input_removal(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory)
            (root/'chapters').mkdir()
            (root/'book-design/curated/assets').mkdir(parents=True)
            paths=[root/'chapters/01.md',root/'book-design/pdf.py',root/'book-design/requirements-pdf.txt',root/'book-design/curated/assets/art.png']
            for p in paths:p.write_text('one')
            a=build.snapshot(root)['fingerprint']
            paths[0].write_text('two')
            b=build.snapshot(root)['fingerprint']
            self.assertNotEqual(a,b)
            paths[-1].write_text('new art')
            c=build.snapshot(root)['fingerprint']
            self.assertNotEqual(b,c)
            paths[-1].unlink()
            self.assertNotEqual(c,build.snapshot(root)['fingerprint'])


class PublicationTests(unittest.TestCase):
    def test_failed_validation_preserves_previous_pdf(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory);curated=root/'curated';output=root/'output'
            (curated/'assets/fonts').mkdir(parents=True)
            (curated/'art.json').write_text('[]')
            output.mkdir();pdf=output/build.PDF_NAME;pdf.write_bytes(b'previous proof')
            (output/'build-state.json').write_text('{}')
            def fake_render(command,check):
                Path(command[-1]).write_bytes(b'failed candidate')
            with patch.object(build,'ROOT',root), patch.object(build,'CURATED',curated), patch.object(build,'OUTPUT',output), patch.object(build,'snapshot',return_value={'fingerprint':'new','files':{}}), patch.object(build.subprocess,'run',side_effect=fake_render), patch('verify.verify',return_value={'passed':False}), patch.object(sys,'argv',['pdf.py','build']):
                with self.assertRaisesRegex(RuntimeError,'previous published proof retained'):
                    build.main()
            self.assertEqual(pdf.read_bytes(),b'previous proof')
            self.assertEqual((output/'build-state.json').read_text(),'{}')


if __name__=='__main__':unittest.main()
