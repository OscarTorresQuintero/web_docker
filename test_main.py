from sample_app import app

def test_ejemplo():
    assert 1 + 1 == 2

def test_ruta_index():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
