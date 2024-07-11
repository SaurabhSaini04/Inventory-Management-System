# Generated by Django 2.1 on 2024-07-05 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0007_auto_20240704_1529'),
    ]

    operations = [
        migrations.CreateModel(
            name='Toughbook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('user_name', models.CharField(max_length=200)),
                ('department', models.CharField(choices=[('QUALITY', 'Quality'), ('MAINTENANCE', 'Maintenance'), ('MEP', 'MEP'), ('PROJECTS_CENTER_SERVICES', 'Projects & Center Services'), ('SAFETY', 'Safety'), ('PROGRAM_MANAGEMENT', 'Program Management'), ('FABRICATIONS_OPERATIONS', 'Fabrications Operations'), ('RECEPTIONS', 'Receptions'), ('COMPLIANCE_TEAM', 'Compliance Team'), ('HUMAN_RESOURCE', 'Human Resource'), ('CENTRAL_PURCHASE', 'Central Purchase'), ('FINANCE', 'Finance'), ('NPP', 'NPP'), ('PRODUCTION_ENGINEERING', 'Production Engineering'), ('DESIGN_CENTER', 'Design Center'), ('SERVICE_TEAM', 'Service Team'), ('IT', 'IT'), ('NETWORK', 'Network')], max_length=200)),
                ('status', models.CharField(choices=[('AVAILABLE', 'Item ready to be purchased'), ('SOLD', 'Item already purchased'), ('RESTOCKING', 'Item restocking in few days'), ('NOT AVAILABLE', 'Item currently not available')], default='SOLD', max_length=10)),
                ('issues', models.CharField(default='No Issues', max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Toughpad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('user_name', models.CharField(max_length=200)),
                ('department', models.CharField(choices=[('QUALITY', 'Quality'), ('MAINTENANCE', 'Maintenance'), ('MEP', 'MEP'), ('PROJECTS_CENTER_SERVICES', 'Projects & Center Services'), ('SAFETY', 'Safety'), ('PROGRAM_MANAGEMENT', 'Program Management'), ('FABRICATIONS_OPERATIONS', 'Fabrications Operations'), ('RECEPTIONS', 'Receptions'), ('COMPLIANCE_TEAM', 'Compliance Team'), ('HUMAN_RESOURCE', 'Human Resource'), ('CENTRAL_PURCHASE', 'Central Purchase'), ('FINANCE', 'Finance'), ('NPP', 'NPP'), ('PRODUCTION_ENGINEERING', 'Production Engineering'), ('DESIGN_CENTER', 'Design Center'), ('SERVICE_TEAM', 'Service Team'), ('IT', 'IT'), ('NETWORK', 'Network')], max_length=200)),
                ('status', models.CharField(choices=[('AVAILABLE', 'Item ready to be purchased'), ('SOLD', 'Item already purchased'), ('RESTOCKING', 'Item restocking in few days'), ('NOT AVAILABLE', 'Item currently not available')], default='SOLD', max_length=10)),
                ('issues', models.CharField(default='No Issues', max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]