def create_log(filename, message: str):
    with open(filename, "a") as logs:
        logs.write(message)


def logs_read(filename):
    with open(filename, "r", encoding="utf8") as lines:
        for line in lines:
            print(line.strip())

