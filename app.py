# konfigurasi global
# coding ini di buat secara manual oleh DevDns team

import views
from flask import Flask, url_for

app = Flask(__name__)

app.add_url_rule('/', view_func=views.home)
# app.add_url_rule('/about', view_func=views.tentangdesa)
# app.add_url_rule('/testing', view_func=views.testing)
# app.add_url_rule('/endtesting', view_func=views.endtesting)
