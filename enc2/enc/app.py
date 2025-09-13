# from flask import Flask, render_template, request, send_file, redirect, url_for, flash
# from werkzeug.utils import safe_join
# from cryptography.fernet import Fernet, InvalidToken
# import os
# from flask_mail import Mail, Message

# app = Flask(__name__)
# app.secret_key = 'your_secret_key'
# app.config['UPLOAD_FOLDER'] = 'uploads'
# app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024  # 100 MB limit for file uploads

# # Email configuration
# app.config['MAIL_SERVER'] = 'smtp.gmail.com'
# app.config['MAIL_PORT'] = 587
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USERNAME'] = 'prernapatil7699@gmail.com'  # Replace with your email
# app.config['MAIL_PASSWORD'] = 'oodd deze fjwz jlui'  # Replace with your App Password if using 2FA

# mail = Mail(app)

# # Ensure the upload folder exists
# os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# # Generate or load the encryption key
# key_file = 'secret.key'
# if os.path.exists(key_file):
#     with open(key_file, 'rb') as key_in:
#         key = key_in.read()
# else:
#     key = Fernet.generate_key()
#     with open(key_file, 'wb') as key_out:
#         key_out.write(key)
# cipher_suite = Fernet(key)

# # Allowed file extensions
# ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'mp3', 'mp4', 'wav', 'avi'}

# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# def send_email_with_attachment(recipient_email, subject, body, attachment_path):
#     msg = Message(subject, sender=app.config['MAIL_USERNAME'], recipients=[recipient_email])
#     msg.body = body

#     # Attach the encrypted file
#     with open(attachment_path, 'rb') as file:
#         msg.attach(os.path.basename(attachment_path), 'application/octet-stream', file.read())

#     try:
#         mail.send(msg)
#         print(f"Email sent to {recipient_email}")
#     except Exception as e:
#         print(f"Failed to send email: {e}")
#         flash(f"Failed to send email. Error: {e}")

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/encrypt', methods=['GET', 'POST'])
# def encrypt_file():
#     if request.method == 'POST':
#         file = request.files['file']
#         password = request.form['password']
#         recipient_email = request.form['email']
        
#         if file and password and recipient_email and allowed_file(file.filename):
#             # Save the original file temporarily
#             filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
#             file.save(filepath)

#             try:
#                 # Encrypt the file data
#                 with open(filepath, 'rb') as f:
#                     file_data = f.read()
#                 encrypted_data = cipher_suite.encrypt(file_data)

#                 # Save the encrypted data as a new file
#                 encrypted_filepath = filepath + '.encrypted'
#                 with open(encrypted_filepath, 'wb') as f:
#                     f.write(encrypted_data)

#                 # Remove the original file after encryption
#                 os.remove(filepath)

#                 # Send email with the encrypted file
#                 subject = "Your Encrypted File"
#                 body = f"Your file has been encrypted. Use the following password to decrypt it: {password}"
#                 send_email_with_attachment(recipient_email, subject, body, encrypted_filepath)

#                 flash("File encrypted and sent successfully!", "success")
#             except Exception as e:
#                 # Clean up in case of errors
#                 if os.path.exists(filepath):
#                     os.remove(filepath)
#                 if os.path.exists(encrypted_filepath):
#                     os.remove(encrypted_filepath)
#                 flash(f"An error occurred: {str(e)}", "danger")
            
#             return redirect(url_for('encrypt_file'))

#     return render_template('encrypt.html')



# @app.route('/decrypt', methods=['GET', 'POST'])
# def decrypt_file():
#     if request.method == 'POST':
#         file = request.files['file']
#         password = request.form['password']
#         if file and password and allowed_file(file.filename):
#             filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
#             file.save(filepath)

#             # Read the encrypted file data
#             with open(filepath, 'rb') as f:
#                 encrypted_data = f.read()

#             try:
#                 # Decrypt the file data
#                 decrypted_data = cipher_suite.decrypt(encrypted_data)
#                 decrypted_filepath = filepath.replace('.encrypted', '')

#                 # Write the decrypted data back to a file
#                 with open(decrypted_filepath, 'wb') as f:
#                     f.write(decrypted_data)

#                 return send_file(decrypted_filepath, as_attachment=True)

#             except InvalidToken:
#                 flash("Incorrect password or corrupted file.")
#                 return redirect(url_for('decrypt_file'))

#     return render_template('decrypt.html')




# if __name__ == '__main__':
#     app.run(debug=False)


