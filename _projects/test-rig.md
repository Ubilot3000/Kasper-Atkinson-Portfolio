---
layout: project
title: "Thrust Testing Rig"
subtitle: "Revolutionizing how we do X"
date: 2025-1-21
image: /assets/images/download.png
tags: [Embedded Systems, C++, IoT]
---

<div class="image-wrapper">
  <img src="{{ site.baseurl }}/assets/images/old_rig.png" alt="old rig" class="project-image">
</div>

### Project Context
The current design of a propeller static thrust testing rig featured an aluminum L-bracket. One end featured an attachment for a motor cross-mount, while the other rested upon an electronic scale. This lever configuration allowed for adequate measurements of max throttle by visibly confirming the scale's readouts. However, little room was available for the inclusion of more precise sensors.  


### Contraint Analysis
- **Modularity:** The system should perform both static and dynamic thrust testing. While static thrust testing would mean a table-mounted setup, a dynamic thrust testing rig could be attached to a car and ran at speed. Wind tunnel access could not be assumed.
- **Data-Aquisition:** The rig should measure and collect data, compiling it in a retrievable format. Later, this data could be displayed and analyzed to learn more about propeller performance. A wired connection for data transfer to a laptop would suffice. 
- **Sensors:** There should be two mandatory sensors: a thrust-testing load cell and throttle reader. If possible, four additional sensors should be added: current sensor, voltage sensor, tachometer, and torque-testing load cells.
- **Orientation** As a safety feature, the propeller plane must be oriented with its normal sideways, so that it can face away from all thrust testing participants. 

### Challenges and Solutions
- **How can throttle be measured or controlled?** There were two possible options of controlling the motor. The standard way involved a radio-controlled reciever, speed controller, transmitter, and manually setting the throttle. Theoretically, the PWM signal wire between the reciever and speed controller could be intercepted by an Adruino. The second alternative was to electrically control the motor from the Arduino, configuring it to interface with the speed controller and send PWM signals.
- **




### Learning Outcomes