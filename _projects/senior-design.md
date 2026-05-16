---
layout: project
title: "Morphing Camber Wing"
subtitle: "Morphing into an engineer..."
date: 2026-5-1
image: /assets/images/final-form-1.jpg
starred: true
tags: [Aerodynamics, XFOIL, Python, Compliant Mechanisms, Prototyping]
---

### Summary

For my MAE 4291 senior design, I designed and built a morphing trailing-edge mechanism for RC-scale fixed-wing aircraft. It replaces a conventional hinged control surface with a continuously deforming rib structure that shifts wing camber while keeping all actuation hardware inside the airfoil profile. No exposed hinge gaps, no external hardware. Just a wing that bends.

The question going in was whether a fully enclosed morphing mechanism is actually practical at RC scale, or whether the complexity kills it. After 13 prototyping iterations across the spring semester and a lot of material testing, the answer is mostly yes. The mechanism fits within the airfoil envelope, hits its deflection and response targets, and survives repeated actuation without failure. What's left is a materials problem, not a design one.

<div class="image-wrapper-large">
    <img src="{{ site.baseurl }}\assets\images\airfoil-sketch.png" alt="design-sketch" class="project-image" style="width:100%;">
</div>


### Why Morphing

Wing warping is how the Wright Brothers controlled their aircraft. A system of cables twisted the wingtips in opposite directions to roll without any discrete surface breaking up the flow. Wings got stiffer over time and ailerons won because they were simpler. The aerodynamic case for continuous surfaces was just parked, not discarded.

Modern small drones are a real opportunity to revisit this. They're light enough that a compliant mechanism is structurally feasible, and the aerodynamic payoff is meaningful. Hinge gaps on conventional control surfaces trip boundary layer transition and add parasitic drag. A morphing surface eliminates that. More usefully, continuous camber control across the span allows washout (reducing incidence toward the wingtip to delay tip stall) and tunable lift distribution in cruise. On a power-constrained drone, these are not small gains.

The specific target was trailing-edge morphing: deflecting the rear 20-30% of the chord up and down like a flap, but with no exposed gap and no discontinuity in the outer surface.

### Aerodynamic Analysis

Airfoil selection started with one hard constraint: positive camber. A symmetric profile would put a constant downward bias on the actuator just to hold level flight, eating into the deflection budget before any maneuvering happens. The USA-35B was the natural pick from the DBF team's existing library. Its flat lower surface simplified the gap-sealing geometry and gave clean pushrod attachment points along the bottom skin.

<img src="{{ site.baseurl }}\assets\images\CP-curves-1.png" alt="coefficient pressure curves" class="project-image" style="width:95%;">

To characterize aerodynamic behavior across deflection angles, I built an XFOIL analysis pipeline in Python. The tricky part was that XFOIL's geometry deformation commands require direct stdin scripting via subprocess. The pipeline splits into two subprocess calls: the first modifies the geometry and runs Gaussian smoothing on the hinge kink before analysis, and the second runs the viscous solver across the angle of attack sweep. Three-layer outlier protection filters non-converged polar points before anything downstream sees the data.

The result is the pressure coefficient distribution above, swept from -30° to +30° deflection at 2° increments. The suction peak near the leading edge grows with positive deflection as camber increases, and the pressure recovery over the aft section shifts with it. This data feeds directly into the torque model.

### Torque Model

Knowing the pressure distribution lets you compute the aerodynamic load resisting deflection. Combined with the structural bending stiffness of the rib, the total restoring moment at the hinge is:

$$
M_{total} = \frac{EI}{L_{flex}} \cdot \delta \; + \; q_\infty \cdot b \cdot c^2 \int_{x_h/c}^{1} \Delta C_p(\xi) \left(\xi - \frac{x_h}{c}\right) d\xi
$$

The first term is the rib's Euler-Bernoulli bending resistance: flexural rigidity $$EI$$ over the flex zone length $$L_{flex}$$, scaled by deflection $$\delta$$. The second is the aerodynamic restoring moment: dynamic pressure times rib thickness $$b$$ times the integral of the pressure differential $$\Delta C_p = C_{p,lower} - C_{p,upper}$$ weighted by moment arm from the hinge location $$x_h$$.

