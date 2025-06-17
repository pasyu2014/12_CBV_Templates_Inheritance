from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .forms import CourseForm
from .models import Course

class CourseListView(ListView):
    """
    Представление для отображения списка курсов.
    """
    model = Course
    template_name = 'courses/index.html'
    paginate_by = 10  # Количество элементов на странице
    queryset = Course.objects.select_related('category').prefetch_related('teachers')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список курсов'
        return context

class CourseDetailView(DetailView):
    """
    Представление для отображения детальной информации о курсе.
    """
    model = Course
    template_name = 'courses/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course = context.get('object')  # или self.object
        if course:
            context['title'] = f'{course.title}'
        else:
            context['title'] = 'Курс'
        return context
    

class CourseCreateView(CreateView):
    """
    Представление для создания нового курса.
    """
    model = Course
    form_class = CourseForm
    success_url = reverse_lazy('courses:list')
    template_name = 'courses/create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить новый курс'
        return context

class CourseUpdateView(UpdateView):
    """
    Представление для редактирования существующего курса.
    """
    model = Course
    form_class = CourseForm
    success_url = reverse_lazy('courses:list')
    template_name = 'courses/update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course = context.get('object')  # или self.object
        if course:
            context['title'] = f'Редактировать "{course.title}"'
        else:
            context['title'] = 'Редактировать курс'
        return context

class CourseDeleteView(DeleteView):
    """
    Представление для удаления курса.
    """
    model = Course
    success_url = reverse_lazy('courses:list')
    template_name = 'courses/delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course = context.get('object')  # или self.object
        if course:
            context['title'] = f'Удалить "{course.title}"'
        else:
            context['title'] = 'Удалить курс'
        return context