from django.shortcuts import render

from .models import Person


def index(request):
    personal_data = Person.objects.get(pk=1)
    return render(request,
                  'hello/index.html',
                  {'personal_data': personal_data}
                  )
