from django.contrib import admin
from courses.models import Category, Course, Lesson, Tag, Comment
from django.utils.html import mark_safe
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class CourseForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Course
        fields = '__all__'


class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_date', 'updated_date']
    search_fields = ['name', 'descriptions']
    list_filter = ['id', 'name', 'created_date']
    readonly_fields = ['my_image']
    form = CourseForm

    def my_image(self, course):
        if course.image:
            return mark_safe(f"<img width='200' src='{course.image.url}' />")

    class Media:
        css = {
            'all': ['/static/css/style.css']
        }


class LessonAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'created_date', 'updated_date']
    search_fields = ['subject']


admin.site.register(Category)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Tag)
admin.site.register(Comment)

