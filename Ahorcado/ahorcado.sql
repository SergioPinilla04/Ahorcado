CREATE TABLE usuarios (
    usuario VARCHAR(50) PRIMARY KEY,
    contrasena_hash VARCHAR(255) NOT NULL
);

CREATE TABLE intentos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(50),
    palabra VARCHAR(50),
    n_fallos INT,
	FOREIGN KEY (usuario) REFERENCES usuarios(usuario) ON DELETE CASCADE
)ENGINE=INNODB;

select * from intentos;
select * from usuarios;