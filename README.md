# IIoT-Simulation-And-Security
Simulating Industrial IoT with IGSS SCADA and Rasberry Pi, Attacking and fixing potential vulnerabilities

## Project Abstract :

Internet of Things (IoT) is being used all over the world to collect data
and perform actions where it requires huge man power or nearly impossible
for a human to spend his time, also in difficult situations relating to
temperature and pressure for a human to function. And such data transfers
need an Intelligent System to handle and process, In case of Industries
SCADA systems do the role of tracking, collecting and managing data from
these IoTs. Here is where security comes into play valuing the data being
stored and processed. Which affects a significant part of a company’s
revenue. Our approach to the problem is to build a working prototype of an
IOT system connected to a SCADA system and understand the various
challenges of building such a model to get a holistic approach on the
topic, followed by fixing any security vulnerabilities if possible.

#### Video link for code explanation and execution of project
https://drive.google.com/file/d/1KV3_qv2VXFXyZqKR1NDP5QNC_NYAJUth/view

### Code Execution :
Setup Ultrasonic sensor and an LED with mentioned gpio pin numbers from
the code
### Dependencies:
* In Raspberry Pi terminal
  * pip install pymodbus // install pymodbus library
  * sudo kill $(lsof -t -i:510)// kill process running on port 510
    
### Running the code:
* sudo python SCADA.py

### SCADA Execution:
* Open IGSS software
* Extract and import the SCADA project RaspberryPiAndSCADA.rar
* Run the project
* Toggle LED On and Off
* Pass objects over the Ultrasonic sensor to see the counter
increasing.

### Exploiting MODBUS TCP vulnerability:
* pip install scapy[basic]
* Open command prompt
  * To toggle LED On
    * python send.py
  * To toggle LED OffChange line 11
  * byte of the payload value to ‘\x00’
    * Save and run python send.py
* View the packets being sent in Wireshark.The port numbers which
represent the source of the SCADA instructions need to be changed
after every execution of the code since it is still listening to
that connection unless the processes running on the port are killed. 
