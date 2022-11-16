package tutorial.misionTIC.seguridad.Repositorios;
import org.springframework.data.mongodb.repository.Query;
import org.springframework.data.mongodb.repository.MongoRepository;
import tutorial.misionTIC.seguridad.Modelos.PermisoRoles;

public interface RepositorioPermisoRoles extends MongoRepository<PermisoRoles,String> {
    @Query("{'rol.$id ': ObjectId(?0),'permiso.$id': ObjectId(?1)}")
    PermisoRoles getPermisoRol(String id_rol,String id_permiso);
}