import re

from datetime import datetime

valid_name = r"^[A-Za-z]+(?: [A-Za-z]+)*$"  # Allow letters and spaces
valid_email = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"  # Allow @ seperated followed by domain
valid_uuid = (
    r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$"  # UUID v4
)


class DataProcessor:
    def __init__(self, data):
        self.data = data
        self._normalize_data()

    def _normalize_data(self):
        for entry in self.data:
            self._normalize_entry(entry)

    def _normalize_entry(self, entry):
        if (
            "user_id" in entry
            and entry["user_id"] != None
            and not re.match(valid_uuid, entry["user_id"])
        ):
            entry["user_id"] = None

        if "name" in entry and not re.match(valid_name, entry["name"]):
            entry["name"] = None

        if "email" in entry and not re.match(valid_email, entry["email"]):
            entry["email"] = None

        if "instagram_handle" in entry and not self._is_valid_handle(
            entry["instagram_handle"]
        ):
            entry["instagram_handle"] = None

        if "tiktok_handle" in entry and not self._is_valid_handle(
            entry["tiktok_handle"]
        ):
            entry["tiktok_handle"] = None

        if "joined_at" in entry and not self._is_valid_date(entry["joined_at"]):
            entry["joined_at"] = None

        if "advocacy_programs" in entry:
            for advocacy_program in entry["advocacy_programs"]:
                self._normalize_advocacy_programs(advocacy_program)

    def _normalize_advocacy_programs(self, advocacy_program):
        if "brand" in advocacy_program and not str(advocacy_program["brand"]).isalnum():
            advocacy_program["brand"] = None
        if "program_id" in advocacy_program and not re.match(
            valid_uuid, advocacy_program["program_id"]
        ):
            advocacy_program["program_id"] = None
        if (
            "total_sales_attributed" in advocacy_program
            and not isinstance(advocacy_program["total_sales_attributed"], float)
            or advocacy_program["total_sales_attributed"] < 0
        ):
            advocacy_program["total_sales_attributed"] = 0.0

        if "tasks_completed" in advocacy_program:
            for completed_task in advocacy_program["tasks_completed"]:
                self._normalize_tasks_completed(completed_task)

    def _normalize_tasks_completed(self, completed_task):
        for field in ["likes", "shares", "reach", "comments"]:
            if field in completed_task and (
                not isinstance(completed_task[field], int) or completed_task[field] < 0
            ):
                completed_task[field] = 0
        if (
            "brand" in completed_task
            and completed_task["brand"] not in ["TikTok", "Instagram"]
        ):
            completed_task["brand"] = None

    def _is_valid_handle(self, handle):
        return (
            isinstance(handle, str) and 30 > len(handle) > 3 and handle.startswith("@")
        )

    def _is_valid_date(self, date_str):
        try:
            datetime.fromisoformat(date_str)
            return True
        except ValueError:
            return False
