from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from directory.serializers import LevelSerializer, SubLevelSerialzer
from rest_framework.response import Response
from directory.models import Level, SubLevel


class PortfolioList(APIView):

    def get(self, request, format=None):
        levels = Level.objects.all()
        serializer = LevelSerializer(levels, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        print(request.data)
        serializer = LevelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PortfolioDetail(APIView):
    def get_object(self, pk):
        try:
            return Level.objects.get(pk=pk)
        except Level.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        level = self.get_object(pk)
        serializer = LevelSerializer(level)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        level = self.get_object(pk)
        serializer = LevelSerializer(level, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        level = self.get_object(pk)
        level.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SubPortfolioList(APIView):
    
    def get(self, request, format=None):
        sublevels = SubLevel.objects.all()
        serializer = SubLevelSerialzer(sublevels, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):

        data = request.data
        # print(data)
        sublevel_name = data.get("name")
        parent = data.get("parent")
        # print("parent: ", parent)
        if type(parent) != int:
            level_name = parent.get('name')
            is_level = Level.objects.filter(name=level_name)
            if is_level.exists():
                return Response(
                    {
                        'error': "Unique constraint failed!",
                        "message": "Level name already exists"
                    },
                    status=status.HTTP_403_FORBIDDEN
                )
            else:
                Level.objects.create(name=level_name)
        serializer = SubLevelSerialzer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SubPortfolioDetail(APIView):
    def get_object(self, pk):
        try:
            return SubLevel.objects.get(pk=pk)
        except SubLevel.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        sublevel = self.get_object(pk)
        serializer = SubLevelSerialzer(sublevel)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        subLevel = self.get_object(pk)
        serializer = SubLevelSerialzer(subLevel, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        level = self.get_object(pk)
        level.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

