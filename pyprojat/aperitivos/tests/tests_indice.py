import pytest
from django.urls import reverse

from pyprojat.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse('aperitivos:indice'))


def test_status_code(resp):
    assert resp.status_code == 200


@pytest.mark.parametrize(
    'titulo',
    [
        'Aula 1: Instalação Windows',
        'Aula 2: Instalação MacOS',
        'Aula 3: Instalação Python Ubuntu'
    ]
)
def test_titulo_video(resp, titulo):
    assert_contains(resp, titulo)


# def test_conteudo_video(resp):
#     assert_contains(resp, '<iframe src="https://player.vimeo.com/video/472243892"')