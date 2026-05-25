import unittest

from fastapi.testclient import TestClient
from main import app


class IcebergContentTests(unittest.TestCase):
    def test_iceberg_data_presence(self):
        response = TestClient(app).get("/")

        self.assertEqual(response.status_code, 200)
        self.assertIn("personal-story__grid", response.text)
        self.assertIn("personal-story__stats", response.text)
        self.assertIn("iceberg-svg", response.text)
        self.assertIn("29.4M", response.text)
        self.assertIn("8.7M", response.text)
        self.assertIn("97.6M", response.text)
        self.assertIn("Undiagnosed", response.text)
        self.assertIn("Prediabetes", response.text)
        self.assertIn("CDC National Diabetes Statistics Report 2024", response.text)
