from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Recipe
from .serializers import RecipeSerializer


class RecipeListViewSet(APIView):
    def get(self, request, format=None):
        queryset = Recipe.objects.all()
        serializer = RecipeSerializer(queryset, many=True)

        return Response(serializer.data, status.HTTP_200_OK)


class RecipeViewSet(APIView):
    def get(self, request, pk, format=None):
        queryset = Recipe.objects.filter(id=pk)
        serializer = RecipeSerializer(queryset, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
