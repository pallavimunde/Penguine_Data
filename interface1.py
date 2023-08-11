from flask import Flask, jsonify,render_template, request
from utils import Penguine
import warnings
warnings.filterwarnings('ignore')
import config

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/Penguine", methods=["GET", "POST"])
def penguin_prediction():
    try:
        if request.method == "POST":
            data = request.form
        elif request.method == 'GET':
            data = request.args
        
        bill_length_mm = float(data.get('bill_length_mm', 0))
        bill_depth_mm = float(data.get('bill_depth_mm', 0))
        flipper_length_mm = float(data.get('flipper_length_mm', 0))
        body_mass_g = float(data.get('body_mass_g', 0))
        species = data.get('Adelie','Chinstrap','Gentoo')
        island = data.get('Biscoe','Dream','Torgersen')

        obj = Penguine(bill_length_mm, bill_depth_mm, flipper_length_mm, body_mass_g, species, island)
        r = obj.Pred_Penguine()
        if r==1.0:
            r="Male"
        else :
            r="female"
        return render_template("index.html", result=r)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config.PORT_NUMBER, debug=False)
