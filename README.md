# Tienda Online – Proyecto Python (CLI)

Aplicación de ejemplo en Python que modela una tienda online simple con usuarios, productos y pedidos. La ejecución imprime en consola el inventario, pedidos simulados y el historial por usuario.

## Requisitos
- Python 3.11+ (recomendado 3.12) o
- Docker 24+

No hay dependencias externas (solo librerías estándar).

## Estructura del proyecto
```
Tienda_Online/
  main.py
  models/
    Producto.py
    Usuario.py
    Pedido.py
  Services/
    Tienda_service.py
```

## Ejecutar localmente (sin Docker)
PowerShell (Windows):
```powershell
python Tienda_Online/main.py
```

## Ejecutar con Docker
1) Construir la imagen (desde la raíz del repo):
```powershell
# Windows PowerShell
docker build -t tienda-online .
```
```bash
# Linux/macOS
docker build -t tienda-online .
```

2) Ejecutar el contenedor:
```powershell
docker run --rm tienda-online
```

El contenedor ejecuta el script y termina al finalizar la simulación.
