from django.urls import path

from menu.views import CategoryListCreateView, CategoryDetailView, MenuItemListCreateView, MenuItemDetailView

urlpatterns = [
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:category_id>/', CategoryDetailView.as_view(), name='category-detail'),
    path('menu-items/', MenuItemListCreateView.as_view(), name='menu-item-list-create'),
    path('menu-items/<int:menu_item_id>/', MenuItemDetailView.as_view(), name='menu-item-detail'),
]
