import csv
from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

@app.route('/')
def home():
    success = request.args.get('success')
    return render_template('index.html', success=success)

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    contact = request.form['contact']
    email = request.form['email']
    date = request.form['date']
    time = request.form['time']
    


    with open('contacts.csv', 'a', newline='') as file :
        writer = csv.writer(file)
        writer.writerow([name, contact,email, date, time])


    return redirect(url_for('home', success='true'))


#to make images slide 

images = ['Frame1.webp', 'Frame2.webp', 'frame3.webp']

@app.route('/')
def image():
    selected_image = random.choice(images)
    image_url = url_for('images', filename=selected_image)
    return render_template('index.html', image_url=image_url)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)