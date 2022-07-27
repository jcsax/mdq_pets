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
SHOP_TYPE = (("PetShop", "PetShop"), 
("Veterinaria","Veterinaria"), 
("Paseador/Recreación","Paseador/Recreación"),
("Guardería","Guardería"),
("Peluquería","Peluquería"))
class Local(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    name = models.CharField(max_length=50, blank=True)
    dir = models.CharField(max_length=50, blank=True)
    shop_type = models.CharField(max_length=20, choices=SHOP_TYPE)
    description = models.TextField(max_length=400, blank=True)
    image = models.ImageField(upload_to ='images', default='mp.jpg')
    class Meta:
        verbose_name = 'Local'
        verbose_name_plural = 'Locales'
    def __str__(self):
        return f'Local de {self.user.username}'