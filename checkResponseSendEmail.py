from flask import Flask, request, jsonify
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)

@app.route('/', methods=['POST'])
def validate_request():
    data = request.get_json()
    
    if 'valid' in data and data['valid']:
        send_email()
        return jsonify({'message': 'Request is valid, email sent.'}), 200
    else:
        return jsonify({'message': 'Request is not valid.'}), 400

def send_email():
    mail_content = '''Hello,
    This is a simple mail. There is only text, no attachments are there The mail is sent using Python SMTP library.
    Thank You
    '''
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = 'youremail@gmail.com'
    message['To'] = 'recipient@gmail.com'
    message['Subject'] = 'A test mail sent by Python. It has an attachment.'   
    message.attach(MIMEText(mail_content, 'plain'))
    
    #use gmail with port
    session = smtplib.SMTP('smtp.gmail.com', 587)
    
    #start tls for security
    session.starttls() 
    
    #Authentication
    session.login('youremail@gmail.com', 'yourpassword') 
    
    #send the mail
    text = message.as_string()
    session.sendmail('youremail@gmail.com', 'recipient@gmail.com', text)
    
    #terminate the session
    session.quit()

if __name__ == '__main__':
    app.run(port=5000, debug=True)
