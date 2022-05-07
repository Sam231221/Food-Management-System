from django.db import models


class Car(models.Model):
    name = models.CharField(max_length=80)
    country = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)


class Model(models.Model):
    name = models.CharField(max_length=50)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.car}-{self.name}"


class Order(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk)
