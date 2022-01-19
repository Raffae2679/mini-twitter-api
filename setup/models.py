from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    username = models.CharField(max_length=50, unique=True, error_messages={'unique': "O username cadastrado já existe."})
    email = models.EmailField(max_length=254, unique=True, error_messages={'unique': "O email cadastrado já existe."})
    seguidores = models.ManyToManyField('self', blank=True, symmetrical=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [] 

    def __str__(self):
        return self.username

class Post(models.Model):
    titulo = models.CharField(max_length=30, blank=False)
    descricao = models.CharField(max_length=100, blank=False)
    imagem = models.ImageField(upload_to='imagens',verbose_name='Imagem Post',
		null=True , blank=True
		)
    autor = models.ForeignKey(Usuario, on_delete= models.CASCADE)

    def __str__(self):
        return self.titulo
