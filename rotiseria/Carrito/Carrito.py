class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito

    def agregar(self, plato):
        id = str(plato.id)
        if id not in self.carrito.keys():
            self.carrito[id]={
                "plato_id": plato.id,
                "nombre": plato.nombre,
                "descripcion": plato.descripcionPlato,
                "tipoPlato": plato.TipoPlato.tipoPlato,
                "acumulado": plato.Precio.precio,
                "activo": plato.activo,
                "menu": plato.Menu.tipo,
                "cantidad": 1,
            }
        else:
            self.carrito[id]["cantidad"] += 1
            self.carrito[id]["acumulado"] += plato.Precio.precio
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, plato):
        id = str(plato.id)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()

    def restar(self, plato):
        id = str(plato.id)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1
            self.carrito[id]["acumulado"] -= plato.Precio.precio
            if self.carrito[id]["cantidad"] <= 0: self.eliminar(plato)
            self.guardar_carrito()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True