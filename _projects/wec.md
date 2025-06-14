---
layout: project
title: "Wave Energy Converter"
subtitle: "Revolutionizing how we do X"
date: 2024-11-15
image: /assets/images/download.png
tags: [Marine Power, Energy Systems]
---

### Project Context
A key aspect of Cornell C-Salt's wave-energy powered desalination plant was the design and implementation of a wave-energy converter (WEC) which could harness the motion of the ocean to push water through a salt-filtrating membrane. The mechanical subteam was tasked with identifying the best type of WEC and method of delivering high-pressure water to the membrane. 


### Contraint Analysis
- **Reliability** Although a pump would be needed to pressurize membrane-bound fluid, it could be run through both mechanical and electrical needs.  
- **Data-Aquisition:** The rig should measure and collect data, compiling it in a retrievable format. Later, this data could be displayed and analyzed to learn more about propeller performance. A wired connection for data transfer to a laptop would suffice. 
- **Sensors:** There should be two mandatory sensors: a thrust-testing load cell and throttle reader. If possible, four additional sensors should be added: current sensor, voltage sensor, tachometer, and torque-testing load cells.
- **Orientation** As a safety feature, the propeller plane must be oriented with its normal sideways, so that it can face away from all thrust testing participants. 

### Challenges and Solutions
- **How can throttle be measured or controlled?** There were two possible options of controlling the motor. The standard way involved a radio-controlled reciever, speed controller, transmitter, and manually setting the throttle. Theoretically, the PWM signal wire between the reciever and speed controller could be intercepted by an Adruino. The second alternative was to electrically control the motor from the Arduino, configuring it to interface with the speed controller and send PWM signals.
- **



### Learning Outcomes