package tutorial.misionTIC.seguridad.Controladores;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;
import tutorial.misionTIC.seguridad.Modelos.Rol;
import tutorial.misionTIC.seguridad.Repositorios.RepositorioRol;

import java.util.List;

@CrossOrigin
@RestController
@RequestMapping("/rol")
public class ControladorRol {
    @Autowired
    private RepositorioRol miRepoRol;

    @ResponseStatus(HttpStatus.CREATED)
    @PostMapping("")
    public Rol created(@RequestBody Rol infoRol){
        return this.miRepoRol.save(infoRol);
    }

    @GetMapping("")
    public List<Rol> index(){
        return this.miRepoRol.findAll();
    }

    @GetMapping("{id}")
    public Rol show(@PathVariable String id){
        Rol rolActual = this.miRepoRol
                .findById(id)
                .orElse(null);
        return rolActual;
    }

    @PutMapping("{id}")
    public Rol update(@PathVariable String id, @RequestBody Rol infoRol){
        Rol rolActual = this.miRepoRol
                .findById(id)
                .orElse(null);
        if(rolActual != null){
            rolActual.setNombre(infoRol.getNombre());
            rolActual.setDescripcion(infoRol.getDescripcion());
            return this.miRepoRol.save(rolActual);
        }else{
            return null;
        }
    }

    @ResponseStatus(HttpStatus.NO_CONTENT)
    @DeleteMapping("{id}")
    public void delete(@PathVariable String id){
        Rol rolActual = this.miRepoRol
                .findById(id)
                .orElse(null);
        if(rolActual != null){
            this.miRepoRol.delete(rolActual);
        }
    }
}
