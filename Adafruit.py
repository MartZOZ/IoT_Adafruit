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

digital_output = board.get_pin('d:3:o')

try:
	digital = aio.feeds('digital')

except RequestError:
	feed = Feed(name='digital')
	digital = aio.create_feed(feed)

while True:
	print('Sending count:', run_count)
	run_count += 1
	aio.send_data('counter', run_count)

	data = aio.receive(digital.key)

	print('Data: ', data.value)

	if data.value == "ON":
		digital_output.write(True)
	else:
		digital_output.write(False)

time.sleep(15)