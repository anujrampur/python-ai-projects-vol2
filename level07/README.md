# Level 7 — Vision AI (Projects 81–85)

These are honest, standard-library-first prototypes that prepare or validate vision workflows. They do **not** claim to run a vision model or OCR engine without one.

- **81 Image Captioning Prep:** validates an image path and exposes an adapter boundary for a real captioning model.
- **82 OCR Text Postprocessor:** cleans text already returned by an OCR engine; no OCR is performed here.
- **83 Visual Question Router:** validates image/question inputs and supports an injected VQA adapter.
- **84 Document Image Inspector:** reports path/extension/size and a filename-based heuristic only; it does not inspect pixels.
- **85 Image Classification Workbench:** ranks caller-provided label confidence scores; it does not classify an image itself.

Run tests from this directory: `python -m unittest discover -v`. Python 3.10+ recommended. No third-party dependencies or API keys are needed for these prototypes.
