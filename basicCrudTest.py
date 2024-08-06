users = []

def showOptions():
    print("""CRUD de usuarios
1.Agregar nuevo usuario
2.Mostrar usuarios
3.Actualizar usuario
4.Borrar usuario
5.Salir""")

def addUsers():
    while True:
        name = input('Ingrese el nombre: ').strip()
        if not name:
            print('Ingrese un nombre!')
            continue
        if name in users:
            print('Ese usuario ya existe!')
            continue
        print(f'El usuario {name} ha sido añadido exitosamente!')
        users.append(name)
        break

def showUsers():
    if not users:
        print('No hay usuarios por mostrar primero añade uno!')
        return
    for index, user in enumerate(users, 1):
        print(f'{index}. {user}')

def updUsers():
    if not users:
        print('No se han encontrado usuarios para modificar!')
        return
    while True:
        user = input('Ingrese el nombre del usuario que quiere actualizar: ').strip()
        if not user:
            print('Debes introducir el nombre del usuario a modificar!')
            continue
        if user not in users:
            print('El usuario no existe!')
            continue
        while True:
            newName = input('Introduzca el nuevo nombre: ').strip()
            if not newName:
                print('Debes introducir un nuevo nombre!')
                continue
            if newName in users:
                print('Ese nombre ya está en uso!')
                continue
            index = users.index(user)
            users[index] = newName
            print(f'Se ha actualizado el nombre del usuario {user} a {newName}')
            break
        break

def delUser():
    if not users:
        print('No hay usuarios para borrar!')
        return
    while True:
        user = input('Ingrese el nombre del usuario que quiere borrar: ').strip()
        if not user:
            print('Debes introducir el nombre del usuario a borrar!')
            continue
        if user not in users:
            print('El usuario no existe!')
            continue
        users.remove(user)
        print(f'El usuario {user} ha sido eliminado exitosamente!')
        break

while True:
    showOptions()
    while True:
        try:
            option = int(input('Seleccione una opción: '))
            if option not in range(1, 6):
                print('Debe escoger una de las opciones disponibles:')
                showOptions()
                continue
        except ValueError:
            print('Debe ingresar un número!')
            continue
        match option:
            case 1:
                addUsers()
                break
            case 2:
                showUsers()
                break
            case 3:
                updUsers()
                break
            case 4:
                delUser()
                break
            case 5:
                print('Adios!')
                exit()
