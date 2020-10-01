from settings import DATABASE_URL
from peewee import Model, CharField, IntegerField, BooleanField
from playhouse.db_url import connect


database = connect(DATABASE_URL)


class Suitor(Model):
    """
    Model que armazena os pretendentes, que irão mandar mensagem para o mozão.
    """
    chat_id = CharField(unique=True)
    messages = IntegerField(default=1)
    said_hi = BooleanField(default=False)

    class Meta:
        database = database
