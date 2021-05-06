import yagmail

receiver = "ctodd678@gmail.com"
sender_email = 'ctodd678@gmail.com'
sender_password = ''

body = "Hello there from Yagmail"


yag = yagmail.SMTP(user = sender_email, password = sender_password)

yag.send(
    to=receiver,
    subject="Yagmail test email",
    contents=body
)