from django.shortcuts import render
from django.views import generic
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import File
from .serializers import FileSerializer
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    return render(request, 'api/index.html', {})

class FileList(APIView):

    def get(self, request):
        files = File.objects.all()
        serializer = FileSerializer(files, many=True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request):
        serializer = FileSerializer(data=request.data)
        if serializer.is_valid():
            file = request.data['file']
            F = open('testFile.txt', 'w')
            F.write(file)
            F.close()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
