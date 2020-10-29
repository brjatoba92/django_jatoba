from django.shortcuts import render


class Video:
    def __init__(self, slug, titulo, vimeo_id):
        self.slug = slug
        self.titulo = titulo
        self.vimeo_id = vimeo_id


videos = [
        Video('motivacao', 'Vídeo Aperitivo: Motivação', 472243892),
        Video('instalacao-windows', 'Aula 1: Instalação Windows', 473186781),
        Video('instalacao-macos', 'Aula 2: Instalação MacOS', 473187531),
        Video('instalacao-ubuntu', 'Aula 3: Instalação Python Ubuntu', 473187848),
]

videos_dct = {v.slug: v for v in videos}


def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})


def video(request, slug):
    video = videos_dct[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
