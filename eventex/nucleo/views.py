from django.shortcuts import render, get_object_or_404, HttpResponse

from eventex.nucleo.models import Course
from eventex.nucleo.models import Speaker
from eventex.nucleo.models import Talk


def home(request):
    speakers = Speaker.objects.all()
    return render(request, 'index.html', {'speakers': speakers})


def speark_detail(request, slug):
    speaker = get_object_or_404(Speaker, slug=slug)
    return render(request, 'nucleo/speaker_detail.html', {'speaker': speaker})


def talk_list(request):
    speaker = Speaker(name='Henrique Bastos', slug='henrique-bastos')
    courses = [
        dict(title='Título do Curso',
             start='09:00',
             description='Descrição do curso.',
             speaker={'all': [speaker]})
    ]

    context = {
        'morning_talks': Talk.objects.at_morning(),
        'afternoon_talks': Talk.objects.at_afternoon(),
        'courses': Course.objects.all()
    }
    return render(request, 'nucleo/talk_list.html', context)
