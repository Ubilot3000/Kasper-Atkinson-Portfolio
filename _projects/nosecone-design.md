---
layout: project
title: "Nosecone Design and Validation"
subtitle: "It might be over for the motor..."
date: 2026-2-20
image: /assets/images/nosecone-airflow-2.png
starred: true
tags: [CFD, ANSYS Fluent, Thermal Analysis, Wind Tunnel, SolidWorks]
---

### Summary

The motor on the 2026 DBF plane is housed by a 3D printed PLA nosecone. That's a clean aero solution, letting air gradually adjust to the rectangular fuselage shape. The tradeoff is that the motor is now enclosed, which raises an obvious question: does it overheat? Not only could the restricted airflow cause the motor to overheat, but the heat being removed from the motor could flow into the PLA, causing it to melt and break up mid-flight.

Answering that took three steps. First, a CFD simulation in ANSYS Fluent to predict how much air actually flows through the nosecone vents. Second, convective heat transfer calculations to translate that airflow into a steady-state motor temperature. Third, a wind tunnel test to check whether reality agreed. The "agreeing with reality" part was most questionable.

### Nosecone Design

The standard approach for a pusher or tractor motor mount is a flat firewall. It works fine structurally, but aerodynamically you're basically bolting a blunt face onto the front of the plane. Moving the motor cross-mount inside the fuselage and enclosing it in a curved nosecone eliminates that flat interface entirely. The motor clamps directly to the forward bulkhead with four fasteners, and the PLA nosecone wraps around it with a smooth, continuously curved forebody. The only structural part of the nosecone becomes the area immediately behind the motor, which is compressed by the screws. This small area can have very high infill and lets the rest of the nosecone act in a purely aerodynamic capacity.

The center mount has two holes cut into it: the side one routes the motor wires through to the front of the fuselage, and the center one just gives the rear motor shaft room to spin. The nosecone is vented to allow cooling air through the motor housing. Sizing those vents required actually knowing how fast air moves through them at cruise, that's where the simulation came in.

<div class="image-row">
    <img src="{{ site.baseurl }}/assets/images/nosecone-cad-3.png" alt="nosecone-cad-1" class="project-image" style="width:20%">
    <img src="{{ site.baseurl }}/assets/images/nosecone-cad-2.png" alt="nosecone-cad-2" class="project-image" style="width:20%">
    <img src="{{ site.baseurl }}/assets/images/nosecone-crossection.png" alt="nosecone-crosssection" class="project-image" style="width:20%">
</div>

### CFD Simulation

The simulation was run in ANSYS Fluent using a steady Reynolds-Averaged Navier-Stokes formulation with a k-ω turbulence model. The operating condition was the expected cruisespeed for the third and slowest mission, just under 20 m/s. These speeds were expected to be the worst for internal airflow. The freestream velocity at that condition produces the least pressure differential across the vents and thus the lowest internal cooling flow. The simulation predicted an average internal velocity of 8m/s through the motor housing. That number feeds directly into the heat transfer calculation.

The simulation did not take into account the effects of the motor spinning. These would have been twofold, as it would've increased the experienced airspeed along the motor housing; it also would have drawn air in. The calculated airspeed was therefore a highly conservative estimate for typical operation.

<img src="{{ site.baseurl }}\assets\images\nosecone-airflow-2.png" alt="nosecone-cfd" class="project-image" style="width:65%;">

### Thermal Analysis

With the internal velocity from CFD in hand, the steady-state motor temperature can be estimated using standard convective heat transfer. The motor generates heat as resistive loss in its windings. That power is:

$$
P_{loss} = I^2 R_m
$$

where $$I$$ is the motor current draw and $$R_m$$ is the winding resistance. That heat has to go somewhere - in this case, it goes into the airflow passing over the exposed motor area. The convective heat transfer coefficient $$\bar{h}$$ for a cylinder in crossflow follows the correlation:

$$
\bar{h} = \frac{k}{L_m} \left[ 0.3 + \frac{0.62 \, Re^{1/2} Pr^{1/3}}{\left(1 + \left(\frac{0.4}{Pr}\right)^{2/3}\right)^{1/4}} \left(1 + \left(\frac{Re}{2.86 \times 10^5}\right)^{5/8}\right)^{4/5} \right]
$$

where $$Re$$ is the Reynolds number based on the internal flow velocity and motor geometry, and $$Pr$$ is the Prandtl number. Given $$\bar{h}$$, the steady-state motor temperature is just a heat balance between power in and convection out:

$$
T_m = T_\infty + \frac{P_{loss}}{\bar{h} A_m}
$$

Running through this with sea-level air properties and the 1.15 in² exposed motor area, the predicted steady-state temperature came out to 80°F. The PLA glass transition temperature is 140°F. It seems the PLA nosecone is not going to melt into the motor mid-flight.

### Wind Tunnel Validation

<div class="image-wrapper">
    <img src="{{ site.baseurl }}\assets\images\wind-tunnel-nosecone.jpg" alt="nosecone-windtunnel" class="project-image" style="width:100%;">
    <img src="{{ site.baseurl }}\assets\images\nosecone-drag.png" alt="nosecone-windtunnel" class="project-image" style="width:100%;">
</div>

However, predictions are only useful if you check them. Two tests were run on the nosecone assembly in the wind tunnel. The first was a static full-discharge thermal test: motor at full throttle, no airflow, measure the steady-state temperature with an infrared thermometer at the end of the run. The second mounted the nosecone assembly to a load cell to measure aerodynamic drag directly at cruise freestream velocity, with the motor running at maximum RPM.

The thermal test measured a steady-state temperature of 90°F, about 10°F higher than the 80°F prediction. This was a surprise, as the simulation was expected to overpredict steady-state temperature. Still, 90°F gives a factor of safety of 1.15 against the 140°F PLA glass transition temperature. Close enough to be a bit uncomfortable, but it held.

The drag test measured a nosecone drag coefficient of $$C_{D_{nosecone}} = 0.70$$. To translate that to a whole-aircraft drag contribution, the coefficient is scaled by the ratio of nosecone frontal area to wing reference area. The resulting aircraft-level drag contribution was $$C_{D_{DF1}} = 0.0251$$. The drag test was meant to further validate our preliminary aerodynamic anlayses.

$$
C_{D_{DF1}} = C_{D_{nosecone}} \times \frac{A_{nosecone}}{S_w}
$$

### Results

The nosecone worked. The motor stayed cool enough that PLA is a viable housing material, though the 10°F underprediction is a known calibration gap in the simulation. For future iterations, adding more vent area or a slightly larger housing would buy more thermal margin without a meaningful drag penalty. The drag result also confirmed that the curved forebody is doing its job. A flat motor plate at the same frontal area would produce meaningfully higher form drag.
