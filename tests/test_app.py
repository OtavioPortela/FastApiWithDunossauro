from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_root_deve_retornar_ok_e_ola_mundo():
    """Test method get"""
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Ola Mundo!'}


def test_exe2_deve_retornar_html_com_ola_mundo():
    """Test method get"""
    client = TestClient(app)

    response = client.get('/exe2')

    assert response.status_code == HTTPStatus.OK
    assert '<h1>Ola Mundo!</h1>' in response.text
