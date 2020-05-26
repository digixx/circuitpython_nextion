import board
import busio
import digitalio
from nextion import Nextion


def create_led():
    led = digitalio.DigitalInOut(board.A3)
    led.direction = digitalio.Direction.OUTPUT
    led.value = True
    return led


def toggle_led(led):
    led.value = not led.value


def create_nextion():
    uart = busio.UART(board.TX, board.RX, stop=1, baudrate=115200, timeout=0.1)
    nextion = Nextion(uart)
	
    # **** String Elements
    # Sensors
    nextion.add_element("Temp", "-")
    nextion.add_element("Press", "-")
    # **** Button Elements
    nextion.add_element("btn1", 0)  # Button 
	
    return nextion


def refresh_page_data(nextion, page, part):
    if page == "1":  # Main screen showing sensor data
        nextion.refresh_element("Temp")
        nextion.refresh_element("Press")
        nextion.set_element("LogRun", nextion.get_element("btn1"), True)

		
def update(nextion, led):
    page, part = nextion.update()
    # print("page-part", page, part)
    if page is not "0":
        toggle_led(led)
        refresh_page_data(nextion, page, part)

