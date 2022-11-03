from Repositorios.MesaRepositorio import MesaRepositorio
from Modelos.Mesa import Mesa

class ControladorMesa():
    def __init__(self):
        self.mesaRepositorio = MesaRepositorio()

    def index(self):
        print('Listando todas las mesas...')
        return self.mesaRepositorio.findAll()

    def create(self, laMesa):
        print('Creando la mesa...')
        nuevaMesa = Mesa(laMesa)
        return self.mesaRepositorio.save(nuevaMesa)

    def show(self, id):
        print('Listando la mesa con id ', id)
        laMesa = Mesa(self.mesaRepositorio.findById(id))
        return laMesa.__dict__

    def update(self, id, laMesa):
        print('Modificando la mesa con id ', id)
        mesaActual = Mesa(self.mesaRepositorio.findById(id))
        mesaActual.numero = laMesa["numero"]
        mesaActual.cantidad_inscritos = laMesa["cantidad_inscritos"]
        return self.mesaRepositorio.save(mesaActual)

    def delete(self, id):
        print('Eliminando la mesa con id ', id)
        return self.mesaRepositorio.delete(id)
