from rest_framework import serializers
from iwedioro.api.models import Voices, Tokens


class VoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Voices
        fields = '__all__'


class TokenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tokens
        fields = '__all__'


class DefaultVoicesSerializers(serializers.Serializer):
    voice_id = serializers.CharField()
    name = serializers.CharField()
    category = serializers.CharField()
    description = serializers.CharField(allow_blank=True, required=False)
    labels = serializers.JSONField()
    samples = serializers.ListField(
        child=serializers.URLField(), required=False)
    design = serializers.JSONField(required=False)
    preview_url = serializers.URLField(required=False)
    settings = serializers.JSONField(required=False)


    class Meta:
        fields = '__all__'


class GeneratorSerializer(serializers.Serializer):

    text = serializers.CharField()
    voice = serializers.IntegerField()
