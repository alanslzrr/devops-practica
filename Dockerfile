# syntax=docker/dockerfile:1

FROM python:3.12-slim

## Variables de entorno para una ejecución de Python limpia y predecible
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PYTHONUTF8=1

WORKDIR /app

## Crear usuario no root antes de copiar los archivos (mejor práctica de seguridad)
RUN useradd -m -u 10001 appuser

## Copiar el código de la aplicación asignando propiedad al usuario no root
COPY --chown=appuser:appuser Tienda_Online/ Tienda_Online/

## Actualizar pip (la app no requiere dependencias externas/requirements.txt)
RUN python -m pip install --upgrade pip

## Cambiar al usuario no root para ejecutar la aplicación
USER appuser

## Comando por defecto: ejecutar el script principal
CMD ["python", "Tienda_Online/main.py"]
