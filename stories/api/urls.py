from django.urls import path
from stories.api import views as api_views

urlpatterns = [
    path('stories/', api_views.story_list_create_api_view, name='story-list'),
    path('stories/<int:pk>', api_views.story_detail_api_view, name='story-detail')
]