This model set the servo torque requirement before any physical hardware was built. It has known gaps: the skin tension restoring moment (roughly 10-30% of total load) is missing, viscous corrections to the thin airfoil theory overpredict the aerodynamic term by 15-30%, and geometric nonlinearity corrections become meaningful past about 10° deflection. I flagged these in the report rather than tuning around them. They're also the reason wind tunnel validation is the obvious next step.

### Design and Iteration

The initial concept had the servo in the thick forward section, an aluminum pushrod running aft to the trailing edge, and a compliant trailing section that deflects with it. Three problems showed up immediately in the first physical iteration. The lower surface gap was large enough to need a lot of skin material to cover it. The deflection targets were bigger than the servo budget could support. And the pushrod running slightly out of the rib plane produced out-of-plane trailing edge motion alongside the intended vertical deflection.

The hinge was its own sub-problem. A PLA flex zone creases under repeated deflection rather than distributing the bend. TPU would likely fix this, but material lead times made direct testing impractical. A rubber transition region distributed curvature well at short lengths but went too floppy by the time it reached the trailing edge. A hardened paper hinge bonded at the rigid-to-compliant interface resolved it: stiff enough to resist lateral play, flexible enough to survive the full deflection range without fatigue failure.

Those three problems drove the next twelve iterations. The milestones that actually changed the design:

| Iteration | Investigation | Conclusion |
|---|---|---|
| 4 | Top surface thickness | 1.5 mm PLA holds the trailing edge without excessive deflection resistance |
| 5 | Control surface chord | 20-30% chord morphing region hits deflection targets while staying compact |
| 6 | Pushrod pin position | Moving the pin to the lower surface increases the moment arm and deflection range |
| 9 | Rib thickness | 8 mm rib with 4 mm pushrod holder eliminates out-of-plane deflection |
| 11 | Rubber hinge feasibility | 12 mm rubber transition distributes curvature but gets too compliant reaching the trailing edge |
| 12 | Bottom surface material | Pre-tensioned latex covers the gap, but demands a high-torque servo |
| 13 | Segment prototype | Comb cutouts enable consistent span-wise assembly across three ribs |

<img src="{{ site.baseurl }}\assets\images\mk-12.jpg" alt="iteration-12" class="project-image" style="width:75%;">

Skin material took a similar path. TPU film at 85A exceeded the servo torque limit. A 1/16" rubber strip did too. 0.25 mm 40A natural rubber latex landed at approximately 11 N·cm, which a 5 kg·cm servo can drive. That upgrade from the previous servo was the last change before the final prototype.

### Prototype and Results

<div class="image-row">
  <img src="{{ site.baseurl }}\assets\images\final-form-1.jpg" alt="prototype-side" class="project-image" style="width:48%;">
  <img src="{{ site.baseurl }}\assets\images\final-form-2.jpg" alt="prototype-bottom" class="project-image" style="width:48%;">
</div>

The final prototype used the full 240 mm chord and 300 mm span with three PLA ribs spaced 100 mm apart. All five design objectives were met. Measured deflections reached ±30°, the full 60° range traversed in under 1 second, and the actuation mechanism stayed entirely inside the airfoil profile throughout. A single continuous skin covered the outer surface with no exposed gaps.

Fatigue testing ran the servo through the full deflection range for 30 minutes continuously via an Arduino-controlled actuation loop. No cracks, creases, or joint failures. The latex loosened slightly in the first few cycles as it settled, which actually reduced actuation resistance. It stayed taut and aerodynamically clean at full downward deflection.

The primary limitation is a visible kink at the paper hinge on the upper surface. Deflection concentrated at the hinge interface rather than distributing smoothly across the transition region, producing a geometric discontinuity in the top surface profile. This increases drag above what the XFOIL analysis predicted for the smoothed geometry. Quantifying that penalty needs a wind tunnel.

The prevailing assumption going into this project was that a fully enclosed morphing mechanism at RC scale would be too complex to be practical. The prototype is a reasonable challenge to that. The integration problem is solved. What separates the current prototype from a flight-ready implementation is two material questions: a lower-durometer rubber for the skin and a more fatigue-resistant flex material at the hinge transition. TPU for the flex zone is the most immediate candidate. Those two swaps exist. They just weren't testable within this project's timeline.