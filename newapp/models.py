# from django.db import models

# class Center(models.Model):
#     id = models.AutoField(primary_key=True)
#     centername = models.CharField(max_length=100)

#     def __str__(self):
#         return self.centername
    
# class User(models.Model):
#     name = models.CharField(max_length=100)
#     fathername = models.CharField(max_length=100, default="")
#     mothername = models.CharField(max_length=100, default="")
#     email = models.EmailField(max_length=100, default="")
#     phone = models.CharField(max_length=10, default="")
#     center = models.ForeignKey(Center, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name
# # Create your models here.


from django.db import models

class Center(models.Model):
    id = models.AutoField(primary_key=True)
    centername = models.CharField(max_length=100)

    def __str__(self):
        return self.centername

# class CustomAutoField(models.AutoField):
#     def __init__(self, *args, **kwargs):
#         kwargs.setdefault('default', 10000)
#         super().__init__(*args, **kwargs)

class UserProfile(models.Model):
    registration_number = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    fathername = models.CharField(max_length=100, null=True, blank=True, default="")
    mothername = models.CharField(max_length=100, null=True, blank=True, default="")
    email = models.EmailField(max_length=100, null=True, blank=True, default="")
    phone = models.CharField(max_length=10, null=True, blank=True, default="")
    center = models.ForeignKey(Center, on_delete=models.CASCADE)
    medium = models.CharField(max_length=10, choices=[('EN', 'English'), ('ML', 'Malayalam')], default='EN')
   

    def __str__(self):
        return self.name

#     def save(self, *args, **kwargs):
#         if self.registration_number is None:
#             last_user = UserProfile.objects.all().order_by('registration_number').last()
#             if last_user is not None and last_user.registration_number is not None:
#                 self.registration_number = last_user.registration_number + 1
#             else:
#                 self.registration_number = 10000
#         super().save(*args, **kwargs)
