from django.contrib import admin
from .models import Category, MenuItem, Cart, CartItem, Order, OrderItem, Table, Reservation, Review, ContactMessage

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'is_available')
    list_filter = ('category', 'is_available')
    search_fields = ('name', 'description')

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'updated_at')
    search_fields = ('user__username',)

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'menu_item', 'quantity')
    search_fields = ('cart__user__username', 'menu_item__name')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'status', 'total_amount', 'payment_status', 'created_at')
    list_filter = ('status', 'payment_status')
    search_fields = ('user__username',)

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'menu_item', 'quantity', 'price')
    search_fields = ('order__user__username', 'menu_item__name')

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('name', 'capacity', 'category', 'is_available')
    list_filter = ('category', 'is_available')
    search_fields = ('name',)

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('user', 'table', 'date', 'time', 'guests', 'status')
    list_filter = ('status', 'date')
    search_fields = ('user__username', 'table__name')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'rating', 'created_at')
    list_filter = ('rating',)
    search_fields = ('user__username', 'comment')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'city', 'created_at')
    search_fields = ('name', 'email', 'city', 'message') 