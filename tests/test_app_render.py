import unittest

from fastapi.testclient import TestClient

from main import app


class AppRenderTests(unittest.TestCase):
    def test_homepage_renders_personal_story(self):
        response = TestClient(app).get("/")

        self.assertEqual(response.status_code, 200)
        self.assertIn("Before it's too late", response.text)
        self.assertIn("personal-story__stats", response.text)
