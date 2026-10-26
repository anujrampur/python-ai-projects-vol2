# Level 7 — Vision AI: Projects 81–85

## Project 81 — Image Captioning Assistant: Model-Ready Starter
**Goal:** Validate an image file and create a clear request for a captioning model. **Run tests:** `python -m unittest test_project81_image_captioning_prep.py -v`. **Limitation:** No model is bundled; an adapter must perform actual caption generation.

## Project 82 — OCR Text Postprocessor
**Goal:** Clean OCR text by normalizing whitespace, retaining line boundaries, or joining wrapped lines. **Run tests:** `python -m unittest test_project82_ocr_text_postprocessor.py -v`. **Limitation:** OCR recognition itself is not included.

## Project 83 — Visual Question Answering Router
**Goal:** Validate an image path and a question before passing them to an injected VQA adapter. **Run tests:** `python -m unittest test_project83_visual_question_router.py -v`. **Limitation:** Answers depend on the external adapter/model and must be checked for errors.

## Project 84 — Document Image Inspector
**Goal:** Inspect basic file metadata and prepare document-image workflows. **Run tests:** `python -m unittest test_project84_document_image_inspector.py -v`. **Limitation:** The filename heuristic does not inspect image pixels, determine document type reliably, or extract text.

## Project 85 — Image Classification Workbench
**Goal:** Validate and rank confidence scores supplied by a classifier. **Run tests:** `python -m unittest test_project85_image_classification_workbench.py -v`. **Limitation:** It ranks supplied scores; it does not infer labels from an image.
