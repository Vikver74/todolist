from django.contrib import admin

from goals.models import GoalCategory, GoalComment, Goal, Board, BoardParticipant


class GoalCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created', 'updated', 'board')
    search_fields = ('title', 'user')


class GoalCommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'user', 'created', 'updated', )
    search_fields = ('text', 'user')


class GoalAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'user', 'created', 'updated', )
    search_fields = ('title', 'description', 'user')


class BoardAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_deleted')


class BoardParticipantAdmin(admin.ModelAdmin):
    list_display = ('board', 'user', 'role')


admin.site.register(GoalCategory, GoalCategoryAdmin)
admin.site.register(GoalComment, GoalCommentAdmin)
admin.site.register(Goal, GoalAdmin)
admin.site.register(Board, BoardAdmin)
admin.site.register(BoardParticipant, BoardParticipantAdmin)
