from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .forms import UserInfoModelForm
from .models import UserInfo

class Create(CreateView):
    form_class = UserInfoModelForm
    template_name = 'classbased/create.html'
    # success_url = '/classbased/list/'
    success_url = reverse_lazy('classbased:list')

class List(ListView):
    template_name = 'classbased/list.html'
    model = UserInfo
    context_object_name = 'data'
    
class Detail(DetailView):
    model = UserInfo
    template_name = 'classbased/detail.html'
    pk_url_kwarg = 'id'
    context_object_name = 'user_obj'
    
class Update(UpdateView):
    form_class = UserInfoModelForm
    pk_url_kwarg = 'id'
    success_url = '/classbased/list/'
    model = UserInfo
    template_name = 'classbased/update.html'

    def form_valid(self, form):
        print('form is valid')
        return super().form_valid(form)
    

class Delete(DeleteView):
    model = UserInfo
    success_url = '/classbased/list/'

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)