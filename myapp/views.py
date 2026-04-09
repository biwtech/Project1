from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Menu, Booking, Review

def home(request):
    featured_menu = Menu.objects.filter(is_available=True)[:6]
    reviews = Review.objects.all().order_by('-created_at')[:3]
    return render(request, 'home.html', {
        'featured_menu': featured_menu,
        'reviews': reviews,
    })

def menu(request):
    query = request.GET.get('q')
    category = request.GET.get('category')
    
    menus = Menu.objects.filter(is_available=True)
    
    if query:
        menus = menus.filter(Q(name__icontains=query) | Q(description__icontains=query))
    
    if category:
        menus = menus.filter(category=category)
    
    categories = Menu.objects.values_list('category', flat=True).distinct()
    
    return render(request, 'menu.html', {
        'menus': menus,
        'categories': categories,
        'query': query,
    })

def booking(request):
    # ========== ส่วนจองโต๊ะ ==========
    if request.method == 'POST' and 'name' in request.POST:
        Booking.objects.create(
            customer_name=request.POST['name'],
            phone=request.POST['phone'],
            email=request.POST.get('email', ''),
            date=request.POST['date'],
            time=request.POST['time'],
            guests=request.POST['guests'],
            special_request=request.POST.get('special_request', '')
        )
        messages.success(request, 'จองโต๊ะสำเร็จ!')
        return redirect('booking')
    
    # ========== ส่วนรีวิว ==========
    if request.method == 'POST' and 'revName' in request.POST:
        Review.objects.create(
            name=request.POST['revName'],
            rating=int(request.POST['revStarHidden']),
            message=request.POST['revMessage']
        )
        messages.success(request, 'ส่งรีวิวสำเร็จ!')
        return redirect('booking')
    
    # ========== ดึงข้อมูลแสดงผล ==========
    bookings = Booking.objects.all().order_by('-created_at')
    reviews = Review.objects.all().order_by('-created_at')
    
    return render(request, 'booking.html', {
        'bookings': bookings,
        'reviews': reviews,
    })

def delete_booking(request, id):
    booking = get_object_or_404(Booking, id=id)
    if request.method == 'POST':
        booking.delete()
        messages.success(request, 'ลบการจองสำเร็จ!')
        return redirect('booking')
    return render(request, 'confirm_delete.html', {'booking': booking})

def about(request):
    return render(request, 'about.html')