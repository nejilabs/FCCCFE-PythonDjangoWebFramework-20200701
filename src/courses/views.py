from django.shortcuts import render,get_object_or_404
from django.views import View

from .models import Course
# HTTP METHODS

class CourseView(View):
    template_name = 'courses/course_detail.html'
    def get(self, request, id=None, *args,**kwargs):
        context = {}
        if id is not None:
            obj = get_object_or_404(Course, *args, **kwargs)
            context['object'] = obj
        return render(request, self.template_name, context)

    #def post(request,*args,**kwargs):
    #    return render(request, 'about.html', {})
