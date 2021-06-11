# -*- coding: utf-8 -*-

import os
import psycopg2

#https://pynative.com/python-postgresql-insert-update-delete-table-data-to-perform-crud-operations/

def connect_db():

    #connection = psycopg2.connect(user="sysadmin",
    #                             password="pynative@#29",
    #                              host="127.0.0.1",
    #                              port="5432",
    #                              database="postgres_db")
    DATABASE_URL = os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    return conn

def insert_db(list1,list2,list3,filtro):
    usuario = 5
    try:
        conn = connect_db()
        cursor = conn.cursor()
        
        #GUARDAR LA BUSQUEDA (SEARCH)
        sql_string = "INSERT INTO search(filtro, id_user) VALUES (%s,%s) RETURNING id;"
        cursor.execute(sql_string, (filtro, usuario))
        id_of_new_row = cursor.fetchone()[0]
        
        #GUARDAR LOS CURSOS (DETAIL_SEARCH) 
        sql_string = "INSERT INTO detail_search(title, link, platform, rating, difficult, description, organization, id_search) VALUES (%s,%s,%s,%s,%s,%s,%s,%s) RETURNING id;"
        
        for list_detail in list1:
            platform = 'Udemy'
            cursor.execute(sql_string, (list_detail['Titulo'], list_detail['Link'], platform, list_detail['Rating'],list_detail['Dificultad'],list_detail['Descripcion'],list_detail['Organizacion'],id_of_new_row))
        
        for list_detail in list2:
            platform = 'Formate'
            cursor.execute(sql_string, (list_detail['Titulo'], list_detail['Link'], platform, list_detail['Rating'],list_detail['Dificultad'],list_detail['Descripcion'],list_detail['Organizacion'],id_of_new_row))
        
        for list_detail in list3:
            platform = 'Crehana'
            cursor.execute(sql_string, (list_detail['Titulo'], list_detail['Link'], platform, list_detail['Rating'],list_detail['Dificultad'],list_detail['Descripcion'],list_detail['Organizacion'],id_of_new_row))
        
        conn.commit()
        
    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into mobile table", error)

    finally:
        # closing database connection.
        if conn:
            cursor.close()
            conn.close()
            print("PostgreSQL connection is closed")    
    