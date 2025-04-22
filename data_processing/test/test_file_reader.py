import os
import unittest
import tempfile
import json
from data_processing.src.file_reader import FileReader

class TestFileReader(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.TemporaryDirectory()
        self.file_reader = FileReader(self.test_dir.name)

    def tearDown(self):
        self.test_dir.cleanup()

    def test_read_files_with_valid_json(self):
        valid_data = {"key": "value"}
        valid_file_path = os.path.join(self.test_dir.name, "valid.json")
        with open(valid_file_path, "w") as f:
            json.dump(valid_data, f)

        self.file_reader.read_files()

        self.assertEqual(len(self.file_reader.user_data_parsed), 1)
        self.assertEqual(self.file_reader.user_data_parsed[0], valid_data)
        self.assertEqual(len(self.file_reader.invalid_files), 0)

    def test_read_files_with_invalid_json(self):
        invalid_file_path = os.path.join(self.test_dir.name, "invalid.json")
        with open(invalid_file_path, "w") as f:
            f.write("{invalid_json}")

        self.file_reader.read_files()

        self.assertEqual(len(self.file_reader.user_data_parsed), 0)
        self.assertEqual(len(self.file_reader.invalid_files), 1)
        self.assertIn("invalid.json", self.file_reader.invalid_files)

    def test_read_files_with_partial_fixable_json(self):
        partial_json = '{"key": "value"'
        partial_file_path = os.path.join(self.test_dir.name, "partial.json")
        with open(partial_file_path, "w") as f:
            f.write(partial_json)

        self.file_reader.read_files()

        self.assertEqual(len(self.file_reader.user_data_parsed), 1)
        self.assertEqual(self.file_reader.user_data_parsed[0], {"key": "value"})
        self.assertEqual(len(self.file_reader.invalid_files), 0)

    def test_read_files_with_mixed_files(self):
        valid_data = {"key": "value"}
        valid_file_path = os.path.join(self.test_dir.name, "valid.json")
        with open(valid_file_path, "w") as f:
            json.dump(valid_data, f)

        invalid_file_path = os.path.join(self.test_dir.name, "invalid.json")
        with open(invalid_file_path, "w") as f:
            f.write("{invalid_json}")

        partial_json = '{"key": "value"'
        partial_file_path = os.path.join(self.test_dir.name, "partial.json")
        with open(partial_file_path, "w") as f:
            f.write(partial_json)

        self.file_reader.read_files()

        self.assertEqual(len(self.file_reader.user_data_parsed), 2)
        self.assertEqual(len(self.file_reader.invalid_files), 1)
        self.assertIn("invalid.json", self.file_reader.invalid_files)


    def test_read_files_with_unicode_decode_error(self):
        invalid_encoding_file_path = os.path.join(self.test_dir.name, "invalid_encoding.json")
        with open(invalid_encoding_file_path, "wb") as f:
            f.write(b'\x80\x81\x82')  # Invalid UTF-8 bytes

        self.file_reader.read_files()

        self.assertEqual(len(self.file_reader.user_data_parsed), 0)
        self.assertEqual(len(self.file_reader.invalid_files), 1)
        self.assertIn("invalid_encoding.json", self.file_reader.invalid_files)