#!/usr/bin/python 
import smtplib
import threading
from random import choice
from string import ascii_uppercase
from random import randrange
from subprocess import call


def status_sent():
    print('executing sent email creation')
    sender = ''.join(choice(ascii_uppercase) for i in range(12)) + '@source.com' 
    recipient = ''.join(choice(ascii_uppercase) for i in range(12)) + '@sent.com'
    message = 'This is a test Message'
    return sender, recipient, message


def status_deferred():
    print('executing deferred email creation')
    sender = ''.join(choice(ascii_uppercase) for i in range(12)) + '@source.com' 
    recipient = ''.join(choice(ascii_uppercase) for i in range(12)) + '@deferred.com'
    message = 'This is a test Message'
    return sender, recipient, message

def status_bounced():
    print('executing bounced email creation')
    sender = ''.join(choice(ascii_uppercase) for i in range(12)) + '@source.com' 
    recipient = ''.join(choice(ascii_uppercase) for i in range(12)) + '@bounced.com'
    message = 'This is a test Message'
    mycmd = 'echo "Test message" | mail -r ' + sender + ' -s "Test Subject" ' + recipient
    print(mycmd)
    call(mycmd, shell=True)
    

#function to send message, requires vars for sender, recipient, and message are passed int
def send_message(sender, recipient, message):
    try:
        smtpObj = smtplib.SMTP('localhost')
        smtpObj.sendmail(sender, recipient, message)
        print('Sucessfully sent message to ', recipient)
    except smtplib.SMTPException:
        print('Error sending message')


#main function
def main():
    #call main function every X seconds
    threading.Timer(5.0, main).start()
    sender=''
    chance = int(randrange(1, 11))
    print(chance)
    if chance <= 8:
        sender, recipient, message = status_sent()
    elif chance == 9:
        sender, recipient, message = status_deferred()
    elif chance == 10:
        status_bounced()
    else:
        print('chance number not matched, I did not send a message')
    #send email
    if sender:
        send_message(sender, recipient, message)
    else:
        print('Message was sent via local shell for bounced status recipient')


#call main function
if __name__ == '__main__':
    main()
