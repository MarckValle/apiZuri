from django.db import models

# Create your models here.

class inicio_sesion(models.Model):
    idUser = models.IntegerField(primary_key=True,db_column='idUser')
    username = models.CharField(max_length=100, db_column='username')
    name = models.CharField(max_length=100, db_column='name1')
    passw = models.CharField(max_length=100, db_column='pasw')
    class Meta: 
        db_table='sesion'