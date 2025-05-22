import datetime
import time
import threading
import os
CHAT_FILE = "chat.txt"
def read_chat():
    

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("===== Chat History =====")
        with open(CHAT_FILE,"r") as f:
            print(f.read())
        print("========================")
        time.sleep(5)    
        
def write_message(name,message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log = f"[{timestamp}] {name}: {message}"
    try:
        with open(CHAT_FILE,"a") as f:
            f.write(f"{log}\n")
    except FileNotFoundError:
        print("No file found")

def chat_loop(name):
    t = threading.Thread(target=read_chat, daemon=True)
    t.start()
    while True:
        if name.lower() == "exit":
            print("Exit chating................")
            break
        message = input("Enter your message: ")
        write_message(name,message)
        time.sleep(0.5)


if __name__ == "__main__":
    name = input("Enter your name to join chat")
    if name == "":
        print("Name is required.")
    else:
        chat_loop(name)

    

