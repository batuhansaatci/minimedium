from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from stories.models import Story
from stories.api.serializers import StorySerializer


#class views
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

class StoryListCreateAPIView(APIView):

    def get(self, request):
        stories = Story.objects.filter(active = True)
        serializer = StorySerializer(stories,many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = StorySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class StoryDetailAPIView(APIView):

    def get_object(self, request, pk):
        story_instance = get_object_or_404(Story, pk=pk)
        return story_instance
    
    def get(self, request, pk):
        story_instance = self.get_object(pk=pk)
        serializer = StorySerializer(story_instance)
        return(serializer.data)
    
    def put(self, request, pk):
        pass

    def delete(self, request, pk):
        pass





###### FUNCTION METHOD ######
# @api_view(['GET','POST'])
# def story_list_create_api_view(request):

#     if request.method == 'GET':
#         stories = Story.objects.filter(active=True)
#         serializer = StorySerializer(stories, many=True)
#         return Response(serializer.data)
    
#     elif request.method == 'POST':
#         serializer = StorySerializer(data=request.data)
#         if  serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET','PUT', 'DELETE'])
# def story_detail_api_view(request, pk):
#     try:
#         story_instance = Story.objects.get(pk = pk)
#     except Story.DoesNotExist:
#         return Response(
#             {
#                 'errors':{
#                     'code':401,
#                     'message': f'Böyle bir id ({pk}) ile ilgili makale bulunamadı'
#                 }
#             },
#             status=status.HTTP_404_NOT_FOUND
#         )

#     if request.method == 'GET':
#         serializer = StorySerializer(story_instance)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = StorySerializer(story_instance, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     elif request.method == 'DELETE':
#             story_instance.delete()
#             return Response(
#                 {
#                     'işlem': {
#                         'code': 204,
#                         'message': f'({pk}) id numaralı makale silinmiştir'
#                     }
#                 }, 
#                 status = status.HTTP_204_NO_CONTENT
#             )
