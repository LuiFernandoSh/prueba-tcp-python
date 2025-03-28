
# Proyecto TCP Cliente-Servidor en Python

Este repositorio contiene una implementación completa de un sistema cliente-servidor usando sockets TCP en Python. El objetivo es permitir que múltiples clientes se conecten a un servidor y envíen mensajes en tiempo real usando una red local (`localhost`), cumpliendo con los requisitos del ejercicio técnico propuesto.

---

## *Requisitos

- Python 3.7 o superior
- Sistema operativo compatible con sockets TCP (Linux, macOS, Windows)

---

## Estructura del Proyecto

```
.
├── cliente.py                # Cliente TCP interactivo
├── servidor.py               # Servidor TCP multicliente con hilos
├── config.py                 # Configuración compartida (host, puerto, buffer)
├── .gitignore                # Ignora archivos de caché
└── README.md                 # Documentación y guía del proyecto
```

---

## Configuración

Todos los valores de red están centralizados en el archivo `config.py`:

```python
HOST = '127.0.0.1'
PORT = 5000
BUFFER_SIZE = 1024
```

Puedes cambiar estos valores si necesitas usar otro puerto o red.

---

## Ejecución

### 1. Iniciar el Servidor

En una terminal:

```bash
python servidor.py
```

###  2. Iniciar el Cliente

En otra terminal:

```bash
python cliente.py
```

---

## Pruebas Manuales

### Prueba 1: Mensaje Normal

- Cliente escribe: `hola servidor`
- Servidor responde: `HOLA CLIENTE`

### Prueba 2: Desconexión

- Cliente escribe: `DESCONEXION`
- El cliente se desconecta correctamente
- El servidor permanece activo para nuevos clientes

---



## -Consideraciones Técnicas-

- El servidor es multicliente gracias al uso de `threading`.
- Todos los mensajes son transformados a mayúsculas como respuesta.
- El mensaje especial `"DESCONEXION"` cierra solo la conexión del cliente.
- No se permite enviar mensajes vacíos.

---
