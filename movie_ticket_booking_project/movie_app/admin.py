from django.contrib import admin
from .models import MovieCategory, Movie, Cart, CartItems

@admin.register(MovieCategory)
class MovieCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'created_at', 'updated_at')
    search_fields = ('category_name',)
    list_filter = ('created_at',)

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('movie_name', 'category', 'price', 'created_at')
    search_fields = ('movie_name',)
    list_filter = ('category',)
    ordering = ('created_at',)

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_paid', 'created_at')
    search_fields = ('user__username',)
    list_filter = ('is_paid',)

@admin.register(CartItems)
class CartItemsAdmin(admin.ModelAdmin):
    list_display = ('cart', 'movie', 'created_at')
    search_fields = ('movie__movie_name',)
    list_filter = ('cart',)
