# Send mail to your freinds using a fake mail ID (like cia@cia.com or anything).
# But don't use it for any illegal purposes. I am not responsible for any such activity.

# IMPORTANT: Sometimes I have noticed that under details section the real mail ID of the
# sender is visible. So be careful while sending the mail

# You need to have yagmail installed on your pc. If not then
# you can use 'pip3 install yagmail' to install it

import yagmail

your_mail_id = input("Please enter your email address: ")
password = input("Please enter password of your mail address: ")
fake_mail_id = input("Please enter a fake mail id: ")
receivers_mail_address = input("Please enter receivers mail address: ")
subject = input("Please enter subject of the mail: ")

text = input("Enter text to be sent: ")

mail = yagmail.SMTP({your_mail_id: fake_mail_id}, password)

mail.send(receivers_mail_address, subject, text)
