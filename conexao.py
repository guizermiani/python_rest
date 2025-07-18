import psycopg2

def conecta_db():
   con =  psycopg2.connect(host="127.0.0.1",
                    database="curso",
                    user='postgres',
                    password="postgres",
                    port=5432)
   return con
