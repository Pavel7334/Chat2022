from django.views.generic import TemplateView, FormView

from .forms import RoomNameForm
from .models import Message
from .utils import slugify


class IndexView(FormView):
    """Отображение главной страницы"""

    template_name = 'chat/index.html'
    form_class = RoomNameForm

    def get_redirect_url(self):
        room_name = slugify(self.request.POST.get('room_name'))
        username = self.request.POST.get('username')
        redirect_to = f'{room_name}/?username={username}'
        return redirect_to

    def get_success_url(self):
        url = self.get_redirect_url()
        return url


class RoomView(TemplateView):
    """Чат комната"""

    template_name = 'chat/room.html'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['messages'] = Message.objects.filter(room=kwargs['room_name'])
        context['username'] = request.GET.get('username', 'Anonymous')
        return self.render_to_response(context)

