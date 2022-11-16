package tutorial.misionTIC.seguridad.Repositorios;

import org.springframework.data.mongodb.repository.MongoRepository;
import tutorial.misionTIC.seguridad.Modelos.Rol;

public interface RepositorioRol extends MongoRepository<Rol, String> {
}
