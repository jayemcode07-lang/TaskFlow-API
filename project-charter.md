# TaskFlow API — Definición y alcance del proyecto

## 1. Problema o necesidad

TaskFlow API es un proyecto personal de aprendizaje orientado al desarrollo backend. No surge de una necesidad empresarial específica, sino de la intención de adquirir experiencia práctica en la construcción y gestión de software.

Como caso de estudio, se desarrollará una API REST para administrar tareas, permitiendo practicar operaciones básicas de registro, consulta, actualización y eliminación de información.

## 2. Objetivo del proyecto

Desarrollar una API REST utilizando Python y FastAPI que permita gestionar tareas mediante operaciones CRUD, aplicando principios básicos de desarrollo backend y gestión de proyectos de software.

### Objetivos de aprendizaje

- Aprender a gestionar un proyecto de software de manera organizada.
- Aplicar Python y FastAPI en la construcción de endpoints REST.
- Implementar operaciones CRUD.
- Fortalecer la lógica de programación.
- Utilizar Git, GitHub y GitHub Projects para gestionar tareas y versiones.
- Incorporar progresivamente buenas prácticas de desarrollo, documentación y pruebas.

## 3. Usuarios

La aplicación será utilizada inicialmente por su propio desarrollador, con fines de aprendizaje y pruebas.

No se implementará un sistema de cuentas de usuario en la primera versión.

## 4. Alcance del MVP

La primera versión permitirá gestionar tareas mediante una API REST.

| Método | Endpoint | Funcionalidad |
|---|---|---|
| POST | /tasks | Crear una tarea |
| GET | /tasks | Consultar todas las tareas |
| GET | /tasks/{id} | Consultar una tarea específica |
| PATCH | /tasks/{id} | Actualizar una tarea |
| DELETE | /tasks/{id} | Eliminar una tarea |

Cada tarea tendrá los siguientes atributos:

- Identificador único.
- Título.
- Descripción.
- Estado de completado.

**Tecnologías iniciales:**

- Python.
- FastAPI.
- Pydantic.
- Almacenamiento temporal en memoria.
- Git y GitHub.

La versión inicial incluirá validaciones básicas de datos y manejo de errores comunes.

## 5. Fuera del alcance inicial

Las siguientes funcionalidades se consideran mejoras para versiones posteriores:

- Persistencia en bases de datos SQLite o PostgreSQL.
- Autenticación y autorización de usuarios.
- Interfaz gráfica frontend.
- Notificaciones automáticas.
- Integración con inteligencia artificial.
- Funcionalidades avanzadas de seguridad.

## 6. Criterios de éxito

Se considerará completado el MVP cuando:

1. Los cinco endpoints CRUD funcionen correctamente.
2. Sea posible crear, consultar, actualizar y eliminar tareas.
3. La API valide los datos de entrada.
4. Las solicitudes a tareas inexistentes devuelvan una respuesta de error apropiada.
5. Los endpoints puedan probarse mediante la documentación interactiva de FastAPI.
6. Las pruebas automatizadas definidas para el MVP se ejecuten correctamente.
7. El código y las instrucciones de ejecución estén documentados en GitHub.

El almacenamiento será temporal en esta versión; los datos podrán perderse al reiniciar la aplicación.
