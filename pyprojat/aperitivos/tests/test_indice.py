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
        'Vídeo Aperitivo: Motivação',
        'Aula 1: Instalação Windows',
        'Aula 2: Instalação MacOS',
        'Aula 3: Instalação Ubuntu'
    ]
)
def test_titulo_video(resp, titulo):
    assert_contains(resp, titulo)


@pytest.mark.parametrize(
    'slug',
    [
        'motivacao',
        'instalacao-windows',
        'instalacao-macos',
        'instalacao-ubuntu'
    ]
)
def test_link_video(resp, slug):
    video_link = reverse('aperitivos:video', args=(slug,))
    assert_contains(resp, f'href="{video_link}"')
