---
layout: project
title: "Dragonfly-Inspired Microglider"
subtitle: "Dragonfly-inspired, MATLAB-approved..."
date: 2025-8-2
image: assets/images/download.png
tags: [glider, dragonfly, modelling]
---

### Summary
This project began as a way to explore the combination of a quadcopter and fixed-wing aircraft: a dragonfly-inspired microglider. Modelling the system primarily as a tailess, tandem-wing aircraft, I was able to track is logitundal aerodynamics and stability. Imitating dragonflies, I modeled a tiny mass sliding along the fuselage under a basic feedback loop, letting the glider self-correct its attitude. Finally, I ran stability and efficiency sweeps across thousands of design variations to pinpoint the setups that offered the best glide performance while remaining robust to disturbances. The final mathematical model ultimately laid the groundwork for a hardware prototype that marries quadcopter-like maneuvering with fixed-wing-style endurance.

### Aerodynamic Modelling
I first implemented a point-mass ODE model in MATLAB where lift and drag act at a single point and the angle of attack equals the flight-path angle. This let me reproduce classic phugoid oscillations and confirmed my equations were correct. Next, I expanded to a four-state rigid-body model, adding pitch angle and rotational rate so the wings see a non-zero AoA. This let me ultimatelly transition into a tailless, tandem-wing model, where a difference in incidence angles of the two wings theoretically balanced the plane.
<!-- 
$$
\begin{aligned}
\dot V &= -\frac{D}{m} - g\,\sin\gamma, \\\\
\dot \gamma &= \frac{L}{m\,V} - \frac{g\,\cos\gamma}{V}, \\\\
\dot \theta &= q, \\\\
\dot q &= \frac{M_{tot}}{I_{yy}}.
\end{aligned}
$$ 
-->

<img src="{{ site.baseurl }}\assets\images\flight_0.004g_nose.jpg" alt="static-margin" class="project-image" style="width:60%;">

There were some simplifications in my modelling, however. Primarily, I approximated the wings with flat-plate aerodynamics at each wing center. No other components had an aerodynamic effect. The downwash angle, created by the front wing, was also modelled as constant. I then used the parallel-axis theorem for glider's inertia, modelling all individual components as point-masses. The resulting setup allowed me to simulate a semi-realistic model flight. 

### Pitch Control with C.G. Variation

<div class="image-wrapper-large">
  <img src="{{ site.baseurl }}\assets\images\ramp_actuator_fwd&bwd.jpg" alt="ramp-actuator" class="project-image" style="width:100%;">
</div>

The idea was to generate pitching moments on demand without relying on servo-driven control surfaces. Looking at slow-motion draggonfly flight, dragonflies are able to achieve this through pivots in their adbomen, changing their C.G. effectively. 

To find the sweet spot, I swept the center of gravity (CG) by virtually moving a small weight along the fuselage. Each run produced different glide slopes and trim angles, and I kept meticulous notes on how small CG shifts translated to changes in flight behavior. It quickly became apparent that the optimal CG location—about 48 % of the fuselage length—balanced minimal sink rate with enough passive stability to avoid wild oscillations. From this sweet-spot, a mass could be ramped up and down the fuselage to pitch the aircraft.

To emulate this I coded a simple PID controller around the position of a 4g mass, tuning the proportional, integral, and derivative gains through repeated hit-and-miss trial runs. Initially, the controller either oscillated wildly or drove the mass to one extreme, so I introduced position limits and a small rate damper in the loop. By adjusting the integrator windup and testing against step changes in target trim angle, I landed on a configuration that settled to level flight in about ten seconds with just a hint of overshoot. It was fast enough for mid-air corrections while avoiding destabilizing the glider. Although the gains were only effective for small target flight angles, they still proved a powerful example for a more robust, future variant.

### Stability and Dynamic Stability Analyses
With the trimmed model in hand, I linearized the equations about various operating points using finite differences to build the Jacobian. Eigenvalue analysis revealed the short-period mode becoming more oscillatory as the CG moved aft, and the phugoid turning unstable past a critical CG location (~98.8 mm from the nose). I also computed the neutral point via a root-finding approach on the pitching-moment slope, then defined static margin (CG–NP) to assess baseline stability. Finally, I evaluated L/D at the trimmed AoA over airspeeds from 0.1 to 10 m/s and found a peak efficiency of about 17.6 in a narrow design band—highlighting the trade-off between stability and performance.

<img src="{{ site.baseurl }}/assets/images/static_margin_configurations_2.jpg" alt="static-margin" class="project-image" style="width:75%;">

### Design Space Exploration
With insights on passive stability, active control, and aerodynamic performance, I set up a high-dimensional sweep over five variables: CG position, front wing incidence and distance, wing gap and decalage angle. The script cranked through tens of thousands of combinations, automatically discarding any design that failed to trim or fell outside our target static-margin window.

From the list of viable designs, I isolated the top 1% by L/D and plotted them in a parallel-coordinates chart. That visualization revealed clear coupling trends: the best configuration all had a C.G. around 43% of the glider's length, a decalage angle of -2.5$$^\circ$$, and a forward-placed front wing. Conversely, the bottom 1% of designs had decalage angles approaching 0, and chose a C.G. 20% of the fuselage. The comparison of these two extrema showed a simlar final theme: the particular placement of the rear wing did not strongly affect L/D. It also suggested the front-wing incidence was irrelevant; however, I realized this was an issue with the program model. The wings were the only aerodynamic bodies simulated, so in-program the model was effectively flying sideways. These multi-variable patterns highlighted a key list of priorities, defining a "goal" for different designs to aim for if they seek high L/Ds.  

<img src="{{ site.baseurl }}/assets/images/multivar_config_compare_1.jpg" alt="multivar-config" class="project-image" style="width:100%; display:block; margin:auto;">
