from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import (
    UserCreationForm,
)
from django.urls import (
    reverse_lazy,
)
from django.views.generic import (
    CreateView,
)

class RegisterView(CreateView): # CreateViewを継承
    template_name = 'user/register.html' # 次に作成する登録用のtemplate
    form_class = UserCreationForm
    success_url = reverse_lazy( # classベースのviewではreverse_lazy()を使う
        'core:MovieList') # 登録に成功した場合のリダイレクト先