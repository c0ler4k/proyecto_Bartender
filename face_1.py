menu = 0
usuarios_validos = ["joel","jesulym"]
contraseñas_validos = ["jadr","apolo"]
contraseñas_admi = ["wilfre"]
administrador = ["profe"]
llave_valida = ("root")
tragos = ["Cosmopolita","Mojito","Mai Tai","Julepe de Menta","Caipirinha","Margarita","Piña colada","Califormication","Long Island Iced Te","Margarita de Manzana",""]
licores = ["Licor de Manzana","Licor de Naranja" ,"Ginebra","Tequila","Ron Brasileño","Vodka","Triple Sec","Ron blanco","Ron","Curazao de Naranja","Bourbon",""]
ingredientes = ["zumo de manzana","cola","jugo de naranja","jugo piña","leche de coco","sal","hielo","azucar morena","menta","zumo de limon ","zumo de arandano","agua","agua con gas","azucar granulada ","azucar en polvo","hierba buena","sirope de horchata",""]
rankin = []
while menu <=3:
    menu = int(input("1.ingresar\n2.registra te\n"))
    if menu == 1:
        usuario = input("ingrese usuario :")
        contraseña = input("ingrese contraseña :")
        if usuario in usuarios_validos and contraseña in contraseñas_validos:
            menu_usu = 0
            print(f"bienvenido {usuario}")
            print("(ojo en tal caso de querer eliminar un registro solo debes \ncolocar el nombre que deseas borrar y luego dejar \nla segunda opcion en blanco) ")
            while menu_usu<=6:
                menu_usu = int(input("1.deseas ver tus tragos favoritos \n2.deseas agregar nuevos tragos a la lista \n3.deseas ver el rankin\n4.modificar lista de tragos\n5.mocdificar lista de licores\n6.modificar lista de ingredientes\n7.salir"))
                if menu_usu ==1:
                    for i in range(len(tragos)):
                        print("\n"+tragos[i])
                elif menu_usu ==2:
                    print("esta es la lista de licores e ingredientes disponibles para crear un nuevo trago :")
                    print("LICORES")
                    for w in range(len(licores)):
                            print(licores[w])
                    print("\nINGREDIENTES")
                    for e in range(len(ingredientes)):
                        print(ingredientes[e])
                    tragos_nuevo = input("ingrese el nombre del nuevo trago ")
                    if tragos_nuevo!="":
                        tragos.append(tragos_nuevo)
                elif menu_usu==3:
                    print("esta es el rankin",rankin)
                elif menu_usu == 4:
                    tragos_mod = input("ingrese el nombre del trago que desea modificar")
                    a = tragos.index(tragos_mod)
                    tragos.remove(tragos_mod)
                    tragos_mod = input("ingrese el nuevo trago :")
                    tragos.insert(a,tragos_mod)
                    if tragos_mod=="":
                        tragos.pop(a)
                elif menu_usu == 5:
                    licores_mod = input("ingrese el nombre del licor que desea modificar :")
                    a = licores.index(licores_mod)
                    licores.remove(licores_mod)
                    licores_mod = input("ingrese el nuevo licor :")
                    licores.insert(a, licores_mod)
                    if licores_mod=="":
                        licores.pop(a)
                elif menu_usu == 6:
                    ingredientes_mod = input("ingrese el nombre del ingrediente que desea modificar :")
                    a = ingredientes.index(ingredientes_mod)
                    ingredientes.remove(ingredientes_mod)
                    ingredientes_mod = input("ingrese el nuevo ingrediente :")
                    ingredientes.insert(a,ingredientes_mod)
                    if ingredientes_mod=="":
                        ingredientes.pop(a)
                else:
                    print("error: opcion invalida ")
        elif usuario in administrador and contraseña in contraseñas_admi:
            menu_admi = 0
            print("bienvenido ",usuario)
            while menu_admi <=2:
                print("estos son todos usuariso de la plataforma ")
                a = 0
                for x in range(len(usuarios_validos)):
                    a += 1
                    c = len(usuarios_validos) - a
                    print(usuarios_validos[c])
                menu_admi = int(input("1.desea eliminar algun usuario\n2.o modificar sus registros\n3.salir "))
                if menu_admi == 1:
                    menu_admi_sub = int(input("el usuario es administrador \n1.Si\n2.No"))
                    if menu_admi_sub==2:
                        usuario_borrar = input("ingrese el nombre del usuario a eliminar:\n")
                        eleccion = int(input("estas seguro que desas eliminar al ususario\n1.Si\n2.No"))
                        if eleccion == 1:
                            eleccion = input("ingrese la llave maestra:\n")
                            if eleccion == llave_valida:
                                contraseña_borrar = usuarios_validos.index(usuario_borrar)
                                usuarios_validos.remove(usuario_borrar)
                                contraseñas_validos.pop(contraseña_borrar)
                            else:
                                print("llave invalida ")
                    elif menu_admi_sub==1:
                        validacion = input("ingrese la llave maestra :")
                        if validacion==llave_valida:
                            usuario_borrar= input("ingrese el nombre del administrador que desea borrar")
                            contraseña_borrar = administrador.index(usuario_borrar)
                            administrador.remove(usuario_borrar)
                            contraseñas_admi.pop(contraseña_borrar)
                elif menu_admi == 2:
                    print("desea modificar o eliminar :\n(ojo en tal caso de querer eliminar un registro solo debes \ncolocar el nombre que deseas eliminar y luego dejar \nla segunda opcion en blanco )")
                    menu_mod = int(input("1.nombre de usuario \n2.contraseña\n3.tragos\n4.licores\n5.ingredientes\n6.salir"))
                    if menu_mod == 1:
                        usuario_mod = input("ingrese el nombre del usuario a modificar ")
                        usuario_mod2 = usuarios_validos.index(usuario_mod)
                        usuarios_validos.remove(usuario_mod)
                        usuario_mod = input("ingrese el nombre del usuario nuevo")
                        usuarios_validos.insert(usuario_mod2,usuario_mod)
                    elif menu_mod == 2:
                        usuario_mod = input("ingrese el nombre del usuario al que\n se le modificara la contraseña ")
                        a = usuarios_validos.index(usuario_mod)
                        contraseñas_validos.pop(a)
                        contraseñas_validos.insert(a,input("ingrese contraseña nueva"))
                    elif menu_mod == 3:
                        tragos_mod = input("ingrese el nombre del trago que desea modificar")
                        a = tragos.index(tragos_mod)
                        tragos.remove(tragos_mod)
                        tragos_mod = input("ingrese el nuevo trago :")
                        tragos.insert(a,tragos_mod)
                        if tragos_mod=="":
                            tragos.pop(a)
                    elif menu_mod == 4:
                        licores_mod = input("ingrese el nombre del trago que desea modificar")
                        a = licores.index(licores_mod)
                        licores.remove(licores_mod)
                        licores_mod = input("ingrese el nuevo trago :")
                        licores.insert(a, licores_mod)
                        if licores_mod=="":
                            licores.pop(a)
                    elif menu_mod == 5:
                        ingredientes_mod = input("ingrese el nombre del trago que desea modificar")
                        a = ingredientes.index(ingredientes_mod)
                        ingredientes.remove(ingredientes_mod)
                        ingredientes_mod = input("ingrese el nuevo trago :")
                        ingredientes.insert(a,ingredientes_mod)
                        if ingredientes_mod=="":
                            ingredientes.pop(a)
        else:
            print("usuario o contraseña invalida ")
    elif menu == 2:
        menu = int(input("1.creacion de usuario regular \n2.greacion de usuartio administrador "))
        if menu == 1:
            usuarios_validos.append(input("nombre del usuario :"))
            contraseñas_validos.append((input("ingrese la comtraseña :")))
        elif menu == 2:
            llave = input("ingrese llave maestra :")
            if llave == llave_valida:
                administrador.append(input("ingrese nombre del nuevo administrador :\n"))
                contraseñas_admi.append(input("ingrese la clave del nuevo administador "))
            else:
                print("error: opcion invalida ")
        else:
            print("error: opcion invalida ")
    else:
        print("error: opcion invalida ")
    print(usuarios_validos,contraseñas_validos,administrador,contraseñas_admi)
    menu = 0
    a = input("hola")