import oracledb
from faker import Faker
import random

fake = Faker('pl_PL')  # Ustawienie generatora danych na polski

connection = oracledb.connect(user='s102523', password='A1asdfgh213', dsn='217.173.198.135/tpdb')

def create_database():
    print("Tworzenie bazy danych...")
    with open('create_database.sql', 'r') as file:
        sql_commands = file.read().split(';')
        for command in sql_commands:
            if command.strip():
                try:
                    with connection.cursor() as cursor:
                        cursor.execute(command)
                    print(f"Executed: {command}")
                    connection.commit()
                except Exception as e:
                    print(f"Failed to execute {command}: {e}")

def save_insert_to_file(table_name, columns, values, file_name="inserts.txt"):
    values_strings = [f"'{value}'" if isinstance(value, str) else str(value) for value in values]
    values_string = ", ".join(values_strings)
    columns_string = ", ".join(columns)
    
    # Tworzenie zapytania INSERT
    insert_query = f"INSERT INTO {table_name} ({columns_string}) VALUES ({values_string});\n"

    # Zapisywanie zapytania do pliku
    with open(file_name, "a") as file:
        file.write(insert_query)

def populate_dictionaries():
    print("Uzupełnianie tabel słownikowych...")
    dictionary_data = {
        'KATEGORIE_EKSPONATOW': {
            'column_name': 'id_kategorii_eksponatu',
            'data': [(1, 'Malarstwo'), (2, 'Rzeźba'), (3, 'Numizmatyka'), (4, 'Archeologia'), (5, 'Etnografia')]
        },
        'TYP_ZASOBU_CYFROWEGO': {
            'column_name': 'id_typu_zasobu_cyfrowego',
            'data': [(1, 'Fotografia'), (2, 'Skan 3D'), (3, 'Dokumentacja video'), (4, 'Katalog cyfrowy'), (5, 'Rejestr inwentarzowy')]
        },
        'STATUS_ZAMOWIENIA': {
            'column_name': 'id_statusu_zamowienia',
            'data': [(1, 'Nowe'), (2, 'W realizacji'), (3, 'Zakończone'), (4, 'Anulowane'), (5, 'Oczekujące na płatność')]
        },
        'STANOWISKO': {
            'column_name': 'id_stanowiska',
            'data': [(1, 'Kurator'), (2, 'Konserwator'), (3, 'Przewodnik'), (4, 'Recepcjonista'), (5, 'Ochroniarz')]
        },
        'STATUS_KONSERWACJI': {
            'column_name': 'id_statusu_konserwacji',
            'data': [(1, 'W trakcie'), (2, 'Zakończona'), (3, 'Planowana'), (4, 'Wstrzymana'), (5, 'Anulowana')]
        }
    }

    try:
        with connection.cursor() as cursor:
            for table, details in dictionary_data.items():
                column_name = details['column_name']
                data = details['data']
                for id_val, name in data:
                    sql = f"INSERT INTO {table} ({column_name}, NAZWA) VALUES (:1, :2)"
                    cursor.execute(sql, [id_val, name])
                    print(f"Inserted into {table}: {name} with ID {id_val}")
            connection.commit()
    except Exception as e:
        print(f"Failed to populate dictionaries: {e}")
        connection.rollback()

def get_next_id(table_name, id_column):
    """ Pobiera najwyższe ID z tabeli i zwraca następne """
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT MAX({id_column}) FROM {table_name}")
        max_id = cursor.fetchone()[0]
        return (max_id if max_id is not None else 0) + 1

def generate_historia_eksponatu(num_rows):
    next_id = get_next_id("historia_eksponatu", "id_historii_eksponatu")
    data_to_insert = []
    
    for _ in range(num_rows):
        data_wydarzenia = fake.date_between(start_date='-10y', end_date='today')
        opis_wydarzenia = fake.sentence(nb_words=10)
        data_to_insert.append((next_id, data_wydarzenia, opis_wydarzenia))
        next_id += 1
    
    with connection.cursor() as cursor:
        cursor.executemany("""
            INSERT INTO historia_eksponatu (id_historii_eksponatu, data_wydarzenia, opis_wydarzenia)
            VALUES (:1, :2, :3)""", data_to_insert)
        connection.commit()
    
    # Zapis do pliku
    for data in data_to_insert:
        query = f"INSERT INTO historia_eksponatu (id_historii_eksponatu, data_wydarzenia, opis_wydarzenia) VALUES {data};"
        save_insert_to_file(query)
    print(f"Dodano {num_rows} historii eksponatu.")

