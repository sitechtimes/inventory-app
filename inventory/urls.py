from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from inventory import views 

urlpatterns = [
    path("items/", views.ItemsList.as_view()),
    path("items/create", views.ItemsCreate.as_view()),
    path("items/update/<name>", views.ItemsUpdate.as_view()),
    path("items/destroy/<int:pk>", views.ItemsDestroy.as_view()),
]
"""     path("items/", views.ItemsView.as_view()),
    path("items/create/", views.ItemsCreate.as_view()) """
urlpatterns = format_suffix_patterns(urlpatterns)