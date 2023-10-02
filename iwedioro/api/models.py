from django.db import models



class Voices(models.Model):
    name = models.CharField(max_length=150)
    descriptiion = models.TextField()
    voice_file  = models.FileField(upload_to='voices')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name



class TokenManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(is_expired=False)



class Tokens(models.Model):
    name = models.CharField(max_length=150)
    token = models.CharField(max_length=255)
    is_expired = models.BooleanField(default=False)
    # is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
    
    def expired(self):
        self.is_expired = True
        self.save()
    
    objects = TokenManager()
    

