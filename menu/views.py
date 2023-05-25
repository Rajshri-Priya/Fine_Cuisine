from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Category, MenuItem
from .serializers import CategorySerializer, MenuItemSerializer


class CategoryListCreateView(APIView):
    def get(self, request):
        try:
            categories = Category.objects.all()
            serializer = CategorySerializer(categories, many=True)
            return Response({'message': 'successfully get list of categories', 'data': serializer.data}, status=200)
        except Exception as e:
            return Response({'message': str(e)}, status=400)

    def post(self, request):
        try:
            # print(request.user.role)
            # if request.user.role != 'admin':
            #     return Response({'message': 'Only admins can create categories.'}, status=status.HTTP_403_FORBIDDEN)

            serializer = CategorySerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'message': 'Category created successfully', 'data': serializer.data}, status=201)
        except Exception as e:
            return Response({'message': str(e)}, status=400)


class CategoryDetailView(APIView):
    def get_category(self, category_id):
        try:
            return Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            return None

    def get(self, request, category_id):
        try:
            category = self.get_category(category_id)
            serializer = CategorySerializer(category)
            return Response({'message': 'Category get successfully', 'data': serializer.data}, status=200)
        except Exception as e:
            return Response({'message': str(e)}, status=400)

    def put(self, request, category_id):
        try:
            # if request.user.role != 'admin':
            #     return Response({'message': 'Only admins can update categories.'}, status=status.HTTP_403_FORBIDDEN)

            category = self.get_category(category_id)
            serializer = CategorySerializer(category, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'message': 'Category updated successfully', 'Updated_data': serializer.data}, status=200)
        except Exception as e:
            return Response({'message': str(e)}, status=400)

    def delete(self, request, category_id):
        try:
            # if request.user.role != 'admin':
            #     return Response({'message': 'Only admins can delete categories.'}, status=status.HTTP_403_FORBIDDEN)

            category = self.get_category(category_id)
            category.delete()
            return Response({'message': 'Category deleted successfully'}, status=204)
        except Exception as e:
            return Response({'message': str(e)}, status=400)


class MenuItemListCreateView(APIView):
    def get(self, request):
        try:
            menu_items = MenuItem.objects.all()
            serializer = MenuItemSerializer(menu_items, many=True)
            return Response({'message': 'successfully get list of menu_items', 'data': serializer.data}, status=200)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = MenuItemSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'message': 'Menu_Item created successfully', 'data': serializer.data}, status=201)
        except Exception as e:
            return Response({'message': str(e)}, status=400)


class MenuItemDetailView(APIView):
    def get_object(self, menu_item_id):
        try:
            return MenuItem.objects.get(id=menu_item_id)
        except MenuItem.DoesNotExist:
            return None

    def get(self, request, menu_item_id):
        try:
            menu_item = self.get_object(menu_item_id)
            serializer = MenuItemSerializer(menu_item)
            return Response(serializer.data)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, menu_item_id):
        try:
            menu_item = self.get_object(menu_item_id)
            serializer = MenuItemSerializer(menu_item, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'message': 'Menu_item updated successfully', 'data': serializer.data}, status=200)
        except Exception as e:
            return Response({'message': str(e)}, status=400)

    def delete(self, request, menu_item_id):
        try:
            menu_item = self.get_object(menu_item_id)
            menu_item.delete()
            return Response({'message': 'Menu item deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
