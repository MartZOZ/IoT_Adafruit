# IoT_Adafruit
This is a project for school.
Connect an adafruit dashboard to control an LED on your arduino board.



Step-by-step

Install PyFirmata, this requires pip to be installed. To install PyFirmata, open CMD and run "pip install Pyfirmata", this should run a quick install, some instances of python already come installed with pyfirmata.

Connect your arduino board with an LED

Download StandardFirmata.ino

Upload the code to your arduino

Download Adafruit.py

Change the adafruit key to your own (the one in the script is old)

Create one or two blocks, one toggle, and another can be a value

rename the toggle block feed to "digital", and rename a value block to "counter"

Run the python script

if you've done everything correctly you should be able to control an LED with the toggle button on your dashboard :)
