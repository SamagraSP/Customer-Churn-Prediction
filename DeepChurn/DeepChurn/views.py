from pathlib import Path
from functools import lru_cache
from django.shortcuts import render
from tensorflow.keras.models import load_model
import pandas as pd
import pickle


BASE_DIR = Path(__file__).resolve().parent.parent


# ============================================================
# Lazy loading
# ============================================================

@lru_cache(maxsize=1)
def get_column_transformer():
    with open(BASE_DIR / 'column_transformer.pkl', 'rb') as c:
        return pickle.load(c)


@lru_cache(maxsize=1)
def get_standard_scaler():
    with open(BASE_DIR / 'standardscaler.pkl', 'rb') as s:
        return pickle.load(s)


@lru_cache(maxsize=1)
def get_model():
    return load_model(BASE_DIR / 'ANN_model.keras')


LOW_RISK_THRESHOLD = 0.30
HIGH_RISK_THRESHOLD = 0.60

FIELD_NAMES = [
    'customerID', 'gender', 'SeniorCitizen', 'Partner', 'Dependents',
    'tenure', 'phoneService', 'multipleLines', 'internetService',
    'onlineSecurity', 'onlineBackup', 'deviceProtection', 'techSupport',
    'streamingTv', 'streamingMovies', 'contract', 'paperlessBilling',
    'paymentMethod', 'monthlyCharges', 'totalCharges',
]


def validate_submission(data):
    errors = {}

    for field in FIELD_NAMES:
        if not data.get(field, '').strip():
            errors[field] = 'This field is required.'

    customer_id = data.get('customerID', '').strip()

    if customer_id and len(customer_id) > 64:
        errors['customerID'] = 'Use 64 characters or fewer.'

    try:
        tenure = int(data.get('tenure', ''))

        if tenure < 0 or tenure > 120:
            errors['tenure'] = 'Enter a tenure between 0 and 120 months.'

    except (TypeError, ValueError):
        errors['tenure'] = 'Enter a whole number of months.'

    numeric_values = {}

    for field in ('monthlyCharges', 'totalCharges'):
        try:
            value = float(data.get(field, ''))

            if value < 0 or value > 1000000:
                errors[field] = 'Enter a value between 0 and 1,000,000.'

            numeric_values[field] = value

        except (TypeError, ValueError):
            errors[field] = 'Enter a valid non-negative amount.'

    if (
        not errors.get('tenure')
        and not errors.get('monthlyCharges')
        and not errors.get('totalCharges')
    ):
        expected_total = tenure * numeric_values['monthlyCharges']

        if (
            numeric_values['totalCharges']
            > expected_total
            + numeric_values['monthlyCharges'] * 3
            + 100
        ):
            errors['totalCharges'] = (
                'Total charges are unusually high for this tenure '
                'and monthly charge.'
            )

    return errors


def build_risk_factors(data):
    factors = []

    indicators = [
        (
            'contract',
            'Month-to-month contract',
            data.get('contract') == 'Month-to-month'
        ),
        (
            'monthlyCharges',
            'Higher monthly charges',
            float(data.get('monthlyCharges', 0)) >= 80
        ),
        (
            'tenure',
            'Short tenure',
            int(data.get('tenure', 0)) <= 12
        ),
        (
            'internetService',
            'Fiber optic internet service',
            data.get('internetService') == 'Fiber optic'
        ),
        (
            'paymentMethod',
            'Electronic check payment',
            data.get('paymentMethod') == 'Electronic check'
        ),
        (
            'onlineSecurity',
            'No online security add-on',
            data.get('onlineSecurity') == 'No'
        ),
        (
            'techSupport',
            'No tech support add-on',
            data.get('techSupport') == 'No'
        ),
        (
            'deviceProtection',
            'No device protection add-on',
            data.get('deviceProtection') == 'No'
        ),
        (
            'onlineBackup',
            'No online backup add-on',
            data.get('onlineBackup') == 'No'
        ),
    ]

    for field, label, applies in indicators:
        if applies:
            factors.append({
                'label': label,
                'field': field
            })

    return factors


def build_recommendations(data, risk_class):
    recommendations = []

    if risk_class == 'high-risk':
        recommendations.append(
            'Prioritize proactive customer contact and a targeted retention offer.'
        )

    elif risk_class == 'medium-risk':
        recommendations.append(
            'Consider a timely engagement check-in and a relevant retention incentive.'
        )

    else:
        recommendations.append(
            'Continue good service and consider loyalty-focused engagement.'
        )

    if data.get('contract') == 'Month-to-month':
        recommendations.append(
            'Offer a clear longer-term contract option with an appropriate incentive.'
        )

    if (
        data.get('techSupport') == 'No'
        or data.get('onlineSecurity') == 'No'
    ):
        recommendations.append(
            'Review whether technical support or online security add-ons '
            'would improve value.'
        )

    if float(data.get('monthlyCharges', 0)) >= 80:
        recommendations.append(
            'Review pricing and plan fit before making an offer.'
        )

    return recommendations


