from django.views.generic import CreateView, FormView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class RegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = '/login/'

class LoginView(FormView):
    template_name = 'registration/login.html'
    form_class = AuthenticationForm
    success_url = '/'

    def form_valid(self, form):
        return super().form_valid(form)
