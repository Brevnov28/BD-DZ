import psycopg2

def create_tables(cur):

    #Создание таблицы основных клиентских данных
    cur.execute("""
    CREATE TABLE IF NOT EXISTS clients_Homework(
    id SERIAL PRIMARY KEY, 
    client_name VARCHAR(100) NOT NULL, 
    client_surname VARCHAR(100) NOT NULL, 
    client_email VARCHAR(100) NOT NULL);
    """)
    #Создание отдельной таблицы с клиентскими номерами
    cur.execute("""
    CREATE TABLE IF NOT EXISTS client_phonenumbers(
    id_phonenumber SERIAL PRIMARY KEY,
    client_id INTEGER NOT NULL REFERENCES clients_Homework(id),
    client_phonenumber VARCHAR(20) UNIQUE);
    """)



def add_new_client(cur, client_name, client_surname, client_email):
    '''Добавление нового клиента в таблицу clients_Homework5'''
    cur.execute("""
    INSERT INTO clients_Homework5(client_name, client_surname, client_email) VALUES(%s, %s, %s);
    """, (client_name, client_surname, client_email))

def add_new_phonenumber(cur, client_id, phonenumber):
    '''Добавление нового номера телефона в таблицу client_phonenumbers'''
    cur.execute("""
    INSERT INTO client_phonenumbers(client_id, client_phonenumber) VALUES(%s, %s);
    """, (client_id, phonenumber))



def change_client_data():
    '''Изменение информации о клиенте'''

    while True:
        command = int(input())
        if command == 1:
            id_for_changing_name = input("Введите id клиента для изменеия имени: ")
            name_for_changing = input("Введите имя для изменения: ")
            cur.execute("""
            UPDATE clients_Homework SET client_name=%s WHERE id=%s;
            """, (name_for_changing, id_for_changing_name))
            break
        elif command == 2:
            id_for_changing_surname = input("Введите id клиента для изменения фамилии: ")
            surname_for_changing = input("Введите фамилию для изменения: ")
            cur.execute("""
            UPDATE clients_Homework SET client_surname=%s WHERE id=%s;
            """, (surname_for_changing, id_for_changing_surname))
            break
        elif command == 3:
            id_for_changing_email = input("Введите id клиента для изменения e-mail: ")
            email_for_changing = input("Введите e-mail для изменения: ")
            cur.execute("""
            UPDATE clients_Homework5 SET client_email=%s WHERE id=%s;
            """, (email_for_changing, id_for_changing_email))
            break
        elif command == 4:
            phonenumber_change = input("Введите старый номер телефона: ")
            phonenumber_for_changing = input("Введите новый номер телефона: ")
            cur.execute("""
            UPDATE client_phonenumbers SET client_phonenumber=%s WHERE client_phonenumber=%s;
            """, (phonenumber_for_changing, phonenumber_change))
            break
        else:
            print("Вы ввели неправильную команду")



def delete_client_phonenumber():
    '''Удаление номера телефона клиента из таблицы client_phonenumbers'''
    id_for_deleting_phonenumber = input("Введите id клиента: ")
    phonenumber_for_deleting = input("Введите номер телефона для удаления: ")
    with conn.cursor() as cur:
        cur.execute("""
        DELETE FROM client_phonenumbers WHERE client_id=%s AND client_phonenumber=%s
        """, (id_for_deleting_phonenumber, phonenumber_for_deleting))



def delete_client():
    '''Удаление имеющейся информации о клиенте'''
    id_for_deleting_client = input("Введите id клиента для удаления: ")
    client_surname_for_deleting = input("Введите фамилию клиента для удаления: ")
    with conn.cursor() as cur:
        #удаление связи с таблицей client_phonenumbers
        cur.execute("""
        DELETE FROM client_phonenumbers WHERE client_id=%s
        """, (id_for_deleting_client,))
        #удаление информации о клиенте из таблицы clients_Homework5
        cur.execute("""
        DELETE FROM clients_Homework WHERE id=%s AND client_surname=%s
        """, (id_for_deleting_client, client_surname_for_deleting))



def find_client():
    '''Поиск клиента по имени'''
    print("Для поиска клиента, введите команду, где:\n "
          "Найти: 1 - по имени; 2 - по фамилии; 3 - по e-mail; 4 - по номеру телефона")
    while True:
        command = int(input("Введите команду для поиска клиента: "))
        if command == 1:
            name_client = input("Введите имя клиента: ")
            cur.execute("""
            SELECT id, client_name, client_surname, client_email, client_phonenumber
            FROM clients_Homework AS ch5
            LEFT JOIN client_phonenumbers AS cp ON cp.id_phonenumber = ch5.id
            WHERE client_name=%s
            """, (name_client,))
            print(cur.fetchall())
        elif command == 2:
            surname_client = input("Введите фамилию клиента: ")
            cur.execute("""
            SELECT id, client_name, client_surname, client_email, client_phonenumber
            FROM clients_Homework AS ch5
            LEFT JOIN client_phonenumbers AS cp ON cp.id_phonenumber = ch5.id
            WHERE client_surname=%s
            """, (surname_client,))
            print(cur.fetchall())
        elif command == 3:
            email_client = input("Введите email клиентa: ")
            cur.execute("""
            SELECT id, client_name, client_surname, client_email, client_phonenumber
            FROM clients_Homework AS ch5
            LEFT JOIN client_phonenumbers AS cp ON cp.id_phonenumber = ch5.id
            WHERE client_email=%s
            """, (email_client,))
            print(cur.fetchall())
        elif command == 4:
            phonenumber_client = input("Введите номер телефона клиентa: ")
            cur.execute("""
            SELECT id, client_name, client_surname, client_email, client_phonenumber
            FROM clients_Homework AS ch5
            LEFT JOIN client_phonenumbers AS cp ON cp.id_phonenumber = ch5.id
            WHERE client_phonenumber=%s
            """, (phonenumber_client,))
            #return cur.fetchone()[0]
            print(cur.fetchall())
        else:
            print("Вы ввели неправильную команду")

with psycopg2.connect(user="postgres", password="280468Br@", database="HomeWork", port="5432") as conn:
    with conn.cursor() as cur:
        create_tables(cur)
        add_new_client(cur, "Bob", "Marli", "bm@g.com")
        add_new_client(cur, "Brus", "Li", "br@g.com")
        add_new_client(cur, "Jacki", "Chan", "jc@g.com")
        add_new_client(cur, "Ed", "Gracham", "eg@g.com")
        add_new_client(cur, "Charley", "Shin", "cs@g.com")
        add_new_phonenumber(cur, 1, "1234567890")
        add_new_phonenumber(cur, 2, "2345678901")
        add_new_phonenumber(cur, 3, "3456789012")
        add_new_phonenumber(cur, 4, "4567890123")
        add_new_phonenumber(cur, 5, "5678901234")
        change_client_data()
        delete_client_phonenumber()
        delete_client()
        find_client()

conn.close()