from abc import ABC, abstractmethod


class Database(ABC):
    @abstractmethod
    def connect(self):
        pass


class MySQL(Database):
    def connect(self):
        print("Connected to MySQL")


class Application:
    def __init__(self, database):
        self.database = database

    def start(self):
        self.database.connect()


db = MySQL()
app = Application(db)
app.start()