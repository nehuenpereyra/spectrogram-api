# Spectrogram API

## Prerequisitos

- [Python 3.9 o superior](https://www.python.org/downloads/)
- [Poetry](https://python-poetry.org/) para manejar la gestion de dependencias de la app (solo ejecutar `pip install poetry`)


## Inicialización del proyecto

1. Clonar el repositorio

```
git clone git@github.com:nehuenpereyra/spectrogram-api.git
```

2. Instalar depedencias

```
cd spectrogram-api
poetry install
poetry lock
```

3. Establecer las variables de entorno en el archivo `.env`

- Crear el archivo: `touch .env`
- Se puede tomar de ejemplo el archivo `.env.example`

4. Ejecutar en local

```bash
task dev
```

## Documentación de la API

En el siguiente enlace puedes ver la documentación de la API:

`http://localhost:8000/api/v1/docs`


## Configuración directorio de trabajo
Si la imagen a cargar no es ```png``` se requiere tener una carpeta en el directorio de trabajo ```train``` que contenga la imagen a trabajar en formato ```png```.


## Observaciones

### Set python interpreter in VScode

- Ejecutar `poetry run which python` y copiar la ruta de python
- `command+shift+p` al abrir los comandos de VScode y precione enter `Python: Select Interpreter`
- Seleccionar `+ Enter interpreter path...` y pega la ruta de python (Ejemplo. `C:/Users/Nehuen/AppData/Local/pypoetry/Cache/virtualenvs/fastapi-aws-5kk-1d1f-py3.11/Scripts/`)
