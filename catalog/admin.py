from django.contrib import admin
from django import forms
from .models import Post, Image, User, TypeUser

# Create an inline formset for the Image model
ImageFormSet = forms.inlineformset_factory(Post, Image, fields=('image',), extra=1, max_num=10)

# Define the ImageInline class for inline display of images in the Post admin
class ImageInline(admin.TabularInline):
    model = Image
    formset = ImageFormSet
    extra = 1

# Register the Post model with the ImageInline formset in the admin site
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [ImageInline]

admin.site.register(User)
admin.site.register(TypeUser)