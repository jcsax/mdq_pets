from django.db import models
from django.contrib.auth.models import User

#Contact form:
query_set = [
    [0, "Consulta"],
    [1, "Eliminar Negocio"],
]
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    query = models.IntegerField(choices=query_set)
    text = models.TextField(max_length=400)
    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'

    def __str__(self):
        return self.name

#Create Local:
query_set = (
    [0, "PetShop"],
    [1, "Veterinaria"],
    [2, "Paseador/Recreación"],
    [3, "Guardería"],
    [4, "Peluquería"]
)
class Local(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    name = models.CharField(max_length=50, blank=True)
    dir = models.CharField(max_length=50, blank=True)
    query = models.IntegerField(choices=query_set, blank=True, default = 0)
    description = models.TextField(max_length=400, blank=True)
    image = models.ImageField(upload_to ='images/profile_image', default='mp.jpg')
    go = models.CharField(max_length=250, blank=True)
    class Meta:
        verbose_name = 'Local'
        verbose_name_plural = 'Locales'
    def __str__(self):
        return f'Local de {self.user.username}'

#Profile:
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    name = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to ='images/profile_image', default='mp.jpg')
    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
    def __str__(self):
        return f'Perfil de {self.user.username}'