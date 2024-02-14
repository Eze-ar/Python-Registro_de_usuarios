# -*- coding: utf-8 -*-
"""
Created on Thu Feb 9 12:14:50 2024
Reto #5:
Listo, llegamos al reto número 5 de la semana. Nuestro programa ya funciona sumamente bien. Ya podemos crear, listar y
editar usarios.
Sin embargo, muy probablemente el código que tengamos hasta ahora pueda mejorar significativamente, es por ello que,
para el reto de hoy vamos a definir 5 nuevas funciones; esto con la finalidad de poder separar nuestro código y que este
sea fácil de leer, comprender y sobre todo mantener.
Las 5 nuevas funciones serán las siguientes.
new_user
show_user
edit_user
delete_user
list_users
Las funciones, como bien sus nombre nos indican, nos permitirán seperar nuestra lógica para poder crear nuevos usuarios,
consultarlos, editarlos, eliminarlos (Que es una nueva acción) y listarlos.
Con Excepción de list_users, cada una de estas funciones deberá recibir como parámetro el ID de usuario con el cual se
desea trabajar.
Un pro Tip. Recuerda que las opciones puedas almacenarlas en como llaves en un diccionario y que, quizás, puedas
almacenar las funciones en valores de esas llaves.
@author: Ing. Adrián Ezequiel Angió
"""

usuarios_lst = []  # lista de diccionarios de usuarios


def input_validado(campo, minimo, maximo):
    ingreso_valido = False
    variable = ""
    while not ingreso_valido:
        variable = input(f"Ingrese {campo}: ")
        if minimo <= len(variable) <= maximo:
            ingreso_valido = True
        else:
            print(f"El campo '{campo}' debe tener entre 5 y 50 caracteres. Reingrese.")
    return variable


def new_user():
    cantidad = int(input("Cuantos usuarios desea registrar?: "))
    for n in range(cantidad):
        print(f"Usuario ID N°: {n + 1}\n")

        nombre = input_validado('nombre', 5, 50)
        apellido = input_validado('apellido', 5, 50)
        telefono = input_validado('teléfono', 10, 10)
        email = input_validado('email', 5, 50)

        usuario_dic = {
            'id': n + 1,  # podría prescindir del id si uso como id la posicion de la lista...
            'nombre': nombre,
            'apellido': apellido,
            'telefono': telefono,
            'email': email
        }

        usuarios_lst.append(usuario_dic)

        print(f"\nHola {nombre} {apellido}, en breve recibirás un correo a {email}.")
        input("Pausa, presione cualquier tecla para seguir\n")


def show_user():
    """
    deberá buscar por ID en la lista de diccionarios de usuario, ya que ahora se pueden borrar
    y podrán quedar ID's no consecutivos, ya que la idea es que no se corran los ID's
    """
    usuario_id = int(input("Ingrese ID de cuyo usuario desea VER la información: "))

    id_encontrado = False

    for usuario_dic in usuarios_lst:
        if usuario_id == usuario_dic['id']:
            for clave in usuario_dic:
                print(f"{clave}: {usuario_dic[clave]}")

            id_encontrado = True
            break

    if not id_encontrado:
        print("ID no valido, vea listado de ID's")

    input("\nPausa, presione cualquier tecla para seguir\n")


def edit_user():
    usuario_id = int(input("Ingrese ID de cuyo usuario desea EDITAR la información: "))
    id_encontrado = False

    for usuario_dic in usuarios_lst:
        if usuario_id == usuario_dic['id']:
            id_encontrado = True
            break

    if not id_encontrado:
        print("ID no valido, vea listado de ID's")
        input("\nPausa, presione cualquier tecla para seguir\n")

    else:
        nombre = input_validado('nombre', 5, 50)
        apellido = input_validado('apellido', 5, 50)
        telefono = input_validado('teléfono', 10, 10)
        email = input_validado('email', 5, 50)

        print()
        usuario_dic = {
            'id': usuario_id,  # podría prescindir del id si uso como id la posicion de la lista...
            'nombre': nombre,
            'apellido': apellido,
            'telefono': telefono,
            'email': email
        }

        usuarios_lst[usuario_id - 1] = usuario_dic


def delete_user():
    usuario_id = int(input("Ingrese ID cuyo usuario desea BORRAR: "))
    id_encontrado = False

    for n, usuario_dic in enumerate(usuarios_lst):
        if usuario_id == usuario_dic['id']:
            del usuarios_lst[n]
            id_encontrado = True
            break

    if not id_encontrado:
        print("ID no valido, vea listado de ID's")

    input("\nPausa, presione cualquier tecla para seguir\n")


def list_users():
    if len(usuarios_lst) == 0:
        print("Ningún usuario creado aún!")
    else:
        print("Listado de todos los ID's de usuarios creados hasta el momento:")
        for u in usuarios_lst:
            print(u['id'])
    input("Pausa, presione cualquier tecla para seguir\n")


if __name__ == "__main__":
    continua = True

    while continua:
        print("A) Registrar nuevos usuarios\n"
              "B) Listar ID's de todos los usuarios\n"
              "C) Ver información de usuario de acuerdo con su ID\n"
              "D) Editar información de usuario de acuerdo con su ID\n"
              "E) Borrar usuario\n"
              "F) Salir")
        opcion = input("Ingrese su opción: ").upper()

        match opcion:
            case 'A':
                new_user()

            case 'B':
                list_users()

            case 'C':
                show_user()

            case 'D':
                edit_user()

            case 'E':
                delete_user()

            case 'F':
                print("\nGracias por haber usado este programa! Nos vemos pronto")
                continua = False

            case _:
                print("Opción incorrecta")
                input("Pausa, presione cualquier tecla para seguir\n")
