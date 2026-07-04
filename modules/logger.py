from datetime import datetime


def log(message):

    with open("scan.log", "a") as file:

        file.write(
            f"[{datetime.now()}] {message}\n"
        )