from django.shortcuts import render,get_object_or_404
from django.views import View

from .models import Course
# HTTP METHODS

class CourseView(View):
    template_name = 'courses/courses_detail.html'
    def get(self, request, id=None, *args,**kwargs):
        return render(request, self.template_name, {})

    #def post(request,*args,**kwargs):
    #    return render(request, 'about.html', {})
