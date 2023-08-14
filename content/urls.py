from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'content'
urlpatterns = [
    path('add/content/', views.addContent, name='addContent'),
    path('add/courses/', views.addCourses, name='addCourses'),
    path('getlevel2/',views.get_level2, name='get_level2'),
    path('showcourses_labale1/',views.showcourses_labale1, name='showcourses_labale1'),
    path('ShowCourses/',views.ShowCourses, name='ShowCourses'),
    path('Spacy/', views.spacy, name='spacy'),
    path('content_list/',views.content_list, name='content_list'),
    path('courses_list/',views.courses_list, name='courses_list'),
    path('all_read_list/',views.all_read_list, name='all_read_list'),
    path('all_courses_list/',views.all_courses_list, name='all_courses_list'),
    path('all_content/',views.all_content, name='all_content'),
    path('all_courses/',views.all_courses, name='all_courses'),
    path('play_list/',views.play_list,name='play_list'),
    path('get_user_level/', views.get_user_level, name='get_user_level')


]
              # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)