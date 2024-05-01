# from http import client
# import pygame
# import socket

# # Server configuration
# SERVER_HOST = '192.168.1.12'
# SERVER_PORT = 5050

# # Pygame colors
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# GRAY = (200, 200, 200)

# # Initialize Pygame
# pygame.init()

# # Set up the display
# WIDTH, HEIGHT = 800, 600
# win = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Chat Client")

# # Fonts
# font = pygame.font.Font(None, 32)
# input_font = pygame.font.Font(None, 24)

# # Function to connect to the server
# def connect_to_server():
#     client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     client.connect((SERVER_HOST, SERVER_PORT))
#     return client

# # Function to send a message to the server
# # Function to send a message to the server
# def send_message(client, message):
#     try:
#         client.send(message.encode())
#     except Exception as e:
#         print(f"Error occurred while sending message: {e}")


# # Function to receive messages from the server
# def receive_message(client):
#     return client.recv(1024).decode()

# # Function to handle user input events
# def handle_input(text):
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             quit()
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_BACKSPACE:
#                 text = text[:-1]
#             elif event.key == pygame.K_RETURN:  # Send message only when Enter key is pressed
#                 send_message(client, text)
#                 text = ""  # Clear the text after sending the message
#             else:
#                 text += event.unicode
#     return text

# login_font = pygame.font.Font(None, 24)
# register_font = pygame.font.Font(None, 24)
# login_text = login_font.render("Login", True, WHITE)
# register_text = register_font.render("Register", True, WHITE)

# # Function to draw login and registration forms
# def draw_forms(username_text, password_text, login_button_rect, register_button_rect, login_text, register_text):
#     win.fill(WHITE)

#     # Draw username input box
#     pygame.draw.rect(win, GRAY, username_text[2])
#     win.blit(username_text[0], username_text[1])

#     # Draw password input box
#     pygame.draw.rect(win, GRAY, password_text[2])
#     win.blit(password_text[0], password_text[1])

#     # Draw login button
#     pygame.draw.rect(win, GRAY, login_button_rect)

#     # Draw register button
#     pygame.draw.rect(win, GRAY, register_button_rect)

#     # Draw text on buttons
#     win.blit(login_text, (login_button_rect.x + 10, login_button_rect.y + 10))
#     win.blit(register_text, (register_button_rect.x + 10, register_button_rect.y + 10))

#     pygame.display.update()

# # Main function to handle user interface
# def main():
#     client = connect_to_server()
#     print(receive_message(client))

#     clock = pygame.time.Clock()

#     # Initialize fonts
#     username_font = pygame.font.Font(None, 24)
#     password_font = pygame.font.Font(None, 24)

#     # Initialize input boxes
#     username = ""
#     password = ""
#     username_rect = pygame.Rect(300, 200, 200, 30)
#     password_rect = pygame.Rect(300, 250, 200, 30)
#     is_username_active = False
#     is_password_active = False

#     # Initialize buttons
#     login_button_rect = pygame.Rect(300, 300, 100, 50)
#     register_button_rect = pygame.Rect(450, 300, 100, 50)

#     while True:
#         draw_forms((username_font.render(username, True, BLACK), (305, 205), username_rect),
#                    (password_font.render("*" * len(password), True, BLACK), (305, 255), password_rect),
#                    login_button_rect, register_button_rect,login_text, register_text)

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 quit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if username_rect.collidepoint(event.pos):
#                     is_username_active = not is_username_active
#                 else:
#                     is_username_active = False

#                 if password_rect.collidepoint(event.pos):
#                     is_password_active = not is_password_active
#                 else:
#                     is_password_active = False

#                 if login_button_rect.collidepoint(event.pos):
#                     send_message(client, f"login {username} {password}")
#                     response = receive_message(client)
#                     print(response)

#                 if register_button_rect.collidepoint(event.pos):
#                     send_message(client, f"register {username} {password}")
#                     response = receive_message(client)
#                     print(response)

#             if event.type == pygame.KEYDOWN:
#                 if is_username_active:
#                     if event.key == pygame.K_RETURN:
#                         is_username_active = False
#                     elif event.key == pygame.K_BACKSPACE:
#                         username = username[:-1]
#                     else:
#                         username += event.unicode

#                 if is_password_active:
#                     if event.key == pygame.K_RETURN:
#                         is_password_active = False
#                     elif event.key == pygame.K_BACKSPACE:
#                         password = password[:-1]
#                     else:
#                         password += event.unicode

