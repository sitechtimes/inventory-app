from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from inventory import views

urlpatterns = [
    path("category/", views.CategoryView.as_view()),
    path("vendor/", views.VendorView.as_view()),
    path("category/<str:category_name>/", views.sortByCategory.as_view()),
    path("lastpurchase/<int:pk>/", views.UpdateLastPurchase.as_view()),
    path("CurrentItem/<int:pk>/", views.getItems.as_view()),
    path("updateQuantity/<int:pk>/<str:from>/", views.moveItems.as_view()),
    path("updateQuantity/manual/<int:pk>/<int:makerspace>/<int:backroom>/",
         views.ManualEditQuantity.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