def generate_lokalizacja_eksponatu(num_rows):
    next_id = get_next_id("lokalizacja_eksponatu", "id_lokalizacji_eksponatu")
    data_to_insert = []
    
    for _ in range(num_rows):
        obecna_lokalizacja = fake.city()
        data_to_insert.append((next_id, obecna_lokalizacja))
        next_id += 1

    with connection.cursor() as cursor:
        cursor.executemany("""
            INSERT INTO lokalizacja_eksponatu (id_lokalizacji_eksponatu, obecna_lokalizacja)
            VALUES (:1, :2)""", data_to_insert)
        connection.commit()

    # Zapis do pliku
    for data in data_to_insert:
        query = f"INSERT INTO lokalizacja_eksponatu (id_lokalizacji_eksponatu, obecna_lokalizacja) VALUES {data};"
        save_insert_to_file(query)
    print(f"Dodano {num_rows} lokalizacji eksponatów.")

def generate_magazyn(num_rows):
    next_id = get_next_id("magazyn", "id_magazynu")
    data_to_insert = []
    
    for _ in range(num_rows):
        nazwa = fake.company()
        data_to_insert.append((next_id, nazwa))
        next_id += 1

    with connection.cursor() as cursor:
        cursor.executemany("""
            INSERT INTO magazyn (id_magazynu, nazwa)
            VALUES (:1, :2)""", data_to_insert)
        connection.commit()

    # Zapis do pliku
    for data in data_to_insert:
        query = f"INSERT INTO magazyn (id_magazynu, nazwa) VALUES {data};"
        save_insert_to_file(query)
    print(f"Dodano {num_rows} magazynów.")

def generate_serwisy_konserwacji(num_rows):
    next_id = get_next_id("serwisy_konserwacji", "id_serwisu_konserwacji")
    data_to_insert = []
    
    for _ in range(num_rows):
        nazwa = fake.company()
        opis = fake.text(max_nb_chars=200)
        adres = fake.address()
        telefon = fake.phone_number()
        data_to_insert.append((next_id, nazwa, opis, adres, telefon))
        next_id += 1

    with connection.cursor() as cursor:
        cursor.executemany("""
            INSERT INTO serwisy_konserwacji (id_serwisu_konserwacji, nazwa, opis, adres, telefon)
            VALUES (:1, :2, :3, :4, :5)""", data_to_insert)
        connection.commit()

    # Zapis do pliku
    for data in data_to_insert:
        query = f"INSERT INTO serwisy_konserwacji (id_serwisu_konserwacji, nazwa, opis, adres, telefon) VALUES {data};"
        save_insert_to_file(query)
    print(f"Dodano {num_rows} serwisów konserwacji.")

def generate_wyplata(num_rows):
    next_id = get_next_id("wyplata", "id_wyplaty")
    data_to_insert = []
    
    for _ in range(num_rows):
        kwota = round(random.uniform(2000.00, 10000.00), 2)
        data_wyplaty = fake.date_between(start_date='-5y', end_date='today')
        data_to_insert.append((next_id, kwota, data_wyplaty))
        next_id += 1

    with connection.cursor() as cursor:
        cursor.executemany("""
            INSERT INTO wyplata (id_wyplaty, kwota, data_wyplaty)
            VALUES (:1, :2, :3)""", data_to_insert)
        connection.commit()

    # Zapis do pliku
    for data in data_to_insert:
        query = f"INSERT INTO wyplata (id_wyplaty, kwota, data_wyplaty) VALUES {data};"
        save_insert_to_file(query)
    print(f"Dodano {num_rows} wypłat.")

