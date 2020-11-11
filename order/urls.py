from django.urls import path,include
from order import views
app_name = "order"
urlpatterns = [
    path('',views.orderListView,name = "order_list"),
    path('<order_id>',views.orderDetailView, name="order_detail"),
    path('<order_id>/item/',views.orderItemListView,name='orderItem_list'),
    path('<order_id>/item/<item_id>', views.orderItemDetailView, name='orderItem_list'),

]
