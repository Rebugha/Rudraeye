import csv
from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('web.html', message='welcome to the registration page!')

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    contact = request.form['contact']
    #phone = request.form.get('phone', '').strip()
    #name = request.form.get('name', '').strip()

    #formatted_phone = ''.join(filter(str.isdigit, contact))
    #formatted_name = ''.join(filter(str.isalpha, name))

    # Save the number to a file
    with open('contacts.csv', 'a', newline='') as file :
        writer = csv.writer(file)
        writer.writerow([name, contact])


    return redirect('/')


#to make images slide 

images = ['Frame1.webp', 'Frame2.webp', 'frame3.webp']

@app.route('/')
def home():
    selected_image = random.choice(images)
    image_url = url_for('static', filename=selected_image)
    return render_template('web.html', image_url=image_url)


if __name__ == '__main__':
    app.run(debug=True)