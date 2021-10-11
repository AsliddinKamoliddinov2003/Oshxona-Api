from rest_framework import  status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from store.models import Product
from .serialisezs import *



class ApiView(APIView):
    serializer_class = ProductSerializers
    permission_classes = (IsAuthenticatedOrReadOnly,)
    

    def get(self, request):
        products = Product.objects.all()

        name = request.GET.get("name", None)
        price = request.GET.get("price", None)
        rating = request.GET.get("rating", None)
        slug = request.GET.get("slug", None)
        image = request.GET.get("image", None)
        category = request.GET.get("category", None)
        is_active = request.GET.get("is_active", None)

        if name:
            name = products.filter(name__contains=name)
        if price:
            price = products.filter(price__contains=price)
        if rating:
            rating = products.filter(rating__contains=rating)
        if slug:
            slug = products.filter(slug__contains=slug)
        if image:
            image = products.filter(image__contains=image)
        if category:
            category = products.filter(category__contains=category)
        if is_active:
            is_active = products.filter(is_active__contains=is_active)
        
        product_serialized = ProductSerializers(products, many=True)
        return Response(product_serialized.data, status=status.HTTP_200_OK)

        
    def post(self, request):
        product_serizlizer = ProductSerializers(data=request.data)
        if product_serizlizer.is_valid():
            product_serizlizer.save()
            return Response({"post":"ma'lumot qo'shildi"}, status=status.HTTP_201_CREATED)
        
        return Response(product_serizlizer.errors, status=status.HTTP_400_BAD_REQUEST)


class SingleApiView(APIView):
    serializer_class = ProductSerializers
    permission_classes = (IsAuthenticatedOrReadOnly,)


    def get(self, request, pk=None):
        product = Product.objects.get(id=pk)
        product_serizlizer = ProductSerializers(product, many=False)
        return Response(product_serizlizer.data, status=status.HTTP_200_OK)

    
    def put(self, request, pk=None):
        product = Product.objects.get(id=pk)
        product_serizlizer = ProductSerializers(instance=product, data=request.data)
        if product_serizlizer.is_valid():
            product_serizlizer.save()
            return Response({"ma'lumot":"o'zgartirildi"}, status=status.HTTP_202_ACCEPTED)
        
        return Response(product_serizlizer.errors, status = status.HTTP_400_BAD_REQUEST)


    def patch(self, request, pk=None):
        product = Product.objects.get(id=pk)
        product_serizlizer = ProductSerializers(instance=product, data=request.data, partial=True)
        if product_serizlizer.is_valid():
            product_serizlizer.save()
            return Response({"ma'lumot":"o'zgartirildi"}, status=status.HTTP_202_ACCEPTED)
        
        return Response(product_serizlizer.errors, status = status.HTTP_400_BAD_REQUEST)

    
    def delete(self, request, pk=None):
        product = Product.objects.get(id=pk)
        product.delete()
        return Response({"ma'lumot":"o'chirildi"}, status=status.HTTP_204_NO_CONTENT)







