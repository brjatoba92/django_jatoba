from django.shortcuts import render

from pyprojat.aperitivos.models import Video

videos = [
    Video(slug='motivacao', titulo='Vídeo Aperitivo: Motivação', vimeo_id='472243892'),
    Video(slug='instalacao-windows', titulo='Aula 1: Instalação Windows', vimeo_id='473186781'),
    Video(slug='instalacao-macos', titulo='Aula 2: Instalação MacOS', vimeo_id='473187531'),
    Video(slug='instalacao-ubuntu', titulo='Aula 3: Instalação Ubuntu', vimeo_id='473187848'),
]

videos_dct = {v.slug: v for v in videos}


def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})


def video(request, slug):
    video = videos_dct[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
