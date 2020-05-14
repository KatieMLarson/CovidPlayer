import bluetooth

client_socket=bluetooth.BluetoothSocket(bluetooth.RFCOMM)

client_socket.connect(("127.0.1.1", 3))

client_socket.send("No Spaces Please");

print("Finished")

client_socket.close()