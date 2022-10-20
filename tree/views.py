from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from tree.models import Parent, Child
from tree.serializers import ParentSerializer, ChildSerializer

class ParentList(APIView):
    def get(self, request):
        parents = Parent.objects.all()
        serializer = ParentSerializer(parents, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        print(request.data)
        serializer = ParentSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ParentDetail(APIView):
    def get(self, request, pk):
        parent = Parent.objects.get(pk=pk)
        serializer = ParentSerializer(parent)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        print(request.data)
        parent = Parent.objects.get(pk=pk)
        serializer = ParentSerializer(parent, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)