import socket
import threading
from config import HOST, PORT, BUFFER_SIZE

def manejar_cliente(conn, addr):
    """
    Maneja la comunicación con un cliente conectado.
    - Si el mensaje es 'DESCONEXION', se cierra la conexión.
    - Si el mensaje es 'HOLA SERVIDOR', responde 'HOLA CLIENTE'.
    - Si el mensaje está vacío, responde con error.
    - Para otros mensajes, responde el mismo en mayúsculas.
    """
    print(f"[+] Conexión establecida con {addr}")
    with conn:
        while True:
            try:
                data = conn.recv(BUFFER_SIZE).decode('utf-8')
                if not data:
                    print(f"[!] {addr} envió mensaje vacío. Cerrando conexión...")
                    break

                mensaje = data.strip().upper()
                print(f"Cliente {addr} envió: {data}")

                if not mensaje:
                    respuesta = "ERROR: Mensaje vacío"
                elif mensaje == "DESCONEXION":
                    print(f"Cliente {addr} solicitó desconexión")
                    break
                elif mensaje == "HOLA SERVIDOR":
                    respuesta = "HOLA CLIENTE"
                else:
                    respuesta = data.upper()

                conn.sendall(respuesta.encode('utf-8'))
                print(f"Enviado a {addr}: {respuesta}")

            except ConnectionResetError:
                print(f"¡Conexión con {addr} interrumpida!")
                break

    print(f"[-] Conexión cerrada con {addr}\n")

def iniciar_servidor():
    """
    Inicia el servidor TCP en modo multicliente.
    Cada conexión se maneja en un hilo separado.
    """
    print("[*] Iniciando servidor TCP...")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        print(f"[+] Servidor escuchando en {HOST}:{PORT}\n")

        while True:
            conn, addr = server_socket.accept()
            hilo = threading.Thread(
                target=manejar_cliente, 
                args=(conn, addr),
                daemon=True
            )
            hilo.start()
            print(f"[~] Hilos activos: {threading.active_count() - 1}")

if __name__ == "__main__":
    iniciar_servidor()
