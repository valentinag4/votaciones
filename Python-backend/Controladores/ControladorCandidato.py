from Repositorios.CandidatoRepositorio import CandidatoRepositorio
from Repositorios.RepositorioPartido import RepositorioPartido
from Modelos.Candidato import Candidato
from Modelos.Partido import Partido

#valen
class ControladorCandidato():
    def __init__(self):
        self.candidatoRepositorio = CandidatoRepositorio()
        self.partidoRepositorio = RepositorioPartido()

    def index(self):
        print('Listando todas los candidatos...')
        return self.candidatoRepositorio.findAll()

    def create(self, elCandidato):
        print('Creando el candidato...')
        nuevoCandidato = Candidato(elCandidato)
        return self.candidatoRepositorio.save(nuevoCandidato)

    def show(self, id):
        print('Listando el candidato con id ', id)
        elCandidato = Candidato(self.candidatoRepositorio.findById(id))
        return elCandidato.__dict__

    def update(self, id, elCandidato):
        print('Modificando el candidato con id ', id)
        candidatoActual = Candidato(self.candidatoRepositorio.findById(id))
        candidatoActual.cedula = elCandidato["cedula"]
        candidatoActual.numero_resolucion = elCandidato["numero_resolucion"]
        candidatoActual.nombre = elCandidato["nombre"]
        candidatoActual.apellido = elCandidato["apellido"]
        return self.candidatoRepositorio.save(candidatoActual)

    def delete(self, id):
        print('Eliminando el candidato con id ', id)
        return self.candidatoRepositorio.delete(id)

    def asignarPartido(self, id, id_partido):
        candidatoActual = Candidato(self.candidatoRepositorio.findById(id))
        partidoActual = Partido(self.partidoRepositorio.findById(id_partido))
        candidatoActual.Partido = partidoActual
        return self.candidatoRepositorio.save(candidatoActual)
