from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50)
    image = models.ImageField(upload_to='photo/', blank=True, null=True)
    is_available = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

class Booking(models.Model):
    customer_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    date = models.DateField()
    time = models.TimeField()
    guests = models.IntegerField()
    special_request = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.customer_name} - {self.date}"

# ← Review ต้องอยู่นอก class Booking (ไม่มี indent)
class Review(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField(choices=[(5, '5 ดาว'), (4, '4 ดาว'), (3, '3 ดาว'), (2, '2 ดาว'), (1, '1 ดาว')], default=5)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.rating} ดาว"