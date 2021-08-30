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

    
