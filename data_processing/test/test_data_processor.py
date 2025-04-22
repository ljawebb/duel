import unittest
from data_processing.src.data_processor import DataProcessor


class TestDataProcessor(unittest.TestCase):
    def test_normalize_name(self):
        data = [{"name": "John Doe"}, {"name": "Invalid123"}, {"name": ""}]
        processor = DataProcessor(data)
        self.assertEqual(processor.data[0]["name"], "John Doe")
        self.assertIsNone(processor.data[1]["name"])
        self.assertIsNone(processor.data[2]["name"])

    def test_normalize_email(self):
        data = [
            {"email": "valid@example.com"},
            {"email": "invalid-email"},
            {"email": ""},
        ]
        processor = DataProcessor(data)
        self.assertEqual(processor.data[0]["email"], "valid@example.com")
        self.assertIsNone(processor.data[1]["email"])
        self.assertIsNone(processor.data[2]["email"])

    def test_normalize_handles(self):
        data = [
            {"instagram_handle": "@validhandle", "tiktok_handle": "@validhandle2"},
            {"instagram_handle": "invalidhandle", "tiktok_handle": "@sh"},
            {"instagram_handle": "", "tiktok_handle": None},
        ]
        processor = DataProcessor(data)
        self.assertEqual(processor.data[0]["instagram_handle"], "@validhandle")
        self.assertEqual(processor.data[0]["tiktok_handle"], "@validhandle2")
        self.assertIsNone(processor.data[1]["instagram_handle"])
        self.assertIsNone(processor.data[1]["tiktok_handle"])
        self.assertIsNone(processor.data[2]["instagram_handle"])
        self.assertIsNone(processor.data[2]["tiktok_handle"])

    def test_normalize_joined_at(self):
        data = [
            {"joined_at": "2023-01-01T12:00:00"},
            {"joined_at": "2024-10-02T08:12:55.806Z"},
            {"joined_at": "invalid-date"},
            {"joined_at": ""},
        ]
        processor = DataProcessor(data)
        self.assertEqual(processor.data[0]["joined_at"], "2023-01-01T12:00:00")
        self.assertEqual(processor.data[1]["joined_at"], "2024-10-02T08:12:55.806Z")
        self.assertIsNone(processor.data[2]["joined_at"])
        self.assertIsNone(processor.data[3]["joined_at"])

    def test_normalize_user_id(self):
        data = [
            {"user_id": "123e4567-e89b-12d3-a456-426614174000"},
            {"user_id": "invalid-uuid"},
            {"user_id": ""},
        ]
        processor = DataProcessor(data)
        self.assertEqual(
            processor.data[0]["user_id"], "123e4567-e89b-12d3-a456-426614174000"
        )
        self.assertIsNone(processor.data[1]["user_id"])
        self.assertIsNone(processor.data[2]["user_id"])

    def test_normalize_advocacy_programs(self):
        data = [
            {
                "advocacy_programs": [
                    {
                        "brand": "Brand123",
                        "program_id": "123e4567-e89b-12d3-a456-426614174000",
                        "total_sales_attributed": 100.0,
                    },
                    {
                        "brand": "Invalid Brand!",
                        "program_id": "invalid-uuid",
                        "total_sales_attributed": "invalid",
                    },
                ]
            },
            {
                "advocacy_programs": [
                    {"brand": "", "program_id": "", "total_sales_attributed": -50.0}
                ]
            },
        ]
        processor = DataProcessor(data)
        self.assertEqual(processor.data[0]["advocacy_programs"][0]["brand"], "Brand123")
        self.assertEqual(
            processor.data[0]["advocacy_programs"][0]["program_id"],
            "123e4567-e89b-12d3-a456-426614174000",
        )
        self.assertEqual(
            processor.data[0]["advocacy_programs"][0]["total_sales_attributed"], 100.0
        )
        self.assertIsNone(processor.data[0]["advocacy_programs"][1]["brand"])
        self.assertIsNone(processor.data[0]["advocacy_programs"][1]["program_id"])
        self.assertEqual(
            processor.data[0]["advocacy_programs"][1]["total_sales_attributed"], 0.0
        )
        self.assertIsNone(processor.data[1]["advocacy_programs"][0]["brand"])
        self.assertIsNone(processor.data[1]["advocacy_programs"][0]["program_id"])
        self.assertEqual(
            processor.data[1]["advocacy_programs"][0]["total_sales_attributed"], 0.0
        )

    def test_normalize_tasks_completed(self):
        data = [
            {
                "advocacy_programs": [
                    {
                        "total_sales_attributed": 100.0,
                        "tasks_completed": [
                            {"likes": 10, "shares": 5, "reach": 100, "comments": 20, "brand": "TikTok"},
                            {"likes": -1, "shares": "invalid", "reach": None, "comments": 0, "brand": "Instagram"},
                            {"likes": 15, "shares": 10, "reach": 200, "comments": 30, "brand": "InvalidBrand"},
                        ]
                    }
                ]
            }
        ]
        processor = DataProcessor(data)
        self.assertEqual(processor.data[0]["advocacy_programs"][0]["tasks_completed"][0]["likes"], 10)
        self.assertEqual(processor.data[0]["advocacy_programs"][0]["tasks_completed"][0]["shares"], 5)
        self.assertEqual(processor.data[0]["advocacy_programs"][0]["tasks_completed"][0]["reach"], 100)
        self.assertEqual(processor.data[0]["advocacy_programs"][0]["tasks_completed"][0]["comments"], 20)
        self.assertEqual(processor.data[0]["advocacy_programs"][0]["tasks_completed"][0]["brand"], "TikTok")

        self.assertEqual(processor.data[0]["advocacy_programs"][0]["tasks_completed"][1]["likes"], 0)
        self.assertEqual(processor.data[0]["advocacy_programs"][0]["tasks_completed"][1]["shares"], 0)
        self.assertEqual(processor.data[0]["advocacy_programs"][0]["tasks_completed"][1]["reach"], 0)
        self.assertEqual(processor.data[0]["advocacy_programs"][0]["tasks_completed"][1]["comments"], 0)
        self.assertEqual(processor.data[0]["advocacy_programs"][0]["tasks_completed"][1]["brand"], "Instagram")

        self.assertEqual(processor.data[0]["advocacy_programs"][0]["tasks_completed"][2]["likes"], 15)
        self.assertEqual(processor.data[0]["advocacy_programs"][0]["tasks_completed"][2]["shares"], 10)
        self.assertEqual(processor.data[0]["advocacy_programs"][0]["tasks_completed"][2]["reach"], 200)
        self.assertEqual(processor.data[0]["advocacy_programs"][0]["tasks_completed"][2]["comments"], 30)
        self.assertIsNone(processor.data[0]["advocacy_programs"][0]["tasks_completed"][2]["brand"])

if __name__ == "__main__":
    unittest.main()
