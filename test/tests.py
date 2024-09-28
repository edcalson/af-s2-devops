import pytest
from fastapi.testclient import TestClient
from src.main import *  # Supondo que o código esteja no arquivo main.py

client = TestClient(app)


# 1. Teste para a rota GET /helloworld
def test_helloworld():
    response = client.get("/helloworld")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


# 2. Teste para a rota GET /funcaoteste
def test_funcaoteste():
    response = client.get("/funcaoteste")
    assert response.status_code == 200
    data = response.json()
    assert data["teste"] is True
    assert 0 <= data["num_aleatorio"] <= 1000


# 3. Teste para a rota POST /estudantes/cadastro
def test_create_estudante():
    estudante_data = {
        "name": "João",
        "curso": "Engenharia",
        "ativo": True
    }
    response = client.post("/estudantes/cadastro", json=estudante_data)
    assert response.status_code == 200
    assert response.json() == estudante_data


# 4. Teste para a rota PUT /estudantes/update/{id_estudante}
@pytest.mark.parametrize("id_estudante, expected_response", [(1, True), (-1, False)])
def test_update_estudante(id_estudante, expected_response):
    response = client.put(f"/estudantes/update/{id_estudante}")
    assert response.status_code == 200
    assert response.json() == expected_response


# 5. Teste para a rota DELETE /estudantes/delete/{id_estudante}
@pytest.mark.parametrize("id_estudante, expected_response", [(1, True), (-1, False)])
def test_delete_estudante(id_estudante, expected_response):
    response = client.delete(f"/estudantes/delete/{id_estudante}")
    assert response.status_code == 200
    assert response.json() == expected_response
