from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from tags.models import Task, Tag


class Index(LoginRequiredMixin, generic.ListView):
    model = Task
    template_name = "task/index.html"
    context_object_name = "todo_list"


class TagListView(LoginRequiredMixin, generic.ListView):
    model = Tag
    template_name = 'task/tag_list.html'
    context_object_name = 'tags'


class TagCreateView(LoginRequiredMixin, generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy('tags:tags')


class TagUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Tag
    fields = ['name']
    success_url = reverse_lazy('tags:tags')


class TagDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Tag
    success_url = reverse_lazy('tags:tags')
    template_name = "task/tag_delete_confirmation.html"


def change_button(request, pk):
    button = Task.objects.get(pk=pk)

    if button.task_completed:
        button.task_completed = False
    else:
        button.task_completed = True
    button.save()

    return render(request, "task/index.html")


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    template_name = 'task/index.html.html'
    context_object_name = 'tasks'


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    fields = [
        "content",
        "deadline_time",
        "task_completed"
    ]
    success_url = reverse_lazy("todo:todo-list")


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    fields = [
        "content",
        "deadline_time",
        "task_completed",
        "tags"
    ]
    success_url = reverse_lazy("todo:todo-list")


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy('todo_list:index')
    template_name = 'task/task_delete_confirm.html'

