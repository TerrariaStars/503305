import socket
import threading

# Создаем сокет сервера
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Привязываем сокет к адресу и порту
server_socket.bind(('0.0.0.0', 12345))

# Слушаем входящие соединения
server_socket.listen()

# Список подключенных клиентов
clients = []

# Функция для обработки запросов клиентов
def handle_client(client_socket):
    while True:
        # Получаем команду от клиента
        command = client_socket.recv(1024).decode()

        # Выполняем команду
        result = eval(command)

        # Отправляем результат клиенту
        client_socket.send(str(result).encode())

# Цикл для приема новых клиентов
while True:
    # Принимаем новое соединение
    client_socket, client_address = server_socket.accept()

    # Добавляем клиента в список
    clients.append(client_socket)

    # Создаем новый поток для обработки запросов клиента
    thread = threading.Thread(target=handle_client, args=(client_socket,))
    thread.start()
