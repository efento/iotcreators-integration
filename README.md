# IoT creators integration
A simple Python application that receives messages from IoT Creators, deserialises the data and saves them in a database. The application is used for demo purposes and should not be used in large scale deployments! Should you have any issues or questions, feel free to drop us a line at help.efento.io
 
The major task of IoT Creators is to provide a bridge of abstraction between IoT devices and IoT platforms and applications. IoT Creators provides connectivity (powered by Deutsche Telekom) and a server platform that receives the data from IoT devices over any of the popular IoT protocols, translates it to REST messages and pushes it to any third party application. To learn more, visit iotcreators.com and read the platform's documentation.
The goal of this tutorial is to set up a connection between Efento sensor and IoT Creators platform, which will forward all the data received from the sensor to any third party application over REST.
![image](https://user-images.githubusercontent.com/19836659/129179738-66a9457d-bedd-41cc-8f85-c2bf53db74c4.png)


# How to use the application?

1. Setup PostgreSQL database with table matching the table used in the Python script
2. Run the script
3. Setup your device and data forwarding at iotcreators.com



