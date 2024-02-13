from chat import get_response

app = Flask(__name__)


# shut off get to use API with Cors
@app.get("/") # Go to home page and render template
def index_get():
    return render_template("base.html")


@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    # TODO: check if test is valid
    response = get_response(text) # gets response from text
    message = {"answer": response} # messages user
    return jsonify(message) # message returned in json format


if __name__ == "__main__":
    app.run(debug=True)
