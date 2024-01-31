from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Subject, Course, Module, Quest
from django.core.paginator import Paginator, EmptyPage


def index(request):  # < here
    subjects = Subject.objects.all()
    return render(request, 'base_generic.html', {'subjects': subjects})


def course_list(request, subject):
    courses = Course.objects.filter(subject=subject)
    context = {'courses': courses}
    return render(request, 'course_list.html', context)


def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    modules = course.modules.all()
    context = {'course': course, 'modules': modules}
    return render(request, 'course_list.html', context)


def module_detail(request, pk, module):
    module = get_object_or_404(Module, pk=pk)
    quests = Quest.objects.filter(module=module)

    # Set the number of questions per page
    questions_per_page = 1

    paginator = Paginator(quests, questions_per_page)
    page = request.GET.get('page', 1)

    try:
        quests_page = paginator.page(page)
    except EmptyPage:
        # If the page is out of range (e.g. 9999), deliver the last page
        quests_page = paginator.page(paginator.num_pages)

    context = {
        'module': module,
        'quests_page': quests_page,
    }
    return render(request, 'module_detail.html', context)


