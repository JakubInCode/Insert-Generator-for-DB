CREATE TABLE eksponat (
    id_eksponatu                              	INTEGER NOT NULL,
    nazwa                                     	VARCHAR2(200 CHAR) NOT NULL,
    opis                                      	CLOB NOT NULL,
    pochodzenie                               	VARCHAR2(255 CHAR) NOT NULL,
    data_nabycia                             	DATE NOT NULL,
    stan_zachowania                           	VARCHAR2(100 CHAR) NOT NULL, 
    ko_id_kategorii_eksponatu    				INTEGER NOT NULL, 
    ko_id_historii_eksponatu       				INTEGER NOT NULL, 
    ko_id_zasobu_cyfrowego              		INTEGER NOT NULL, 
    ko_id_lokalizacji_eksponatu 				INTEGER NOT NULL,
    ko_id_magazynu                            	INTEGER NOT NULL
);

ALTER TABLE eksponat ADD CONSTRAINT eksponat_pk PRIMARY KEY ( id_eksponatu );

ALTER TABLE eksponat ADD CONSTRAINT eksponat_nazwa_un UNIQUE ( nazwa );

CREATE TABLE eksponaty_na_wystawie (
    data_umieszczenia     						DATE NOT NULL,
    ko_id_wystawy    							INTEGER NOT NULL,
    ko_id_eksponatu 							INTEGER NOT NULL
);

CREATE TABLE historia_eksponatu (
    id_historii_eksponatu 						INTEGER NOT NULL,
    data_wydarzenia       						DATE NOT NULL,
    opis_wydarzenia       						CLOB NOT NULL
);

ALTER TABLE historia_eksponatu ADD CONSTRAINT historia_eksponatu_pk PRIMARY KEY ( id_historii_eksponatu );

CREATE TABLE kategorie_eksponatow (
    id_kategorii_eksponatu 						INTEGER NOT NULL,
    nazwa                  						VARCHAR2(100 CHAR) NOT NULL
);

ALTER TABLE kategorie_eksponatow ADD CONSTRAINT kategorie_eksponatow_pk PRIMARY KEY ( id_kategorii_eksponatu );

ALTER TABLE kategorie_eksponatow ADD CONSTRAINT kategorie_eksponatow_nazwa_un UNIQUE ( nazwa );

CREATE TABLE konserwacje (
    id_konserwacji                             	INTEGER NOT NULL,
    data_rozpoczecia                           	DATE NOT NULL,
    data_zakonczenia                           	DATE NOT NULL,
    opis                                       	CLOB,
    wynik_przegladu                            	CLOB NOT NULL,
    decyzja                                    	VARCHAR2(100 CHAR) NOT NULL,
    ko_id_eksponatu                      		INTEGER NOT NULL, 
    ko_id_serwisu_konserwacji 					INTEGER NOT NULL, 
    ko_id_statusu_konserwacji  					INTEGER NOT NULL
);

ALTER TABLE konserwacje ADD CONSTRAINT konserwacje_pk PRIMARY KEY ( id_konserwacji );

CREATE TABLE lokalizacja_eksponatu (
    id_lokalizacji_eksponatu 					INTEGER NOT NULL,
    obecna_lokalizacja       					VARCHAR2(100 CHAR) NOT NULL
);

ALTER TABLE lokalizacja_eksponatu ADD CONSTRAINT lokalizacja_eksponatu_pk PRIMARY KEY ( id_lokalizacji_eksponatu );

CREATE TABLE magazyn (
    id_magazynu 								INTEGER NOT NULL,
    nazwa       								VARCHAR2(255 CHAR) NOT NULL
);

ALTER TABLE magazyn ADD CONSTRAINT magazyn_pk PRIMARY KEY ( id_magazynu );

CREATE TABLE pracownik (
    id_pracownika            					INTEGER NOT NULL,
    imie                     					VARCHAR2(100 CHAR) NOT NULL,
    nazwisko                 					VARCHAR2(100 CHAR) NOT NULL,
    data_zatrudnienia        					DATE NOT NULL,
    data_zwolnienia          					DATE,
    powód_zwolnienia         					CLOB,
    "E-mail"                 					VARCHAR2(255 CHAR),
    telefon                  					VARCHAR2(15 CHAR),
    ko_id_stanowiska 							INTEGER NOT NULL,
    ko_id_wyplaty       						INTEGER NOT NULL
);

ALTER TABLE pracownik ADD CONSTRAINT pracownik_pk PRIMARY KEY ( id_pracownika );

ALTER TABLE pracownik ADD CONSTRAINT "Pracownik_E-mail_UN" UNIQUE ( "E-mail" );

ALTER TABLE pracownik ADD CONSTRAINT pracownik_telefon_un UNIQUE ( telefon );

