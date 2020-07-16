from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)
print(__name__)


#landing page
@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_file(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'Something went wrong. Try again!'



#type in any string and get the html template with the same name
@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

# def write_to_file(data):
#     #a is append
#     with open('database.txt', mode='a') as database:
#         email = data['email']
#         subject = data['subject']
#         message = data['message']
#         file = database.write(f'\n{email},{subject},{message}')

def write_to_file(data):
    #a is append
    with open('database2.csv', mode='a', newline='') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

#contact form


# @app.route('/works.html')
# def works():
# 	return render_template('works.html')

# @app.route('/contact.html')
# def contact():
# 	return render_template('contact.html')

# @app.route('/index.html')
# def index():
#     return render_template('index.html')

# @app.route('/components.html')
# def components():
#     return render_template('components.html')



# @app.route('/blog')
# def hello_world2():
#     # for i in range(100):
#     #     print('*')
#     return 'Hello fuckface'

# @app.route('/blog/2020/dogs')
# def dogs():
#     # for i in range(100):
#     #     print('*')
#     return 'fuck dogs!'

# @app.route('/favicon.ico')
# def fave():
# 	return 'favicon.ico'