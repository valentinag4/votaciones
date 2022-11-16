package tutorial.misionTIC.seguridad.Controladores;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;
import tutorial.misionTIC.seguridad.Modelos.Permiso;
import tutorial.misionTIC.seguridad.Repositorios.RepositorioPermiso;

import java.util.List;

@CrossOrigin
@RestController
@RequestMapping("/permiso")
public class ControladorPermiso {
    @Autowired
    private RepositorioPermiso miRepoPermiso;

    @GetMapping("")
    public List<Permiso> index(){
        return this.miRepoPermiso.findAll();
    }

    @ResponseStatus(HttpStatus.CREATED)
    @PostMapping
    public Permiso create(@RequestBody  Permiso infoPermiso){
        return this.miRepoPermiso.save(infoPermiso);
    }

    @GetMapping("{id}")
    public Permiso show(@PathVariable String id){
        Permiso permisoActual = this.miRepoPermiso
                .findById(id)
                .orElse(null);
        return permisoActual;
    }

    @PutMapping("{id}")
    public Permiso update(@PathVariable String id,@RequestBody  Permiso infoPermiso){
        Permiso permisoActual=this.miRepoPermiso
                .findById(id)
                .orElse(null);
        if (permisoActual!=null){
            permisoActual.setUrl(infoPermiso.getUrl());
            permisoActual.setMetodo(infoPermiso.getMetodo());
            return this.miRepoPermiso.save(permisoActual);
        }else{
            return  null;
        }
    }

    @ResponseStatus(HttpStatus.NO_CONTENT)
    @DeleteMapping("{id}")
    public void delete(@PathVariable String id){
        Permiso permisoActual=this.miRepoPermiso
                .findById(id)
                .orElse(null);
        if (permisoActual!=null){
            this.miRepoPermiso.delete(permisoActual);
        }
    }
}
