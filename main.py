import gestor

ls = gestor.from_event()

while True:
    des = input(
    "que desea hacer: \n" \
    "1 - crear evento\n" \
    "2 - eliminar evento\n" \
    "3 - editar evento\n" \
    "4 - listar eventos\n" \
    "0 - salir: ")

    if des == '0':
        gestor.save_event(ls)
        break

    if des == '1':
        aux = gestor.crear_evento()
        ls.append(aux)
    elif des == '2':
        gestor.eliminar_evento(ls)
    elif des == '3':
        gestor.edit_event(ls)
    elif des == '4':
        gestor.list_event(ls)
    else:
        print ("variable fuera de rango")