from flask import Flask, render_template, request, send_file, redirect, url_for, flash
from werkzeug.utils import safe_join
from cryptography.fernet import Fernet, InvalidToken
import os
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = '4oPHg68L9VadkCbfziXvSmDvT9OI2oLQZgDVcyXylqQ='
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024  # 100 MB limit for file uploads

# Email configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'pujachavhan666@gmail.com'  # Replace with your email
app.config['MAIL_PASSWORD'] = 'eqmy mjyk suvn ysfq'  # Replace with your App Password if using 2FA

mail = Mail(app)

# Ensure the upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Generate or load the encryption key
key_file = 'secret.key'
if os.path.exists(key_file):
    with open(key_file, 'rb') as key_in:
        key = key_in.read()
else:
    key = Fernet.generate_key()
    with open(key_file, 'wb') as key_out:
        key_out.write(key)
cipher_suite = Fernet(key)

# Allowed file extensions
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'mp3', 'mp4', 'wav', 'avi', 'encrypted'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def send_email_with_attachment(recipient_email, subject, body, attachment_path):
    msg = Message(subject, sender=app.config['MAIL_USERNAME'], recipients=[recipient_email])
    msg.body = body

    # Attach the encrypted file
    with open(attachment_path, 'rb') as file:
        msg.attach(os.path.basename(attachment_path), 'application/octet-stream', file.read())

    try:
        mail.send(msg)
        print(f"Email sent to {recipient_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")
        flash(f"Failed to send email. Error: {e}")

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/encrypt', methods=['GET', 'POST'])
def encrypt_file():
    if request.method == 'POST':
        file = request.files['file']
        password = request.form['password']
        recipient_email = request.form['email']
        
        if file and password and recipient_email and allowed_file(file.filename):
            # Save the original file temporarily
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)

            try:
                # Encrypt the file data
                with open(filepath, 'rb') as f:
                    file_data = f.read()
                encrypted_data = cipher_suite.encrypt(file_data)

                # Save the encrypted data as a new file
                encrypted_filepath = filepath + '.encrypted'
                with open(encrypted_filepath, 'wb') as f:
                    f.write(encrypted_data)

                # Remove the original file after encryption
                os.remove(filepath)

                # Send email with the encrypted file
                subject = "Your Encrypted File"
                body = f"Your file has been encrypted. Use the following password to decrypt it: {password}"
                send_email_with_attachment(recipient_email, subject, body, encrypted_filepath)

                flash("File encrypted and sent successfully!", "success")
            except Exception as e:
                # Clean up in case of errors
                if os.path.exists(filepath):
                    os.remove(filepath)
                if os.path.exists(encrypted_filepath):
                    os.remove(encrypted_filepath)
                flash(f"An error occurred: {str(e)}", "danger")
            
            return redirect(url_for('encrypt_file'))

    return render_template('encrypt.html')

@app.route('/decrypt', methods=['GET', 'POST'])
def decrypt_file():
    if request.method == 'POST':
        file = request.files['file']
        password = request.form['password']
        
        # Check if the file and password are provided
        if not file or not password:
            flash("Please provide both the file and the password.", "danger")
            return redirect(url_for('decrypt_file'))
        
        # Check if the uploaded file has the correct extension
        if not allowed_file(file.filename):
            flash("Invalid file type. Please upload an encrypted file.", "danger")
            return redirect(url_for('decrypt_file'))
        
        # Define the file path to save the uploaded file
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        # Read the encrypted file data
        with open(filepath, 'rb') as f:
            encrypted_data = f.read()

        try:
            # Attempt to decrypt the file data
            decrypted_data = cipher_suite.decrypt(encrypted_data)
            decrypted_filepath = filepath.replace('.encrypted', '')  # Remove .encrypted extension

            # Write the decrypted data to a new file
            with open(decrypted_filepath, 'wb') as f:
                f.write(decrypted_data)

            # Check if the file was created successfully
            if os.path.exists(decrypted_filepath):
                flash("Your file has been decrypted successfully!", "success")
                return send_file(decrypted_filepath, as_attachment=True)

            else:
                flash("Decrypted file could not be created.", "danger")
                return redirect(url_for('decrypt_file'))

        except InvalidToken:
            flash("Incorrect password or corrupted file.", "danger")
            return redirect(url_for('decrypt_file'))

        except Exception as e:
            flash(f"An error occurred: {e}", "danger")
            return redirect(url_for('decrypt_file'))

    return render_template('decrypt.html')

if __name__ == '__main__':
    app.run(debug=False)
