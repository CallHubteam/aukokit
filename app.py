from flask import Flask, request, jsonify, render_template_string
import stripe

app = Flask(__name__)

stripe.api_key = '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'

@app.route('/')
def home():
    return render_template_string(open('aukokime_vaikams.html').read())

@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    data = request.get_json()
    name = data['name']
    email = data['email']
    amount = int(data['amount']) * 100  # Convert to cents
    message = data['message']

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'eur',
                'product_data': {
                    'name': 'Donation',
                    'description': f'Donation from {name} - {message}',
                },
                'unit_amount': amount,
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='http://localhost:5000/success',
        cancel_url='http://localhost:5000/cancel',
    )

    return jsonify(id=session.id)

@app.route('/success')
def success():
    return 'Thank you for your donation!'

@app.route('/cancel')
def cancel():
    return 'Your donation was canceled.'

if __name__ == '__main__':
    app.run(debug=True)
