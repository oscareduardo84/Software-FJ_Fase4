
# SOFTWARE FJ
## Sistema Integral de Gestión de Clientes, Servicios y Reservas

### 1. Descripción del proyecto

Software FJ es un sistema desarrollado en Python que permite administrar clientes, servicios y reservas mediante programación orientada a objetos (POO).

El proyecto busca facilitar el registro de clientes, la administración de servicios y el control de reservas, utilizando estructuras de datos en memoria, sin necesidad de una base de datos.

### 2. Objetivo general

Desarrollar un sistema de gestión que permita administrar clientes, servicios y reservas, aplicando los principios de programación orientada a objetos, encapsulamiento, herencia, abstracción, polimorfismo y manejo de excepciones.

### 3. Funcionalidades principales

- Registro y validación de clientes.
- Registro de servicios.
- Administración de reservas de salas.
- Alquiler de equipos.
- Gestión de asesorías especializadas.
- Búsqueda de clientes y servicios.
- Creación y registro de reservas.
- Confirmación, procesamiento y cancelación de reservas.
- Cálculo de costos con descuentos e impuestos.
- Control de errores mediante excepciones personalizadas.
- Registro de eventos y errores mediante archivos LOG.
- Consulta de clientes, servicios y reservas.

### 4. Tecnologías utilizadas

- Lenguaje de programación: Python.
- Entorno de desarrollo: Visual Studio Code.
- Paradigma: Programación orientada a objetos.
- Control de versiones: Git y GitHub.
- Manejo de registros: módulo logging.
- Manejo de excepciones: try, except, else y finally.

### 5. Estructura del proyecto

Software_FJ_Fase4/
- main.py
- README.md
- modelos/
  - entidad.py
  - cliente.py
  - servicio.py
  - reserva_salas.py
  - alquiler_equipos.py
  - asesoria.py
  - reserva.py
- gestion/
  - sistema.py
- excepciones/
  - errores.py
- registros/
  - sistema.log

### 6. Instrucciones de ejecución

1. Abrir la carpeta del proyecto en Visual Studio Code.
2. Verificar que Python esté instalado.
3. Abrir la terminal integrada.
4. Ejecutar el siguiente comando:

python main.py

5. Observar los resultados de las operaciones en la terminal.
6. Consultar el archivo registros/sistema.log para revisar los eventos y errores registrados.

### 7. Pruebas realizadas

Se realizaron pruebas de registro de clientes, registro de servicios, creación de reservas, confirmación, procesamiento y cancelación.

También se probaron situaciones incorrectas, como el registro de clientes duplicados, la búsqueda de información inexistente y la cancelación de reservas procesadas.

El sistema controla estas situaciones mediante excepciones y permite continuar con las siguientes operaciones.

### 8. Autor

Desarrollado por: Oscar Anaya

Programa académico: Ingeniería de Sistemas

Universidad: Universidad Nacional Abierta y a Distancia (UNAD)

Actividad: Fase 4 - Sistema Integral de Gestión de Clientes, Servicios y Reservas

### 9. Repositorio GitHub

Enlace del repositorio: Pendiente de publicar.
