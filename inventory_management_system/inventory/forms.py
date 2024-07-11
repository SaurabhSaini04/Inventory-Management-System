from django import forms
from .models import *

class LaptopForm(forms.ModelForm):
    class Meta:
        model = Laptops
        fields = ('type', 'price', 'user_name','department','status', 'issues')


class DesktopForm(forms.ModelForm):
    class Meta:
        model = Desktops
        fields = ('type', 'price', 'user_name','department','status', 'issues')
        

class MobileForm(forms.ModelForm):
    class Meta:
        model = Mobiles
        fields = ('type', 'price', 'user_name','department','status', 'issues')


class PrinterForm(forms.ModelForm):
    class Meta:
        model = Printers
        fields = ('type', 'price', 'user_name','department','status', 'issues')

class RouterForm(forms.ModelForm):
    class Meta:
        model = Routers
        fields = ('type', 'price', 'user_name', 'department', 'status', 'issues')
# ----
class ToughpadForm(forms.ModelForm):
    class Meta:
        model = Toughpad
        fields = ('type','price','user_name', 'department', 'status', 'issues')
class ToughbookForm(forms.ModelForm):
    class Meta:
        model = Toughbook
        fields = ('type','price','user_name', 'department', 'status', 'issues')
# -----