from django.core.management.base import BaseCommand
from users.models import User


class Command(BaseCommand):
    help = 'Tạo user admin mặc định'

    def add_arguments(self, parser):
        parser.add_argument(
            '--username',
            type=str,
            default='admin',
            help='Tên đăng nhập (mặc định: admin)',
        )
        parser.add_argument(
            '--password',
            type=str,
            default='admin123',
            help='Mật khẩu (mặc định: admin123)',
        )

    def handle(self, *args, **options):
        username = options['username']
        password = options['password']

        if User.objects.filter(username=username).exists():
            self.stdout.write(
                self.style.WARNING(f'User "{username}" da ton tai.')
            )
            return

        user = User(
            username=username,
            vaitro='admin'
        )
        user.set_password(password)
        user.save()

        self.stdout.write(
            self.style.SUCCESS(
                f'Da tao user admin thanh cong!\n'
                f'Username: {username}\n'
                f'Password: {password}'
            )
        )

