from peewee import Model, CharField, IntegerField, PostgresqlDatabase


database = PostgresqlDatabase(None)


class Suitor(Model):
    """
    Model que armazena os pretendentes, que irão mandar mensagem para o mozão.
    """
    chat_id = CharField()
    messages = IntegerField()
    class Meta:
        database = database

# 'postgresql://postgres:admin@postgres:5432/postgres'
