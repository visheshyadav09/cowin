from django.urls import path
from .views import *

urlpatterns = [
    path('<id>/<date>/', ByDistrict.as_view(), name="discrict"),
    path('cert/', GetCert.as_view(), name="cert"),
    path('', index, name="index"),
]