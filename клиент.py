import socket

# Получаем список доступных IP-адресов в локальной сети
ip_addresses = [ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if ip != '127.0.0.1']

# Выводим список IP-адресов и запрашиваем выбор пользователя
print("Доступные IP-адреса:")
for i, ip in enumerate(ip_addresses):
    print(f"{i+1}. {ip}")
ip_index = input("Выберите IP-адрес: ")

# Создаем сокет клиента
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if ip_index.count(".")==3:
    client_socket.connect((ip_index, 25565))
# Подключаемся к серверу
else:
    client_socket.connect((ip_addresses[int(ip_index)-1], 12345))

# Цикл для отправки команд серверу
while True:
    # Получаем команду от пользователя
    command = input("Введите команду: ")

    # Отправляем команду серверу
    client_socket.send(command.encode())

    # Получаем результат от сервера
    result = client_socket.recv(1024).decode()

    # Выводим результат
    print(f"Результат: {result}")
