from django.contrib import admin
from myApp.models import Category,Post


class categoryAdmin(admin.ModelAdmin):
    list_display = ('image_tag','title','description',"add_date")
    search_fields = ('title',)

class postAdmin(admin.ModelAdmin):
    list_display = ('image_tag','title','cat')       # its show data in a list title , category  and pass tuple
    search_fields = ('title',)          # it search the record by title  and pass tuple
    list_filter = ('cat',)              # it filter the reecord by category  and pass tuple
    list_per_page = 50
    
    # class Media():
    #     js =('https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js','js/script.js',)

admin.site.register(Category,categoryAdmin)
admin.site.register(Post,postAdmin)
