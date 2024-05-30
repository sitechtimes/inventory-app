from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from inventory import views

urlpatterns = [
    path("log/", views.LogView.as_view()),
    path("category/", views.CategoryView.as_view()),
    path("vendor/", views.VendorView.as_view()),
    path("category/<str:category_name>/", views.sortByCategory.as_view()),
    path("vendor/<str:vendor_name>/", views.sortByVendor.as_view()),
    path("lastpurchase/<int:pk>/", views.UpdateLastPurchase.as_view()),
    path("CurrentItem/<int:pk>/", views.getItems.as_view()),
    path("updateQuantity/<int:pk>/<str:from>/", views.moveItems.as_view()),
    path("updateQuantity/manual/<int:pk>/<int:makerspace>/<int:backroom>/",
         views.ManualEditQuantity.as_view()),
    path("deleteItem/<int:pk>/",
         views.deleteItems.as_view()),
    path("updateMinAmount/<int:pk>/<int:amount>/",
         views.updateMinAmount.as_view()),
    # send Data to these Url as request body
    path("addItems/", views.AddItems.as_view()),
    path('addLog/', views.AddLog.as_view()),
    path("editItems/<int:pk>/", views.editItems.as_view()),
    # path('items_csv', views.item_csv, name='items_csv')
]
urlpatterns = format_suffix_patterns(urlpatterns)