def generate_zasob_cyfrowy(num_rows):
    next_id = get_next_id("zasob_cyfrowy", "id_zasobu_cyfrowego")
    data_to_insert = []
    
    for _ in range(num_rows):
        opis = fake.text(max_nb_chars=200)
        sciezka_dostepu = fake.file_path(depth=3, extension='pdf')
        ko_id_typu_zasobu_cyfrowego = random.randint(1, 5)
        data_to_insert.append((next_id, opis, sciezka_dostepu, ko_id_typu_zasobu_cyfrowego))
        next_id += 1

    with connection.cursor() as cursor:
        cursor.executemany("""
            INSERT INTO zasob_cyfrowy (id_zasobu_cyfrowego, opis, sciezka_dostepu, ko_id_typu_zasobu_cyfrowego)
            VALUES (:1, :2, :3, :4)""", data_to_insert)
        connection.commit()

    # Zapis do pliku
    for data in data_to_insert:
        query = f"INSERT INTO zasob_cyfrowy (id_zasobu_cyfrowego, opis, sciezka_dostepu, ko_id_typu_zasobu_cyfrowego) VALUES {data};"
        save_insert_to_file(query)
    print(f"Dodano {num_rows} zasobów cyfrowych.")

def generate_pracownik(num_rows):
    next_id = get_next_id("pracownik", "id_pracownika")
    data_to_insert = []
    
    for _ in range(num_rows):
        imie = fake.first_name()
        nazwisko = fake.last_name()
        data_zatrudnienia = fake.date_between(start_date='-10y', end_date='today')
        data_zwolnienia = fake.date_between(start_date=data_zatrudnienia, end_date='today') if random.choice([True, False]) else None
        powod_zwolnienia = fake.sentence(nb_words=5) if data_zwolnienia else None
        email = fake.email()
        telefon = fake.phone_number()
        ko_id_stanowiska = random.randint(1, 5)
        ko_id_wyplaty = random.randint(1, 100)

        data_to_insert.append((next_id, imie, nazwisko, data_zatrudnienia, data_zwolnienia, powod_zwolnienia, email, telefon,
                               ko_id_stanowiska, ko_id_wyplaty))
        next_id += 1

    with connection.cursor() as cursor:
        cursor.executemany("""
            INSERT INTO pracownik (id_pracownika, imie, nazwisko, data_zatrudnienia, data_zwolnienia, powod_zwolnienia, "E-mail", telefon,
                                   ko_id_stanowiska, ko_id_wyplaty)
            VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10)""", data_to_insert)
        connection.commit()

    # Zapis do pliku
    for data in data_to_insert:
        query = f"INSERT INTO pracownik (id_pracownika, imie, nazwisko, data_zatrudnienia, data_zwolnienia, powod_zwolnienia, \"E-mail\", telefon, ko_id_stanowiska, ko_id_wyplaty) VALUES {data};"
        save_insert_to_file(query)
    print(f"Dodano {num_rows} pracowników.")

