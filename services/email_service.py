import smtplib
from utils.mail_config import EMAIL, PASSWORD


def send_email(to_email, subject, message):

    server = smtplib.SMTP("smtp.gmail.com", 587)

    server.starttls()

    server.login(EMAIL, PASSWORD)

    msg = f"Subject: {subject}\n\n{message}"

    server.sendmail(EMAIL, to_email, msg)

    server.quit()

    return True
