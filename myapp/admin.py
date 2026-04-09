from django.contrib import admin
from .models import Menu, Booking, Review  # ← เพิ่ม Review ตรงนี้

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'is_available']
    list_filter = ['category', 'is_available']
    search_fields = ['name', 'description']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'date', 'time', 'guests', 'created_at']
    list_filter = ['date', 'created_at']
    search_fields = ['customer_name', 'phone', 'email']
    date_hierarchy = 'date'

# ← Review ต้องอยู่นอก class (ไม่มี indent)
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating', 'created_at']
    list_filter = ['rating', 'created_at']