from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import *
from rest_framework.response import Response
from library.models import *

@api_view(['GET', 'POST'])
def book_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, context={'request' : request}, many=True)
        return Response({'data' : serializer.data})

    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)