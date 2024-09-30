from django.db import models
from django.utils.text import slugify
from django.conf import settings

# Create your models here

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, default=None )

    def __str__(self):
        return self.name

class Painting(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='paintings', default=None)
    image = models.ImageField(upload_to="products_images/", default=None, null=True )
    rating = models.DecimalField(decimal_places=1, max_digits=3, default=0.0, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10, default=1000.00, null=True)
    
    is_new = models.BooleanField(default=False)
    is_selling = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    

class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Cart for {self.user.username}'

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    painting = models.ForeignKey(Painting, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    def __str__(self):
        return f'{self.quantity} of {self.painting.title}'

    def get_total_price(self):
        return self.quantity * self.painting.price
