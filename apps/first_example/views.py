from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from django.views.generic import TemplateView
from apps.first_example.services.generate import generate_users


class UsersView(TemplateView):

    template_name = "first_example/generate.html"

    def get_context_data(self, amount: int = 7, **kwargs) -> dict:
        context_data = super().get_context_data(**kwargs)
        context_data["title"] = "Generate Users"

        context_data["amount"] = amount
        context_data["users"] = generate_users(amount=amount)

        return context_data


def index(request: WSGIRequest):
    return render(
        request=request,
        template_name='index.html'
    )
