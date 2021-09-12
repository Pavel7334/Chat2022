from django import forms


class RoomNameForm(forms.Form):
    """Форма: имя комнаты, юзернейм"""

    room_name = forms.CharField()
    username = forms.CharField()