from fastapi.testclient import TestClient
from app.main import app


class TestApp:
    client = TestClient(app)

    def test_redirect(self):
        response = self.client.get("/")
        assert response.status_code == 200
    
    def test_users(self):
        response = self.client.get("/users")
        assert response.status_code == 200
    
    def test_users_profile(self):
        response = self.client.get("/users/1")
        assert response.status_code == 200
    
    def test_users_random(self):
        response = self.client.get("/users/random")
        assert response.status_code == 200