

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Scores',
            fields=[
                ('Id', models.AutoField(auto_created=True, primary_key=True)),
                ('Player_name', models.CharField(max_length=50)),
                ('Score', models.BigIntegerField(max_length=50)),
            ],
            options={
                'db_table': 'scores',
            },
        ),
    ]
