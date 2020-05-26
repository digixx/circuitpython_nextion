import board
import busio
import digitalio
import time
import m_nextion


# Display
Nextion_LED = m_nextion.create_led()
Nextion_UI = m_nextion.create_nextion()
ct = time.monotonic()

Nextion_UI.addElement('Temp', '24.5')	# Textelement on Nextion
Nextion_UI.addElement('Press', '985.2') # Textelement on Nextion
Nextion_UI.addElement('btn1', 0)		# Button on Nextion
Nextion_UI.addElement('LogRun', 0)		# Variable on Nextion, used for changing picture of Button

while True:
    if ct + 0.5 < time.monotonic():
        ct = time.monotonic()
        # update often
		m_nextion.update(Nextion_UI, Nextion_LED)

		Nextion_UI.set_element('Temp', '28.0')
		Nextion_UI.set_element('Press', '1013')		

        if Nextion_UI.getElement('btn1') == 1: # if button ist pressed on Nextion
            Nextion_UI.setElement('LogRun', 1, True) # set 'LogRun' to 1 on Nextion (changes Picture to ON)
        else:
            Nextion_UI.setElement('LogRun', 0, True) # set 'LogRun' to 0 on Nextion (changes Picture to OFF)
