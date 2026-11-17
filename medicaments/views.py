from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import  Medicament
from .serializers import  MedicamentSerializer
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAdminUser

class MedicamentGetPostView(APIView): 
    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAdminUser()]
    
    def get(self,request):
            medicaments = Medicament.objects.all()
            serializer = MedicamentSerializer(medicaments, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request):
        serializer = MedicamentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Medicament created!"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class MedicamentDetailPutPatchDelete(APIView):
    permission_classes = [IsAdminUser]
    def detail(self,request, pk):
        medicament = get_object_or_404(Medicament, pk=pk)
        serializer = MedicamentSerializer(medicament)

    def put(self,request, pk):
        serializer = MedicamentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self,request, pk):
        serializer = MedicamentSerializer(data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request, pk):
        medicament = Medicament.objects.filter(pk=pk)
        medicament.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
