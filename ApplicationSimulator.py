import Generator
from replit import clear
 
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
    clear()
    num_rows = int(input("Podaj ilość wierszy do dodania: "))
    print("\nGenerator Danych:")
    print("1. Dodaj podaną ilość wierszy do wszystkich tabel")
    print("2. Dodaj podaną ilość wierszy do tabeli Historia_eksponatu")
    print("3. Dodaj podaną ilość wierszy do tabeli Lokalizacja_eksponatu")
    print("4. Dodaj podaną ilość wierszy do tabeli Magazyn")
    print("5. Dodaj podaną ilość wierszy do tabeli Serwisy_konserwacji")
    print("6. Dodaj podaną ilość wierszy do tabeli Wyplata")
    print("7. Dodaj podaną ilość wierszy do tabeli Zasob_cyfrowy")
    print("8. Dodaj podaną ilość wierszy do tabeli Pracownik")
    print("9. Dodaj podaną ilość wierszy do tabeli Eksponat")
    print("10. Dodaj podaną ilość wierszy do tabeli Konserwacje")
    print("11. Dodaj podaną ilość wierszy do tabeli Wystawa")
    print("12. Dodaj podaną ilość wierszy do tabeli Eksponaty_na_wystawie")
    print("13. Dodaj podaną ilość wierszy do tabeli Zamowienie_eksponatu")
    print("14. Dodaj podaną ilość wierszy do tabeli Zgloszenie_konserwacji")
    print("0. Powrót do menu głównego")
    
    choice = input("Wybierz opcję: ")
    
    if choice == "1":
        Generator.generate_historia_eksponatu(num_rows)
        Generator.generate_lokalizacja_eksponatu(num_rows)
        Generator.generate_magazyn(num_rows)
        Generator.generate_serwisy_konserwacji(num_rows)
        Generator.generate_wyplata(num_rows)
        Generator.generate_zasob_cyfrowy(num_rows)
        Generator.generate_pracownik(num_rows)
        Generator.generate_eksponat(num_rows)
        Generator.generate_konserwacje(num_rows)
        Generator.generate_wystawa(num_rows)
        Generator.generate_eksponaty_na_wystawie(num_rows)
        Generator.generate_zamowienie_eksponatu(num_rows)
        Generator.generate_zgloszenie_konserwacji(num_rows)
        print("Dane dodane do wszystkich tabel.")
    elif choice == "2":
        Generator.generate_historia_eksponatu(num_rows)
        print("Dane dodane do tabeli Historia_eksponatu.")
    elif choice == "3":
        Generator.generate_eksponat(num_rows)
        print("Dane dodane do tabeli Eskponat.")
    elif choice == "4":
        Generator.generate_konserwacje(num_rows)
        print("Dane dodane do tabeli Konserwacje.")
    elif choice == "5":
        Generator.generate_lokalizacja_eksponatu(num_rows)
        print("Dane dodane do tabeli Lokalizacja_eksponatu.")
    elif choice == "6":
        Generator.generate_zasob_cyfrowy(num_rows)
        print("Dane dodane do tabeli Zasob_cyfrowy.")
    elif choice == "7":
        Generator.generate_pracownik(num_rows)
        print("Dane dodane do tabeli Pracownik.")
    elif choice == "8":
        Generator.generate_zamowienie_eksponatu(num_rows)
        print("Dane dodane do tabeli Zamowienie_eksponatu.")
    elif choice == "9":
        Generator.generate_eksponaty_na_wystawie(num_rows)
        print("Dane dodane do tabeli Eksponaty_na_wystawie.")
    elif choice == "10":
        Generator.generate_wystawa(num_rows)
        print("Dane dodane do tabeli Wystawa.")
    elif choice == "11":
        Generator.generate_wyplata(num_rows)
        print("Dane dodane do tabeli Wyplata.")
    elif choice == "12":
        Generator.generate_zgloszenie_konserwacji(num_rows)
        print("Dane dodane do tabeli Zgloszenie_konserwacji.")
    elif choice == "13":
        Generator.generate_serwisy_konserwacji(num_rows)
        print("Dane dodane do tabeli Serwisy_konserwacji.")
    elif choice == "14":
        Generator.generate_magazyn(num_rows)
        print("Dane dodane do tabeli Magazyn.")
    elif choice == "0":
        return
    else:
        print("Nieprawidłowa opcja. Proszę wybrać ponownie.")

if __name__ == "__main__":
    main_menu()

