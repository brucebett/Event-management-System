from rest_framework import serializers

import Events.models 
import Events


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'