import time
from Adafruit_IO import Client, Feed, RequestError
import pyfirmata
	
run_count = 0
ADAFRUIT_IO_USERNAME = "MartZOZ"
ADAFRUIT_IO_KEY = "aio_MiRh54jyRgfsySEv6XAkdNX8qtQH"
#Adafruit IO keys regenerate semi-regularly, make sure to check if it is active!

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

board = pyfirmata.Arduino('COM4')

it = pyfirmata.util.Iterator(board)
it.start()

digital_output = board.get_pin('d:3:o')#LED pin on arduino

try:
	digital = aio.feeds('digital') #This requests the feed from the feed "digital"

except RequestError:
	feed = Feed(name='digital') 
	digital = aio.create_feed(feed)

while True:
	print('Sending count:', run_count)
	run_count += 1

	aio.send_data('counter', run_count) #This checks and updates the counter value every time the code checks for an update from the "counter" feed

	data = aio.receive(digital.key)

	print('Data: ', data.value)

	if data.value == "ON": #This checks if the toggle key on adafruit is On or Off
		digital_output.write(True)
	else:
		digital_output.write(False)

time.sleep(15)