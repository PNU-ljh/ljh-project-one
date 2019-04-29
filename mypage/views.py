from django.shortcuts import render
from .models import Introduce

# Create your views here.
def content_list(request):
    qs = Introduce.objects.all()

    return render(request, 'content_list.html', {
        'content_list': qs,
    })

def content_detail(request, pk):
    content = Introduce.objects.get(pk=pk)

    return render(request, 'content_detail.html', {
        'content': content,
    })
    