# Generated by Django 4.1.3 on 2022-12-06 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0005_rename_skiptest_skiptestn50s'),
    ]

    operations = [
        migrations.CreateModel(
            name='n50sict2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Componente', models.CharField(max_length=30)),
                ('Falha', models.CharField(choices=[('preshort', 'preshort'), ('short', 'short'), ('analog', 'analog'), ('vectorless', 'vectorless')], max_length=30)),
                ('Motivo', models.CharField(max_length=50)),
                ('modelo', models.CharField(choices=[('NEO50s', 'NEO50s'), ('M75', 'M75'), ('IDEAPAD3i', 'IDEAPAD3i'), ('IDEAPAD3a', 'IDEAPAD3a'), ('IDEAPAD1', 'IDEAPAD1'), ('E14', 'E14')], max_length=30)),
                ('data', models.DateField(auto_now_add=True)),
                ('atualizado', models.TimeField(auto_now_add=True)),
                ('status', models.CharField(blank=True, choices=[('ON', 'ON'), ('OFF', 'OFF')], default='OFF', max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='skiptestn50s',
        ),
    ]
