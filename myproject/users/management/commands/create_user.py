from django.core.management.base import BaseCommand
from users.models import User


class Command(BaseCommand):
    help = 'Tao user voi vai tro cu the'

    def add_arguments(self, parser):
        parser.add_argument(
            '--username',
            type=str,
            required=True,
            help='Ten dang nhap',
        )
        parser.add_argument(
            '--password',
            type=str,
            required=True,
            help='Mat khau',
        )
        parser.add_argument(
            '--vaitro',
            type=str,
            choices=['admin', 'canbo', 'ketoan', 'user'],
            default='user',
            help='Vai tro: admin (To truong/To pho), canbo (Can bo), ketoan (Ke toan), user (Nguoi dung)',
        )

    def handle(self, *args, **options):
        username = options['username']
        password = options['password']
        vaitro = options['vaitro']

        if User.objects.filter(username=username).exists():
            self.stdout.write(
                self.style.WARNING(f'User "{username}" da ton tai.')
            )
            return

        user = User(
            username=username,
            vaitro=vaitro
        )
        user.set_password(password)
        user.save()

        vaitro_names = {
            'admin': 'To truong/To pho',
            'canbo': 'Can bo',
            'ketoan': 'Ke toan',
            'user': 'Nguoi dung'
        }

        self.stdout.write(
            self.style.SUCCESS(
                f'Da tao user thanh cong!\n'
                f'Username: {username}\n'
                f'Password: {password}\n'
                f'Vai tro: {vaitro_names[vaitro]}'
            )
        )

