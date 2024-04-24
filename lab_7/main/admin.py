from django.contrib import admin
from . import models

# Register your models here.

class BranchInstanceInline(admin.TabularInline):
    model=models.Employee

class EmployeeInstanceInline(admin.TabularInline):
    model=models.Contract

class ClientInstanceInline(admin.TabularInline):
    model=models.Contract

class ClientModelAdmin(admin.ModelAdmin):
    list_display=['__unicode__','name','surname','patronymic','phone']
    list_display_links = ['name','surname','patronymic']
    list_filter=['surname']
    search_fields = ['name','surname','patronymic','phone']

    inlines = [ClientInstanceInline]
    class Meta:
        model=models.Client
class BranchModelAdmin(admin.ModelAdmin):
    list_display=['__unicode__','name','city','adress','phone']
    list_display_links = ['name','city']
    list_filter=['name']
    search_fields = ['name','city','phone']

    inlines=[BranchInstanceInline]
    class Meta:
        model=models.Branch

class EmployeeModelAdmin(admin.ModelAdmin):
    list_display=['__unicode__','name','surname','patronymic','phone','email','branch']
    list_display_links = ['surname']
    list_filter=['surname']
    search_fields = ['surname','phone','email','branch']
    list_editable = ['email']


    inlines = [EmployeeInstanceInline]
    class Meta:
        model=models.Employee

class ContractModelAdmin(admin.ModelAdmin):
    list_display=['__unicode__','name_of_insurance','object','client','employee','client']
    list_display_links = ['name_of_insurance','object','client','employee','client']
    list_filter=['name_of_insurance']
    search_fields = ['name_of_insurance','object','client','employee','client']
    class Meta:
        model=models.Contract


admin.site.register(models.Client,ClientModelAdmin)
admin.site.register(models.Employee,EmployeeModelAdmin)
admin.site.register(models.Branch,BranchModelAdmin)
admin.site.register(models.Contract,ContractModelAdmin)