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
        self.assertEqual(html.count('data-status="diagnosed"'), 9)
        self.assertEqual(html.count('data-status="undiagnosed"'), 3)
        self.assertEqual(html.count('data-status="prediabetes"'), 35)
        self.assertEqual(html.count('data-status="healthy"'), 53)
        
        # Total should be 100
        self.assertEqual(html.count('class="waffle-icon"'), 100)

    def test_waffle_legend_labels(self):
        response = TestClient(app).get("/")
        
        # Verify stats from content.json (hero style)
        self.assertIn("40.1M", response.text)
        self.assertIn("Have diabetes", response.text)
        self.assertIn("27.6%", response.text)
        self.assertIn("Patients are undiagnosed", response.text)
        self.assertIn("115.2M", response.text)
        self.assertIn("Have prediabetes", response.text)
        self.assertIn("178.9M", response.text)
        self.assertIn("People are normal", response.text)

    def test_elderly_callout_presence(self):
        response = TestClient(app).get("/")
        self.assertIn("Among adults over 65, prediabetes rises to 52.1%.", response.text)

    def test_waffle_source_attribution(self):
        response = TestClient(app).get("/")
        
        # Verify source text
        self.assertIn("Source: CDC National Diabetes Statistics Report 2024", response.text)

    def test_accessibility_attributes(self):
        response = TestClient(app).get("/")
        
        # Verify ARIA labels
        self.assertIn('role="img"', response.text)
        self.assertIn('aria-label="Waffle chart showing diabetes statistics: 9% diagnosed, 3% undiagnosed, 35% in the warning zone, and 53% normal."', response.text)
        # Note: aria-hidden="true" removed for stats as they are now hero-style and should be accessible

