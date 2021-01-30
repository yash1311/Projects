import smtplib
from email_body2 import email_html
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from secret import email_password



def send_mail(df,topic):
    print("Connecting to email server.....")
    server =smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    print("Server Connection established.....")


    print("Login to email....")

    server.login('yashpatel0013@gmail.com',email_password)

    print("Email login successful.")

    me = "from_user@gmail.com"
    you = "to_user@gmail.com"

    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = f"All about {topic} for the day."
    msg['From'] = me
    msg['To'] = you

    # Create the body of the message (a plain-text and an HTML version).
    text = "Here is the top news you are interested in..."
    html = email_html(df,topic)
    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)

    # sendmail function takes 3 arguments: sender's address, recipient's address
    # and message to send - here it is sent as one string.
    server.sendmail(me, you, msg.as_string())

    print("email sent.")

    server.quit()

    print("Server Closed.")
