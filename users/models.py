from django.db import models

class UserDetails(models.Model):
    # Character Fields
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=50)
    mobile = models.CharField(max_length=15)  # Assuming mobile is a character field

    # Numeric Fields
    age = models.IntegerField()
    height = models.FloatField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)

    # Date and Time Fields
    birth_date = models.DateField()
    last_login = models.DateTimeField()

    # Boolean Field
    is_active = models.BooleanField(default=True)

    # Email and File Fields
    email = models.EmailField()
    profile_picture = models.ImageField(upload_to='profile_pics/')

    # AutoField
    user_id = models.AutoField(primary_key=True)

    # Slug and URL Fields
    user_slug = models.SlugField(max_length=50)
    personal_website = models.URLField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
