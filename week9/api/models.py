from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }

class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField(default='')
    count = models.IntegerField()

    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'count': self.count
        }
