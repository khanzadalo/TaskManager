from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.db import transaction
from django.shortcuts import get_object_or_404, render

from django.urls import reverse, reverse_lazy
from django.views import generic
from . import models, forms


class RegisterView(generic.CreateView):
    form_class = forms.CustomUserCreationForm
    template_name = 'users/register.html'

    def get_success_url(self):
        return reverse_lazy('users:login')


class InLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'

    def get_success_url(self):
        return reverse_lazy('tasks:tasks_list')


class OutLogoutView(LogoutView):
    next_page = reverse_lazy('users:login')


def profile_view(request):
    if request.method == 'GET':
        return render(request, 'users/user_profile.html', {"user": request.user})


class ProfileUpdateView(generic.UpdateView):
    model = models.UserProfile
    form_class = forms.ProfileUpdateForm
    template_name = 'users/profile_edit.html'

    def get_object(self, queryset=None):
        return self.request.user.profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f"Editing a user's profile: {self.request.user.username}"
        if self.request.POST:
            context['user_form'] = forms.UserUpdateForm(self.request.POST, instance=self.request.user)
        else:
            context['user_form'] = forms.UserUpdateForm(instance=self.request.user)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        user_form = context['user_form']
        with transaction.atomic():
            if all([form.is_valid(), user_form.is_valid()]):
                user_form.save()
                form.save()
            else:
                context.update({'user_form': user_form})
                return self.render_to_response(context)
        return super(ProfileUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('users:profile', kwargs={'username': self.request.user.username})
