import Generator

def main_menu():
    while True:
        print("\nMenu Główne:")
        print("1. Stwórz bazę danych")
        print("2. Uzupełnij tabele słownikowe")
        print("3. Generator danych")
        print("4. Usuń bazę danych")
        print("0. Wyjście")
        
        choice = input("Wybierz opcję: ")
        
        if choice == "1":
            Generator.create_database()
        elif choice == "2":
            Generator.populate_dictionaries()
        elif choice == "3":
            data_generation_menu()
        elif choice == "4":
            Generator.drop_database()
        elif choice == "0":
            print("Zamykanie programu...")
            break
        else:
            print("Nieprawidłowa opcja. Proszę wybrać ponownie.")

def data_generation_menu():
    print("\nGenerator Danych:")
    print("1. Generuj dane dla wszystkich tabel")
    print("2. Dodaj wiersze do wybranej tabeli")
    print("0. Powrót do menu głównego")
    
    choice = input("Wybierz opcję: ")
    
    if choice == "1":
        Generator.generate_data_for_all_tables(100)  # Zakładając, że jest funkcja obsługująca wszystkie tabele
    elif choice == "2":
        Generator.add_rows_to_table()  # Funkcja, która pozwala dodać wiersze do wybranej tabeli
    elif choice == "0":
        return

if __name__ == "__main__":
    main_menu()
