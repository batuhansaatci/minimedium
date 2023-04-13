from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from stories.models import Story
from stories.api.serializers import StorySerializer

@api_view(['GET','POST'])
def story_list_create_api_view(request):

    if request.method == 'GET':
        stories = Story.objects.filter(active=True)
        serializer = StorySerializer(stories, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = StorySerializer(data=request.data)
        if  serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
