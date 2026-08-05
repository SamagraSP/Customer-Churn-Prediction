from pathlib import Path
from django.shortcuts import render
from tensorflow.keras.models import load_model
import pandas as pd
import matplotlib.pyplot as plt
import pickle

BASE_DIR = Path(__file__).resolve().parent.parent

with open(BASE_DIR / 'column_transformer.pkl', 'rb') as c:
    ct = pickle.load(c)

with open(BASE_DIR / 'standardscaler.pkl', 'rb') as s:
    sc = pickle.load(s)

model = load_model(BASE_DIR / 'ANN_model.keras')

def churn(request):
    predict = None
    show_result = False
    risk_label = 'Analysis Ready'
    risk_class = 'low-risk'
    summary = 'The system will display the churn risk level and supporting details here after submission.'
    recommendation = 'Recommended action: Review customer engagement strategy.'
    confidence = 82
    customer_id = '—'
    contract = '—'
    monthly_charges = '—'
    internet_service = '—'

    if request.method == 'POST':
        customer_data = pd.DataFrame([{
            'customerID': request.POST.get('customerID'),
            'gender': request.POST.get('gender'),
            'SeniorCitizen': int(request.POST.get('SeniorCitizen')),
            'Partner': request.POST.get('Partner'),
            'Dependents': request.POST.get('Dependents'),
            'tenure': int(request.POST.get('tenure')),
            'PhoneService': request.POST.get('phoneService'),
            'MultipleLines': request.POST.get('multipleLines'),
            'InternetService': request.POST.get('internetService'),
            'OnlineSecurity': request.POST.get('onlineSecurity'),
            'OnlineBackup': request.POST.get('onlineBackup'),
            'DeviceProtection': request.POST.get('deviceProtection'),
            'TechSupport': request.POST.get('techSupport'),
            'StreamingTV': request.POST.get('streamingTv'),
            'StreamingMovies': request.POST.get('streamingMovies'),
            'Contract': request.POST.get('contract'),
            'PaperlessBilling': request.POST.get('paperlessBilling'),
            'PaymentMethod': request.POST.get('paymentMethod'),
            'MonthlyCharges': float(request.POST.get('monthlyCharges')),
            'TotalCharges': float(request.POST.get('totalCharges')),
        }])

        customer_data = customer_data.drop('customerID', axis=1)
        new_data = ct.transform(customer_data)
        standard_data = sc.transform(new_data)
        prediction = model.predict(standard_data)
        per_value= prediction[0][0]*100
        percentage= round(per_value, 2)
        predict = int(prediction[0][0] > 0.5)

        show_result = True
        customer_id = request.POST.get('customerID') or 'Unknown'
        contract = request.POST.get('contract') or '—'
        monthly_charges = f"${float(request.POST.get('monthlyCharges') or 0):.2f}"
        internet_service = request.POST.get('internetService') or '—'

        if predict == 1:
            risk_label = 'HIGH RISK'
            risk_class = 'high-risk'
            summary = 'The customer is likely to churn, with the profile showing strong indicators of potential customer loss. Current engagement patterns and account signals suggest an elevated churn risk that requires proactive attention.'
            recommendation = 'Recommended actions include reviewing recent customer interactions, identifying key drivers of dissatisfaction, addressing unresolved concerns, and initiating targeted retention efforts to improve the likelihood of maintaining the relationship.'
            confidence = percentage
        else:
            risk_label = 'LOW RISK'
            risk_class = 'low-risk'
            summary = 'The customer is unlikely to churn, with the profile showing strong indicators of continued engagement and account stability. Current usage patterns, customer interactions, and overall account health suggest a low risk of customer loss.'
            recommendation = 'The customer demonstrates positive engagement and ongoing value realization, indicating a strong likelihood of maintaining the relationship. Continued monitoring and proactive engagement are recommended to sustain satisfaction and support long-term retention.Maintain loyalty offers and continue proactive engagement.'
            confidence = (100-percentage)

    

    # Calculate average churner profile for comparison
    chart_data = None
    if show_result:
        monthly_charge_value = float(request.POST.get('monthlyCharges') or 0)
        tenure_value = int(request.POST.get('tenure') or 0)
        
        # Average churner profile (estimated based on typical churn patterns)
        avg_monthly_charges = 74.5
        avg_tenure = 18
        
        chart_data = {
            'monthly_charges': {
                'customer': round(monthly_charge_value, 2),
                'average_churner': avg_monthly_charges
            },
            'tenure': {
                'customer': tenure_value,
                'average_churner': avg_tenure
            }
        }

    return render(request, 'churn.html', {
        'predict': predict,
        'show_result': show_result,
        'risk_label': risk_label,
        'risk_class': risk_class,
        'summary': summary,
        'recommendation': recommendation,
        'confidence': confidence,
        'customer_id': customer_id,
        'contract': contract,
        'monthly_charges': monthly_charges,
        'internet_service': internet_service,
        'chart_data': chart_data,
    })