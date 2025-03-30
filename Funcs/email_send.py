import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv, dotenv_values

config = dotenv_values(".env")

# Use your Gmail address and App Password
EMAIL_ADDRESS =  config['EMAIL']
EMAIL_PASSWORD = config['PASSWORD']

def sendEmail(email, status, id, lab, macNum, prob):

    html_content = f"""
<html>
<body>
    <p>Dear <strong>Student</strong>,</p>
    <p>We would like to inform you that the status of your complaint (Complaint ID: <strong>{id}</strong>) has been updated to: <strong>{status}</strong>.</p>

    <h3>Complaint Details:</h3>
    <ul>
        <li><strong>Complaint ID:</strong> {id}</li>
        <li><strong>Issue Reported:</strong> {prob}</li>
        <li><strong>Current Status:</strong> {status}</li>
        <li><strong>Machine number:</strong> {macNum}</li>
        <li><strong>Lab number:</strong> {lab}</li>

    </ul>

    <p>We appreciate your patience and assure you that we are working diligently to resolve your issue. If you require any further assistance or have any questions, please feel free to contact us.</p>

    <p>Thank you for reaching out.</p>
    <p><strong>Best regards,</strong><br>
    Tech Team<br>
    College IT Support<br>
    support@college.edu</p>
</body>
</html>
"""
    msg = EmailMessage()
    msg["Subject"] = "Test Email from Python"
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = email
    msg.set_content(" ")
    msg.add_alternative(html_content, subtype="html")

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
        print("Email sent successfully!")
    except Exception as e:
        print("Error:", e)
