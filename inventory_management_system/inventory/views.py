from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

from .models import *

from .forms import *


def index(request):
    return render(request, 'inv/index.html')

def display_laptops(request):
    items = Laptops.objects.all()
    context = {
        'items': items,
        'header': 'Laptops',
    }
    return render(request, 'inv/index.html', context)


def display_desktops(request):
    items = Desktops.objects.all()
    context = {
        'items': items,
        'header': 'Desktops',
    }
    return render(request, 'inv/index.html', context)


def display_mobiles(request):
    items = Mobiles.objects.all()
    context = {
        'items': items,
        'header': 'Mobiles',
    }
    return render(request, 'inv/index.html', context)

def display_printers(request):
    items = Printers.objects.all()
    context = {
        'items': items,
        'header': 'Printers',
    }
    return render(request, 'inv/index.html', context)

def display_routers(request):
    items = Routers.objects.all()
    context = {
        'items': items,
        'header': 'Routers',
    }
    return render(request, 'inv/index.html', context)

# ---------------
def display_toughpad(request):
    items = Toughpad.objects.all()
    context = {
        'items': items,
        'header': 'Toughpad',
    }
    return render(request,'inv/index.html', context)
def display_toughbook(request):
    items = Toughbook.objects.all()
    context = {
        'items': items,
        'header': 'Toughbook',
    }
    return render(request,'inv/index.html', context)
# ---------------

def add_item(request, cls):
    if request.method == "POST":
        form = cls(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = cls()
        return render(request, 'inv/add_new.html', {'form' : form})


def add_laptop(request):
    return add_item(request, LaptopForm)

def add_desktop(request):
    return add_item(request, DesktopForm)


def add_mobile(request):
    return add_item(request, MobileForm)

def add_printers(request):
    return add_item(request, PrinterForm)

def add_routers(request):
    return add_item(request, RouterForm)
# ------
def add_toughpad(request):
    return add_item(request,ToughpadForm)

def add_toughbook(request):
    return add_item(request, ToughbookForm)
# --------

def edit_item(request, pk, model, cls):
    item = get_object_or_404(model, pk=pk)

    if request.method == "POST":
        form = cls(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = cls(instance=item)

        return render(request, 'inv/edit_item.html', {'form': form})



def edit_laptop(request, pk):
    return edit_item(request, pk, Laptops, LaptopForm)


def edit_desktop(request, pk):
    return edit_item(request, pk, Desktops, DesktopForm)


def edit_mobile(request, pk):
    return edit_item(request, pk, Mobiles, MobileForm)

def edit_printers(request, pk):
    return edit_item(request, pk, Printers, PrinterForm)

def edit_routers(request, pk):
    return edit_item(request, pk, Routers, RouterForm)
# ----
def edit_toughpad(request, pk):
    return edit_item(request, pk, Routers, ToughpadForm)
def edit_toughbook(request, pk):
    return edit_item(request, pk, Routers, ToughbookForm)
# ----


def delete_laptop(request, pk):

    template = 'inv/index.html'
    Laptops.objects.filter(id=pk).delete()

    items = Laptops.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)


def delete_desktop(request, pk):

    template = 'inv/index.html'
    Desktops.objects.filter(id=pk).delete()

    items = Desktops.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)


def delete_mobile(request, pk):

    template = 'inv/index.html'
    Mobiles.objects.filter(id=pk).delete()

    items = Mobiles.objects.all()

    context = {
        'items': items,
    }

def delete_printers(request, pk):

    template = 'inv/index.html'
    Printers.objects.filter(id=pk).delete()

    items = Printers.objects.all()

    context = {
        'items': items,
    }    

    return render(request, template, context)

def delete_routers(request, pk):

    template = 'inv/index.html'
    Routers.objects.filter(id=pk).delete()

    items = Routers.objects.all()

    context = {
        'items': items,
    }    
    
    return render(request, template, context)


# ----
def delete_toughpad(request, pk):

    template = 'inv/index.html'
    Toughpad.objects.filter(id=pk).delete()

    items = Toughpad.objects.all()

    context = {
        'items': items,
    }    
    
    return render(request, template, context)
def delete_toughbook(request, pk):

    template = 'inv/index.html'
    Toughbook.objects.filter(id=pk).delete()

    items = Toughbook.objects.all()

    context = {
        'items': items,
    }    
    
    return render(request, template, context)
# ----

