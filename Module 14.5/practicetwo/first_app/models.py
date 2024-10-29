from django.db import models

# Create your models here.

class MyModel(models.Model):
    # auto_field = models.AutoField(primary_key=True)
    # big_auto_field = models.BigAutoField(primary_key=True)
    # binary_field = models.BinaryField()
    # ---------above field issue----------
    
    # big_integer_field = models.BigIntegerField()    
    # boolean_field = models.BooleanField()
    # char_field = models.CharField(max_length=255)
    
    # comma_separated_field = models.CharField(
    #     # validators=[comma_separated_validator],
    #     max_length=255
    # )
    
    # date_field = models.DateField()
    # date_time_field = models.DateTimeField()
    # decimal_field = models.DecimalField(max_digits=5, decimal_places=2)
    # duration_field = models.DurationField()
    # email_field = models.EmailField()
    # file_field = models.FileField(upload_to='files/')


    # file_path_field = models.FilePathField(path='/path/to/files/') //issue
    float_field = models.FloatField()
    image_field = models.ImageField(upload_to='images/')
    integer_field = models.IntegerField()
    json_field = models.JSONField()

    slug_field = models.SlugField()
    time_field = models.TimeField()
    url_field = models.URLField()
    uuid_field = models.UUIDField()
        
        





