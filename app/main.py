from flask import Flask, jsonify
from load_data import load_data
from utils import top_consumers, sector_comparison, company_info

app = Flask(__name__)

# Load data once when the API starts
df = load_data()

@app.route("/top_consumers/<resource>/<top_n_order>", methods=["GET"])
def get_order_n_consumers(resource, top_n_order):
    """Returns the top 5 consumers by deafualt of the specified resource (energy, water, CO2)."""
    if df is None or resource not in df.columns:
        return jsonify({"error": "Invalid resource or data unavailable"}), 400
    else:
        top_n, order = top_n_order.split("_")
    return jsonify(top_consumers(df, resource, top_n, order))


@app.route("/top_consumers/<resource>", methods=["GET"])
def get_top_consumers(resource):
    """Returns the top 5 consumers by deafualt of the specified resource (energy, water, CO2)."""
    if df is None or resource not in df.columns:
        return jsonify({"error": "Invalid resource or data unavailable"}), 400
    return jsonify(top_consumers(df, resource))


@app.route("/sector_comparison/<resource>", methods=["GET"])
def get_sector_comparison(resource):
    """Compares average resource consumption across sectors."""
    if df is None or resource not in df.columns:
        return jsonify({"error": "Invalid resource or data unavailable"}), 400
    return jsonify(sector_comparison(df, resource))


@app.route("/company_info/<id>", methods=["GET"])
def get_company_info(id):
    """Compares average resource consumption across sectors."""
    if df is None or int(id) == 0:
        return jsonify({"error": "Invalid resource or data unavailable"}), 400
    return jsonify(company_info(df, id))

@app.route("/", methods=["GET"])
def home():
    return jsonify({
                    "/top_consumers/resource": "Get the top 5 consumers of a resource (energia, agua, emissoes) by default.",
                    "/top_consumers/resource/top_n_order": "Get the top 5 consumers of a resource (energia, agua, emissoes) by default. Order can be 'asc' or 'desc'. Top_n is the number of consumers to return.",
                    "/sector_comparison/resource": "Compare average resource consumption across sectors (energia, agua, emissoes).",
                    "resources_units": "energia - kwh, agua - m3, emissoes - CO2",
                    "message": "Welcome to the GreenFlow report API!. Get the results of each resource by accessing the respective endpoint."
                    })
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)