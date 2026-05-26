import unittest
from fastapi.testclient import TestClient
from main import app

class WaffleContentTests(unittest.TestCase):
    def test_waffle_chart_presence_and_structure(self):
        response = TestClient(app).get("/")
        self.assertEqual(response.status_code, 200)
        
        # Verify main containers
        self.assertIn('id="waffle-chart"', response.text)
        self.assertIn('class="waffle-grid"', response.text)
        self.assertIn('class="waffle-scan-bar"', response.text)

    def test_waffle_icons_count(self):
        response = TestClient(app).get("/")
        html = response.text
        
        # Count icons by status
        self.assertEqual(html.count('data-status="diagnosed"'), 11)
        self.assertEqual(html.count('data-status="undiagnosed"'), 5)
        self.assertEqual(html.count('data-status="prediabetes"'), 38)
        self.assertEqual(html.count('data-status="healthy"'), 46)
        
        # Total should be 100
        self.assertEqual(html.count('class="waffle-icon"'), 100)

    def test_waffle_legend_labels(self):
        response = TestClient(app).get("/")
        
        # Verify legend labels from content.json
        self.assertIn("Diagnosed (29.4M)", response.text)
        self.assertIn("Hidden Millions (8.7M)", response.text)
        self.assertIn("The Warning Zone (97.6M)", response.text)
        self.assertIn("Normal (120M)", response.text)

    def test_waffle_source_attribution(self):
        response = TestClient(app).get("/")
        
        # Verify source text
        self.assertIn("Source: CDC National Diabetes Statistics Report 2024", response.text)
        self.assertIn("NCHS Data Brief No. 516", response.text)

    def test_accessibility_attributes(self):
        response = TestClient(app).get("/")
        
        # Verify ARIA labels
        self.assertIn('role="img"', response.text)
        self.assertIn('aria-label="Waffle chart showing diabetes statistics', response.text)
        self.assertIn('aria-hidden="true"', response.text) # For icons and legend dots