#         pygame.display.update()
#         clock.tick(30)

#     client.close()

# if __name__ == "__main__":
#     main()




from http import client
from threading import Thread
import threading
import pygame
import socket

# Server configuration
SERVER_HOST = '192.168.1.12'
SERVER_PORT = 5050

# Pygame colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chat Client")

# Fonts
font = pygame.font.Font(None, 32)
input_font = pygame.font.Font(None, 24)

login_font = pygame.font.Font(None, 24)
register_font = pygame.font.Font(None, 24)
login_text = login_font.render("Login", True, WHITE)
register_text = register_font.render("Register", True, WHITE)

# Function to connect to the server
def connect_to_server():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER_HOST, SERVER_PORT))
    return client

# Function to send a message to the server
def send_message(client, message):
    try:
        client.send(message.encode())
    except Exception as e:
        print(f"Error occurred while sending message: {e}")

# Function to receive messages from the server
def receive_message(client):
    return client.recv(1024).decode()

# Function to handle user input events
def handle_input(text):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                text = text[:-1]
            elif event.key == pygame.K_RETURN:  # Send message only when Enter key is pressed
                send_message(client, text)
                text = ""  # Clear the text after sending the message
            else:
                text += event.unicode
    return text

# Function to draw login and registration forms
def draw_forms(username_text, password_text, login_button_rect, register_button_rect, login_text, register_text):
    win.fill(WHITE)

    # Draw username input box
    pygame.draw.rect(win, GRAY, username_text[2])
    win.blit(username_text[0], username_text[1])

    # Draw password input box
    pygame.draw.rect(win, GRAY, password_text[2])
    win.blit(password_text[0], password_text[1])

    # Draw login button
    pygame.draw.rect(win, GRAY, login_button_rect)

    # Draw register button
    pygame.draw.rect(win, GRAY, register_button_rect)

    # Draw text on buttons
    win.blit(login_text, (login_button_rect.x + 10, login_button_rect.y + 10))
    win.blit(register_text, (register_button_rect.x + 10, register_button_rect.y + 10))

    pygame.display.update()
# Main function to handle user interface
def main():
    global message_list
    message_list = []
    client = connect_to_server()
    print(receive_message(client))

    clock = pygame.time.Clock()

    # Initialize fonts
    username_font = pygame.font.Font(None, 24)
    password_font = pygame.font.Font(None, 24)

    # Initialize input boxes
    username = ""
    password = ""
    username_rect = pygame.Rect(300, 200, 200, 30)
    password_rect = pygame.Rect(300, 250, 200, 30)
    is_username_active = False
    is_password_active = False

    # Initialize buttons
    login_button_rect = pygame.Rect(300, 300, 100, 50)
    register_button_rect = pygame.Rect(450, 300, 100, 50)

    
    while True:
        draw_forms((username_font.render(username, True, BLACK), (305, 205), username_rect),
                (password_font.render("*" * len(password), True, BLACK), (305, 255), password_rect),
                login_button_rect, register_button_rect, login_text, register_text)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if username_rect.collidepoint(event.pos):
                    is_username_active = not is_username_active
                else:
                    is_username_active = False

                if password_rect.collidepoint(event.pos):
                    is_password_active = not is_password_active
                else:
                    is_password_active = False

                if login_button_rect.collidepoint(event.pos):
                    send_message(client, f"login {username} {password}")
                    response = receive_message(client)
                    print(response)
                    if response == "Login successful!":  # Open chat window if login successful
                        start_chat_client(client,username)  # Pass username to start_chat_client

                if register_button_rect.collidepoint(event.pos):
                    send_message(client, f"register {username} {password}")
                    response = receive_message(client)
                    print(response)
                    print(username)
                    if response == "Registration successful!":  # Automatically login after successful registration
                        start_chat_client(client,username)  # Pass username to start_chat_client

    
    # while True:
    #     draw_forms((username_font.render(username, True, BLACK), (305, 205), username_rect),
    #                (password_font.render("*" * len(password), True, BLACK), (305, 255), password_rect),
    #                login_button_rect, register_button_rect, login_text, register_text)

    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             pygame.quit()
    #             quit()
    #         if event.type == pygame.MOUSEBUTTONDOWN:
    #             if username_rect.collidepoint(event.pos):
    #                 is_username_active = not is_username_active
    #             else:
    #                 is_username_active = False

    #             if password_rect.collidepoint(event.pos):
    #                 is_password_active = not is_password_active
    #             else:
    #                 is_password_active = False

    #             if login_button_rect.collidepoint(event.pos):
    #                 send_message(client, f"login {username} {password}")
    #                 response = receive_message(client)
    #                 print(response)
    #                 if response == "Login successful!":  # Open chat window if login successful
    #                     # chat_window(client, message_list)  # Pass message_list argument here
    #                     start_chat_client()

    #             if register_button_rect.collidepoint(event.pos):
    #                 send_message(client, f"register {username} {password}")
    #                 response = receive_message(client)
    #                 print(response)
    #                 if response == "Registration successful!":  # Automatically login after successful registration
    #                     # send_message(client, f"login {username} {password}")
    #                     # login_response = receive_message(client)
    #                     # print(login_response)
    #                     # if login_response == "Login successful!":
    #                         start_chat_client() # Pass message_list argument here

            if event.type == pygame.KEYDOWN:
                if is_username_active:
                    if event.key == pygame.K_RETURN:
                        is_username_active = False
                    elif event.key == pygame.K_BACKSPACE:
                        username = username[:-1]
                    else:
                        username += event.unicode

                if is_password_active:
                    if event.key == pygame.K_RETURN:
                        is_password_active = False
                    elif event.key == pygame.K_BACKSPACE:
                        password = password[:-1]
                    else:
                        password += event.unicode

        pygame.display.update()
        clock.tick(30)

    client.close()


