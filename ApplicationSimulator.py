import oracledb

# Dane potrzebne do połączenia
username = "s102523"
password = "H12XardaS13"
dsn = "217.173.198.135/tpdb"

# Nawiązanie połączenia
try:
    conn = oracledb.connect(user=username, password=password, dsn=dsn)
    print("Połączono z bazą danych!")
except oracledb.Error as e:
    print("Wystąpił błąd podczas połączenia:", e)

# Pamiętaj o zamknięciu połączenia po zakończeniu
conn.close()
