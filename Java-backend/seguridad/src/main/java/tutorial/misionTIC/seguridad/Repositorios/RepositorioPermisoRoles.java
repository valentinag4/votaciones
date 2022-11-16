package tutorial.misionTIC.seguridad.Repositorios;
import org.springframework.data.mongodb.repository.Query;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface RepositorioPermisoRoles extends MongoRepository<PermisosRoles,String> {
    @Query("{'rol.$id ': ObjectId(?0),'permiso.$id': ObjectId(?1)}")
    PermisosRoles getPermisoRol(String id_rol,String id_permiso);
}