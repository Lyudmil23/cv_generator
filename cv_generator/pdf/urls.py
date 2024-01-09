from django.urls import path

from cv_generator.pdf.views import accept, resume

urlpatterns = [
    path('', accept, name='accept'),
    path('<int:pk>/', resume, name='resume'),
]