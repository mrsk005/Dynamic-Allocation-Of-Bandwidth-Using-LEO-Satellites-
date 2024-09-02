from flask import Blueprint, render_template, request, jsonify
from drl.agent import DRLAgent
from fcmr.routing import FuzzyCNNRouter

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/analyze', methods=['POST'])
def analyze():
    try:
        # Get JSON data from the request
        data = request.get_json()
        
        # Validate the input data (you might want to add more validation)
        if not data:
            return jsonify({"error": "No data provided"}), 400

        # Instantiate and use DRL agent
        agent = DRLAgent()
        allocation = agent.allocate_bandwidth(data)
        
        # Instantiate and use FCMR router
        router = FuzzyCNNRouter()
        routing_results = router.route_allocation(allocation)
        
        return jsonify({"results": routing_results})
    except Exception as e:
        return jsonify({"error": str(e)}), 500