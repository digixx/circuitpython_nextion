# digixx_circuitpython_nextion 

This is a circuitpython library for Nextion LCD Displays

Parsing data send from Nextion is somehow complicated. So I use a much simpler protocoll. It uses a common technique known from GPS NMEA sentences.
The data is enveloped between a startmarker and endmarker. Both markers coulnd't be used inside the data.
Reading the incoming stream of data, you start collecting data after the startmarker is found. The endmarker stops collecting and the command will be parsed and executed.

Sending data to the Nextion will use the normal API of the Nextion.

Buttons / Textfields etc. will be declared with there name used on the Nextion. Inside the library they will be added to a dictionary. This is the central datastorage. If the Nextion send a value, it is stored in the corresponding dictionary_element. If the Nextion request a page/part update, the microcontroller sends the programmed elements to the Nextion.

In this demo, there is an LED declared, showing the requests from the Nextion (toggles by request)

The method update(nextion,led) returns a tuble containing a page and part data. If page is 0, no page data is been requested. If not, the code on the microcontroller sends data for all the elements located on this page. If you want to have more underpages, use parts as paging function.


