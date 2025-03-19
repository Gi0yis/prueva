from flask import Flask, request, jsonify
from services.key_vault import get_secret

"""
El servidor recibe un JSON con los siguientes campos:

- budget: Presupuesto
- duration_months: Duración del proyecto en meses
- employees: Número de empleados
- management_resources: Recursos de gestión
- training_costs: Costos de capacitación
- communication_costs: Costos de comunicación
- adoption_speed_months: Velocidad de adopción en meses
- employee_competence_percent: Porcentaje de competencia de los empleados
- utilization_percent: Porcentaje de utilización
- financial_risks: Riesgos financieros
- productivity_savings: Ahorros de productividad
- risk_reduction: Reducción de riesgos
"""

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"]) 
def home():
    return get_secret("esto-es-un-secreto")

@app.route("/data", methods=["POST"])
def data():
    try:
        json_data = request.get_json()
        
        # Extraer los valores del JSON
        budget = json_data.get("budget")
        duration_months = json_data.get("duration_months")
        employees = json_data.get("employees")
        management_resources = json_data.get("management_resources")
        training_costs = json_data.get("training_costs")
        communication_costs = json_data.get("communication_costs")
        adoption_speed_months = json_data.get("adoption_speed_months")
        employee_competence_percent = json_data.get("employee_competence_percent")
        utilization_percent = json_data.get("utilization_percent")
        financial_risks = json_data.get("financial_risks")
        productivity_savings = json_data.get("productivity_savings")
        risk_reduction = json_data.get("risk_reduction")
        
        # Simulación de cálculos
        employee_demotion_percent = (employees / (employees + management_resources)) * 20
        success_probability_percent = (employee_competence_percent + utilization_percent) / 2
        roi_percent = (productivity_savings - (training_costs + communication_costs)) / budget * 100
        
        processed_data = {
            "employee_demotion_percent": round(employee_demotion_percent, 2),
            "success_probability_percent": round(success_probability_percent, 2),
            "roi_percent": round(roi_percent, 2)
        }
        
        return jsonify({"received_data": json_data, "processed_data": processed_data}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
