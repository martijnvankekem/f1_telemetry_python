# F1 Telemetry - Python
Receives and processes the UDP Telemetry data of the Codemasters' Formula One game.

### F1 Setup
In order for this program to work, you need to enable the UDP Telemetry option in F1 2017. To to this, follow these steps:
1. Open the game options.
2. Choose 'UDP Telemetry settings', under 'Preferences'.
3. Switch 'UDP Telemetry' to 'On'
4. Switch 'Broadcast Mode' to 'Off'
5. Set 'IP Address' to the IP of the system where Python is running on.
6. Set 'Port' to the same port as in the script. By default, they are the same and in most cases, there is no need to change this.
7. Set 'Send rate' to the highest value possible, as long as you don't experience any lag in Python or the game itself.

### Python Setup
Make sure you set the IP-address and port to the right values. These differ from network to network.

### Usage
Inside the 'while True:' function, call the following function to retrieve the F1 UDP data:
```python
getValByName(tag)
```
Tag is here a string object, containing the name of the value you want to receive. All the possible values can be found under 'ArrayStructure.py'

### Credits
This program was written from scratch by myself. I want to thank all the sources that helped me create this application.
+ https://github.com/gmaslowski/f1game-telemetry/wiki/udp-packet-1237-structure
- http://forums.codemasters.com/discussion/53139/f1-2017-d-box-and-udp-output-specification
