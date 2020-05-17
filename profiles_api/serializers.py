from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Test out APIView"""
    name=serializers.CharField(max_length=10)
