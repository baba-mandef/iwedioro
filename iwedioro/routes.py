from django.urls import path, include
from rest_framework.routers import DefaultRouter
from iwedioro.api.viewsest import VoiceViewSet, DefaultVoiceViewSet, GenerateAudioViewSet, TokenViewSet

router = DefaultRouter(trailing_slash=False)

router.register('token', TokenViewSet, basename='token')
router.register('voice_set', VoiceViewSet, basename='voice_set')
router.register('voice_default', DefaultVoiceViewSet, basename='voice_default')
router.register('audio', GenerateAudioViewSet, basename='voice'),

urlpatterns = [
    path('', include(router.urls))
]

