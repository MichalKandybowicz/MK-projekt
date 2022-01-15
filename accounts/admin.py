from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from backend.models import CustomUser, ConfigLvl, Item, Monster,\
    MonsterStatisticIncrease, Region, Ritual, Shop, Warehouse
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('username', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('username', 'cash_balance', 'coin_balance')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('id', 'email', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(ConfigLvl)
admin.site.register(Item)
admin.site.register(Monster)
admin.site.register(MonsterStatisticIncrease)
admin.site.register(Region)
admin.site.register(Ritual)
admin.site.register(Shop)
admin.site.register(Warehouse)