def churn(request):
    predict = None
    show_result = False

    risk_label = 'Analysis Ready'
    risk_class = 'low-risk'

    summary = (
        'The system will display the churn risk level and supporting '
        'details here after submission.'
    )

    recommendation = (
        'Recommended action: Review customer engagement strategy.'
    )

    probability = None
    customer_id = '—'
    contract = '—'
    monthly_charges = '—'
    internet_service = '—'

    form_values = (
        request.POST.dict()
        if request.method == 'POST'
        else {}
    )

    errors = (
        validate_submission(form_values)
        if request.method == 'POST'
        else {}
    )

    prediction_data = None

    if request.method == 'POST' and not errors:

        customer_data = pd.DataFrame([{
            'customerID': form_values['customerID'],
            'gender': form_values['gender'],
            'SeniorCitizen': int(form_values['SeniorCitizen']),
            'Partner': form_values['Partner'],
            'Dependents': form_values['Dependents'],
            'tenure': int(form_values['tenure']),
            'PhoneService': form_values['phoneService'],
            'MultipleLines': form_values['multipleLines'],
            'InternetService': form_values['internetService'],
            'OnlineSecurity': form_values['onlineSecurity'],
            'OnlineBackup': form_values['onlineBackup'],
            'DeviceProtection': form_values['deviceProtection'],
            'TechSupport': form_values['techSupport'],
            'StreamingTV': form_values['streamingTv'],
            'StreamingMovies': form_values['streamingMovies'],
            'Contract': form_values['contract'],
            'PaperlessBilling': form_values['paperlessBilling'],
            'PaymentMethod': form_values['paymentMethod'],
            'MonthlyCharges': float(form_values['monthlyCharges']),
            'TotalCharges': float(form_values['totalCharges']),
        }])

        customer_data = customer_data.drop(
            'customerID',
            axis=1
        )

        # --------------------------------------------------------
        # Load ML artifacts only when a prediction is requested
        # --------------------------------------------------------

        ct = get_column_transformer()
        sc = get_standard_scaler()
        model = get_model()

        # --------------------------------------------------------
        # Preprocess and predict
        # --------------------------------------------------------

        new_data = ct.transform(customer_data)

        standard_data = sc.transform(new_data)

        prediction = model.predict(
            standard_data,
            verbose=0
        )

        probability = round(
            float(prediction[0][0]),
            4
        )

        percentage = round(
            probability * 100,
            1
        )

        predict = int(
            probability >= HIGH_RISK_THRESHOLD
        )

        show_result = True

        customer_id = (
            request.POST.get('customerID')
            or 'Unknown'
        )

        contract = (
            request.POST.get('contract')
            or '—'
        )

        monthly_charges = (
            f"${float(form_values['monthlyCharges']):.2f}"
        )

        internet_service = form_values['internetService']

        # --------------------------------------------------------
        # Determine risk level
        # --------------------------------------------------------

        if probability >= HIGH_RISK_THRESHOLD:

            risk_label = 'HIGH RISK'
            risk_class = 'high-risk'

            summary = (
                'This customer shows a strong likelihood of churn. '
                'Immediate retention action is recommended.'
            )

        elif probability >= LOW_RISK_THRESHOLD:

            risk_label = 'MEDIUM RISK'
            risk_class = 'medium-risk'

            summary = (
                'This customer shows moderate churn risk. '
                'Proactive engagement may reduce the likelihood of cancellation.'
            )

        else:

            risk_label = 'LOW RISK'
            risk_class = 'low-risk'

            summary = (
                'This customer currently appears relatively stable. '
                'Continue good service and consider loyalty-focused engagement.'
            )

        factors = build_risk_factors(
            form_values
        )

        recommendations = build_recommendations(
            form_values,
            risk_class
        )

        recommendation = recommendations[0]

        prediction_data = {
            'label': risk_label,
            'probability': probability,
            'percentage': percentage,
            'risk_class': risk_class,
            'summary': summary,
            'risk_factors': factors,
            'recommendations': recommendations,
        }

    # ============================================================
    # Calculate average churner profile for comparison
    # ============================================================

    chart_data = None

    if show_result:

        monthly_charge_value = float(
            form_values['monthlyCharges']
        )

        tenure_value = int(
            form_values['tenure']
        )

        total_charge_value = float(
            form_values['totalCharges']
        )

        # Average churner profile
        # Estimated based on typical churn patterns

        avg_monthly_charges = 74.5
        avg_tenure = 18
        avg_total_charges = 2283.3

        chart_data = {
            'monthly_charges': {
                'customer': round(
                    monthly_charge_value,
                    2
                ),
                'average_churner': avg_monthly_charges
            },

            'tenure': {
                'customer': tenure_value,
                'average_churner': avg_tenure
            },

            'total_charges': {
                'customer': round(
                    total_charge_value,
                    2
                ),
                'average_churner': avg_total_charges
            }
        }

    return render(
        request,
        'churn.html',
        {
            'predict': predict,
            'show_result': show_result,
            'risk_label': risk_label,
            'risk_class': risk_class,
            'summary': summary,
            'recommendation': recommendation,
            'probability': probability,
            'prediction_data': prediction_data,
            'errors': errors,
            'form_values': form_values,
            'customer_id': customer_id,
            'contract': contract,
            'monthly_charges': monthly_charges,
            'internet_service': internet_service,
            'chart_data': chart_data,

            'model_info': {
                'algorithm': 'Artificial Neural Network',
                'dataset': 'Telco Customer Churn',
                'features': '29 engineered features',
                'prediction_type': 'Binary churn classification',
                'version': 'Not specified',
            },
        }
    )
