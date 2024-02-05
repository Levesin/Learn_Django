from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from apps.contacts.models import Contact


def list_contacts(request):
    return render(
        request=request,
        template_name="contacts/contacts_list.html",
        context={
            "contacts": Contact.objects.all(),
        },
    )


class ContactCreateView(CreateView):
    model = Contact
    fields = (
        "name",
        "phone",
    )
    success_url = reverse_lazy("contacts:list")


class ContactUpdateView(UpdateView):
    model = Contact
    fields = (
        "id",
        "name",
        "phone",
    )
    success_url = reverse_lazy("contacts:list")


class ContactDeleteView(DeleteView):
    model = Contact
    template_name = "contacts/contacts_confirm_delete.html"
    success_url = reverse_lazy("contacts:list")


class ContactDetailView(DetailView):
    model = Contact
    pk_url_kwarg = "pk"
