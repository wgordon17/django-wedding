from django.db import models
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver


class Article(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    background_image = models.FileField(upload_to='Wedding/backgrounds')
    order = models.PositiveSmallIntegerField(default=0, help_text='This value is used in determining the order in which to display individual pages')

    def title_id(self):
        return self.title.replace(" ", "_").lower()

    def __str__(self):
        return self.title

    class Meta():
        ordering = ['order']


@receiver(pre_save, sender=Article)
def article_remove_old_pics_on_save(sender, **kwargs):
    instance = kwargs['instance']
    if instance.id is not None:
        prev_image = sender.objects.get(id=instance.id).background_image
        storage, path = prev_image.storage, prev_image.path
        storage.delete(path)

@receiver(post_delete, sender=Article)
def article_remove_old_pics_on_delete(sender, **kwargs):
    instance = kwargs['instance']
    prev_image = instance.background_image
    storage, path = prev_image.storage, prev_image.path
    storage.delete(path)
