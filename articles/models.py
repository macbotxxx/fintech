from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Blog (models.Model):
    """
    this is the db structure for the blog post.
    """

    title = models.CharField(
        verbose_name= _('Blog Title'),
        max_length=200, null = True,
        unique = True,
        help_text = _('Blog title for this particular blog')
        )
    
    img = models.ImageField(
        verbose_name= _('Post Image'),
        null = True,
        # default = "my_image/default.jpg",
        upload_to = "blog_post/",
        help_text = _('Blog post image ')
    )

    # amount = models.FloatField(
          
    # )

    # amount = models.PositiveIntegerField(

    # )

    # description = models.TextField (

    # )
    


    class Meta:
        verbose_name = _('Blog')
        verbose_name_plural = _('Blog')

    def __str__(self):
        return str(self.title)

ALL_GEARS = (
    ('Manual' ,'Manual'),
    ('Automatic' , 'Automatic'),
)
    
class My_Cars (models.Model):

    car_name = models.CharField(
        verbose_name=_('Car Name'),
        max_length=250,
        null=True, 
        help_text=_('the name of the car'))

    price_tag = models.PositiveIntegerField(
        verbose_name=_('Price'),
        null=True,
        help_text=_('the price tag of the current car')
    )

    img1 = models.ImageField(
        verbose_name=_('Image 1'),
        null=True,
        upload_to = 'car_images/',
        help_text=_('the first image of the car')
    )

    img2 = models.ImageField(
        verbose_name=_('Image 2'),
        null=True,
        upload_to = 'car_images/',
        help_text=_('the second image of the car')
    )

    img3 = models.ImageField(
        verbose_name=_('Image 3'),
        null=True,
        upload_to = 'car_images/',
        help_text=_('the third image of the car')
    )

    gear = models.CharField(
        choices=ALL_GEARS,
        verbose_name=_('Car Gear'),
        null=True,
        max_length=250,
        help_text=_('the gear of the current car')
    )

    door = models.CharField(
    verbose_name=_('Car Door'),
    max_length=10,
    null=True,
    help_text=_('the door of the current car')
    )

    color = models.CharField(
        verbose_name=_('Car Color'),
        null=True,
        max_length=250,
        help_text=_('the color of the car')
    )

    spear_tyre = models.BooleanField(
        verbose_name=_('Spear Tyre'),
        default=False,
        null=True,
        help_text=_('the current status of the car spear tyre')
    )

    description = models.TextField(
        verbose_name=_('Description of the car'),
        null=True,
        help_text=_('the description of the car'),
    )


    #Metadata
    class Meta :
        verbose_name = _('My Car')
        verbose_name_plural = _('My Car')

    #Methods
    # def get_absolute_url(self):
    #     return reverse('url', args=[args])

    def __str__(self):
        return self.car_name