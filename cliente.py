import socket
from config import HOST, PORT, BUFFER_SIZE

def iniciar_cliente():
    """
    Inicia el cliente TCP, permite enviar mensajes al servidor,
    recibe la respuesta y la muestra.
    Finaliza al enviar 'DESCONEXION'.
    """
    print("=== Cliente TCP ===")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT))
            print(f"Conectado al servidor {HOST}:{PORT}")
        except ConnectionRefusedError:
            print("¡Servidor no disponible!")
            return

        while True:
            # Validar entrada no vacía
            while True:
                mensaje = input("\nEscribe tu mensaje > ").strip()
                if mensaje:
                    break
                print("¡Error! No puedes enviar mensajes vacíos.")

            s.sendall(mensaje.encode('utf-8'))

            if mensaje.upper() == "DESCONEXION":
                print("Desconectando...")
                break
            
            try:
                respuesta = s.recv(BUFFER_SIZE).decode('utf-8')
                print(f"Respuesta del servidor: {respuesta}")
            except ConnectionResetError:
                print("¡El servidor cerró la conexión!")
                break

if __name__ == "__main__":
    iniciar_cliente()
