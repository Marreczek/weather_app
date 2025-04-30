def create_log(message: str):
    with open("logs.txt", "a") as logs:
        logs.write(message)

#funkcja dla odczytywania treści pliku logs.txt
def logs_read():
    with open('logs.txt',"r", encoding="utf8") as lines:
        for line in lines:
            print(line.strip())