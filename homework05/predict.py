import pickle

from flask import Flask
from flask import request
from flask import jsonify

# model_file = 'model1.bin'
model_file = 'model2.bin'

dv_file = 'dv.bin'

with open(model_file, 'rb') as f_in, open(dv_file, 'rb') as f_in2:
    model = pickle.load(f_in)
    dv = pickle.load(f_in2)

app = Flask('credit_score')

@app.route('/predict', methods=['POST'])
def predict():
    client = request.get_json()

    X = dv.transform([client])
    y_pred = model.predict_proba(X)[0, 1]
    credit = y_pred >= 0.5

    result = {
        'credit_probability': float(y_pred),
        'credit': bool(credit)
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)