CREATE TABLE serwisy_konserwacji (
    id_serwisu_konserwacji 						INTEGER NOT NULL,
    nazwa                  						VARCHAR2(100 CHAR) NOT NULL,
    opis                   						CLOB,
    adres                  						VARCHAR2(255 CHAR) NOT NULL,
    telefon                						VARCHAR2(15 CHAR)
);

ALTER TABLE serwisy_konserwacji ADD CONSTRAINT serwisy_konserwacji_pk PRIMARY KEY ( id_serwisu_konserwacji );

ALTER TABLE serwisy_konserwacji ADD CONSTRAINT serwisy_konserwacji_telefon_un UNIQUE ( telefon );

CREATE TABLE stanowisko (
    id_stanowiska 								INTEGER NOT NULL,
    nazwa         								VARCHAR2(100 CHAR) NOT NULL
);

ALTER TABLE stanowisko ADD CONSTRAINT stanowisko_pk PRIMARY KEY ( id_stanowiska );

ALTER TABLE stanowisko ADD CONSTRAINT stanowisko_nazwa_un UNIQUE ( nazwa );

CREATE TABLE status_konserwacji (
    id_statusu_konserwacji 						INTEGER NOT NULL,
    nazwa                  						VARCHAR2(100 CHAR) NOT NULL
);

ALTER TABLE status_konserwacji ADD CONSTRAINT status_konserwacji_pk PRIMARY KEY ( id_statusu_konserwacji );

ALTER TABLE status_konserwacji ADD CONSTRAINT status_konserwacji_nazwa_un UNIQUE ( nazwa );

CREATE TABLE status_zamowienia (
    id_statusu_zamowienia 						INTEGER NOT NULL,
    nazwa                 						VARCHAR2(100 CHAR) NOT NULL
);

ALTER TABLE status_zamowienia ADD CONSTRAINT status_zamowienia_pk PRIMARY KEY ( id_statusu_zamowienia );

ALTER TABLE status_zamowienia ADD CONSTRAINT status_zamowienia_nazwa_un UNIQUE ( nazwa );

CREATE TABLE typ_zasobu_cyfrowego (
    id_typu_zasobu_cyfrowego 					INTEGER NOT NULL,
    nazwa                    					VARCHAR2(100 CHAR) NOT NULL
);

ALTER TABLE typ_zasobu_cyfrowego ADD CONSTRAINT typ_zasobu_cyfrowego_pk PRIMARY KEY ( id_typu_zasobu_cyfrowego );

ALTER TABLE typ_zasobu_cyfrowego ADD CONSTRAINT typ_zasobu_cyfrowego_nazwa_un UNIQUE ( nazwa );

CREATE TABLE wyplata (
    id_wyplaty   								INTEGER NOT NULL,
    kwota        								NUMBER(10, 2) NOT NULL,
    data_wyplaty 								DATE NOT NULL
);

ALTER TABLE wyplata ADD CONSTRAINT wyplata_pk PRIMARY KEY ( id_wyplaty );

CREATE TABLE wystawa (
    id_wystawy       							INTEGER NOT NULL,
    nazwa            							VARCHAR2(255 CHAR) NOT NULL,
    opis             							CLOB NOT NULL,
    data_rozpoczecia 							DATE NOT NULL,
    data_zakonczenia 							DATE NOT NULL
);

ALTER TABLE wystawa ADD CONSTRAINT wystawa_pk PRIMARY KEY ( id_wystawy );

CREATE TABLE zamowienie_eksponatu (
    id_zamowienia_eksponatu                 	INTEGER NOT NULL,
    data_zamówienia                         	DATE NOT NULL,
    ko_id_eksponatu                   			INTEGER NOT NULL,
    ko_id_pracownika                 			INTEGER NOT NULL, 
    ko_id_statusu_zamowienia 					INTEGER NOT NULL
);

ALTER TABLE zamowienie_eksponatu ADD CONSTRAINT zamowienie_eksponatu_pk PRIMARY KEY ( id_zamowienia_eksponatu );

CREATE TABLE zasob_cyfrowy (
    id_zasobu_cyfrowego                     	INTEGER NOT NULL,
    opis                                      	CLOB,
    sciezka_dostepu                          	VARCHAR2(255 CHAR), 
    ko_id_typu_zasobu_cyfrowego 				INTEGER NOT NULL
);

ALTER TABLE zasob_cyfrowy ADD CONSTRAINT zasob_cyfrowy_pk PRIMARY KEY ( id_zasobu_cyfrowego );

CREATE TABLE zgloszenie_konserwacji (
    id_zgloszenia_konserwacji  					INTEGER NOT NULL,
    data_zgloszenia            					DATE NOT NULL,
    opis                       					CLOB NOT NULL,
    ko_id_pracownika    						INTEGER NOT NULL,
    ko_id_konserwacji 							INTEGER NOT NULL,
    ko_id_eksponatu      						INTEGER NOT NULL
);

