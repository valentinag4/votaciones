package tutorial.misionTIC.seguridad.Repositorios;

import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.mongodb.repository.Query;
import tutorial.misionTIC.seguridad.Modelos.Permiso;
import tutorial.misionTIC.seguridad.Modelos.Rol;

public interface RepositorioRol extends MongoRepository<Rol, String> {
    @Query("{'nombre':?0,'descripcion':?1}")
    Permiso getPermiso(String nombre, String descripcion);
}
