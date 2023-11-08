# auth-easy



     Animal {
        id          INT         primary key
        nombre      VARCHAR(255)
        raza        VARCHAR(255)
        sexo        VARCHAR(255)
        fechaNacimiento DATE
    }

    Nacimiento {
        id          INT         primary key
        fecha       DATE
        hora        TIME
        lugar       VARCHAR(255)
        animal_id   INT         references Animal
    }

    Enfermedad {
        id          INT         primary key
        nombre      VARCHAR(255)
        descripcion VARCHAR(255)
        sintomas    VARCHAR(255)
        animal_id   INT         references Animal
    }

    Evolución {
        id          INT         primary key
        fecha       DATE
        peso        BIGINT
        altura      FLOAT
        animal_id   INT         references Animal
    }
´´´
