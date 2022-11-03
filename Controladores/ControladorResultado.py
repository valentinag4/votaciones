from Modelos.Resultado import Resultado
from Modelos.Mesa import Mesa
from Modelos.Candidato import Candidato
from Modelos.Partido import Partido
from Repositorios.RepositorioResultado import RepositorioResultado
from Repositorios.MesaRepositorio import MesaRepositorio
from Repositorios.RepositorioPartido import RepositorioPartido
from Repositorios.CandidatoRepositorio import CandidatoRepositorio

class ControladorResultado():

    def __init__(self):
        self.repositorioResultado = RepositorioResultado()
        self.repositorioMesa = MesaRepositorio()
        self.repositorioPartido = RepositorioPartido()

    def index(self):
        return self.repositorioResultado.findAll()

    def create(self, infoResultados, id_mesa, id_candidato):
        nuevoResultado = Resultado(infoResultados)
        laMesa = Mesa(self.repositorioMesa.findById(id_mesa))
        elCandidato = Candidato(self.repositorioCandidato.findById(id_candidato))
        nuevoResultado.mesa = laMesa
        nuevoResultado.candidato = elCandidato
        return self.repositorioResultado.save()

    def show(self, id):
        elResultado = Resultado(self.repositorioResultado.findById(id))
        return elResultado.__dict__

    def update(self, id, infoResultados, id_mesa, id_candidato):
        elResultado = Resultado(self.repositorioResultado.findById(id))
        elResultado.Numero_mesa = infoResultados["Numero_mesa"]
        elResultado.id_partido = infoResultados["id_partido"]
        laMesa = Mesa(self.repositorioMesa.findById(id_mesa))
        elCandidato = Candidato(self.repositorioCandidato.findById(id_candidato))
        elResultado.mesa = laMesa
        elResultado.candidato = elCandidato
        return self.repositorioResultado.save(elResultado)

    def delete(self, id):
        return self.repositorioResultado.delete(id)
