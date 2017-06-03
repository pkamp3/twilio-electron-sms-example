# twilio-electron-sms-example

Convert SMSes and MMSes to Morse Code with Twilio and a Particle Electron

This file is one half of a SMS to Morse Code translator using Twilio and a Particle Electron.  You need to run this Flask Python server to listen for Twilio Webhooks, which will then be forwarded onto your claimed Particle Electron.

Find everything you need on the Twilio and Particle sites:

* https://twilio.com
* https://particle.io

## Running

These instructions will work on *NIX derived operating systems and environments, but you may need to adapt if you are on others.

```
git clone https://github.com/pkamp3/twilio-electron-sms-example.git

# Optional
virtualenv -p python3 env
source env/bin/activate

# Non-optional
pip install twilio

export FLASK_APP=app.py
flask run
```

You'll also need to publically expose the /message endpoint.  Insert that into a 'Messaging' webhook for your choice of number inside the [Twilio Console.](https://twilio.com/console)

## Client Side

You can find the associated client side code here.  Burn this to your Particle Electron from the Particle Web IDE:

* [Particle Electron SMS to Morse Code Firmware](https://build.particle.io/shared_apps/5931e08c07e2001a5c000eae)

## Meta & Licensing

* [MIT License](http://www.opensource.org/licenses/mit-license.html)
* Lovingly crafted by [Twilio Developer Education](https://twilio.com/docs).