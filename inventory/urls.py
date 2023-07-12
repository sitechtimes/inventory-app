from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from inventory import views 

urlpatterns = [
    path("inventory/", views.ItemsView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)