from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

@login_required
def inbox(request):
    return HttpResponse('Inbox OK')

@login_required
def sent(request):
    return HttpResponse('Enviados OK')

@login_required
def compose(request):
    if request.method == 'POST':
        return HttpResponse('Compose POST OK')
    return HttpResponse('Compose GET OK')

@login_required
def detail(request, pk):
    return HttpResponse(f'Detail OK (id={pk})')
