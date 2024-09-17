from rest_framework import serializers
from todo.models import ToDo  # Make sure the import is correct

class TodoSerializer(serializers.ModelSerializer):
    created = serializers.ReadOnlyField()  # Make this field read-only
    completed = serializers.ReadOnlyField()

    class Meta:
        model = ToDo
        fields = ['id', 'title', 'memo', 'created', 'completed']  # Adjust fields as per your model

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ['title', 'memo', 'created', 'completed']
