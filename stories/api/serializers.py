from rest_framework import serializers
from stories.models import Story


class StorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    author = serializers.CharField()
    title = serializers.CharField()
    description = serializers.CharField()
    content = serializers.CharField()
    active = serializers.BooleanField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    released_at = serializers.DateField()

    def create(self, validated_data):
        print(validated_data)
        return Story.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.author = validated_data.get('author', instance.author)
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.content = validated_data.get('content', instance.content)
        instance.active = validated_data.get('active', instance.active)
        instance.released_at = validated_data.get('released_at', instance.released_at)
        instance.save()
        return instance