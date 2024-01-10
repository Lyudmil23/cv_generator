from django.urls import path

from cv_generator.pdf.views import accept, resume, profiles_list

urlpatterns = [
    path('', accept, name='accept'),
    path('<int:pk>/', resume, name='resume'),
    path('list/', profiles_list, name='profiles list')
]