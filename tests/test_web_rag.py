import unittest
from fastapi.testclient import TestClient
from app.api import app

class TestWebRAG(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_crawl_and_query(self):
        url = "https://erhatechnologies.com"
        res_crawl = self.client.post("/crawl", json={"url": url, "max_pages": 3})
        self.assertEqual(res_crawl.status_code, 200)
        
        res_query = self.client.post("/query", json={"url": url, "query": "Where is Erha Technologies headquartered?"})
        self.assertEqual(res_query.status_code, 200)
        self.assertIn("Multan", res_query.json()["answer"])

if __name__ == "__main__":
    unittest.main()
