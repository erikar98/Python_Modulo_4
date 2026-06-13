# appRegistro — Sistema de Gestión de Usuarios

Aplicación de consola en Python para registrar, consultar, buscar, eliminar y obtener estadísticas de usuarios almacenados en un archivo de texto plano.

## Autores:
Erika Yessenia Restrepo Sandoval.
Kevin Alejandro Lancheros Arevalo.

Proyecto desarrollado como ejercicio integrador de Python en el Módulo 4.
---

## Requisitos

- Python 3.x
- No requiere librerías externas

---

## Estructura de archivos

```
./
├── appRegistro.py       # Código fuente principal
├── usuarios.txt         # Base de datos de usuarios (se crea automáticamente)
├── logs_info.txt        # Registro de operaciones exitosas (se crea automáticamente)
├── logs_error.txt       # Registro de errores (se crea automáticamente)
└── README.md            # Este archivo
```

---

## Cómo ejecutar

```bash
python appRegistro.py
```

---

## Menú principal

Al ejecutar la aplicación se muestra el siguiente menú:

```
 ==== USUARIOS ====
1. Registrar usuario
2. Mostrar usuarios
3. Buscar usuario por nombre
4. Estadísticas de usuarios (cantidad y edad promedio)
5. Eliminar usuario por nombre
6. Salir
```

---

## Funcionalidades

### 1. Registrar usuario
Solicita nombre y edad. Guarda el registro en `usuarios.txt` con el formato:
```
nombre,edad,fecha_registro
```
- No permite nombres vacíos.
- No permite edades negativas ni no numéricas.
- No permite duplicados: si el nombre ya existe, rechaza el registro.

### 2. Mostrar usuarios
Lista todos los usuarios registrados con su nombre, edad y fecha de registro.
Si una línea del archivo tiene un formato inválido, la omite y la reporta en pantalla.

### 3. Buscar usuario por nombre
Solicita un nombre y lo busca en el archivo. Si lo encuentra, muestra nombre, edad y fecha. Si no existe, informa al usuario.

### 4. Estadísticas de usuarios
Submenú con dos opciones:
- **Opción 1 — Cantidad de usuarios:** muestra el total de registros en el archivo.
- **Opción 2 — Edad promedio:** calcula y muestra el promedio de edad de todos los usuarios válidos.
- **Opción 3 — Volver:** regresa al menú principal.

### 5. Eliminar usuario por nombre
Solicita un nombre y elimina el registro correspondiente del archivo.
- Funciona tanto con registros en formato válido (`nombre,edad,fecha`) como con líneas mal formadas (por ejemplo `nombre` sin comas).
- Si el nombre no existe, informa que no fue encontrado.
- Las líneas con formato inválido que **no coincidan** con el nombre a eliminar se conservan en el archivo.

### 6. Salir
Finaliza el programa.

---

## Formato del archivo `usuarios.txt`

Cada línea representa un usuario con tres campos separados por coma:

```
erika,28,2026-06-13 12:42:44.341515
kevin,26,2026-06-13 12:42:44.341515
```

| Campo          | Tipo   | Descripción                        |
|----------------|--------|------------------------------------|
| nombre         | string | Nombre del usuario                 |
| edad           | int    | Edad del usuario                   |
| fecha_registro | string | Fecha y hora del registro          |

---

## Sistema de logs

Todas las operaciones quedan registradas automáticamente en archivos de log:

| Archivo          | Contenido                                      |
|------------------|------------------------------------------------|
| `logs_info.txt`  | Operaciones exitosas (registros, búsquedas...) |
| `logs_error.txt` | Errores y formatos inválidos detectados        |

Formato de cada entrada de log:
```
<mensaje descriptivo>, Fecha: <fecha y hora>
```

---

## Manejo de errores

La aplicación maneja los siguientes errores en todas las operaciones:

| Error              | Mensaje mostrado                                        |
|--------------------|---------------------------------------------------------|
| `FileNotFoundError`| No se encontró el archivo de usuarios                  |
| `PermissionError`  | No se tienen permisos para leer/escribir en el archivo  |
| `ValueError`       | La edad debe de ser numérica                           |
| Formato inválido   | Formato de línea inválido: `<contenido de la línea>`   |
| Otros              | Ocurrió un error inesperado: `<detalle del error>`     |
