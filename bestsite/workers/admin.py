from django.contrib import admin
from .models import Worker
from .models import Contact
from .models import Adress
# Register your models here.

class ViewColombsWorker(admin.ModelAdmin):
    list_display = ['id', 'name', 'fname', 'create_date', 'balance']
    list_display_links = ['name', 'fname', 'create_date', 'balance']
    list_filter = ['create_date', 'balance']
    search_fields = ['name', 'fname']
    class Meta():
        model = Worker

class ViewColombsAdress(admin.ModelAdmin):
    list_display = ['worker', 'indx', 'region', 'sity', 'street', 'home']
    list_display_links = ['worker', 'indx', 'region', 'sity', 'street', 'home']
    list_filter = ['region', 'sity']
    # search_fields = ['name', 'fname']
    class Meta():
        model = Adress


class ViewColombsContact(admin.ModelAdmin):
    list_display = ['worker', 'type_contact', 'contact']
    list_display_links = ['worker', 'type_contact', 'contact']
    list_filter = ['type_contact']
    # search_fields = ['name', 'fname']
    class Meta():
        model = Contact

admin.site.register(Worker, ViewColombsWorker)
admin.site.register(Contact, ViewColombsContact)
admin.site.register(Adress, ViewColombsAdress)



# admin.site.register(Worker)
