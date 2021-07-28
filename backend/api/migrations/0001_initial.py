from django.db import migrations 
from api.user.models import CustomUser

#NOTE:For clarifiaction, this file is viewable on github.  In production, add to .gitignore/.dockerignore. 

class Migration(migrations.Migration):
    """
    New 0001_initial.py file. Created after deleting the db.
    We are creating this file to debug the superuser error that prevents 
    admin from logging on to site. This is because user/passwd was changed to email/passwd
    Their are a lot of potential solutions on stack overflow and this seems to be the most 
    simple soulution. 
    """
    def seed_data(apps, schema_editor):
        user = CustomUser(name="shane",
                email="shane47r@gmail.com",
                is_staff=True,
                is_superuser=True,
                phone="1234567",
                gender="Male"
                )
        user.set_password("changethis")
        user.save()
        dependencies = [] #Can leave this array empty.
        operations = [migrations.RunPython(seed_data),] #Add trailing comma to ensure only one item in list.  
