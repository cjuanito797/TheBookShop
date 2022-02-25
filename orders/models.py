import random
from django.db import models
from accounts.models import User
from library.models import Book


# Create your models here.

def create_ref_number():
    return str (random.randint (100000, 999999))


class Order (models.Model):
    id = models.CharField (
        primary_key=True,
        max_length=6,
        blank=True,
        editable=False,
        unique=True,
        default=create_ref_number ( )
    )

    user = models.ForeignKey (User,
                              related_name='user',
                              on_delete=models.CASCADE,
                              default=None
                              )
    created = models.DateTimeField (auto_now_add=True)
    updated = models.DateTimeField (auto_now_add=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created', )
        unique_together = (("user", "id", "created"), )

    def __str__(self):
        return f'{self.id}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order,
                              related_name='items',
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Book,
                                related_name='order_items',
                                on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
