import serial.tools.list_ports                                                                                                                         
import time                                                                                                                                            
                                                                                                                                                       
relay_ON = [[0, 0, 0, 0, 0,   0,   0,   0],                                                                                                            
            [1, 6, 0, 0, 0, 255, 201, 138],                                                                                                            
            [2, 6, 0, 0, 0, 255, 201, 185],                                                                                                            
            [3, 6, 0, 0, 0, 255, 200, 104],                                                                                                            
            [4, 6, 0, 0, 0, 255, 201, 223],                                                                                                            
            [5, 6, 0, 0, 0, 255, 200,  14],                                                                                                            
            [6, 6, 0, 0, 0, 255, 200,  61]]                                                                                                            
                                                                                                                                                       
relay_OFF = [[0, 0, 0, 0, 0,  0,   0,   0],                                                                                                            
             [1, 6, 0, 0, 0,  0, 137, 202],                                                                                                            
             [2, 6, 0, 0, 0,  0, 137, 249],                                                                                                            
             [3, 6, 0, 0, 0,  0, 136,  40],                                                                                                            
             [4, 6, 0, 0, 0,  0, 137, 159],                                                                                                            
             [5, 6, 0, 0, 0,  0, 136,  78],                                                                                                            
             [6, 6, 0, 0, 0,  0, 136, 125]]                                                                                                            
MAX_ID = 7                                                                                                                                             
                                                                                                                                                       
port = "/dev/ttyAMA2"                                                                                                                                  
baudrate = 9600                                                                                                                                        
print("Find port {} - baudrate {}".format(port, baudrate))                                                                                             
"""ser = serial.Serial(port, baudrate, timeout=1, bytesize=8, parity="N",stopbits=1)"""                                                                
ser = serial.Serial(port, baudrate)                                                                                                                    
print(ser)                                                                                                                                             
                                                                                                                                                       
                                                                                                                                                       
def serial_read_data(ser):                                                                                                                             
    bytesToRead = ser.inWaiting()                                                                                                                      
    if bytesToRead > 0:                                                                                                                                
        out = ser.read(bytesToRead)                                                                                                                    
        data_array = [b for b in out]                                                                                                                  
        print(data_array)                                                                                                                              
        if len(data_array) >= 7:                                                                                                                       
            array_size = len(data_array)                                                                                                               
            value = data_array[array_size - 4] * 256 + data_array[array_size - 3]                                                                      
            return value                                                                                                                               
        else:                                                                                                                                          
            return -1                                                                                                                                  
    return 0                                                                                                                                           
                                                                                                                                                       
                                                                                                                                                       
def relay_all(ser):                                                                                                                                    
    for relay_ID in range(1, MAX_ID):                                                                                                                  
        print("\n\nTest relay ID=", relay_ID)                                                                                                          
        print("relay ON array: ",relay_ON[relay_ID])                                                                                                   
        ser.write(relay_ON[relay_ID])                                                                                                                  
        print("RESPONSE: ",serial_read_data(ser))                                                                                                      
        time.sleep(6)                                                                                                                                  
                                                                                                                                                       
        print("\nrelay OFF array: ", relay_OFF[relay_ID])                                                                                              
        ser.write(relay_OFF[relay_ID])                                                                                                                 
        print("RESPONSE: ",serial_read_data(ser))                                                                                                      
        time.sleep(6)                                                                                                                                  
                                                                                                                                                       
                                                                                                                                                       
def relay_all_on(ser):                                                                                                                                 
    for relay_ID in range(1, MAX_ID):                                                                                                                  
        print("Test ON relay ID=", relay_ID)                                                                                                           
                                                                                                                                                       
        ser.write(relay_ON[relay_ID])                                                                                                                  
        print("RESPONSE: ", serial_read_data(ser))                                                                                                     
        time.sleep(2)                                                                                                                                  
                                                                                                                                                       
                                                                                                                                                       
def relay_all_off(ser):                                                                                                                                
    for relay_ID in range(1, MAX_ID):                                                                                                                  
        print("Test OFF relay ID=", relay_ID)                                                                                                          
                                                                                                                                                       
        ser.write(relay_OFF[relay_ID])                                                                                                                 
        print(serial_read_data(ser))                                                                                                                   
        time.sleep(2)                                                                                                                                  
                                                                                                                                                       
                                                                                                                                                       
while True:                                                                                                                                            
    relay_all(ser)                                                                                                                                     
    #relay_all_on(ser)                                                                                                                                 
    #time.sleep(8)                                                                                                                                     
    #relay_all_off(ser) 