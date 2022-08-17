import smtplib
from email.message import EmailMessage

#Email Function 

def email_function(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to
    user = 'YourEmail@gmail.com'
    msg['From'] = user
    password = 'YourPassword'
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(user,password)
    server.send_message(msg)
    server.quit()


print("[+] Sending")
email_function('Spam Email', 'This is a sapm email', 'Pytohntutorial.test@gmail.com')
print(f'[+] Email has been send') 


# Spam Emails, just remove line 22 and 23 + uncomment the below.

# ServerIsRunning = True
# try:
#     while ServerIsRunning:
#         email_function('Spam Email', 'This is a sapm email', 'Pytohntutorial.test@gmail.com')
#         print(f'[+] Email has been send') 

# except KeyboardInterrupt:
#     print('[-] Keyboard Interrupt')

    
