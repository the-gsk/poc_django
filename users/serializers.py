from rest_framework import serializers
from .models import UserDetails
from django.core.files.base import ContentFile
import base64

class Base64ImageField(serializers.ImageField):
    """
    A custom serializer field to handle base64-encoded images.
    """
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            # Handle base64-encoded image
            format, imgstr = data.split(';base64,')  # Split the data string
            ext = format.split('/')[-1]  # Extract the image extension
            data = ContentFile(base64.b64decode(imgstr), name=f'uploaded_image.{ext}')

        return super().to_internal_value(data)


class UserDetailsSerializer(serializers.ModelSerializer):
    profile_picture = Base64ImageField(required=False)
    
    class Meta:
        model = UserDetails
        fields = '__all__'
