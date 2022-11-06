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


#Try and Except Statement for connecting cloud
try:
    deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
    deviceCli = ibmiotf.device.Client(deviceOptions)
except Exception as e:
    print ("Caught exception connecting device %s" %str(e))
    sys.exit()

#Device CLI Connectivity
deviceCli.connect()


#Sensing Distance and Alerting Cloud
while True:
    distance = random.randint(0,100)
    data = {'temperature': distance}
    def myOnPublishCallback():
        print("Published Distance", distance)
    success = deviceCli.publishEvent("IoTSensor", "json", data, qos=0, on_publish=myOnPublishCallback)
    if not success:
        print ("Not Connected to IoT")
    
    time.sleep(1)

deviceCli.disconnect()