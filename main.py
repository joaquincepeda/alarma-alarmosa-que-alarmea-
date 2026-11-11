from microdot import Microdot, send_file
from machine import Pin
import time 
import ntptime

print(time.localtime())
ntptime.settime(

def tiempo actual():
    return time.localtime(time.time() - (3 * 3600))

print(tiempo actual)

)
pins = {
    12: Pin(12,Pin.OUT),
    14: Pin(14,Pin.OUT)
}

for pin in pins.values():
    pin.value(0)

app=Microdot()

def estado_pin(gpio):
    return "checked" if pins[gpio].value() else ""

def armar_botones():
    botones = ""
    for gpio in pins:
        html= f"""
            <h3>salida - GPIO {gpio}</h3>
            <label class="switch">
                <input type="checkbox" onchange="toggleCheckbox(this)" id="{gpio}" {estado_pin(gpio)}>
                <span class="slider"></span>
            </label>
        """
        botones += html
    return botones

def mainpage():
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>whi so sirius?</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <h1>ESP web server madein peru</h1>
        <!--llos leds-->
        {armar_botones()}

        <script src="script.js"></script>
	<div class="nowDateTime">
  	<p>
    	<span id="fecha"></span><br />
    	<span id="hora"></span>
  	</p>
	</div>
    </body>
    </html>
"""


@app.route("/")
async def index(request):
    return mainpage(), 200, {"content-Type": "text/html"}

@app.route("/style.css")
async def css(request):
    return send_file("style.css")

@app.route("/script.js")
async def css(request):
    return send_file("script.js")

@app.route("/update")
async def update(request):
    gpio_param = request.args.get("output")
    state_param = request.args.get("state")

    if gpio_param is not None and state_param is not None:
        gpio = int(gpio_param)
        state = int(state_param)
        if gpio in pins:
            pins[gpio].value(state)
        print(f"GPIO:{gpio} - Estado:{state}")
    else:
        print("No se encontraron los parametros")

    return "OK", 200, {"Content-Type": "text/plain"}

@app.route("/input")
async def input_state(request):
    estado = "1" if pir.value() == 0 else "0"
    return estado, 200, {"Content-Type": "text/plain", "Cache-Control": 'no-store'}

app.run(port=80)
