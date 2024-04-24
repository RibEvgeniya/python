from django.contrib import admin
from .models import Client,Employee,Branch,Contract

# Register your models here.

class BranchInstanceInline(admin.TabularInline):
    model=Employee

class EmployeeInstanceInline(admin.TabularInline):
    model=Contract

class ClientInstanceInline(admin.TabularInline):
    model=Contract

class ClientModelAdmin(admin.ModelAdmin):
    list_display=['__unicode__','name','surname','patronymic','phone']
    list_display_links = ['name','surname','patronymic']
    list_filter=['surname']
    search_fields = ['name','surname','patronymic','phone']

    inlines = [ClientInstanceInline]
    class Meta:
        model=Client
class BranchModelAdmin(admin.ModelAdmin):
    list_display=['__unicode__','name','city','adress','phone']
    list_display_links = ['name','city']
    list_filter=['name']
    search_fields = ['name','city','phone']

    inlines=[BranchInstanceInline]
    class Meta:
        model=Branch

class EmployeeModelAdmin(admin.ModelAdmin):
    list_display=['__unicode__','name','surname','patronymic','phone','email','branch']
    list_display_links = ['surname']
    list_filter=['surname']
    search_fields = ['surname','phone','email','branch']
    list_editable = ['email']


    inlines = [EmployeeInstanceInline]
    class Meta:
        model=Employee

class ContractModelAdmin(admin.ModelAdmin):
    list_display=['__unicode__','name_of_insurance','object','client','employee','client']
    list_display_links = ['name_of_insurance','object','client','employee','client']
    list_filter=['name_of_insurance']
    search_fields = ['name_of_insurance','object','client','employee','client']
    class Meta:
        model=Contract


admin.site.register(Client,ClientModelAdmin)
admin.site.register(Employee,EmployeeModelAdmin)
admin.site.register(Branch,BranchModelAdmin)
admin.site.register(Contract,ContractModelAdmin)