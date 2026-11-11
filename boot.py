import network
import esp
import gc

esp.osdebug(None)
gc.collect()

ssid = "AcademiasIndetec"
password = "Indetec_2026"

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

print (f'conectando a {ssid}')
wlan.connect(ssid, password)
while not wlan.isconnected():
    pass

wlan.config(pm=network.WLAN.PM_NONE)

print(f'conexion exitosa. \nIP: {wlan.ifconfig()[0]}')