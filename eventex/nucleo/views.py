from django.shortcuts import render, get_object_or_404
from eventex.nucleo.models import Speaker


def home(request):
    speakers = Speaker.objects.all()
    return render(request, 'index.html', {'speakers': speakers})


def speark_detail(request, slug):
    speaker = get_object_or_404(Speaker, slug=slug)
    return render(request, 'nucleo/speaker_detail.html', {'speaker': speaker})
