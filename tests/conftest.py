# from pytest_factoryboy import register
#
# from tests.factories import BoardFactory, GoalCategoryFactory, GoalFactory, GoalCommentFactory, BoardParticipantFactory, \
#     UserFactory
#
#
# register(factory_class=BoardFactory, _name='board')
# register(factory_class=GoalCategoryFactory, _name='goal_category')
# register(factory_class=GoalFactory, _name='goal')
# register(factory_class=GoalCommentFactory, _name='goal_comment')
# register(factory_class=BoardParticipantFactory, _name='board_participant')
# register(factory_class=UserFactory, _name='user')


pytest_plugins = "tests.fixtures"
