# This is a serializers page
from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Contact
		fields = ('id','url','name','phone')
