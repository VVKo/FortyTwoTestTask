from django.views.generic import View
from django.shortcuts import render
from .models import Person


class ShowPersonalDataView(View):

    template_name = 'hello/index.html'

    def get(self, request):
        personal_data = Person.objects.get(pk=1)
        return render(request,
                      self.template_name,
                      {'personal_data': personal_data}
                      )
