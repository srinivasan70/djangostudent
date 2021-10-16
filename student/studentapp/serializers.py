from rest_framework import serializers
from studentapp.models import studentmarks

class studentmarklistSerializer(serializers.ModelSerializer):
    class Meta:
        
        
        model = studentmarks
        fields = '_all_'
