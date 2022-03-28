import psycopg2
import os

HOST = os.getenv("DB_HOST")
DATABASE = os.getenv("DB_DATABASE")
USER = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PASSWORD")


class Series:
    def __init__(self, **kwargs):
        self.serie = kwargs["serie"]
        self.seasons = kwargs["seasons"]
        self.released_date = kwargs["released_date"]
        self.genre = kwargs["genre"]
        self.imdb_rating = kwargs["imdb_rating"]

    # cria tabela
    def table_models():
        conn = psycopg2.connect(
            host=HOST, database=DATABASE, user=USER, password=PASSWORD
        )

        create_table = """
                CREATE TABLE IF NOT EXISTS ka_series (
                id BIGSERIAL PRIMARY KEY,
                serie VARCHAR(100) NOT NULL UNIQUE,
                seasons INTEGER NOT NULL,
                released_date DATE NOT NULL,
                genre VARCHAR(50) NOT NULL,
                imdb_rating FLOAT NOT NULL
            );
            """

        cur = conn.cursor()

        cur.execute(create_table)

        conn.commit()

        cur.close()
        conn.close()

    # todos
    def get_series():
        query = "SELECT * FROM ka_series"

        conn = psycopg2.connect(
            host=HOST, database=DATABASE, user=USER, password=PASSWORD
        )

        cur = conn.cursor()

        cur.execute(query)

        data = cur.fetchall()

        cur.close()
        conn.close()

        return data

    # por id
    def get_by_id_series(serie_id):
        query = f"SELECT * FROM ka_series WHERE id = {serie_id}"

        conn = psycopg2.connect(
            host=HOST, database=DATABASE, user=USER, password=PASSWORD
        )

        cur = conn.cursor()

        cur.execute(query)

        data = cur.fetchone()

        cur.close()
        conn.close()

        return data

    # cria
    def create_series(payload):
        data = payload.__dict__

        new_serie = (
            data["serie"],
            data["seasons"],
            data["released_date"],
            data["genre"],
            data["imdb_rating"],
        )

        query = """
            INSERT INTO ka_series (serie, seasons, released_date, genre, imdb_rating)
            VALUES (%s, %s, %s, %s, %s)
            RETURNING *
        """

        conn = psycopg2.connect(
            host=HOST, database=DATABASE, user=USER, password=PASSWORD
        )

        cur = conn.cursor()

        cur.execute(query, new_serie)

        conn.commit()

        created_series = cur.fetchone()

        cur.close()
        conn.close()

        return created_series
