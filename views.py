# konfigurasi untuk file views
# berfungsi untuk memanggil file html
# include dengan jinja template
# thanks to flask community
# thanks to StackOverflow

from flask import Flask, render_template, url_for
app = Flask(__name__)

def home():
    return render_template('views/index.html')

# def tentangdesa():
#     return render_template('views/tentangdesa.html')

# def testing():
#     return render_template('views/testing.html')

# def endtesting():
#     return render_template('views/endtesting.html')