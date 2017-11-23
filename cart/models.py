from django.db import models

# Create your models here.
class Line(models.Model):
    cart = models.ForeignKey('cart.Cart')
    item = models.ForeignKey('shop.Item', on_delete=models.CASCADE)
    quantity = models.IntegerField()


    def __string__(self):
        return str(self.item)

    def price(self):
        return self.item.price() * self.quantity


class Cart(models.Model):
    time = models.DateTimeField(auto_now=True)
