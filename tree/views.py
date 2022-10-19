# from rest_framework.views import APIView
# from rest_framework import status
# from rest_framework.response import Response
# from tree.models import Parent, Child
# from tree.serializers import ParentSerializer, ChildSerializer


# class ParentList(APIView):

#     def get(self, request, format=None):
#         parents = Parent.objects.all()
#         serializer = ParentSerializer(parents, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def post(self, request, format=None):
#         serializer = ParentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             print(serializer.errors)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class ChildList(APIView):
    
#     def get(self, request, format=None):
#         childs = Child.objects.all()
#         serializer = ChildSerializer(childs, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def post(self, request, format=None):
#         serializer = ChildSerializer(data=request.data, many=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
