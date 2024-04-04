from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[str(self.id)])

    def __str__(self):
        return self.title
    
    # class Meta:
    #     ordering = ['title', 'content']
    #     verbose_name = 'author'
    #     verbose_name_plural = ['created_date', 'published_date']

    #     def get_absolute_url(self):
    #         return reverse('blog:post_detail', args=[str(self.ordering)])

    #     def __str__(self):
    #         return self.verbose_name

