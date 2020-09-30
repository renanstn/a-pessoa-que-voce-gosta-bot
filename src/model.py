from peewee import Model, CharField, IntegerField, PostgresqlDatabase
from playhouse.db_url import connect


class Suitor(Model):
    """
    Model que armazena os pretendentes, que irão mandar mensagem para o mozão.
    """
    chat_id = CharField()
    messages = IntegerField()
