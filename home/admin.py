from django.contrib import admin
from .models import Color,UserDetails,Restaurant
from django.http import HttpResponseRedirect
from .models import LoginEntry
from .models import Blog
from django.urls import reverse
from .models import Restaurant
from django.urls import path
from django.shortcuts import render

from django.urls import reverse, NoReverseMatch

# Register your models here.


admin.site.register(Color)
admin.site.register(UserDetails)
# admin.site.register(Restaurant)
@admin.register(LoginEntry)
class LoginAdmin(admin.ModelAdmin):
    def changelist_view(self, request, extra_context=None):
        return HttpResponseRedirect('/custom-login/')  # URL to your login template

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'phone']
    
    def get_urls(self):
        """Add custom URLs to admin"""
        urls = super().get_urls()
        custom_urls = [
            path('custom-restaurant-view/', 
                 self.admin_site.admin_view(self.custom_restaurant_view),
                 name='restaurant_custom_view'),
        ]
        return custom_urls + urls
    
    def custom_restaurant_view(self, request):
        """Custom view method - now render is properly imported"""
        # Get all restaurants to pass to template
        restaurants = Restaurant.objects.all()
        
        context = {
            'title': 'Custom Restaurant View',
            'restaurants': restaurants,
            'opts': self.model._meta,
            'has_permission': True,
            'total_count': restaurants.count(),
            'active_count': restaurants.filter(is_active=True).count() if hasattr(Restaurant, 'is_active') else 0,
        }
        
        # This will now work because render is imported
        return render(request, 'restaurant_custom.html', context)
    
    def changelist_view(self, request, extra_context=None):
        try:
            return HttpResponseRedirect(reverse('restaurant_custom_view'))
        except NoReverseMatch:
        # Fall back to normal changelist view if reverse fails
            return super().changelist_view(request, extra_context)
      
    

# Register the model with custom admin
admin.site.register(Restaurant, RestaurantAdmin)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    def changelist_view(self, request, extra_context=None):
        # Don't let Django try to access Blog.objects.all()
        return render(request, "blog.html", {"message": "Hello from admin blog view!"})

    def has_add_permission(self, request): return False
    def has_change_permission(self, request, obj=None): return False
    def has_delete_permission(self, request, obj=None): return False
