from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/v1.0/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        data = request.get_json(silent=True) or {}
        num1 = float(data.get('num1', 0))
        num2 = float(data.get('num2', 0))
    else:  
        num1 = float(request.args.get('num1', 0))
        num2 = float(request.args.get('num2', 0))
    
    sum = num1 + num2
    prediction = 1 if sum > 5.8 else 0
    
    response = {
        "prediction": prediction,
        "features": {
            "num1": num1,
            "num2": num2,
            "sum": sum
        }
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)