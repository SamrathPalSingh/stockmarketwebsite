from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
path('', views.homepage, name = 'homepage')
]

# urlpatterns += [
# path('', RedirectView.as_view(url='<int/page>', permanent=True))
# ]
