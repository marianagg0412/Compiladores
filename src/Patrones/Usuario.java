package Patrones;

public class Usuario {//Builder
    private String name;
    private String id;
    private String email;

    public String getName() {
        return name;
    }

    public Usuario setName(String name) {
        this.name = name;
        return this;
    }

    public String getId() {
        return id;
    }

    public Usuario setId(String id) {
        this.id = id;
        return this;
    }

    public String getEmail() {
        return email;
    }

    private Usuario(String id) {
        this.id = id;
    }

    public Usuario setEmail(String email) {
        this.email = email;
        return this;
    }

    public static Usuario make(String id){
        return new Usuario(id);
    }

    @Override //This is a decorator
    public String toString() {
        return "Usuario{" +
                "name='" + name + '\'' +
                ", id='" + id + '\'' +
                ", email='" + email + '\'' +
                '}';
    }

    public Usuario build(){
        return this;
    }

}