def generate_eksponat(num_rows):
    next_id = get_next_id("eksponat", "id_eksponatu")
    data_to_insert = []

    for _ in range(num_rows):
        nazwa = fake.sentence(nb_words=3)
        opis = fake.text(max_nb_chars=200)
        pochodzenie = fake.country()
        data_nabycia = fake.date_between(start_date='-10y', end_date='today')
        stan_zachowania = fake.word(ext_word_list=['dobry', 'średni', 'zły'])
        ko_id_kategorii_eksponatu = random.randint(1, 5)
        ko_id_historii_eksponatu = random.randint(1, 5)
        ko_id_zasobu_cyfrowego = random.randint(1, 5)
        ko_id_lokalizacji_eksponatu = random.randint(1, 5)
        ko_id_magazynu = random.randint(1, 5)

        row_data = (next_id, nazwa, opis, pochodzenie, data_nabycia, stan_zachowania,
                    ko_id_kategorii_eksponatu, ko_id_historii_eksponatu, ko_id_zasobu_cyfrowego,
                    ko_id_lokalizacji_eksponatu, ko_id_magazynu)
        
        data_to_insert.append(row_data)
        next_id += 1

    # Wstawianie do bazy danych używając cursor.executemany()
    with connection.cursor() as cursor:
        cursor.executemany("""
            INSERT INTO eksponat (id_eksponatu, nazwa, opis, pochodzenie, data_nabycia, stan_zachowania,
                                  ko_id_kategorii_eksponatu, ko_id_historii_eksponatu, ko_id_zasobu_cyfrowego,
                                  ko_id_lokalizacji_eksponatu, ko_id_magazynu)
            VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11)
        """, data_to_insert)
        connection.commit()

    # Zapis do pliku
    for data in data_to_insert:
        query = f"INSERT INTO eksponat (id_eksponatu, nazwa, opis, pochodzenie, data_nabycia, stan_zachowania, ko_id_kategorii_eksponatu, ko_id_historii_eksponatu, ko_id_zasobu_cyfrowego, ko_id_lokalizacji_eksponatu, ko_id_magazynu) VALUES {data};"
        save_insert_to_file(query)
    print(f"Dodano {num_rows} eksponatów.")


def generate_konserwacje(num_rows):
    next_id = get_next_id("konserwacje", "id_konserwacji")
    data_to_insert = []
    
    for _ in range(num_rows):
        data_rozpoczecia = fake.date_between(start_date='-5y', end_date='today')
        data_zakonczenia = fake.date_between(start_date=data_rozpoczecia, end_date='today')
        opis = fake.sentence(nb_words=8)
        wynik_przegladu = fake.sentence(nb_words=8)
        decyzja = fake.word(ext_word_list=['zaakceptowano', 'odrzucono'])
        ko_id_eksponatu = random.randint(1, 100)
        ko_id_serwisu_konserwacji = random.randint(1, 5)
        ko_id_statusu_konserwacji = random.randint(1, 5)
        data_to_insert.append((next_id, data_rozpoczecia, data_zakonczenia, opis, wynik_przegladu, decyzja,
                               ko_id_eksponatu, ko_id_serwisu_konserwacji, ko_id_statusu_konserwacji))
        next_id += 1
    
    with connection.cursor() as cursor:
        cursor.executemany("""
            INSERT INTO konserwacje (id_konserwacji, data_rozpoczecia, data_zakonczenia, opis, wynik_przegladu, decyzja,
                                     ko_id_eksponatu, ko_id_serwisu_konserwacji, ko_id_statusu_konserwacji)
            VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9)""", data_to_insert)
        connection.commit()
    
    # Zapis do pliku
    for data in data_to_insert:
        query = f"INSERT INTO konserwacje (id_konserwacji, data_rozpoczecia, data_zakonczenia, opis, wynik_przegladu, decyzja, ko_id_eksponatu, ko_id_serwisu_konserwacji, ko_id_statusu_konserwacji) VALUES {data};"
        save_insert_to_file(query)
    print(f"Dodano {num_rows} konserwacji.")

def generate_wystawa(num_rows):
    next_id = get_next_id("wystawa", "id_wystawy")
    data_to_insert = []
    
    for _ in range(num_rows):
        nazwa = fake.sentence(nb_words=3)
        opis = fake.text(max_nb_chars=200)
        data_rozpoczecia = fake.date_between(start_date='-5y', end_date='today')
        data_zakonczenia = fake.date_between(start_date=data_rozpoczecia, end_date='+5y')
        data_to_insert.append((next_id, nazwa, opis, data_rozpoczecia, data_zakonczenia))
        next_id += 1

    with connection.cursor() as cursor:
        cursor.executemany("""
            INSERT INTO wystawa (id_wystawy, nazwa, opis, data_rozpoczecia, data_zakonczenia)
            VALUES (:1, :2, :3, :4, :5)""", data_to_insert)
        connection.commit()

    # Zapis do pliku
    for data in data_to_insert:
        query = f"INSERT INTO wystawa (id_wystawy, nazwa, opis, data_rozpoczecia, data_zakonczenia) VALUES {data};"
        save_insert_to_file(query)
    print(f"Dodano {num_rows} wystaw.")

