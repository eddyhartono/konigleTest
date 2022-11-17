from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import emailList
from .serializers import EmailSerializer

class EmailList(APIView):
    # permission_classes = [IsAuthenticated] # Protect the API 
    def get(self, request):
        email = emailList.objects.get_queryset().order_by('-date_action')
        serializer = EmailSerializer(email, many=True)
        return Response(serializer.data)

class EmailCreate(APIView):
    # permission_classes = [IsAuthenticated] # Protect the API 
    def post(self, request):
        serializer = EmailSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmailDetail(APIView):
    # permission_classes = [IsAuthenticated] # Protect the API 
    def get_object(self, id):
        try:
            return emailList.objects.get(id=id)
        except emailList.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
        
    def get(self, request, id):
        email = self.get_object(id)
        serializer = EmailSerializer(email)
        return Response(serializer.data)

    def put(self, request, id):
        email = self.get_object(id)
        serializer = EmailSerializer(email, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, id):
    #     email = self.get_object(id)
    #     email.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)