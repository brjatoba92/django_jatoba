from django.shortcuts import render


def video(request, slug):
    videos = {
        'instalacao-windows': {'titulo': 'Aula 1: Instalação Windows', 'vimeo_id': 473186781},
        'instalacao-macos': {'titulo': 'Aula 2: Instalação MacOS', 'vimeo_id': 473187531},
        'instalacao-ubuntu': {'titulo': 'Aula 3: Instalação Python Ubuntu', 'vimeo_id': 473187848},
    }
    video = videos[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
