from flask import Flask, render_template
from cleaning_data import data_titanic
from plots import grafik1

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/data')
def data():
    data= data_titanic()
    return render_template('table_data.html', data=data)

@app.route('/plots')
def plots():
    plot1 = grafik1()
    return render_template('plots.html', data=plot1)

if __name__ == '__main__':
    app.run(debug=True, port=4444)