# SmartPi

The pi has three different loggers: weather, wifi, and physical sensors. Next up is the creation of a web server which can show the information stored in the MySQL database.

The server will likely use python and flask as the backend.

## Weather

Using a weather underground api call, the current weather is stored in a MySQL table every 10 minutes.

## Wifi

Using speedtest-cli, the wifi's ping, download and upload speeds are recorded in a MySQL table every 30 minutes.

## Sensors

The pi is hooked up to a DHT22 temperature/humidity sensor. This table contains information from the DHT22 and a reading of cpu usage.
