"""Focused offline tests for the optional Project 82 OCR adapter."""
import builtins
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from project82_ocr_text_extraction import extract_text


class Tests(unittest.TestCase):
    def test_missing_file_is_reported_before_dependency_loading(self):
        with self.assertRaisesRegex(FileNotFoundError, "Image not found"):
            extract_text("missing-image-2821.png")

    def test_missing_optional_dependency_has_actionable_message(self):
        original_import = builtins.__import__

        def import_without_ocr_dependencies(name, *args, **kwargs):
            if name == "PIL" or name == "pytesseract":
                raise ImportError("simulated missing optional OCR dependency")
            return original_import(name, *args, **kwargs)

        with tempfile.NamedTemporaryFile(suffix=".png") as image_file:
            with patch("builtins.__import__", side_effect=import_without_ocr_dependencies):
                with self.assertRaisesRegex(RuntimeError, "Install Pillow and pytesseract"):
                    extract_text(image_file.name)

    def test_invalid_image_is_not_misreported_as_dependency_error(self):
        try:
            from PIL import UnidentifiedImageError  # noqa: F401
            import pytesseract  # noqa: F401
        except ImportError:
            self.skipTest("Pillow and pytesseract are required for the invalid-image adapter test")

        with tempfile.NamedTemporaryFile(suffix=".png") as image_file:
            image_file.write(b"not a valid image")
            image_file.flush()
            from PIL import UnidentifiedImageError
            with self.assertRaises(UnidentifiedImageError):
                extract_text(image_file.name)


if __name__ == "__main__":
    unittest.main()
