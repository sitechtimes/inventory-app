from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from inventory import views

urlpatterns = [
    path("category/", views.ItemsView.as_view()),
    path("categoryy/<str:category_name>/", views.category_list.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)