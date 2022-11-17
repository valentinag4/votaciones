package tutorial.misionTIC.seguridad.Controladores;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;
import tutorial.misionTIC.seguridad.Modelos.Rol;
import tutorial.misionTIC.seguridad.Modelos.Usuario;
import tutorial.misionTIC.seguridad.Repositorios.RepositorioRol;
import tutorial.misionTIC.seguridad.Repositorios.RepositorioUsuario;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.List;

@CrossOrigin
@RestController
@RequestMapping("/usuario")
public class ControladorUsuario {
    @Autowired
    private RepositorioUsuario miRepoUsuario;

    @Autowired
    private RepositorioRol miRepoRol;

    @ResponseStatus(HttpStatus.CREATED)
    @PostMapping
    public Usuario create(@RequestBody Usuario infoUsuario){
        infoUsuario.setContrasena(convertirSHA256(infoUsuario.getContrasena()));
        return this.miRepoUsuario.save(infoUsuario);
    }

    @GetMapping("")
    public List<Usuario> index(){
        return this.miRepoUsuario.findAll();
    }

    @GetMapping("{id}")
    public Usuario show(@PathVariable String id){
        Usuario usuarioActual = this.miRepoUsuario
                .findById(id)
                .orElse(null);
        return usuarioActual;
    }

    @PutMapping("{id}")
    public Usuario update(@PathVariable String id, @RequestBody Usuario infoUsuario){
        Usuario usuarioActual = this.miRepoUsuario
                .findById(id)
                .orElse(null);
        if(usuarioActual != null){
            usuarioActual.setSeudonimo(infoUsuario.getSeudonimo());
            usuarioActual.setCorreo(infoUsuario.getCorreo());
            usuarioActual.setContrasena(convertirSHA256(infoUsuario.getContrasena()));
            return this.miRepoUsuario.save(usuarioActual);
        }else{
            return null;
        }
    }

    @ResponseStatus(HttpStatus.NO_CONTENT)
    @DeleteMapping("{id}")
    public void delete(@PathVariable String id){
        Usuario usuarioActual = this.miRepoUsuario
                .findById(id)
                .orElse(null);
        if(usuarioActual != null){
            this.miRepoUsuario.delete(usuarioActual);
        }
    }

    /**
     * Relación (1 a n) entre usuario y rol
     * @param
     * @return
     * Correcto
     */
    @PutMapping("{id}/rol/{id_rol}")
    public Usuario asignarRolUsuario(@PathVariable String id, @PathVariable String id_rol){
        Usuario usuarioActual = this.miRepoUsuario
                .findById(id)
                .orElse(null);
        Rol rolActual = this.miRepoRol
                .findById(id_rol)
                .orElse(null);
        if(usuarioActual != null && rolActual != null){
            usuarioActual.setRol(rolActual);
            return this.miRepoUsuario.save(usuarioActual);
        }else{
            return null;
        }
    }

    public String convertirSHA256(String password) {
        MessageDigest md = null;
        try {
            md = MessageDigest.getInstance("SHA-256");
        }
        catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
            return null;
        }
        byte[] hash = md.digest(password.getBytes());
        StringBuffer sb = new StringBuffer();
        for(byte b : hash) {
            sb.append(String.format("%02x", b));
        }
        return sb.toString();
    }
}
