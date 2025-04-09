from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic, View
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .forms import TaskForm, TagForm
from .models import Task, Tag

class IndexView(LoginRequiredMixin, generic.TemplateView):
    template_name = "todo/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        num_tasks = Task.objects.count()
        num_tags = Tag.objects.count()
        num_done_tasks = Task.objects.filter(is_done=True).count()
        num_pending_tasks = Task.objects.filter(is_done=False).count()

        num_visits = self.request.session.get("num_visits", 0)
        self.request.session["num_visits"] = num_visits + 1

        context.update({
            "num_tasks": num_tasks,
            "num_tags": num_tags,
            "num_done_tasks": num_done_tasks,
            "num_pending_tasks": num_pending_tasks,
            "num_visits": num_visits + 1,
        })
        return context


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    context_object_name = 'task_list'
    template_name = 'todo/task-list.html'
    paginate_by = 5

    def get_queryset(self):
        pending_tasks = Task.objects.filter(is_done=False).order_by('deadline', '-created_at')
        completed_tasks = Task.objects.filter(is_done=True).order_by('deadline', '-created_at')
        return pending_tasks | completed_tasks


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'todo/add-task.html'
    success_url = reverse_lazy('todo:task_list')


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'todo/update-task.html'
    success_url = reverse_lazy('todo:task_list')


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    template_name = 'todo/task_confirm_delete.html'
    success_url = reverse_lazy('todo:task_list')


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'todo/task-detail.html'


class ToggleTaskStatusView(LoginRequiredMixin, View):
    def post(self, request, pk):
        task = Task.objects.get(pk=pk)
        task.is_done = not task.is_done
        task.save()
        return redirect('todo:index')


class AddTaskUserView(LoginRequiredMixin, View):
    def post(self, request, pk):
        task = Task.objects.get(pk=pk)
        task.users.add(request.user)
        return redirect('todo:task_detail', pk=pk)


class RemoveTaskUserView(LoginRequiredMixin, View):
    def post(self, request, pk):
        task = Task.objects.get(pk=pk)
        task.users.remove(request.user)
        return redirect('todo:task_detail', pk=pk)


class TagListView(LoginRequiredMixin, generic.ListView):
    model = Tag
    context_object_name = 'tag_list'
    template_name = 'todo/tag-list.html'


class TagCreateView(LoginRequiredMixin, generic.CreateView):
    model = Tag
    form_class = TagForm
    template_name = 'todo/add-tag.html'
    success_url = reverse_lazy('todo:tag_list')


class TagDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Tag
    template_name = 'todo/tag_confirm_delete.html'
    success_url = reverse_lazy('todo:tag_list')


class TagDetailView(LoginRequiredMixin, generic.DetailView):
    model = Tag
    context_object_name = 'tag'
    template_name = 'todo/tag-detail.html'


class TagUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Tag
    fields = ['name']
    template_name = 'todo/tag_form.html'
    success_url = reverse_lazy('todo:tag_list')

