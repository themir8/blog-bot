from django.contrib import admin

from .models import Article, ArticleView, Category, Blog, BlogSubscribers


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', "name", "owner")
    list_display_links = ('id',)
    search_fields = ('owner', "name")
    save_as = True


@admin.register(BlogSubscribers)
class BlogSubscribersAdmin(admin.ModelAdmin):
    def has_add_permission(self, request) -> bool:
        return False

    def has_change_permission(self, request, obj=None):
        return False
    list_display = ('id', "subscriber", "blog")
    list_display_links = ('id',)
    search_fields = ('subscriber', "blog")
    save_as = True


admin.site.register(Article)
admin.site.register(Category)
admin.site.register(ArticleView)
