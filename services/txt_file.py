def create_log(message: str):
    with open("logs.txt", "a") as logs:
        logs.write(message)

#funkcja dla odczytywania treści pliku logs.txt