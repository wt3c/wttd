from django.shortcuts import render, get_object_or_404, HttpResponse
from eventex.nucleo.models import Speaker
from eventex.nucleo.models import Talk


def home(request):
    speakers = Speaker.objects.all()
    return render(request, 'index.html', {'speakers': speakers})


def speark_detail(request, slug):
    speaker = get_object_or_404(Speaker, slug=slug)
    return render(request, 'nucleo/speaker_detail.html', {'speaker': speaker})


def talk_list(request):
    context = {
        'morning_talks': Talk.objects.filter(start__lt='12:00'),
        'afternoon_talks': Talk.objects.filter(start__gte='12:00'),
    }
    return render(request, 'nucleo/talk_list.html', context)
