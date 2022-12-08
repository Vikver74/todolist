from django.contrib import admin

from goals.models import GoalCategory, GoalComment, Goal


class GoalCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created', 'updated', )
    search_fields = ('title', 'user')


class GoalCommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'user', 'created', 'updated', )
    search_fields = ('text', 'user')


class GoalAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'user', 'created', 'updated', )
    search_fields = ('title', 'description', 'user')


admin.site.register(GoalCategory, GoalCategoryAdmin)
admin.site.register(GoalComment, GoalCommentAdmin)
admin.site.register(Goal, GoalAdmin)
