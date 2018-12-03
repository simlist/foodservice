from django.db import models

# Create your models here.
class Cart(models.Model):
    time = models.DateTimeField(auto_now=True)

    def __iter__(self):
        for line in Cart.lines.all():
            yield line

    def __str__(self):
        print('cart', self.time)


class Line(models.Model):
    cart = models.ForeignKey(Cart, related_name='lines', on_delete=models.CASCADE)
    item = models.ForeignKey('shop.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __string__(self):
        return str(self.item)

    def price(self):
        return self.item.price() * self.quantity
