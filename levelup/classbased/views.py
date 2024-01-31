from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, RedirectView

class FirstView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('THIs is get')
    
    def post(self, request, *args, **kwargs):
        return HttpResponse('this is post')
    
    def abcd(self, request):
        if request.method == 'POST':
            pass

class FirstTemplate(TemplateView):
    template_name = 'classbased/template.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['msg'] = 'hello world'
        return context
    

class FirstTemplateRegirect(RedirectView):
    url = 'classbased/template/'