def generate_eksponaty_na_wystawie(num_rows):
    next_id = get_next_id("eksponaty_na_wystawie", "ko_id_eksponatu")
    data_to_insert = []
    
    for _ in range(num_rows):
        data_umieszczenia = fake.date_between(start_date='-5y', end_date='today')
        ko_id_wystawy = random.randint(1, 10)
        ko_id_eksponatu = next_id
        data_to_insert.append((data_umieszczenia, ko_id_wystawy, ko_id_eksponatu))
        next_id += 1

    with connection.cursor() as cursor:
        cursor.executemany("""
            INSERT INTO eksponaty_na_wystawie (data_umieszczenia, ko_id_wystawy, ko_id_eksponatu)
            VALUES (:1, :2, :3)""", data_to_insert)
        connection.commit()

    # Zapis do pliku
    for data in data_to_insert:
        query = f"INSERT INTO eksponaty_na_wystawie (data_umieszczenia, ko_id_wystawy, ko_id_eksponatu) VALUES {data};"
        save_insert_to_file(query)
    print(f"Dodano {num_rows} eksponatów na wystawie.")

def generate_zamowienie_eksponatu(num_rows):
    next_id = get_next_id("zamowienie_eksponatu", "id_zamowienia_eksponatu")
    data_to_insert = []
    
    for _ in range(num_rows):
        data_zamowienia = fake.date_between(start_date='-2y', end_date='today')
        ko_id_eksponatu = random.randint(1, 100)
        ko_id_pracownika = random.randint(1, 100)
        ko_id_statusu_zamowienia = random.randint(1, 5)

        data_to_insert.append((next_id, data_zamowienia, ko_id_eksponatu, ko_id_pracownika, ko_id_statusu_zamowienia))
        next_id += 1

    with connection.cursor() as cursor:
        cursor.executemany("""
            INSERT INTO zamowienie_eksponatu (id_zamowienia_eksponatu, data_zamowienia, ko_id_eksponatu, ko_id_pracownika, ko_id_statusu_zamowienia)
            VALUES (:1, :2, :3, :4, :5)""", data_to_insert)
        connection.commit()

    # Zapis do pliku
    for data in data_to_insert:
        query = f"INSERT INTO zamowienie_eksponatu (id_zamowienia_eksponatu, data_zamowienia, ko_id_eksponatu, ko_id_pracownika, ko_id_statusu_zamowienia) VALUES {data};"
        save_insert_to_file(query)
    print(f"Dodano {num_rows} zamówień eksponatów.")

def generate_zgloszenie_konserwacji(num_rows):
    next_id = get_next_id("zgloszenie_konserwacji", "id_zgloszenia_konserwacji")
    data_to_insert = []
    
    for _ in range(num_rows):
        data_zgloszenia = fake.date_between(start_date='-2y', end_date='today')
        opis = fake.sentence(nb_words=10)
        ko_id_pracownika = random.randint(1, 100)
        ko_id_konserwacji = random.randint(1, 100)
        ko_id_eksponatu = random.randint(1, 100)
        data_to_insert.append((next_id, data_zgloszenia, opis, ko_id_pracownika, ko_id_konserwacji, ko_id_eksponatu))
        next_id += 1

    with connection.cursor() as cursor:
        cursor.executemany("""
            INSERT INTO zgloszenie_konserwacji (id_zgloszenia_konserwacji, data_zgloszenia, opis, ko_id_pracownika, ko_id_konserwacji, ko_id_eksponatu)
            VALUES (:1, :2, :3, :4, :5, :6)""", data_to_insert)
        connection.commit()

    # Zapis do pliku
    for data in data_to_insert:
        query = f"INSERT INTO zgloszenie_konserwacji (id_zgloszenia_konserwacji, data_zgloszenia, opis, ko_id_pracownika, ko_id_konserwacji, ko_id_eksponatu) VALUES {data};"
        save_insert_to_file(query)
    print(f"Dodano {num_rows} zgłoszeń konserwacji.")


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