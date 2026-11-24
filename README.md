# Catálogo musical

API de Django REST Framework para gestionar álbumes y canciones. Usa SQLite y conserva los comandos del archivo original.

## Ejecutar en local

Necesitas Python 3.10 o posterior. Abre una terminal en la carpeta que contiene `app.py`.

```bash
python -m pip install -r requirements.txt
python app.py
```

Al iniciar, Django prepara la base de datos y carga un álbum de ejemplo si el catálogo está vacío. Para reutilizar una base del proyecto original que ya tenga ambas tablas, copia `catalogo.sqlite3` junto a `app.py` antes de iniciar.

| Recurso | URL local |
| --- | --- |
| Índice de la API | http://localhost:8000/api/ |
| Álbumes | http://localhost:8000/api/albumes/ |
| Canciones | http://localhost:8000/api/tracks/ |

Para ejecutar la prueba original de 100 peticiones, deja el servidor activo y abre una segunda terminal en la misma carpeta.

```bash
python app.py prueba
```

La configuración incluida está pensada para desarrollo local. La API permite operaciones CRUD sin autenticación.

## Subir a GitHub

Descomprime el ZIP y sube el contenido de esta carpeta a tu repositorio. Conserva las carpetas `catalogo/` y `proyecto/` y asegúrate de incluir `.gitignore`. La base SQLite y el entorno virtual se excluyen del repositorio.
