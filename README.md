Arduino-Based Redundant Transmission for Buoy Networks



Overview

This repository contains the implementation and documentation for the Arduino-Based Redundant Transmission for Buoy Networks. The project aims to establish a resilient communication network among marine buoys using redundant transmission techniques to enhance reliability in harsh environments.

Project Objective

Buoy networks play a critical role in oceanographic data collection, weather monitoring, and maritime security. However, signal transmission between buoys and land stations is often unreliable due to environmental interference, range limitations, and power constraints. This project addresses these challenges by implementing:

✅ Redundant Data Transmission – Ensuring robust communication using dual-path transmission.✅ Arduino-Based Control System – Leveraging low-power microcontrollers to manage signal relaying.✅ Error Correction Techniques – Enhancing data integrity through redundancy.✅ Low Power Consumption – Optimizing power efficiency for extended deployments.

System Architecture

🔧 Hardware Components

Arduino Uno – Core microcontroller for processing and communication.

nRF24L01 Radio Module with Passive Amplifier – Wireless communication between buoy nodes.

Custom Energy Production System – Utilizes a pendulum motion to drive a motor for power generation.

** Battery Pack** – Supplemental energy source for continuous operation.

Sensors (Temperature, Humidity, GPS, etc.) – Environmental data collection and real-time monitoring.

📌 The energy system, as detailed in the project reports, leverages mechanical motion from oceanic movements to generate power, ensuring the buoys remain operational in remote locations.

💻 Software Stack

Arduino IDE – Firmware development.

Python & MATLAB – Data analysis and visualization.

Embedded C – Microcontroller programming.

nRF24L01 Radio Communication Library – Wireless data transmission.

SPI & Wire Libraries – Communication with sensors and external components.

DHT Library – Environmental data collection from temperature and humidity sensors.

EEPROM Library – Data logging and storage for backup transmission.

🌐 Network Design

The buoy network operates using a hybrid communication model:

1️⃣ Primary Channel (nRF24L01) – Long-range transmission to the base station.2️⃣ Error Detection & Resend Mechanism – If data loss is detected, retransmission is triggered via an alternate route.

🚀 Features

Reliable Transmission – Radio transmission for long-range reliable connectivity.

Real-Time Data Logging – Sensor data is recorded and transmitted periodically.

Fault Tolerance – Automatic failover mechanism for communication disruptions.

Efficient Power Management – custom-powered system ensures sustainable operation.

📥 Installation & Setup

1️⃣ Clone the Repository

git clone https://github.com/AhmadShah-1/Arduino-Based-Redundant-Transmission-for-Buoy-Networks.git
cd Arduino-Based-Redundant-Transmission-for-Buoy-Networks

2️⃣ Required Libraries

Ensure the following libraries are installed in the Arduino IDE:

DHT.h  # For temperature & humidity sensors
Wire.h  # I2C communication



📊 Data Flow

Sensor data is collected.

Data is transmitted via the primary nRF24L01 channel.

The base station logs and processes the data for further analysis.

🛠 Testing & Results

🔹 Range Tests – The nRF24L01 module achieved communication up to 2 km with a passive amplifier.🔹 Power Consumption – The system operated for 48 hours on a single charge cycle.🔹 Redundancy Efficiency – Data loss was reduced by 80% compared to single-channel transmission.

👥 Contributors

Ahmad Shah – Lead Developer, Software and Electrical Engineer

[Team Members] – Mechanical Engineers, Business Analysts, Market Analysts

🔮 Future Improvements

📌 Improve power efficiency by refining the custom energy production system and optimizing energy storage management.📌 Enhance data transmission stability by fine-tuning the nRF24L01 communication protocol and testing alternative amplification methods.📌 Enhance error correction algorithms.📌 Expand support for additional sensors and real-time alerts.

📝 License

This project is licensed under the MIT License. See LICENSE for details.

🎓 Acknowledgments

Stevens Institute of Technology

Department of Civil, Environmental, and Ocean Engineering

For any inquiries, please contact ahmadsyedshah123@gmail.com.
