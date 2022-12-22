from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from bot.models import TgUser
from bot.serializers import BotVerifyCodeUpdateView


class BotVerifyCodeUpdate(generics.UpdateAPIView):
    model = TgUser
    serializer_class = BotVerifyCodeUpdateView
    http_method_names = ['patch']
    queryset = TgUser.objects.all()
    permission_classes = [IsAuthenticated]

    def get_object(self):
        # return TgUser.objects.get(verification_code=self.request.data['verification_code'])
        return get_object_or_404(TgUser, verification_code=self.request.data['verification_code'])

    # def get_queryset(self):
    #     return TgUser.objects.filter(verification_code=self.request.data['verification_code'])

    # def perform_update(self, serializer):
    #     return TgUser.objects.update(
    #         user=self.request.user
    #     )


