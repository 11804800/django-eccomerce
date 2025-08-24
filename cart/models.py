from django.db import models
from products.models import Products

class Cart(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    
    def get_total_price(self):
        return sum(items.get_total_price() for items in self.items.all() )
    
    
class CartItem(models.Model):
    product=models.ForeignKey(Products,related_name="cart_items",on_delete=models.CASCADE)
    cart=models.ForeignKey(Cart,related_name="items",on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    
    def get_total_price(self):
        return self.quantity*self.product.price
    
    def update_quantity(self, new_quantity):
        if new_quantity > 0:
            self.quantity = new_quantity
            self.save()
        else:
            self.delete()