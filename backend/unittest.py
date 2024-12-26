import unittest
from fastapi.testclient import TestClient
from app.main import app


class TestFastAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up the test client before running tests."""
        cls.client = TestClient(app)

    def test_create_student(self):
        """Test creating a new student."""
        response = self.client.post(
            "/api/students/", json={"full_name": "John Doe", "date_of_birth": "2000-01-01", "gender": "Male"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("id", response.json())

    def test_read_student(self):
        """Test retrieving a student by ID."""
        # Create a student first
        create_response = self.client.post(
            "/api/students/", json={"full_name": "Jane Doe", "date_of_birth": "1999-05-15", "gender": "Female"}
        )
        student_id = create_response.json()["id"]

        # Retrieve the student
        response = self.client.get(f"/api/students/{student_id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["full_name"], "Jane Doe")

    def test_create_subject(self):
        """Test creating a new subject."""
        response = self.client.post("/api/subjects/", json={"name": "Mathematics"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("id", response.json())

    def test_read_subject(self):
        """Test retrieving a subject by ID."""
        # Create a subject first
        create_response = self.client.post("/api/subjects/", json={"name": "Physics"})
        subject_id = create_response.json()["id"]

        # Retrieve the subject
        response = self.client.get(f"/api/subjects/{subject_id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["name"], "Physics")

    def test_create_score(self):
        """Test creating a score for a student in a subject."""
        # Create a student
        student_response = self.client.post(
            "/api/students/", json={"full_name": "Alex Smith", "date_of_birth": "2002-03-10", "gender": "Male"}
        )
        student_id = student_response.json()["id"]

        # Create a subject
        subject_response = self.client.post("/api/subjects/", json={"name": "Chemistry"})
        subject_id = subject_response.json()["id"]

        # Create a score
        response = self.client.post(
            "/api/scores/", json={"student_id": student_id, "subject_id": subject_id, "score": 85.5}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("id", response.json())

    def test_read_score(self):
        """Test retrieving a score by ID."""
        # Create a student
        student_response = self.client.post(
            "/api/students/", json={"full_name": "Emily White", "date_of_birth": "2001-07-22", "gender": "Female"}
        )
        student_id = student_response.json()["id"]

        # Create a subject
        subject_response = self.client.post("/api/subjects/", json={"name": "English"})
        subject_id = subject_response.json()["id"]

        # Create a score
        score_response = self.client.post(
            "/api/scores/", json={"student_id": student_id, "subject_id": subject_id, "score": 92.3}
        )
        score_id = score_response.json()["id"]

        # Retrieve the score
        response = self.client.get(f"/api/scores/{score_id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["score"], 92.3)


if __name__ == "__main__":
    unittest.main()
