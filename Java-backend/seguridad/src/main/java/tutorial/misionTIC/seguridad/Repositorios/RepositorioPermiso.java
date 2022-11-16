package tutorial.misionTIC.seguridad.Repositorios;

import org.springframework.data.mongodb.repository.MongoRepository;
import tutorial.misionTIC.seguridad.Modelos.Permiso;

public interface RepositorioPermiso extends MongoRepository<Permiso, String> {
}
