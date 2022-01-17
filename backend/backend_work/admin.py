from django.contrib import admin

from .models import ImgModel, FormModel, AuthorModel, TagsModel, PostModel, CommentsModel
# CommentsModel


# class CommentItemInline(admin.TabularInline):
#     model = CommentsModel
#     raw_id_fields = ['post']


class FormModelAdmi(admin.ModelAdmin):
    list_diplay = ('name', 'title', "text",)


class CommentAdmi(admin.ModelAdmin):
    list_diplay = ('name', 'title', "date",)


class PostModelAdmi(admin.ModelAdmin):
    list_diplay = ('title', "author",)
    prepopulated_fields = {'slug': ('title',), }
    # inlines = [CommentItemInline]


admin.site.register(TagsModel)
admin.site.register(CommentsModel, CommentAdmi)
admin.site.register(AuthorModel)
admin.site.register(PostModel, PostModelAdmi)
admin.site.register(FormModel, FormModelAdmi)
