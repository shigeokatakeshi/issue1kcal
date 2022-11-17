from playhouse.db_url import connect
from peewee import Model
from peewee import CharField

db = connect("sqlite:///peewee_db.sqlite")

if not db.connect():
    print("接続NG")
    exit()
print("接続OK")


class Kcal(Model):
    kcal = CharField()  # カロリー

    class Meta:
        database = db
        table_name = "Kcal"


db.create_tables([Kcal])
