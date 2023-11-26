from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm


class HomeView(TemplateView):
    template_name = "index.html"


# inicio de sesion
def signup(request):
    return render(request, "signup.html", {"form": UserCreationForm})
