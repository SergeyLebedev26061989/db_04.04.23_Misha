import psycopg2
from psycopg2 import OperationalError


class DB:
    def __init__(self, database='ems_prod', user='postgres', password='seryoga1989'):
        self.connect = psycopg2.connect(database=database, user=user, password=password, host="127.0.0.1", port="5432")
        with self.connect.cursor() as cur:
            try:
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS folders (
                        id SERIAL PRIMARY KEY,
                        name VARCHAR NOT NULL,
                        surname VARCHAR NOT NULL
                    );
                """)
                self.connect.commit()
                print('база данных успешно создана')
            except OperationalError as e:
                print(f'Произошла ошибка {e}')

    def insert_client(self, name: str, surname: str):
        with self.connect.cursor() as cur:
            try:
                cur.execute("""
                    INSERT INTO folders(
                        name,
                        surname)
                    VALUES(
                        %s, %s
                    );
            """, (name, surname))
                self.connect.commit()
                print(f'клиент {name} {surname} успешно добавлен')
            except OperationalError as e:
                print(f'Произошла ошибка при добавлении клиента {e}')
                
    def look_db(self):
        with self.connect.cursor() as cur:
            try:
                cur.execute("""
                    SELECT id, name, surname FROM folders
                    """)
                self.connect.commit()
                return cur.fetchall()
            except OperationalError as e:
                print(f'Произошла {e} ошибка')

    def read_db(self, path):
        responce = requests.get(path)


    def close_connect(self):
        self.close_connect()


add = DB().insert_client('Петр', 'Петров')
add1 = DB().insert_client('Иван', 'Иванов')

look_db = DB().look_db()
for id in look_db:
    resp = requests.get(f'http://www.google.com/{id[0]}')
    time.sleep(0.2)
    print(resp)
