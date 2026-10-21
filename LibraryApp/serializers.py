from rest_framework import serializers
from LibraryApp.models import BookDb


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model=BookDb
        fields='__all__'