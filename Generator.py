import oracledb
from faker import Faker
import random

fake = Faker('pl_PL')  # Ustawienie generatora danych na polski

# Zakładamy, że połączenie jest zdefiniowane globalnie
connection = oracledb.connect(user='username', password='password', dsn='dsn')  # Dostosuj dane

def create_database():
    """ Tworzy strukturę bazy danych na podstawie pliku SQL """
    print("Tworzenie bazy danych...")
    with open('create_database.sql', 'r') as file:
        sql_commands = file.read().split(';')
        for command in sql_commands:
            if command.strip():
                try:
                    with connection.cursor() as cursor:
                        cursor.execute(command)
                    print(f"Executed: {command}")
                except Exception as e:
                    print(f"Failed to execute {command}: {e}")

def populate_dictionaries():
    """ Wypełnia tabele słownikowe predefiniowanymi danymi """
    print("Uzupełnianie tabel słownikowych...")
    dictionary_data = {
        'kategorie_eksponatow': [(1, 'Malarstwo'), (2, 'Rzeźba'), (3, 'Numizmatyka'), (4, 'Archeologia'), (5, 'Etnografia')],
        'typ_zasobu_cyfrowego': [(1, 'Fotografia'), (2, 'Skan 3D'), (3, 'Dokumentacja video'), (4, 'Katalog cyfrowy'), (5, 'Rejestr inwentarzowy')],
        # Dodaj inne tabeli według potrzeb
    }
    try:
        with connection.cursor() as cursor:
            for table, values in dictionary_data.items():
                for id_val, name in values:
                    cursor.execute(f"INSERT INTO {table} (id_{table[:-1]}, nazwa) VALUES (:1, :2)", [id_val, name])
                    print(f"Inserted into {table}: {name} with ID {id_val}")
    except Exception as e:
        print(f"Failed to populate dictionaries: {e}")

def add_rows_to_table():
    """ Pozwala użytkownikowi dodać określoną liczbę wierszy do wybranej tabeli """
    print("Wybierz tabelę, do której chcesz dodać wiersze:")
    tables = ['eksponat', 'historia_eksponatu', 'konserwacje', 'pracownik']
    for idx, table in enumerate(tables):
        print(f"{idx + 1}. {table}")
    choice = int(input("Podaj numer tabeli: "))
    num_rows = int(input("Podaj liczbę wierszy do dodania: "))
    table_name = tables[choice - 1]

    # Ta funkcja powinna wywoływać odpowiednie funkcje generate_* w zależności od wybranej tabeli
    # Przykład, jak można zaimplementować generowanie danych:
    if table_name == 'eksponat':
        generate_eksponat(num_rows)

def drop_database():
    """ Usuwa całą strukturę bazy danych """
    print("Usuwanie bazy danych...")
    with open('drop_database.sql', 'r') as file:
        sql_commands = file.read().split(';')
        for command in sql_commands:
            if command.strip():
                try:
                    with connection.cursor() as cursor:
                        cursor.execute(command)
                    print(f"Dropped: {command}")
                except Exception as e:
                    print(f"Failed to drop database: {e}")

# Można dodać więcej pomocniczych funkcji lub rozszerzyć istniejące o dodatkową logikę
