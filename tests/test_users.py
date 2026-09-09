"""Tests for User CRUD endpoints and validation rules."""

def test_create_user_success(client):
    response = client.post("/users", json={"name": "Alice Silva", "email": "alice@example.com"})
    assert response.status_code == 201
    body = response.json()
    assert body["success"] is True
    assert body["message"] == "User created successfully"
    assert body["data"]["id"] is not None
    assert body["data"]["name"] == "Alice Silva"
    assert body["data"]["email"] == "alice@example.com"
    assert "created_at" in body["data"]


def test_create_user_duplicate_email(client):
    client.post("/users", json={"name": "Alice", "email": "unique@example.com"})
    response = client.post("/users", json={"name": "Bob", "email": "unique@example.com"})
    assert response.status_code == 409
    body = response.json()
    assert body["success"] is False
    assert "already exists" in body["message"]
    assert body["data"] is None


def test_create_user_invalid_email(client):
    response = client.post("/users", json={"name": "Alice", "email": "invalid-email"})
    assert response.status_code == 422
    body = response.json()
    assert body["success"] is False
    assert body["data"] is None


def test_list_users(client):
    client.post("/users", json={"name": "User 1", "email": "u1@example.com"})
    client.post("/users", json={"name": "User 2", "email": "u2@example.com"})

    response = client.get("/users")
    assert response.status_code == 200
    body = response.json()
    assert body["success"] is True
    assert len(body["data"]) == 2


def test_get_user_by_id(client):
    create_res = client.post("/users", json={"name": "Charlie", "email": "charlie@example.com"})
    user_id = create_res.json()["data"]["id"]

    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    body = response.json()
    assert body["success"] is True
    assert body["data"]["id"] == user_id
    assert body["data"]["name"] == "Charlie"


def test_get_user_not_found(client):
    response = client.get("/users/9999")
    assert response.status_code == 404
    body = response.json()
    assert body["success"] is False
    assert "not found" in body["message"]


def test_update_user(client):
    create_res = client.post("/users", json={"name": "Old Name", "email": "old@example.com"})
    user_id = create_res.json()["data"]["id"]

    response = client.put(f"/users/{user_id}", json={"name": "New Name", "email": "new@example.com"})
    assert response.status_code == 200
    body = response.json()
    assert body["success"] is True
    assert body["data"]["name"] == "New Name"
    assert body["data"]["email"] == "new@example.com"


def test_update_user_duplicate_email(client):
    client.post("/users", json={"name": "User A", "email": "usera@example.com"})
    user_b = client.post("/users", json={"name": "User B", "email": "userb@example.com"}).json()["data"]

    response = client.put(f"/users/{user_b['id']}", json={"name": "User B", "email": "usera@example.com"})
    assert response.status_code == 409
    body = response.json()
    assert body["success"] is False
    assert "already in use" in body["message"]


def test_delete_user(client):
    create_res = client.post("/users", json={"name": "To Delete", "email": "delete@example.com"})
    user_id = create_res.json()["data"]["id"]

    del_res = client.delete(f"/users/{user_id}")
    assert del_res.status_code == 200
    assert del_res.json()["success"] is True

    get_res = client.get(f"/users/{user_id}")
    assert get_res.status_code == 404
