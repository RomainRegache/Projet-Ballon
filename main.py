import dirigeable
import pycom
import time
from machine import Pin, I2C
from MPL3115A2 import MPL3115A2,ALTITUDE,PRESSURE
import ccs811
from machine import ADC
import mq135class
import urequests
import mcp9808

def cc118():
    sda = 'P22'
    scl = 'P21'
    i2c = I2C(0, mode=I2C.MASTER, pins=(sda, scl))
    s = ccs811.CCS811(i2c)
    time.sleep(1)
    if s.data_ready():
            print('eCO2: %d ppm, TVOC: %d ppb' % (s.eCO2, s.tVOC))
            time.sleep(1)
    return s.eCO2, S.tVOC


def MCP9808_example():#test ok
    sda = 'P22'
    scl = 'P21'
    i2c = I2C(0, mode=I2C.MASTER, pins=(sda, scl))
    mcp = mcp9808.MCP9808(i2c)
    print("Temperature MCP9808 : %f" % (mcp.get_temp()))
    temperature = mcp.get_temp()
    mcp.set_shutdown_mode()
    return temperature

def test_sensor_mq135():#Test OK
    adc = ADC()               # create an ADC object
    apin = adc.channel(pin='P16', attn=ADC.ATTN_11DB)
    while(1):
    # create an analog pin on P16 & connect CO2 sensor
        print("")
        print("CO2 sensor Warming Up")
        #need initial delay (180) # CO2 sensor needs 3 minutes to warm up
        print("Reading CO2 Sensor...")
        value = apin()
        print("ADC count = %d" %(value))
        co2 = (value) * (3900/4096.0)
        print("CO2 Level = %5.1f ppm" % (co2))
        time.sleep(10)
        return co2

def data_sensor_mpl():#Test ok
    mp = MPL3115A2() # Returns height in meters. Mode may also be set to PRESSURE, returning a value in Pascals
    print("MPL3115A2 temperature: " + str(mp.temperature()))
    print("Altitude: " + str(mp.altitude()))
    Altitude = mp.altitude()
    mp = MPL3115A2(mode = PRESSURE)
    print("pressure: " + str(mp.pressure()))
    Pressure = mp.pressure()

    return Altitude,Pressure

def led():#Test ok
    pycom.rgbled(0x0A0A08) # white
    pycom.rgbled(0x007f00) # vert
    pycom.rgbled(0x00007f) # bleu
    pycom.rgbled(0x7f0000) # rouge

def trame(value1,value2,value3,value4):#Test ok
    trame_send =  {
        "dirigeable" : 'OK',
        "Temperature" : str(value1) ,
        "Altitude" :  str(value2)  ,
        "Pression" :  str(value3)  ,
        "CO2" :  str(value4)
    }
    return trame_send

def communication(trame):#Test ok
    print("DEBUT COMMUNICATION")
    d = dirigeable.Dirigeable()
    d.sleep(60000)
    pycom.rgbled(0x00007f) # bleu
    print(trame)
    userdata = trame
    value = 1
    url = "http://192.168.4.1/post.php"
    res = urequests.post('http://192.168.4.1/post.php',json = trame)
    res.close()
    print(res.status_code)
    print(res.reason)
    if(res.status_code -200) <100:
        print('done')
        pycom.rgbled(0x007f00) # vert
    else:
        print('error')
        pycom.rgbled(0x7f0000) # rouge


def test_com():#Test non
    print("DEBUT")
    d = dirigeable.Dirigeable()
    d.sleep(2000)
    d.data_add_test()
    d.data_send_default()


def mq135lib_example():#Test non
    """MQ135 lib example"""
    # setup
    temperature = 21.0
    humidity = 25.0
    mq135 = mq135class.MQ135(16) # analog PIN 0
    # loop
    while True:
        rzero = mq135.get_rzero()
        corrected_rzero = mq135.get_corrected_rzero(temperature, humidity)
        resistance = mq135.get_resistance()
        ppm = mq135.get_ppm()
        corrected_ppm = mq135.get_corrected_ppm(temperature, humidity)

        print("MQ135 RZero: " + str(rzero) +"\t Corrected RZero: "+ str(corrected_rzero)+
              "\t Resistance: "+ str(resistance) +"\t PPM: "+str(ppm)+
              "\t Corrected PPM: "+str(corrected_ppm)+"ppm")
        time.sleep(0.3)


if __name__ == "__main__":
    pycom.heartbeat(False)
    pycom.rgbled(0x0A0A08) # white
    d = dirigeable.Dirigeable()
    d.wifi_start()
    still = 1
    while (True):
        print("DEBUT PRISE DE MESURE")
        #CO2,VOC = cc118()
        altitude,pressure = data_sensor_mpl()
        temperature = MCP9808_example()
        CO2 = test_sensor_mq135()
        trame_tr = trame(temperature,altitude,pressure,CO2)
        communication(trame_tr)
        time.sleep(10) #sleep 1 seco
