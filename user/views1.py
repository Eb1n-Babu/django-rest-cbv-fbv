from .models import Userlist
from django.views import generic
from .forms import UserForm

class UserView(generic.ListView):
    queryset = Userlist.objects.all()
    template_name = 'userlist.html'
    context_object_name = 'userlist'

class UserDetailView(generic.DetailView):
    queryset = Userlist.objects.all()
    template_name = 'userdetail.html'
    context_object_name = 'userdetail'

class UserUpdateView(generic.UpdateView):
    queryset = Userlist.objects.all()
    form_class = UserForm
    template_name = 'userupdate.html'
    success_url = "/users/"

class UserDeleteView(generic.DeleteView):
    queryset = Userlist.objects.all()
    template_name = 'userdelete.html'
    success_url = "/users/"

class UserCreateView(generic.CreateView):
    queryset = Userlist.objects.all()
    form_class = UserForm
    template_name = 'usercreate.html'
    success_url = "/users/"