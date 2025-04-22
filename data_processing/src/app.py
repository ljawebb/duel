import os

from data_processor import DataProcessor
from file_reader import FileReader
from flask import Flask


app = Flask(__name__)


@app.route("/")
def raw_data():
    return data_processor.data


@app.route("/user/<user_id>")
def user_data_by_id(user_id):
    user_records = [
        record for record in data_processor.data if record.get("user_id") == user_id
    ]
    return user_records if user_records else "User not found"


@app.route("/top_users")
def user_data():
    top_users = sorted(
        data_processor.data,
        key=lambda x: sum(program['total_sales_attributed'] for program in x['advocacy_programs']),
        reverse=True,
    )[:10]
    return top_users



if __name__ == "__main__":
    user_data_dir = os.path.join(os.path.dirname(__file__), "../user_data")
    file_reader = FileReader(user_data_dir)

    file_reader.read_files()
    file_reader.print_summary()

    data_processor = DataProcessor(file_reader.user_data_parsed)

    app.run(host='0.0.0.0', port=5000, debug=True)
