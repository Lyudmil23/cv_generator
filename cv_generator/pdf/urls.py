from django.urls import path

from cv_generator.pdf.views import accept

urlpatterns = [
    path('', accept, name='accept'),
]