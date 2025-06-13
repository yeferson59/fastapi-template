from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "Service is running smoothly" in data["message"]


def test_user_crud_flow():
    # Create a user
    user_data = {
        "email": "testuser@example.com",
        "password": "testpassword",
        "full_name": "Test User",
    }
    response = client.post("/api/v1/users/", json=user_data)
    assert response.status_code == 200
    created_user = response.json()
    assert created_user["email"] == user_data["email"]
    assert created_user["full_name"] == user_data["full_name"]
    assert created_user["is_active"] is True
    assert created_user["is_superuser"] is False
    user_id = created_user["id"]

    # Get user by id
    response = client.get(f"/api/v1/users/{user_id}")
    assert response.status_code == 200
    user = response.json()
    assert user["email"] == user_data["email"]

    # Search user by name
    response = client.get("/api/v1/users/search/Test")
    assert response.status_code == 200
    users = response.json()
    assert any(u["id"] == user_id for u in users)

    # Update user
    update_data = {"full_name": "Updated User", "is_active": False}
    response = client.put(f"/api/v1/users/{user_id}", json=update_data)
    assert response.status_code == 200
    updated_user = response.json()
    assert updated_user["full_name"] == "Updated User"
    assert updated_user["is_active"] is False

    # Delete user
    response = client.delete(f"/api/v1/users/{user_id}")
    assert response.status_code == 200
    deleted_user = response.json()
    assert deleted_user["id"] == user_id

    # Confirm user is deleted
    response = client.get(f"/api/v1/users/{user_id}")
    assert response.status_code == 404
