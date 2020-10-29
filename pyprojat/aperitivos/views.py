from django.shortcuts import render

videos = [
        {'slug': 'motivacao', 'titulo': 'Vídeo Aperitivo: Motivação', 'vimeo_id': 472243892},
        {'slug': 'instalacao-windows', 'titulo': 'Aula 1: Instalação Windows', 'vimeo_id': 473186781},
        {'slug': 'instalacao-macos', 'titulo': 'Aula 2: Instalação MacOS', 'vimeo_id': 473187531},
        {'slug': 'instalacao-ubuntu', 'titulo': 'Aula 3: Instalação Python Ubuntu', 'vimeo_id': 473187848},
]

videos_dct = {dct['slug']: dct for dct in videos}


def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})


def video(request, slug):
    video = videos_dct[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
