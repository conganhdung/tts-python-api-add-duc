import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
class send_single_email:
    def send_mail(receiver_email,sender_email,massage,password):
        # sender_email = "nguyenminhduc.jvb@gmail.com"
        # receiver_email = "nguyenminhduc2_t64@hus.edu.vn"
        # password = ("wiuurcuovguhawgt")

        message = MIMEMultipart("alternative")
        message["Subject"] = "multipart test"
        message["From"] = sender_email
        message["To"] = receiver_email

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(massage, "plain")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part1)
        # message.attach(part2)

        # Create secure connection with server and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )