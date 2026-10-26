import unittest
from project70_chunking_embeddings_visualizer import chunk_text, describe_chunks

class TestProject70(unittest.TestCase):
    def test_overlap_and_coverage(self):
        chunks=chunk_text('abcdefghij', 4, 1)
        self.assertEqual(chunks[0].text, 'abcd')
        self.assertEqual(chunks[1].start, 3)
        self.assertEqual(chunks[-1].end, 10)
    def test_invalid_overlap(self):
        with self.assertRaises(ValueError): chunk_text('abc', 3, 3)
    def test_description(self):
        self.assertIn('Chunks: 1', describe_chunks(chunk_text('hello', 10, 0)))

if __name__ == '__main__': unittest.main()
