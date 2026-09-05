# API Flask - Gestión de Productos

Backend desarrollado en Flask con operaciones CRUD (GET, POST, PUT, DELETE) sobre un catálogo de productos.

## Requisitos previos

- Python instalado (verificar con `python --version`)
- Git instalado (verificar con `git --version`)
- Postman 

## Instructivo paso a paso

### 1. Clonar el repositorio

```bash
git clone https://github.com/MrHuesitozzz/api.git
cd api
```

### 2. Crear el entorno virtual

```bash
python -m venv .env
```

### 3. Activar el entorno virtual

En Windows (PowerShell):

```powershell
.\.env\Scripts\Activate.ps1
```

> Si aparece un error de permisos de ejecución de scripts, correr una sola vez:
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```

Cuando el entorno esté activo, el prompt se verá así:

```
(.env) PS C:\NTD\api>
```

### 4. Instalar las dependencias

```bash
pip install flask
```

O, si el proyecto incluye `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 5. Ejecutar la aplicación

```bash
python app.py
```

La consola debe mostrar algo como:

```
Running on http://127.0.0.1:5000
```

Dejar esta terminal abierta mientras se hacen las pruebas.

> _[Pantallazo: terminal mostrando la app corriendo]_

## Pruebas de los endpoints en Postman

Base URL: `http://127.0.0.1:5000`

> **Nota:** si Postman pide seleccionar un agente para conectarse a `127.0.0.1`, elegir **Desktop Agent** (no Cloud Agent), ya que el Cloud Agent no puede acceder a servidores locales.

### GET - Obtener todos los productos

- **Método:** GET
- **URL:** `http://127.0.0.1:5000/api/productos`
- **Body:** ninguno

Respuesta esperada: `200 OK` con el listado de productos en formato JSON.

> [Pantallazo: request y response del GET de todos los productos](ScreenShot-get.png)

### GET - Obtener un producto por ID

- **Método:** GET
- **URL:** `http://127.0.0.1:5000/api/productos/2`
- **Body:** ninguno

Respuesta esperada: `200 OK` con el producto solicitado, o `404 Not Found` si el ID no existe.

> [Pantallazo: request y response del GET por ID](ScreenShot-get1.png)

### POST - Crear un producto

- **Método:** POST
- **URL:** `http://127.0.0.1:5000/api/productos`
- **Body:** raw → JSON

```json
{
    "nombre": "Monitor",
    "precio": 300
}
```

Respuesta esperada: `201 Created` con el producto creado, incluyendo el `id` generado automáticamente.

> [Pantallazo: request y response del POST](ScreenShot-post.png)

### PUT - Actualizar un producto

- **Método:** PUT
- **URL:** `http://127.0.0.1:5000/api/productos/1` (reemplazar `1` por el ID del producto a actualizar)
- **Body:** raw → JSON

```json
{
    "precio": 999
}
```

Respuesta esperada: `200 OK` con el producto actualizado, o `404 Not Found` si el ID no existe.

> [Pantallazo: request y response del PUT](ScreenShot-put.png)

### DELETE - Eliminar un producto

- **Método:** DELETE
- **URL:** `http://127.0.0.1:5000/api/productos/1` (reemplazar `1` por el ID del producto a eliminar)
- **Body:** ninguno

Respuesta esperada: `200 OK` con un mensaje de confirmación, o `404 Not Found` si el ID no existe.

> [Pantallazo: request y response del DELETE](ScreenShot-del.png)

## Notas

- Los datos se almacenan en memoria (lista de Python), por lo que se reinician a los valores originales cada vez que se reinicia el servidor.
- Todas las peticiones con body (POST, PUT) deben configurarse en Postman como **Body → raw → JSON**, para que el header `Content-Type: application/json` se envíe automáticamente.
