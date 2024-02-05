from django.shortcuts import render

from apps.contacts.models import Contact


def list_contacts(request):
    return render(
        request=request,
        template_name="contacts/contacts_list.html",
        context={
            "contacts": Contact.objects.all(),
        },
    )
