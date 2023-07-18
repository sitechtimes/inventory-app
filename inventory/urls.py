from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from inventory import views

urlpatterns = [
    path("category/", views.ItemsView.as_view()),
    path("category/<str:category_name>/", views.sortByCategory.as_view()),
    path("categoryCount/", views.categoryCount.as_view()),
    path("location/makerspace/", views.MakerspaceView.as_view()),
    path("location/backroom/", views.BackroomView.as_view()),
    path("lastpurchase/<int:pk>/", views.UpdateLastPurchase.as_view()),
    path("CurrentItem/<str:item_name>/", views.getItems.as_view()),
    path("updateQuantity/<str:item_name>/<int:amount>/<str:from>/<str:to>/", views.moveItems.as_view()),
    path("updateQuantity/manual/<str:item_name>/<int:makerspace>/<int:backroom>/", views.UpdateItem.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)