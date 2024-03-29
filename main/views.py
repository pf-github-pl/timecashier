from allauth.account.views import PasswordChangeView
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.urls import reverse_lazy

from main.forms import ChangePasswordForm


def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("entries:home"))
    return render(request, "main/index.html")


def profile(request):
    context = {}
    return render(request, "main/profile.html", context)


class PasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy("main:profile")

    def get_context_data(self, **kwargs):
        change_password_form = ChangePasswordForm()
        context = super(PasswordChangeView, self).get_context_data(**kwargs)
        context["change_password_form"] = change_password_form
        return context


def lockout(request, credentials, *args, **kwargs):
    messages.error(
        request,
        "Zbyt wiele prób logowania. Konto zostało zablokowane. Skontaktuj się z administratorem.",
    )
    return HttpResponseRedirect(reverse("main:index"))
