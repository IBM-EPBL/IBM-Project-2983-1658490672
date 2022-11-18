import sys
import random
import time
import ibmiotf.application                 
import ibmiotf.device

#IBM Cloud Credentials
organization = "jtp3hb"
deviceType = "ESP32"
deviceId = "123456789"
authMethod = "token"
authToken = "1234567890"

def myCommandCallback(cmd):
    print("Command Recived: %s" % cmd.data['command'])
    status = cmd.data['command']
    if status == "motoron":
        print("Motor is ON")
    else:
        print("Motor is OFF")

#Try and Except Statement for connecting cloud
try:
    deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
    deviceCli = ibmiotf.device.Client(deviceOptions)
except Exception as e:
    print ("Caught exception connecting device %s" %str(e))
    sys.exit()

#Device CLI Connectivity
deviceCli.connect()


#Sensing and Alerting Cloud
while True:
    humidity = random.randint(0,100)
    temperature = random.randint(0,100)
    soilmoisture = random.randint(0,100)

    data = {'temperature': temperature, 'humidity' : humidity, 'soilmoisture' : soilmoisture}
    def myOnPublishCallback():
        print("Published Metrics", humidity, temperature, soilmoisture)
    success = deviceCli.publishEvent("IoTSensor", "json", data, qos=0, on_publish=myOnPublishCallback)
    if not success:
        print ("Not Connected to IoT")
    
    time.sleep(1)
    deviceCli.commandCallback = myCommandCallback

deviceCli.disconnect()