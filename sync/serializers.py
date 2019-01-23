from rest_framework import serializers
from .models import Message, Contact


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('uuid', 'contact', 'text', 'attachment', 'log', 'sent_date')


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('uuid', 'name', 'number', 'alt_number', 'created_on')
