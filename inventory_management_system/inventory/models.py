from django.db import models

# Create your models here.

class Device(models.Model):

    type = models.CharField(max_length=200, blank=False)
    price = models.IntegerField()
    user_name = models.CharField(max_length=200) # koi aur model ho users ki to vo bhi daal skte

    choices_department = (
                        ('QUALITY', 'Quality'),
                        ('MAINTENANCE', 'Maintenance'),
                        ('MEP', 'MEP'),
                        ('PROJECTS_CENTER_SERVICES', 'Projects & Center Services'),
                        ('SAFETY', 'Safety'),
                        ('PROGRAM_MANAGEMENT', 'Program Management'),
                        ('FABRICATIONS_OPERATIONS', 'Fabrications Operations'),
                        ('RECEPTIONS', 'Receptions'),
                        ('COMPLIANCE_TEAM', 'Compliance Team'),
                        ('HUMAN_RESOURCE', 'Human Resource'),
                        ('CENTRAL_PURCHASE', 'Central Purchase'),
                        ('FINANCE', 'Finance'),
                        ('NPP', 'NPP'),
                        ('PRODUCTION_ENGINEERING', 'Production Engineering'),
                        ('DESIGN_CENTER', 'Design Center'),
                        ('SERVICE_TEAM', 'Service Team'),
                        ('IT', 'IT'),
                        ('NETWORK', 'Network'),
                        )
    department = models.CharField(max_length=200,choices=choices_department )


    choices = (
        ('AVAILABLE', 'Item ready to be purchased'),
        ('SOLD', 'Item already purchased'),
        ('RESTOCKING', 'Item restocking in few days'),
        ('NOT AVAILABLE','Item currently not available')
    )

    status = models.CharField(max_length=10, choices=choices, default='SOLD')
    issues = models.CharField(max_length=50, default="No Issues")

    # date = models.DateField()



    class Meta:
        abstract = True

    def __str__(self):
        return 'Type: {0} Price: {1}'.format(self.type, self.price)

class Desktops(Device):
    pass

class Laptops(Device):
    pass

class Mobiles(Device):
    pass

class Printers(Device):
    pass

class Routers(Device):
    pass
# ----------
class Toughpad(Device):
    pass
class Toughbook(Device):
    pass
# -----------

class employee(models.Model):
    emp_id = models.IntegerField()
    name = models.CharField(max_length=50)
    emp_dep = models.CharField(max_length=50)

class department(models.Model):
    dep_id = models.IntegerField()
    dep_name = models.CharField(max_length=50)

# class Desktops(models.Model):
#     type = models.CharField(max_length=200, blank=False)
#     price = models.IntegerField()
#
#     choices = (
#         ('SOLD', 'Item already purchased'),
#         ('AVAILABLE', 'Item ready to be purchased'),
#         ('RESTOCKING', 'Item restocking in few days')
#     )
#
#     status = models.CharField(max_length=10, choices=choices, default='SOLD')
#     issues = models.CharField(max_length=50, default="No Issues")
#
#     def __str__(self):
#         return 'Type: {0} Price: {1}'.format(self.type, self.price)
#
#
# class Laptops(models.Model):
#     type = models.CharField(max_length=200, blank=False)
#     price = models.IntegerField()
#
#     choices = (
#         ('SOLD', 'Item already purchased'),
#         ('AVAILABLE', 'Item ready to be purchased'),
#         ('RESTOCKING', 'Item restocking in few days')
#     )
#
#     status = models.CharField(max_length=10, choices=choices, default='SOLD')
#     issues = models.CharField(max_length=50, default="No Issues")
#
#     def __str__(self):
#         return 'Type: {0} Price: {1}'.format(self.type, self.price)
#
#
# class Mobiles(models.Model):
#     type = models.CharField(max_length=200, blank=False)
#     price = models.IntegerField()
#
#     choices = (
#         ('SOLD', 'Item already purchased'),
#         ('AVAILABLE', 'Item ready to be purchased'),
#         ('RESTOCKING', 'Item restocking in few days')
#     )
#
#     status = models.CharField(max_length=10, choices=choices, default='SOLD')
#     issues = models.CharField(max_length=50, default="No Issues")
#
#     def __str__(self):
#         return 'Type: {0} Price: {1}'.format(self.type, self.price)
