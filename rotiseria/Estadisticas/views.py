from operator import itemgetter

from django.shortcuts import render
from Cadete.models import Cadete
from Estadisticas.forms import DateRangeForm, DateRangeCadeteForm
from Pedido.models import Pedido
from Plato.models import Plato


# Create your views here.

def Estadisticas(request):  # Vista comun que se ejecuta al entrar a la pág
    rangoFechasPedidosDiarios = DateRangeForm()  # Forms inicializados por cada estadistica disponible
    rangoFechasCantidadesCadete = DateRangeCadeteForm()
    rangoFechasPlatos = DateRangeForm()
    rangoFechasMenus = DateRangeForm()

    context = {  # Contexto. En todas las vistas incluye obligatoriamente los forms (para inicializarlos)
        'formPedidos': rangoFechasPedidosDiarios,
        'formMenus': rangoFechasMenus,
        'formCadete': rangoFechasCantidadesCadete,
        'formPlatos': rangoFechasPlatos,
    }
    return render(request, 'Estadisticas/estadisticas.html', context)


def ListarVentas(request):  # Listado de ventas/pedidos diarios en un rango de fechas
    pedidos = None  # Inicializada la variable en la que se almacenaran todos los pedidos realizados en un rango de fechas
    if request.method == 'POST':  # Si el formulario correspondiente fue completado
        rangoFechasPedidosDiarios = DateRangeForm(request.POST, request.FILES)
        if rangoFechasPedidosDiarios.is_valid():
            fecha_desde = rangoFechasPedidosDiarios[
                'Fecha_desde'].value()  # Se obtienen las fechas ingresadas por el usuario para obtener el rango de fecha en el que se obtendran los pedidos
            fecha_hasta = rangoFechasPedidosDiarios['Fecha_hasta'].value()
            pedidos = Pedido.objects.filter(fechaPedido__range=[fecha_desde,
                                                                fecha_hasta])  # Se obtienen (de la BD) todos los pedidos cuya fecha en la que fueron encargados se encuentra en el rango de fechas establecido anteriormente
    else:
        rangoFechasPedidosDiarios = DateRangeForm()  # Si el formulario no fue completado, entonces es inicializado para que el usuario tenga la oportunidad de completarlo
    print(
        rangoFechasPedidosDiarios.errors.as_data())  # Mensaje de error en consola en caso de que ocurra algun problema el cual deba ser investigado

    rangoFechasPedidosDiarios = DateRangeForm()
    rangoFechasCantidadesCadete = DateRangeCadeteForm()
    rangoFechasPlatos = DateRangeForm()
    rangoFechasMenus = DateRangeForm()

    context = {
        'formPedidos': rangoFechasPedidosDiarios,
        'formMenus': rangoFechasMenus,
        'formCadete': rangoFechasCantidadesCadete,
        'formPlatos': rangoFechasPlatos,
        'pedidos': pedidos,
        # Se envia dentro del contexto la variable pedidos para visualizar su información en el archivo HTML correspondiente
    }
    return render(request, 'Estadisticas/estadisticas.html', context)


def ListarCantidadesEntregadasPorCadete(request):
    pedidoCadete = None
    if request.method == 'POST':
        rangoFechasCantidadesCadete = DateRangeCadeteForm(request.POST,
                                                          request.FILES)  # Esta vista utiliza un Form distinto al resto, ya que ademas de pedir dos fechas tambien necesita saber qué cadete elegio.
        if rangoFechasCantidadesCadete.is_valid():
            fecha_desde = rangoFechasCantidadesCadete['Fecha_desde'].value()
            fecha_hasta = rangoFechasCantidadesCadete['Fecha_hasta'].value()
            cadete = rangoFechasCantidadesCadete[
                'Cadete'].value()  # Este formulario pide como valor extra, a un cadete encargado de llevar los pedidos. Se obtiene la clave primaria (o CUIL en este caso)
            ObjetoCadete = Cadete.objects.get(
                pk=cadete)  # Obtenemos la información del cadete utilizando la clave primaria
            cantidadEntregaPorCadete = cantidadPedidosDeUnCadete(ObjetoCadete, fecha_desde,
                                                                 fecha_hasta)  # Llamada a la función
            # cantidadPedidosDeUnCadete que se encarga de enumerar cuantos pedidos ha llevado un cadete en el rango
            # de fechas establecido

            nombreCadete = ObjetoCadete.nombre + ObjetoCadete.apellido  # La información que va a ser mostrada en
            # HTML, va a guardarse en una tupla de 3 elementos
            cuilCadete = ObjetoCadete.cuil
            pedidoCadete = (cuilCadete, nombreCadete, cantidadEntregaPorCadete)
    else:
        rangoFechasCantidadesCadete = DateRangeCadeteForm()
    print(rangoFechasCantidadesCadete.errors.as_data())
    rangoFechasPedidosDiarios = DateRangeForm
    rangoFechasPlatos = DateRangeForm()
    rangoFechasMenus = DateRangeForm()
    context = {
        'formPedidos': rangoFechasPedidosDiarios,
        'formMenus': rangoFechasMenus,
        'formCadete': rangoFechasCantidadesCadete,
        'formPlatos': rangoFechasPlatos,
        'pedidoCadete': pedidoCadete,
        # Envia la tupla con la información del cadete y la cantidad de pedidos entregados por este
    }
    return render(request, 'Estadisticas/estadisticas.html', context)


def cantidadPedidosDeUnCadete(cadete, fecha_desde,
                              fecha_hasta):  # Función utilizada por la vista ListarCantidadesEntregadasPorCadete. Se
    # encarga de contar cuantos pedidos fueron entregados por un cadete especifico en un rango de fechas establecido
    pedidos = Pedido.objects.filter(fechaPedido__range=[fecha_desde, fecha_hasta])
    contador = 0
    for pedido in pedidos:
        if (pedido.Cadete == cadete):
            contador += 1
    return contador


