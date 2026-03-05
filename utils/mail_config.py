import smtplib
from email.mime.text import MIMEText
from config import Config


EMAIL = Config.MAIL_EMAIL
PASSWORD = Config.MAIL_PASSWORD


def send_email(to_email, subject, body):

    try:

        msg = MIMEText(body)

        msg["Subject"] = subject

        msg["From"] = EMAIL

        msg["To"] = to_email


        server = smtplib.SMTP(

            "smtp.gmail.com",

            587

        )

        server.starttls()

        server.login(

            EMAIL,

            PASSWORD

        )

        server.sendmail(

            EMAIL,

            to_email,

            msg.as_string()

        )

        server.quit()

        return True

    except Exception as e:

        print("Email Error:", e)

        return False
