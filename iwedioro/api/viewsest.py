from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from iwedioro.api.models import Voices, Tokens
from iwedioro.api.serializers import VoiceSerializer, DefaultVoicesSerializers, TokenSerializer, GeneratorSerializer
from iwedioro.xlibs.client import Iwedioro
from elevenlabs.api import UnauthenticatedRateLimitError, RateLimitError

client = Iwedioro()


class VoiceViewSet(viewsets.ModelViewSet):
    serializer_class = VoiceSerializer
    http_method_names = ['get', 'post']
    queryset = Voices.objects.all()


class TokenViewSet(viewsets.ModelViewSet):
    serializer_class = TokenSerializer
    http_method_names = ['get', 'post']
    queryset = Tokens.objects.all()


class DefaultVoiceViewSet(viewsets.ViewSet):
    http_method_names = ['get']

    def list(self, request):
        try:
            token = Tokens.objects.all().first()
            client.set_token(token.token)
            voices = client.get_voice_list()
        except (UnauthenticatedRateLimitError, RateLimitError):
            token.expired()
            token = Tokens.objects.all().first()
            client.set_token(token.token)
            voices = client.get_voice_list()

        serializer = DefaultVoicesSerializers(voices, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class GenerateAudioViewSet(viewsets.ViewSet):

    http_method_names = ['post']
    serializer_class = GeneratorSerializer

    def create(self, request):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        text = serializer.validated_data.get('text')
        voice = serializer.validated_data.get('voice')

        try:
            token = Tokens.objects.all().first()
            client.set_token(token.token)
            voices_list = client.get_voice_list()
            generated = client.generate(text=text, voice=voices_list[voice])

            response = Response(
                generated, content_type='audio/mpeg', status=status.HTTP_201_CREATED)
            response['Content-Disposition'] = 'attachment; filename="generated_audio.mp3'
            return response

        except (UnauthenticatedRateLimitError, RateLimitError):
            token.expired()
            token = Tokens.objects.all().first()
            client.set_token(token.token)
            voices_list = client.get_voice_list()
            generated = client.generate(text=text, voice=voices_list[voice])

            response = Response(
                generated, content_type='audio/mpeg', status=status.HTTP_201_CREATED)
            response['Content-Disposition'] = 'attachment; filename="generated_audio.mp3'
        except AttributeError:
            response = Response(
                {'message': 'You run out of token try again'}, status=status.HTTP_401_UNAUTHORIZED)
            return response
