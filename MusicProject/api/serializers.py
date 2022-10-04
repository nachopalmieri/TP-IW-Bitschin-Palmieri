
from rest_framework import serializers
from tuneup.models.publications import MusicHit

class MusicHitSerializer(serializers.ModelSerializer):
    class Meta:
        model = MusicHit
        fields = ['id', 'title', 'author', 'cover', 'publish_date', 'audio']