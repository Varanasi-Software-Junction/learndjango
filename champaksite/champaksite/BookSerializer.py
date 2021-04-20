# serializers.py
from rest_framework import serializers

from pappu import models

class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.BookModel
        fields = ('bookname', 'price')
		
		
		
