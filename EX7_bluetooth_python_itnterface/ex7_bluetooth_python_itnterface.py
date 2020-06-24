'''
Upload "e7_bluetooth_python_itnterfacel.ino" sketch to arduino (or)
"e1_led_control.ino" sketch to arduino
Use Pyhton 3.7 
Install respective packages if its missing or you get module not found error
Please take care of indenting your code
'''
#Import following packages
import serial
import tkinter
import tk_tools

'''
Connect to HC-05 Bluetooth via serial port: Password: 1234
Goto --> Device manager to find the serail port number of BLE module
com7 --> Change port accordingly to yours as the bluetooth is connected 
'''
arduino = serial.Serial('com6', 9600) 

#Function call for led_on button
def led_on():
    arduino.write(b'0') #write this value to arduino 
    led.to_green(True)  #Glow the led to green --> Refer to tk-tools docs
    button_on.config(state = "disabled") #disable button_on 
    button_off.config(state = "normal") # enable button_off to normal state

#function call for led_off button
def led_off():
    arduino.write(b'1') #write this value to arduino 
    led.to_green() #Switch off the led --> Refer to tk-tools docs
    button_off.config(state = "disabled") #disable button_off
    button_on.config(state = "normal") #enable button_on to normal state

#exit function call for closing the program
def close_window():
    arduino.close() #close Serial connection with arduino
    window.destroy() #destro tkinter app
    
# MAIN
window = tkinter.Tk() #create tkinter window
window.title("Arduino RGB Led Control") #give title
window.configure(background="white") #change background color 

#Create buttons
button_on = tkinter.Button(window, text="ON", 
                           font= ('Verdana',16), padx=50, pady =20, 
                           bg="green",fg="white",
                           command = led_on)

button_off = tkinter.Button(window, text="OFF", 
                            font=('Verdana',16), padx=50, pady =20, 
                            bg="red",fg="white",
                            command = led_off)

button_exit = tkinter.Button(window, text="Exit", 
                             font=('Verdana',16), 
                             padx=130, pady =20, 
                             command = close_window)

#Pack buttons
button_on.grid(row=1,column=1)
button_off.grid(row=1,column=2)
button_off.config(state = "disabled")
button_exit.grid(row=2,column=1, columnspan =2)

#Create interactive led using tk-tools
led = tk_tools.Led(window, size=100)
led.to_green() #set led to green switch off condition) --> Refer tk-tools docs
led.grid(row=0,column=1, columnspan =2)
    
#execute the loop
window.mainloop()