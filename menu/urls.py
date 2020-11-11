from django.urls import path,include
from menu.views import MenuCategoryListView,MenuListView,ItemListView
app_name = 'menu'


urlpatterns = [
    path('category',MenuCategoryListView.as_view()),
    path('category/<category_id>/menu',MenuListView.as_view()),
    path('items',ItemListView.as_view())
]
