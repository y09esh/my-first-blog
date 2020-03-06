import django
class Post(django.db.models.Model):
    """docstring for Posts."""
    auther = django.db.models.ForeignKey(django.conf.settings.AUTH_USER_MODEL,on_delete=django.db.models.CASCADE)
    title = django.db.models.CharField(max_length = 200)
    text = django.db.models.TextField()
    created_date = django.db.models.DateTimeField(default = django.utils.timezone.now())
    published_date = django.db.models.DateTimeField(blank = True, null = True)
    def publish(self):
        self.published_date = django.utils.timezone.now()
        self.save()
    def __str__(self):
        return self.title
