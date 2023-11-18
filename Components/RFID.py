#MFRC522 RFID Module	Raspberry Pi GPIO Pin
#SDA	24 (GPIO8)
#SCK	23 (GPIO11)
#MOSI	19 (GPIO10)
#MISO	21 (GPIO9)
#GND	Any Ground Pin
#RST	22 (GPIO25)
#3.3V	3.3V Power

import RPi.GPIO as GPIO
import MFRC522
import signal

# Create an instance of the RFID reader
reader = MFRC522.MFRC522()

# Function to read RFID tags
def read_rfid():
    (status, TagType) = reader.MFRC522_Request(reader.PICC_REQIDL)
    if status == reader.MI_OK:
        (status, uid) = reader.MFRC522_Anticoll()
        if status == reader.MI_OK:
            # Convert UID to a string format
            uid_str = ":".join([str(i) for i in uid])
            return uid_str
    return None

# Cleanup GPIO on program exit
def end_read(signal,frame):
    print("Ctrl+C captured, ending read.")
    GPIO.cleanup()
    exit()

# Hook the Ctrl+C signal to end the read loop
signal.signal(signal.SIGINT, end_read)

# # Main loop to continuously read RFID tags
while True:
    uid = read_rfid()
    print(uid)
    if uid:
        print("RFID card detected!")
        # Replace the following UID with your allowed UID
        allowed_uid = "71:80:CD:24"
        if uid == allowed_uid:
            print("Access granted!")
        else:
            print("Access denied!")
