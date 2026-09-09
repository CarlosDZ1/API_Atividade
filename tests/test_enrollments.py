"""Tests for Enrollment endpoints and Relational Queries."""

def test_enroll_user_success(client):
    user_res = client.post("/users", json={"name": "Carlos", "email": "carlos@example.com"})
    user_id = user_res.json()["data"]["id"]

    course_res = client.post("/courses", json={"title": "Data Structures", "workload": 60})
    course_id = course_res.json()["data"]["id"]

    enroll_res = client.post("/enrollments", json={"user_id": user_id, "course_id": course_id})
    assert enroll_res.status_code == 201
    body = enroll_res.json()
    assert body["success"] is True
    assert body["message"] == "Enrollment completed successfully"
    assert body["data"]["user_id"] == user_id
    assert body["data"]["course_id"] == course_id
    assert "enrolled_at" in body["data"]


def test_enroll_duplicate_prevention(client):
    user_res = client.post("/users", json={"name": "Diana", "email": "diana@example.com"})
    user_id = user_res.json()["data"]["id"]

    course_res = client.post("/courses", json={"title": "Algorithms", "workload": 50})
    course_id = course_res.json()["data"]["id"]

    # First enrollment succeeds
    client.post("/enrollments", json={"user_id": user_id, "course_id": course_id})

    # Second enrollment must fail with 409 Conflict
    duplicate_res = client.post("/enrollments", json={"user_id": user_id, "course_id": course_id})
    assert duplicate_res.status_code == 409
    body = duplicate_res.json()
    assert body["success"] is False
    assert "already enrolled" in body["message"]


def test_enroll_nonexistent_user(client):
    course_res = client.post("/courses", json={"title": "Databases", "workload": 40})
    course_id = course_res.json()["data"]["id"]

    res = client.post("/enrollments", json={"user_id": 99999, "course_id": course_id})
    assert res.status_code == 404
    assert res.json()["success"] is False
    assert "User with ID 99999 not found" in res.json()["message"]


def test_enroll_nonexistent_course(client):
    user_res = client.post("/users", json={"name": "Eduardo", "email": "edu@example.com"})
    user_id = user_res.json()["data"]["id"]

    res = client.post("/enrollments", json={"user_id": user_id, "course_id": 99999})
    assert res.status_code == 404
    assert res.json()["success"] is False
    assert "Course with ID 99999 not found" in res.json()["message"]


def test_get_user_courses_relational(client):
    # 1. Create a user
    user_res = client.post("/users", json={"name": "Fernanda", "email": "fernanda@example.com"})
    user_id = user_res.json()["data"]["id"]

    # 2. Create two courses
    course1 = client.post("/courses", json={"title": "Python 101", "workload": 20}).json()["data"]
    course2 = client.post("/courses", json={"title": "FastAPI Pro", "workload": 30}).json()["data"]

    # 3. Enroll user in both courses
    client.post("/enrollments", json={"user_id": user_id, "course_id": course1["id"]})
    client.post("/enrollments", json={"user_id": user_id, "course_id": course2["id"]})

    # 4. Fetch user courses via relational endpoint
    response = client.get(f"/users/{user_id}/courses")
    assert response.status_code == 200
    body = response.json()
    assert body["success"] is True
    assert body["data"]["user"]["id"] == user_id
    assert body["data"]["user"]["email"] == "fernanda@example.com"

    courses_list = body["data"]["courses"]
    assert len(courses_list) == 2
    titles = [c["title"] for c in courses_list]
    assert "Python 101" in titles
    assert "FastAPI Pro" in titles


def test_get_user_courses_empty(client):
    user_res = client.post("/users", json={"name": "Gabriel", "email": "gabriel@example.com"})
    user_id = user_res.json()["data"]["id"]

    response = client.get(f"/users/{user_id}/courses")
    assert response.status_code == 200
    body = response.json()
    assert body["success"] is True
    assert len(body["data"]["courses"]) == 0


def test_get_user_courses_user_not_found(client):
    response = client.get("/users/9999/courses")
    assert response.status_code == 404
    body = response.json()
    assert body["success"] is False
