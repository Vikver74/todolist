from rest_framework import serializers

from core.models import User
from goals.models import GoalCategory, Goal, GoalComment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']


class GoalCategoryCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = GoalCategory
        read_only = ('id', 'created', 'updated', 'user')
        fields = '__all__'


class GoalCategorySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = GoalCategory
        fields = '__all__'


class GoalCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Goal
        read_only = ('id', 'created', 'updated', 'user')
        fields = '__all__'

    def validate_category(self, value):
        if value.is_deleted:
            raise serializers.ValidationError('not allowed in deleted category')
        if value.user != self.context.get('request').user:
            raise serializers.ValidationError('not owner of category')

        return value


class GoalSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Goal
        fields = '__all__'


class GoalCommentCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = GoalComment
        read_only = ('id', 'created', 'updated', 'user')
        fields = '__all__'


class GoalCommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    goal = serializers.IntegerField(source='goal.id', read_only=True)

    class Meta:
        model = GoalComment
        read_only = ('id', 'created', 'updated')
        fields = '__all__'
