
from rest_framework import serializers
from tuneup.models.publications import MusicHit

class MusicHitSerializer(serializers.ModelSerializer):
    class Meta:
        model = MusicHit