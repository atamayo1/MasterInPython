from rest_framework.response import Response
from .serializers import PageSerializer
from rest_framework.views import APIView
from rest_framework import status

class PageApi(APIView):
    def post(self, request):
        serializer = PageSerializer(data = request.data)
        if serializer.is_valid():
            page = serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)    
