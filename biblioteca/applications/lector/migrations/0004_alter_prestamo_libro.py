# Generated by Django 3.2.8 on 2021-10-13 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0002_alter_libro_categoria'),
        ('lector', '0003_auto_20211012_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamo',
            name='libro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='libro_prestamo', to='libro.libro'),
        ),
    ]