PgP 7/26/2023-
IoT4 builds on IOT3B, with some changes-
began creating new RPi image using Buster Legacy, Raspbian OS 5/3/2023 with the following:
wpa_supplicant for Som301and304-so that students do not have to worry about wifi
wait for network on boot so that IP address is assigned before ippi.py runs
ippi.py that displays IP address in the upper right corner of desktop-runs on bootup
screen blanking turned off so the IP address is always available-no need for mouse/keyboard
updateRestart.sh is a cron job runs at 2am every morning to update and restart RPi, has randomized wait function so all RPis not doing so at once

GrovePiReset.sh to reset the GrovePi ATMega328P chip without need to turn off system 
IOT00 introduced to show students correct way to startup/shutdown Pi, and look for GrovePi+ red reset light on


PgP 7/6/2022-
breaking it into two sections, IOT01-IOTxx which are for single board computers like the Raspberry Pi, and later LattePanda?
the second section will be IOTu01-IOTuxx which are for microcontroller assignments like Arduino, micro:bit and Pico


Here is initial list:

IOT2 name		IOT3 Name		Type-sbc or u	spearate sensors/actuators/breadboard?	Notes
IOTP01	Single Board Computers	IOT01	Single Board Computers	sbc		
IOTP02	VNC GUI RPi	IOT02	VNC GUI RPi	sbc		
IOTP03	SSH CLI RPi	IOT03	SSH CLI RPi	sbc		
IOTA01	Arduino UNO Setup	IOTu01	Arduino UNO Setup	u		
IOTB01	micro:bit Setup	IOTu02	micro:bit Setup	u		
IOT01	RPi, WaveMon	IOT04	RPi, WaveMon	sbc		
IOT02	RPi, Apache2	IOT05	RPi, Apache2	sbc		
IOT03	RPi, Web Pages	IOT06	RPi, Web Pages	sbc		
IOT04	RPi, Zenmap	IOT07	RPi, Zenmap	sbc		
IOT05	RPi, Nagios	IOT08	RPi, Nagios	sbc		
IOT06	RPi Monitor	IOT09	RPi Monitor	sbc		
IOT07	RPi, MySQL	IOT10	RPi, MySQL	sbc		
IOT08	RPi, MagicMirror	IOT11	RPi, MagicMirror	sbc		
IOT09	RPi, Node RED	IOT12	RPi, Node RED	sbc		
IOT10	RPi, GrovePi+ Sensor and Actuator System	IOT13	RPi, GrovePi+ Sensor and Actuator System	sbc	Y	
IOT_TTL	RPi, USB TTL	IOT14	RPi, USB TTL	sbc		
IOT_Zoom	RPi, Zoom for RPi 4	IOT15	RPi, Zoom for RPi 4	sbc		can do on RPi3, but slow, screenshots begun
NR01	Node RED	IOT16	Node RED	sbc		
NR02	Node RED Flows	IOT17	Node RED Flows	sbc		
NR03	Node RED sensors	IOT18	Node RED sensors	sbc	Y	
		IOTu03	Pico Setup	u		setup micropython envirnonment
		IOTu04	Pico program	u		run simple microPython program
		IOTu05	Pico Digital Actuator	u 		turn on onboard LED, digital actuator, through program (toggle?)
		IOTu06	Pico HW Digital Actuator	u	Y	 use pushbutton hw to toggle onboard LED   
		IOTu07	Pico Analog Sensor	u		 read onboard temp analog sensor, print to shell   
		IOTu08	Pico HW Analog Sensor	u	Y	 use thermistor hw to read analog sensor, write to shell   
		IOTu09	Pico Analog Actuator	u		 turn on  buzzer analog actuator through program 
		IOTu10	Pico HW Analog Actuator	u	Y	 use pushbutton hw  to create varying tone on passive analog  buzzer acutator  





PgP 7/3/2022
IoT3 is a renumbering of the IoT assignments, using a simple IOT01-IOTxx system.
