import bluetooth
import subprocess

button_name = "Mooni"
#address = "20:14:11:36:93:CD"
port = 1
address = "F4:4E:FD:43:77:CC"
#nearby_devices = bluetooth.discover_devices(lookup_names=True)

#print("Found {} devices.".format(len(nearby_devices)))

#for addr, name in nearby_devices:
#    print("  {} - {}".format(addr, name))
status = subprocess.call("bluetoothctl &",shell=True)

#when Mooni is found, then it loads the script to wait for button press
try:
    s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    s.connect((address,port))
    print("Successfully connected!")
except bluetooth.btcommon.BluetoothError as err:
    # Error handler
    pass

while True:
    data = s.recv(1024)
    if len(data) == 0: break
    print("received [%s]" % data)


