from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

from bot.tg.client import TgClient
from bot.models import TgUser


class Command(BaseCommand):
    help = 'Command to start TodolistBot'

    def handle(self, *args, **options):
        tg_client = TgClient(token='5973175163:AAHQh3Vfv7h2cMKFosg-GM8iRf3bEdeC050')
        offset: int = 0
        while True:
            response = tg_client.get_updates(offset=offset)
            for item in response.result:
                offset = item.update_id + 1
                if not item.message:
                    continue

                tg_user: TgUser = self.get_tg_user(item.message)
                if not tg_user:  # state A пользователя нет в базе данных
                    verification_code = self.generate_verification_code()
                    self.create_tg_user(item.message, verification_code)
                    tg_client.send_message(chat_id=item.message.chat.id,
                                           text=f'Привет, {item.message.msg_from.first_name}!\n'
                                                f'[verification_code]: {verification_code}')
                elif tg_user.user_id is None:  # state B пользователь есть в базе, но не подтвержден
                    verification_code = self.generate_verification_code()
                    self.update_tg_user_verification_code(item.message, verification_code)
                    tg_client.send_message(chat_id=item.message.chat.id,
                                           text=f'Привет, {item.message.msg_from.first_name}!\n'
                                                f'[Verification_code]: {verification_code}')
                else:
                    tg_client.send_message(chat_id=item.message.chat.id,
                                                   text='Пользователь уже проверен')

    def get_tg_user(self, message):
        # return TgUser.objects.filter(tg_user_id=message.msg_from.id).exists()
        # return TgUser.objects.get(tg_user_id=message.msg_from.id)
        try:
            tg_user = TgUser.objects.get(tg_user_id=message.msg_from.id)
        except:
            return None

        return tg_user

    def generate_verification_code(self):
        return get_random_string(length=32)

    def create_tg_user(self, message, verification_code):
        TgUser.objects.create(
            tg_chat_id=message.chat.id,
            tg_user_id=message.msg_from.id,
            tg_username=message.msg_from.username,
            verification_code=verification_code
        )

    def update_tg_user_verification_code(self, message, verification_code):
        tg_user = TgUser.objects.filter(tg_user_id=message.msg_from.id)
        tg_user.update(
            verification_code=verification_code
        )