def ListarPlatosSolicitados(request):
    platosSolicitados = []
    if request.method == 'POST':
        rangoFechasMenus = DateRangeForm(request.POST, request.FILES)
        if rangoFechasMenus.is_valid():
            fecha_desde = rangoFechasMenus['Fecha_desde'].value()
            fecha_hasta = rangoFechasMenus['Fecha_hasta'].value()

            platos = Plato.objects.all()
            for plato in platos:  # Primero se almacena una lista de todos los platos registrados y por cada uno de
                # estos, obtenemos la información respecto a cuantas veces fue solicitado. Toda la información
                # relevante del plato es almacenada en una tupla la cual sera agregada a una lista de platos
                # solicitados.
                cantidadSolicitada = cantidadSolicitadaPlato(plato, fecha_desde, fecha_hasta)
                tuplaPlato = (plato.id, plato.nombre, plato.TipoPlato.tipoPlato, plato.Precio.precio, plato.Menu.tipo,
                              cantidadSolicitada)
                platosSolicitados.append(tuplaPlato)
            platosSolicitados = sorted(platosSolicitados, key=itemgetter(5),
                                       reverse=True)  # La lista es ordenada (de forma descencidente - reverse=True)
            # segun el 6to elemento (indice 5) de la tupla, el cual es la cantidad de veces que un plato fue
            # solicitado (key=itemgetter(5)
            platosSolicitados = platosSolicitados[
                                :5]  # Unicamente almacenamos los primeros 5 elementos de la lista (del indice 0 al
            # 5, sin incluir este ultimo)
    else:
        rangoFechasMenus = DateRangeForm()
    print(rangoFechasMenus.errors.as_data())

    rangoFechasPedidosDiarios = DateRangeForm()
    rangoFechasCantidadesCadete = DateRangeCadeteForm()
    rangoFechasPlatos = DateRangeForm()
    context = {
        'formPedidos': rangoFechasPedidosDiarios,
        'formMenus': rangoFechasMenus,
        'formCadete': rangoFechasCantidadesCadete,
        'formPlatos': rangoFechasPlatos,
        'platosSolicitados': platosSolicitados,
    }
    return render(request, 'Estadisticas/estadisticas.html', context)


def cantidadSolicitadaPlato(plato, fecha_desde,
                            fecha_hasta):  # Función utilizada por la vista ListarPlatosSolicitados. Se encarga de
    # contar cuantas veces un plato aparece en todos los pedidos realizados en un rango de fechas establecido.
    pedidos = Pedido.objects.filter(fechaPedido__range=[fecha_desde, fecha_hasta])
    contador = 0
    for pedido in pedidos:
        platosDelPedido = pedido.platos.all()
        for platoDelPedido in platosDelPedido:
            if plato.id == platoDelPedido.id:
                contador += 1
    return contador


def ListarMenus(request):  # Lista los menus e indica cuantas veces fueron solicitados
    menus = None
    if request.method == 'POST':
        rangoFechasMenus = DateRangeForm(request.POST, request.FILES)
        if rangoFechasMenus.is_valid():
            fecha_desde = rangoFechasMenus['Fecha_desde'].value()
            fecha_hasta = rangoFechasMenus['Fecha_hasta'].value()

            # Obtiene los valores de cuantos platos pedidos pertenecen a cada menu.
            cantidadNormal = cantidadPedidosDeUnMenu("Normal", fecha_desde, fecha_hasta)
            cantidadVegetariano = cantidadPedidosDeUnMenu("Vegetariano", fecha_desde, fecha_hasta)
            cantidadCeliaco = cantidadPedidosDeUnMenu("Celiaco", fecha_desde, fecha_hasta)
            cantidadDiabetico = cantidadPedidosDeUnMenu("Diabetico", fecha_desde, fecha_hasta)

            # Lista de tuplas, almacena el nombre de menu y la cantidad de veces que fue solicitado en algun plato.
            menus = [("Normal", cantidadNormal), ("Vegetariano", cantidadVegetariano), ("Celiaco", cantidadCeliaco),
                     ("Diabetico", cantidadDiabetico)]

            menus = sorted(menus, key=itemgetter(1),
                           reverse=True)  # Ordenado de mayor a menor, segun la cantidad de veces que fue solicitado.
    else:
        rangoFechasMenus = DateRangeForm()
    print(rangoFechasMenus.errors.as_data())
    rangoFechasPedidosDiarios = DateRangeForm()
    rangoFechasCantidadesCadete = DateRangeCadeteForm()
    rangoFechasPlatos = DateRangeForm()
    context = {
        'formPedidos': rangoFechasPedidosDiarios,
        'formMenus': rangoFechasMenus,
        'formCadete': rangoFechasCantidadesCadete,
        'formPlatos': rangoFechasPlatos,
        'menus': menus,
    }
    return render(request, 'Estadisticas/estadisticas.html', context)


def cantidadPedidosDeUnMenu(tipoMenu, fecha_desde,
                            fecha_hasta):  # Función utilizada por la vista ListarMenus. Se encarga de contar cuantas
    # veces un plato de un menu especifico aparece en cada uno de los pedidos realizados en un rango de fechas
    # establecido.
    pedidos = Pedido.objects.filter(fechaPedido__range=[fecha_desde, fecha_hasta])
    contador = 0
    for pedido in pedidos:
        platos = pedido.platos.all()
        for plato in platos:
            if plato.Menu.tipo == tipoMenu:
                contador += 1
    return contador
