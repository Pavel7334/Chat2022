from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Message


class IndexView(TemplateView):
    template_name = 'chat/index.html'


def room(request, room_name):
    username = request.GET.get('username', 'Anonymous')
    messages = Message.objects.filter(room=room_name)[0:25]

    return render(request, 'chat/room.html', {'room_name': room_name, 'username': username, 'messages': messages})