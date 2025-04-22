import os
import json

class FileReader:
    def __init__(self, user_data_dir):
        self.user_data_dir = user_data_dir
        self.user_data_parsed = []
        self.invalid_files = []

    def read_files(self):
        for file_name in os.listdir(self.user_data_dir):
            file_path = os.path.join(self.user_data_dir, file_name)
            if file_name.endswith('.json'):
                self._process_file(file_name, file_path)

    def _process_file(self, file_name, file_path):
        with open(file_path, 'r') as file:
            try:
                data = json.load(file)
                self.user_data_parsed.append(data)
            except UnicodeDecodeError as e:
                self.invalid_files.append(file_name)
            except json.JSONDecodeError as e:
                try:
                    file.seek(0)
                    invalid_file = file.read()
                    invalid_file += "}"
                    data = json.loads(invalid_file)
                    self.user_data_parsed.append(data)
                except json.JSONDecodeError as e:
                    self.invalid_files.append(file_name)

    def print_summary(self):
        data = len(self.user_data_parsed)
        if data > 0:
            print(f"Valid files count: {data}")

        invalid_files_count = len(self.invalid_files)
        if invalid_files_count > 0:
            print(f"Invalid files count: {invalid_files_count}")

