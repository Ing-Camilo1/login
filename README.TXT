Descripción del Proyecto
Este proyecto es una aplicación web de gestión de usuarios que permite a los usuarios gestionar sus cuentas a través de las siguientes funcionalidades:

Inicio de Sesión: Permite a los usuarios autenticarse con sus credenciales para acceder a la plataforma.
Crear Cuenta: Los usuarios pueden crear nuevas cuentas proporcionando su nombre completo, correo electrónico y contraseña.
Restablecimiento de Contraseña: Permite a los usuarios restablecer su contraseña en caso de olvido.
Página Principal: Después del inicio de sesión, los usuarios serán redirigidos a una página principal donde se muestra su información y un mensaje de bienvenida.
Tecnologías Utilizadas
Backend: El backend de la aplicación está desarrollado en Python utilizando Flask.
Base de Datos: La base de datos está gestionada con MySQL, administrada a través de MySQL Workbench.
Frontend: Se han implementado formularios y páginas web utilizando HTML y JavaScript.
Estructura de la Base de Datos
La base de datos utilizada para la gestión de usuarios se llama user_management y contiene las siguientes tablas:

Tabla Usuarios
Esta tabla almacena la información básica de los usuarios.
CREATE DATABASE IF NOT EXISTS user_management;
USE user_management;

CREATE TABLE Usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_completo VARCHAR(255) NOT NULL,
    correo_electronico VARCHAR(255) UNIQUE NOT NULL,
    contrasena VARCHAR(255) NOT NULL,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
id: Identificador único del usuario (clave primaria).
nombre_completo: Nombre completo del usuario.
correo_electronico: Correo electrónico del usuario, debe ser único.
contrasena: Contraseña del usuario.
fecha_creacion: Fecha y hora en que se creó la cuenta.
Tabla Sesiones
Esta tabla gestiona las sesiones de los usuarios para el inicio de sesión y la autenticación.
CREATE TABLE Sesiones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT,
    token_sesion VARCHAR(255) UNIQUE NOT NULL,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_expiracion TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES Usuarios(id)
);
id: Identificador único de la sesión (clave primaria).
usuario_id: Identificador del usuario asociado a la sesión (clave foránea).
token_sesion: Token único de sesión para autenticar al usuario.
fecha_creacion: Fecha y hora en que se creó la sesión.
fecha_expiracion: Fecha y hora en que la sesión expirará.
Cómo Ejecutar el Proyecto
Instalar Dependencias: Asegúrate de tener Python y las dependencias necesarias instaladas. Puedes instalar las dependencias con el siguiente comando:
pip install -r requirements.txt
Configurar la Base de Datos: Ejecuta los scripts SQL proporcionados para crear la base de datos y las tablas en MySQL Workbench.

Ejecutar la Aplicación: Inicia la aplicación Flask con el siguiente comando:
python app.py
Acceder a la Aplicación: Abre tu navegador web y navega a http://localhost:5000 para interactuar con la aplicación.
Estructura del Proyecto
app.py: Archivo principal que contiene el backend de la aplicación Flask.
static/: Carpeta que contiene los archivos estáticos como CSS y JavaScript.
templates/: Carpeta que contiene los archivos HTML para las diferentes páginas de la aplicación.
requirements.txt: Archivo que lista las dependencias necesarias para el proyecto.