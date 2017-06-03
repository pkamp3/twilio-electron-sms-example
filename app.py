"""
Basic example of routing Twilio Messaging Webhook requests.

We take incoming SMS messages, do some basic sanity checking,
then forward the bodies to Particle's Cloud Function APIs. On
our Electrons, we react with Morse code on the LEDs.
"""

from flask import Flask, request, abort
from twilio.twiml.messaging_response import MessagingResponse
import requests
import os

app = Flask(__name__)
DEVICE_NAME = os.environ['PARTICLE_DEVICE']
FUNCTION_NAME = os.environ['PARTICLE_FUNCTION']
PARTICLE_TOKEN = os.environ['PARTICLE_TOKEN']
TWILIO_TOKEN = os.getenv('TWILIO_TOKEN', None)


@app.route('/')
def hello_world():
    """Just an empty route with a string."""
    return "Hello there.  This route doesn't do anything."


@app.route("/message", methods=['GET', 'POST'])
def hello_sms():
    """Handle incoming Twilio message routing."""
    if not request or not request.form \
            or not request.form['Body'] or request.form['Body'] == '':
        # Some error, check your Webhook.
        resp = MessagingResponse().message(
            "Unknown error or empty.  Check Twilio's console and debugger."
        )
        return str(resp)

    # Happy cases!
    morse_body = request.form['Body'].lower()
    if len(request.form['Body']) > 63:
        # We're only going to take the first 63 characters, warn them.
        resp = MessagingResponse().message(
            "We can only handle 63 maximum characters.  "
            "Message truncated."
        )
        morse_body = morse_body[0:63]
        print(morse_body)
    else:
        # Awesome!  Full Morse code coming up.
        resp = MessagingResponse().message(
            "We'll make it - ahem, blink it - so!"
        )

    r = requests.post(
        'https://api.particle.io/v1/devices/' + DEVICE_NAME +
        '/' + FUNCTION_NAME,
        data={
            'access_token': PARTICLE_TOKEN,
            'arg': morse_body
        }
    )

    print(r.url)
    print(r.text)

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
