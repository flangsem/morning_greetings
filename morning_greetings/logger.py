import datetime
def log_message(mail: str, message: str):
    with open("morning_greetings/logs/message_log.txt", "a") as log_file:
        log_file.write(f"{datetime.datetime.now()}\n- Sent to {mail}: {message}\n ----------------- \n")

def log_error(error, func):
    with open("morning_greetings/logs/error_log.txt", "a") as log_file:
        log_file.write(f"{datetime.datetime.now()} \n Function {func} rasied Error: {error}\n ------------------ \n")