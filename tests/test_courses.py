"""Tests for Course CRUD endpoints and validation rules."""

def test_create_course_success(client):
    payload = {
        "title": "Clean Architecture in Python",
        "description": "Comprehensive course on Clean Architecture and SOLID",
        "workload": 40,
    }
    response = client.post("/courses", json=payload)
    assert response.status_code == 201
    body = response.json()
    assert body["success"] is True
    assert body["message"] == "Course created successfully"
    assert body["data"]["id"] is not None
    assert body["data"]["title"] == payload["title"]
    assert body["data"]["workload"] == 40


def test_create_course_invalid_workload(client):
    payload = {
        "title": "Invalid Workload Course",
        "description": "Zero hours",
        "workload": 0,
    }
    response = client.post("/courses", json=payload)
    assert response.status_code == 422
    body = response.json()
    assert body["success"] is False
    assert body["data"] is None


def test_list_courses(client):
    client.post("/courses", json={"title": "Course 1", "workload": 10})
    client.post("/courses", json={"title": "Course 2", "workload": 20})

    response = client.get("/courses")
    assert response.status_code == 200
    body = response.json()
    assert body["success"] is True
    assert len(body["data"]) == 2


def test_get_course_by_id(client):
    res = client.post("/courses", json={"title": "FastAPI Master", "workload": 30})
    course_id = res.json()["data"]["id"]

    response = client.get(f"/courses/{course_id}")
    assert response.status_code == 200
    body = response.json()
    assert body["success"] is True
    assert body["data"]["id"] == course_id
    assert body["data"]["title"] == "FastAPI Master"


def test_get_course_not_found(client):
    response = client.get("/courses/8888")
    assert response.status_code == 404
    body = response.json()
    assert body["success"] is False


def test_update_course(client):
    res = client.post("/courses", json={"title": "Old Title", "workload": 15})
    course_id = res.json()["data"]["id"]

    response = client.put(
        f"/courses/{course_id}",
        json={"title": "New Title", "description": "Updated description", "workload": 25},
    )
    assert response.status_code == 200
    body = response.json()
    assert body["success"] is True
    assert body["data"]["title"] == "New Title"
    assert body["data"]["workload"] == 25


def test_delete_course(client):
    res = client.post("/courses", json={"title": "To Delete Course", "workload": 5})
    course_id = res.json()["data"]["id"]

    del_res = client.delete(f"/courses/{course_id}")
    assert del_res.status_code == 200
    assert del_res.json()["success"] is True

    get_res = client.get(f"/courses/{course_id}")
    assert get_res.status_code == 404
