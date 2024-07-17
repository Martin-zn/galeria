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

    def agregar(self, Obras):
        id = str(Obras.id_obra)
        if id not in self.carrito.keys():
            self.carrito[id]={
                "obra_id":Obras.id_obra,
                "nombre":Obras.nombre,
                "acumulado":Obras.precio,
                "cantidad":1,
            }
        else:
            self.carrito[id]["cantidad"] = 1
            # self.carrito[id]["acumulado"]
        self.guardar_carrito()

    
    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, Obras):
        id = str(Obras.id_obra)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True
