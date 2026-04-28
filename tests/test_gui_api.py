import sys
import os
import json
import asyncio
from fastapi.testclient import TestClient

# Add src to path
sys.path.append(os.path.abspath("src"))

from gui.app import app

client = TestClient(app)

def test_rref():
    response = client.post(
        "/api/process",
        json={"matrix": "[[1, 2], [3, 4]]", "operation": "rref"}
    )
    if response.status_code != 200:
        print(f"Status: {response.status_code}")
        print(f"Response: {response.text}")
    assert response.status_code == 200
    data = response.json()
    print("RREF Result:", data)
    assert "result" in data
    assert "1 & 0" in data["result"]

def test_eigenvals():
    response = client.post(
        "/api/process",
        json={"matrix": "[[2, 0], [0, 3]]", "operation": "eigenvals"}
    )
    assert response.status_code == 200
    data = response.json()
    print("Eigenvals Result:", data)
    assert "result" in data
    assert "2" in data["result"]
    assert "3" in data["result"]

def test_latex_input():
    response = client.post(
        "/api/process",
        json={"matrix": r"\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}", "operation": "det"}
    )
    assert response.status_code == 200
    data = response.json()
    print("Determinant Result:", data)
    assert "result" in data
    assert "1" in data["result"]

def test_repeated_calls():
    # Simulate repeated calls to check consistency (backend side)
    for _ in range(3):
        response = client.post(
            "/api/process",
            json={"matrix": "[[1, 2], [3, 4]]", "operation": "rref"}
        )
        assert response.status_code == 200
        data = response.json()
        assert "result" in data

def test_api_equivalent_repeated():
    for _ in range(3):
        response = client.post(
            "/api/equivalent",
            json={"matrix": "[[1, 0], [0, 1]]"}
        )
        assert response.status_code == 200
        data = response.json()
        assert "category" in data
        assert "properties" in data

if __name__ == "__main__":
    try:
        test_rref()
        test_eigenvals()
        test_latex_input()
        test_repeated_calls()
        test_api_equivalent_repeated()
        print("All tests passed!")
    except AssertionError as e:
        print(f"Assertion failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Tests failed: {e}")
        traceback.print_exc()
        sys.exit(1)
