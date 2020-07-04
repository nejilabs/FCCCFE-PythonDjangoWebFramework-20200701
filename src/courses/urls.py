from django.urls import path
from courses.views import (
    CourseView
)

app_name = 'courses'
urlpatterns = [
    path('',CourseView.as_view(template_name='contact.html'), name='courses-list'),


    #path('', courses_list_view, name='courses-list'),
    #path('create/', courses_create_view, name='courses-create'),
    path('<int:id>/', CourseView.as_view(), name='courses-detail'),
    #path('<int:id>/update/', courses_update_view, name='courses-update'),
    #path('<int:id>/delete/', courses_delete_view, name='courses-delete'),


]