ALTER TABLE zgloszenie_konserwacji ADD CONSTRAINT zgloszenie_konserwacji_pk PRIMARY KEY ( id_zgloszenia_konserwacji );

ALTER TABLE eksponat
    ADD CONSTRAINT eksponat_his_eks_fk FOREIGN KEY ( ko_id_historii_eksponatu )
        REFERENCES historia_eksponatu ( id_historii_eksponatu );
 
ALTER TABLE eksponat
    ADD CONSTRAINT eksponat_kat_eks_fk FOREIGN KEY ( ko_id_kategorii_eksponatu )
        REFERENCES kategorie_eksponatow ( id_kategorii_eksponatu );

ALTER TABLE eksponat
    ADD CONSTRAINT eksponat_lok_eks_fk FOREIGN KEY ( ko_id_lokalizacji_eksponatu )
        REFERENCES lokalizacja_eksponatu ( id_lokalizacji_eksponatu );

ALTER TABLE eksponat
    ADD CONSTRAINT eksponat_mag_fk FOREIGN KEY ( ko_id_magazynu )
        REFERENCES magazyn ( id_magazynu );

ALTER TABLE eksponat
    ADD CONSTRAINT eksponat_zas_cyf_fk FOREIGN KEY ( ko_id_zasobu_cyfrowego )
        REFERENCES zasob_cyfrowy ( id_zasobu_cyfrowego );
 
ALTER TABLE eksponaty_na_wystawie
    ADD CONSTRAINT eksponaty_na_wystawie_eks_fk FOREIGN KEY ( ko_id_eksponatu )
        REFERENCES eksponat ( id_eksponatu );

ALTER TABLE eksponaty_na_wystawie
    ADD CONSTRAINT eksponaty_na_wystawie_wys_fk FOREIGN KEY ( ko_id_wystawy )
        REFERENCES wystawa ( id_wystawy );

ALTER TABLE konserwacje
    ADD CONSTRAINT konserwacje_eks_fk FOREIGN KEY ( ko_id_eksponatu )
        REFERENCES eksponat ( id_eksponatu );

ALTER TABLE konserwacje
    ADD CONSTRAINT konserwacje_ser_kon_fk FOREIGN KEY ( ko_id_serwisu_konserwacji )
        REFERENCES serwisy_konserwacji ( id_serwisu_konserwacji );

ALTER TABLE konserwacje
    ADD CONSTRAINT konserwacje_sta_kon_fk FOREIGN KEY ( ko_id_statusu_konserwacji )
        REFERENCES status_konserwacji ( id_statusu_konserwacji );

ALTER TABLE pracownik
    ADD CONSTRAINT pracownik_sta_fk FOREIGN KEY ( ko_id_stanowiska )
        REFERENCES stanowisko ( id_stanowiska );

ALTER TABLE pracownik
    ADD CONSTRAINT pracownik_wyp_fk FOREIGN KEY ( ko_id_wyplaty )
        REFERENCES wyplata ( id_wyplaty );

ALTER TABLE zamowienie_eksponatu
    ADD CONSTRAINT zamowienie_eksponatu_eks_fk FOREIGN KEY ( ko_id_eksponatu )
        REFERENCES eksponat ( id_eksponatu );

ALTER TABLE zamowienie_eksponatu
    ADD CONSTRAINT zamowienie_eksponatu_pra_fk FOREIGN KEY ( ko_id_pracownika )
        REFERENCES pracownik ( id_pracownika );

ALTER TABLE zamowienie_eksponatu
    ADD CONSTRAINT zamowienie_eksponatu_st_za_fk FOREIGN KEY ( ko_id_statusu_zamowienia )
        REFERENCES status_zamowienia ( id_statusu_zamowienia );

ALTER TABLE zasob_cyfrowy
    ADD CONSTRAINT zasob_cyfrowy_typ_zas_cyf_fk FOREIGN KEY ( ko_id_typu_zasobu_cyfrowego )
        REFERENCES typ_zasobu_cyfrowego ( id_typu_zasobu_cyfrowego );

ALTER TABLE zgloszenie_konserwacji
    ADD CONSTRAINT zgloszenie_konserwacji_eks_fk FOREIGN KEY ( ko_id_eksponatu )
        REFERENCES eksponat ( id_eksponatu );

ALTER TABLE zgloszenie_konserwacji
    ADD CONSTRAINT zgloszenie_konserwacji_kon_fk FOREIGN KEY ( ko_id_konserwacji )
        REFERENCES konserwacje ( id_konserwacji );
 
ALTER TABLE zgloszenie_konserwacji
    ADD CONSTRAINT zgloszenie_konserwacji_pra_fk FOREIGN KEY ( ko_id_pracownika )
        REFERENCES pracownik ( id_pracownika );