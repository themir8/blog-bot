from django.db import models as db
from django.utils import timezone


class BotUser(db.Model):
    user_id = db.IntegerField("User telegram id", null=False, unique=True)
    username = db.CharField("Username", max_length=32, unique=True)
    first_name = db.CharField("First name", max_length=15)
    last_name = db.CharField("Last name", max_length=15)
    phone = db.CharField("Phone number", max_length=12)
    date_joined = db.DateTimeField('Date joined', default=timezone.now)
    is_active = db.BooleanField("User is active?", default=True)
    ban = db.BooleanField("Banned", default=False)

    def __str__(self) -> str:
        return str(self.username)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users registered in the bot"
