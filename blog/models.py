from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,
                     self).get_queryset() \
                     .filter(status='published')
               
class Post(models.Model):
    """docstring for Posts."""
    STATUS_CHOICES = (
        ('drafy','Draft'),
        ('published','Published'),
        )
    
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_posts')
    title = models.CharField(max_length = 200)
    slug = models.SlugField(max_length = 200,
                            unique_for_date='publish',
                            null='Null')
    text = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')
    objects=models.Manager() #the default manager
    published = PublishedManager() # Our custom manager.
    class Meta:
        ordering = ('-publish',)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.publish.year,
                            self.publish.month,
                            self.publish.day,
                            self.slug])
