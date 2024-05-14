from django.db import migrations


def create_initial_data(apps, schema_editor):
    Device = apps.get_model('datarecovery', 'Device')
    FileType = apps.get_model('datarecovery', 'FileType')

    devices = ['Phone', 'Laptop', 'SSD', 'HDD', 'USB Drive']
    file_types = ['Photos', 'Documents', 'Videos']

    for device in devices:
        Device.objects.create(name=device)

    for file_type in file_types:
        FileType.objects.create(name=file_type)


class Migration(migrations.Migration):
    dependencies = [
        ('datarecovery', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_initial_data),
    ]
