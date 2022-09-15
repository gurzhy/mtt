from .forms import RouterForm
from django.shortcuts import render
from core.utils.passwd import generate_passwd


def index(request):
    soft_data = {
        "wifi_passwd": generate_passwd(8),
        "client_passwd": generate_passwd(17),
        "isp_passwd": generate_passwd(17),
    }
    form = RouterForm(request.POST or None, initial=soft_data)
    if request.method == "POST" and form.is_valid():
        context = form.cleaned_data
        return render(request, "config.html", {"context": context})
    return render(request, "index.html", {"form": form})
