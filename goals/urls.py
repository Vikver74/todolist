from django.urls import path

from goals.views import GoalCategoryCreateAPIView, GoalCategoryListAPIView, GoalCategoryDetailUpdateDelete

urlpatterns = [
    path('goal_category/create', GoalCategoryCreateAPIView.as_view(), name='goal_category_create'),
    path('goal_category/list', GoalCategoryListAPIView.as_view(), name='goal_category_list'),
    path('goal_category/<int:pk>', GoalCategoryDetailUpdateDelete.as_view(), name='goal_category_detail_update_delete'),
]
