from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


# Register your models here.
class ArticlesAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Articles
        fields = '__all__'


class ArticlesAdmin(admin.ModelAdmin):
    form = ArticlesAdminForm
    list_display = ['title', 'get_icon', 'description', 'created_at', 'is_published']
    list_display_links = ['title', 'get_icon', 'description', 'created_at']
    list_editable = ['is_published']


    def get_icon(self, obj):
        if obj.icon:
            return mark_safe(f'<img src="{obj.icon.url}" width="70px" height="70px"')
        else:
            return '-'

    get_icon.short_description = 'Иконка'


class FeedBackAdmin(admin.ModelAdmin):
    list_display = ['FIO', 'email', 'text', 'date']
    readonly_fields = ['FIO', 'email', 'text', 'date']

admin.site.register(Articles, ArticlesAdmin)
admin.site.register(FeedBack, FeedBackAdmin)

admin.site.site_title = 'Управление сайтом'
admin.site.site_header = 'Управление сайтом'
