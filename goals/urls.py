from django.urls import path

from goals.views import GoalCategoryCreateAPIView, GoalCategoryListAPIView, GoalCategoryDetailUpdateDeleteAPIView, \
    GoalCreateAPIView, GoalListAPIView, GoalDetailUpdateDeleteAPIView, GoalCommentCreateAPIView, \
    GoalCommentListAPIView, GoalCommentDetailUpdateDeleteAPIView, BoardCreateAPIView, BoardListAPIView,\
    BoardDetailUpdateDeleteAPIView

urlpatterns = [
    path('goal_category/create', GoalCategoryCreateAPIView.as_view(), name='goal_category_create'),
    path('goal_category/list', GoalCategoryListAPIView.as_view(), name='goal_category_list'),
    path('goal_category/<int:pk>', GoalCategoryDetailUpdateDeleteAPIView.as_view(),
         name='goal_category_detail_update_delete'),
    path('goal/create', GoalCreateAPIView.as_view(), name='goal_create'),
    path('goal/list', GoalListAPIView.as_view(), name='goal_list'),
    path('goal/<int:pk>', GoalDetailUpdateDeleteAPIView.as_view(), name='goal_detail_update_delete'),
    path('goal_comment/create', GoalCommentCreateAPIView.as_view(), name='goal_comment_create'),
    path('goal_comment/list', GoalCommentListAPIView.as_view(), name='goal_comment_list'),
    path('goal_comment/<int:pk>', GoalCommentDetailUpdateDeleteAPIView.as_view(),
         name='goal_comment_detail_update_delete'),
    path('board/create', BoardCreateAPIView.as_view(), name='board_create'),
    path('board/list', BoardListAPIView.as_view(), name='board_list'),
    path('board/<int:pk>', BoardDetailUpdateDeleteAPIView.as_view(), name='board_detail_update_delete'),
]
