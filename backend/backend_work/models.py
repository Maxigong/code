from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class ImgModel(models.Model):
    img = models.ImageField(
        upload_to="uploads/",
        max_length=100,
        blank=True,
        null=True,)

    def get_image(self):
        print
        if self.img:
            return 'http://127.0.0.1:8000' + self.img.url
        return ''


class FormModel(models.Model):
    name = models.CharField(max_length=150)
    title = models.CharField(max_length=250)
    text = models.TextField()

    class Meta:
        verbose_name_plural = 'Forms'

    def __str__(self):
        return self.name


class AuthorModel(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=254)

    class Meta:
        verbose_name_plural = "Authors"

    def __str__(self):
        return self.name


class TagsModel(models.Model):
    tag = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.tag


class PostModel(models.Model):
    title = models.CharField(max_length=50)
    Author = models.ForeignKey(
        AuthorModel, related_name='post', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, unique=True, editable=True)
    body = RichTextField()
    tag = models.ManyToManyField(TagsModel)
    description = models.CharField(max_length=250)
    date = models.DateField(auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name_plural = "Post"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(PostModel, self).save(*args, **kwargs)


class CommentsModel(models.Model):
    name = models.CharField(max_length=150)
    title = models.CharField(max_length=150)
    messege = models.TextField(max_length=800)
    data = models.DateField(auto_now=True, auto_now_add=False)
    post = models.ForeignKey(
        PostModel, null=True, related_name='comments', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Comments"

    def __str__(self):
        return self.name
