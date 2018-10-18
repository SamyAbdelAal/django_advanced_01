from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from .models import Inventory
def inventory_list(request):
    inventories = Inventory.objects.all()
   
    context = {
       "inventories": inventories,
    }
    return render(request, 'inventory_list.html', context)