# def chat_window(client, message_list):
#     chatting_win = pygame.display.set_mode((400, 400))
#     pygame.display.set_caption("Chatting")

#     font = pygame.font.Font(None, 24)
#     input_rect = pygame.Rect(50, 350, 300, 30)
#     input_text = ""

#     while True:
#         chatting_win.fill(WHITE)

#         # Display received messages
#         y = 50
#         for message in message_list:
#             message_render = font.render(message, True, BLACK)
#             chatting_win.blit(message_render, (50, y))
#             y += 30

#         # Draw input box
#         pygame.draw.rect(chatting_win, GRAY, input_rect)
#         input_render = font.render(input_text, True, BLACK)
#         chatting_win.blit(input_render, (input_rect.x + 5, input_rect.y + 5))

#         pygame.display.update()

#         # Handle input events
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 quit()
#             elif event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_BACKSPACE:
#                     input_text = input_text[:-1]
#                 elif event.key == pygame.K_RETURN:
#                     send_message(client, input_text)
#                     input_text = ""
#                 else:
#                     input_text += event.unicode


def start_chat_client(client,username):
    # Initialize Pygame
    pygame.init()

    # Screen dimensions
    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 400

    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (200, 200, 200)

    # Function to send messages to the server
    def send_message(client, message):
        try:
            client.send(message.encode())
        except Exception as e:
            print(f"Error occurred while sending message: {e}")

    # Function to receive messages from the server
    def receive_message():
        while True:
            try:
                message = client.recv(1024).decode('utf-8')
                message_list.append(message)
            except:
                break

    # Function to connect to the server
    def connect_to_server():
        # global client_socket
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('192.168.1.12', 5050))

    # Initialize Pygame screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Chat Client")

    # Fonts
    font = pygame.font.Font(None, 24)

    # Create message list
    message_list = []

    # Entry field
    entry_rect = pygame.Rect(50, 350, 400, 30)
    entry_text = ""

    # Connect to the server
    connect_to_server()

    # Create a thread to receive messages from the server
    receive_thread = threading.Thread(target=receive_message)
    receive_thread.start()

    # Send "start_chat" command with the username
    send_message(client,f"start_chat {username}")

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    entry_text = entry_text[:-1]
                elif event.key == pygame.K_RETURN:
                    if entry_text.lower() == "end_chat":
                        send_message(client,"end_chat")
                        running = False
                    else:
                        send_message(client,entry_text)
                    entry_text = ""
                else:
                    entry_text += event.unicode

        # Clear the screen
        screen.fill(WHITE)

        # Render message list
        y = 50
        for message in message_list:
            message_render = font.render(message, True, BLACK)
            screen.blit(message_render, (50, y))
            y += 30

        # Render entry field
        pygame.draw.rect(screen, GRAY, entry_rect)
        entry_render = font.render(entry_text, True, BLACK)
        screen.blit(entry_render, (entry_rect.x + 5, entry_rect.y + 5))

        # Update the display
        pygame.display.flip()

    # Close the socket and quit Pygame
    client.close()
    pygame.quit()





# Run the main function when the script is executed
if __name__ == "__main__":
    main()
