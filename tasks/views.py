from django.shortcuts import render, get_object_or_404
from django.views import generic

from TaskManager import settings
from . import models, forms
from .models import Task
from .forms import TaskForm
from datetime import datetime


class TaskListView(generic.ListView):
    model = Task
    template_name = 'tasks/tasks_list.html'
    context_object_name = 'tasks'
    paginate_by = settings.PAGE_SIZE

    def get_queryset(self):
        return Task.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_date'] = datetime.now().strftime('%Y-%m-%d')  # Get formatted date
        return context


class TaskDetailView(generic.DetailView):
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task_id'

    def get_object(self, **kwargs):
        task_id = self.kwargs.get('id')
        return get_object_or_404(models.Task, id=task_id)


class TaskCreateView(generic.CreateView):
    template_name = 'tasks/task_create.html'
    form_class = TaskForm
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreateView, self).form_valid(form=form)


class TaskUpdateView(generic.UpdateView):
    template_name = 'tasks/task_update.html'
    form_class = forms.TaskForm
    queryset = models.Task.objects.all()
    success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(TaskUpdateView, self).form_valid(form=form)

    def get_object(self, **kwargs):
        task_id = self.kwargs.get('id')
        return get_object_or_404(models.Task, id=task_id)


class TaskDeleteView(generic.DeleteView):
    template_name = 'tasks/confirm_delete_task.html'
    success_url = '/'

    def get_object(self, **kwargs):
        task_id = self.kwargs.get('id')
        return get_object_or_404(models.Task, id=task_id)


class SearchTaskView(generic.ListView):
    template_name = 'tasks_list.html'
    context_object_name = 'tasks'
    paginate_by = '5'

    def get_queryset(self):
        return Task.objects.filter(title__icontains=self.request.GET.get('q')).order_by('id')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context


