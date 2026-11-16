flowchart TD
    Cliente["Cliente HTTP"]
    Main["main.py<br/>Crea FastAPI e incluye routers"]

    subgraph Routers["routers/"]
        Post["POST.py<br/>POST /post_taks/post/"]
        Get["GET.py<br/>GET /get_taks/get"]
        Put["PUT.py<br/>PUT /put_taks/{id}"]
        Delete["DELETE.py<br/>DELETE /delete_taks/{id}"]
    end

    Model["models/task.py<br/>Tasks: id, title, description, completed"]

    subgraph Service["services/task_service.py"]
        Create["task_create(task)"]
        List["list_tasks()"]
        State[("task_list<br/>Lista compartida en memoria")]
    end

    Cliente --> Main
    Main --> Post
    Main --> Get
    Main --> Put
    Main --> Delete

    Post -->|"Valida el cuerpo"| Model
    Post --> Create
    Create -->|"Agrega tarea"| State
    Create -->|"Devuelve tarea creada"| Post

    Get --> List
    List -->|"Lee todas las tareas"| State
    List -->|"Devuelve la lista"| Get

    Put -->|"Valida el cuerpo"| Model
    Put -->|"Busca por id y reemplaza"| State
    Delete -->|"Busca por id y elimina"| State

    Post --> Cliente
    Get --> Cliente
    Put --> Cliente
    Delete --> Cliente