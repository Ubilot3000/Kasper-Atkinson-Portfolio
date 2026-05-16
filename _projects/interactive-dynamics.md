---
layout: project
title: "Interactive Flight Dynamics Tool"
subtitle: "Breaking planes on purpose, so we know how to fix them..."
date: 2026-5-1
image: /assets/images/design-concept-plane.png
starred: false
tags: [MATLAB, AVL, Flight Dynamics, Stability Analysis, Teaching]
---

### Summary

At the end of the 2025-26 DBF season, I built an interactive simulation tool for newer team members to use over the summer. The goal was to give people a way to build real intuition for aircraft stability before the next design cycle, without sitting through a lecture. Most people come in knowing XFLR5 but not really understanding why the outputs matter. This was built to close that gap.

The tool is a MATLAB Live Script backed by AVL (MIT's Athena Vortex Lattice solver), with sliders to control the aircraft geometry and a full set of outputs that update together: mass layout, aerodynamic performance, static stability indicators, dynamic mode analysis, and a scoring estimate. After working through the interactive section, students move into three guided scenario exercises, each featuring a broken aircraft with one or two design flaws to diagnose and fix.

### Geometry and Mass Layout

The first thing the tool shows you after you set the geometry is where everything actually sits on the aircraft. This matters more than most people expect. Every slider change adjusts not just the aerodynamic surfaces but the mass distribution too. A bigger wing is a heavier wing. A longer tail arm moves the tail spar further aft. The CG moves as a consequence of all of it.

<img src="{{ site.baseurl }}\assets\images\massDistribution.png" alt="mass-layout" class="project-image" style="width:75%;">

The side and top view plots show each component as a point mass, with the CG marked in red. For the 2026 competition aircraft, this lands at 13.8% MAC with a total mass of 3.552 kg, with the motor and battery cluster pulled well forward of the wing leading edge. The side view also shows the horizontal tail incidence angle, which at 1° downward is the trim correction baked into the geometry.

<div class="image-wrapper-large" style="width: 35%">
    <img src="{{ site.baseurl }}\assets\images\drag-curve-learn.png" alt="drag-thrust-climb" class="project-image" style="width:100%;">
    <img src="{{ site.baseurl }}\assets\images\roc.png" alt="takeoff-climb" class="project-image" style="width:100%;">
</div>

### Aerodynamic Performance

With the geometry defined, the tool computes the full aerodynamic picture. The drag decomposition breaks total drag into its profile and induced components as a function of velocity, which immediately shows the classic crossover: induced drag dominates at low speed and falls as $$1/V^2$$, while profile drag climbs with $$V^2$$. Minimum drag sits at the crossover point.

The thrust vs drag plot overlays the propeller's available thrust at a given throttle setting onto the drag curve. Where they intersect is the equilibrium cruise speed. For the competition aircraft at 55% throttle, that equilibrium is 21.6 m/s. The tool also estimates takeoff ground roll and climb performance directly. Ground roll comes out to 17.4 m, well within the 60 m competition runway. Best climb rate is 14.54 m/s at 21.3 m/s, which is healthy. A plane that can't climb in the first straightaway after takeoff is a problem before it becomes a stability problem.

### Static Stability

Before getting to the dynamic modes, the tool shows two quick static indicators. The static margin tells you how far the CG sits ahead of the neutral point, expressed as a fraction of mean chord:

$$
SM = \frac{x_{NP} - x_{CG}}{\bar{c}} \times 100\%
$$

For a DBF aircraft, 10 to 25% MAC is the target. Below 5% and the plane becomes twitchy and sensitive to any pitch disturbance. Above 30% and the elevator starts losing the fight against the tail on takeoff rotation. The gauge below makes it immediately clear where you are.

The competition aircraft sits at 23.8% MAC, comfortably in the green. The elevator schematic shows the corresponding trim deflection: 2.6° at cruise, well within the comfortable range. The color bands radiate from the hinge point so you can see at a glance how much of the available travel is being used up just to hold level flight.

<div class="image-row" style="width: 70%; margin-left: auto; margin-right: auto;">
    <img src="{{ site.baseurl }}/assets/images/static-margin-learn.png" alt="static-margin" class="project-image">
    <img src="{{ site.baseurl }}/assets/images/elevator-trim.png" alt="elevator-trim" class="project-image">
</div>



### Dynamic Stability

<div class="image-wrapper-large">
    <img src="{{ site.baseurl }}\assets\images\eigenValuePlot.png" alt="root-locus" class="project-image" style="width:85%;">
    <img src="{{ site.baseurl }}\assets\images\doubling-times.png" alt="doubling-time" class="project-image" style="width:85%;">
</div>

The static margin tells you whether the plane wants to return to level flight after a disturbance. The dynamic modes tell you how it actually gets there. To compute them, I built the linearized state matrices from AVL's aerodynamic derivatives following a rigid-body flight dynamics formulation. Small perturbations from trim allow the full 6-DOF equations of motion to decouple into two independent systems. The longitudinal matrix governs pitch behavior:

$$
A_{lon} = \begin{bmatrix}
X_u & X_\alpha & 0 & -g \\
Z_u/V & Z_\alpha/V & 1 + Z_q/V & 0 \\
0 & M_\alpha & M_q & 0 \\
0 & 0 & 1 & 0
\end{bmatrix}
$$

The eigenvalues of $$A_{lon}$$ and the equivalent lateral matrix give five natural modes. Anything with a negative real part is stable. Anything with a positive real part grows over time.

Using the example of our competition aircraft, our stabilities are imperfect. The short period mode is stable and well-damped, sitting deep in the left half plane. The phugoid, however, is in the right half plane. That means the slow porpoising oscillation the aircraft makes when speed is disturbed will grow rather than decay on its own. This is actually common in lightly loaded competition aircraft where the phugoid damping depends heavily on the drag-to-lift ratio. Mitch knows to manage it with light throttle corrections, and it doesn't affect handling in any meaningful way during a scored run. But it shows up, and the tool shows it.

On the lateral side, Dutch roll and roll subsidence are stable. The spiral mode is barely positive, sitting just right of the origin. That means the aircraft will very slowly tighten a banked turn if left alone. For that mode specifically, what matters is how slowly. The doubling time plot answers that directly.

Spiral divergence at 11.0 seconds is in the green band. Under 3 seconds would be a real problem. Under 8 is uncomfortable. At 11, you have time to notice and correct it before anything dramatic happens. The color-coded thresholds in the chart make that judgment immediate without having to look up what the numbers mean.

### Scoring Output

The final output ties everything back to what actually matters in the competition: the score. Mission lap times feed from the aerodynamic analysis, and the scoring model computes individual and total scores.

The score breakdown for the competition aircraft shows M3 dominating at 2.554 out of a total of 4.736. GM contributes 0.160, which reflects the team's loading time in the mission model. M1 and M2 come in near 1.0 each. This output is the reason the tool connects geometry sliders to a score rather than just to aerodynamic outputs. When someone asks why we sized the wing the way we did, the answer isn't an eigenvalue. It's a bar on that chart.

<img src="{{ site.baseurl }}\assets\images\mission-scoring.png" alt="score-breakdown" class="project-image" style="width:50%;">

### Scenarios and Challenges

After the interactive section, the tool moves into three guided scenarios. Each one presents a complete aircraft with one or two design parameters quietly set to bad values. The simulation outputs show something wrong. The written scenario describes what the pilot sees. The goal is to connect those two descriptions and identify the specific geometric cause.

Scenario 1 features a negatively dihedralled wing. The plane lifts off, then immediately begins rolling and yawing into an increasingly tight turn. The Dutch roll mode or spiral is the primary suspect, and negative dihedral directly degrades the roll stability derivative $$C_{l_\beta}$$ that keeps those modes damped.

Scenario 2 is a taildragger that won't rotate. The CG is set very far forward, giving an enormous static margin. On paper that sounds stable. In practice the elevator can't generate enough pitching moment to unstick the tail from the runway. The plane accelerates and stays flat.

Scenario 3 has a CG sitting at 30% chord with heavy cargo pushing it aft. The pilot is pulling the stick hard to rotate, struggles to climb, and when he lets go the nose pitches down immediately. Letting go and getting an immediate pitch divergence is the phugoid going unstable, and at near-zero static margin the phugoid damping collapses entirely.

Following the scenarios are three open-ended design challenges: smallest possible empennage while keeping all modes stable, fastest possible equilibrium cruise speed with a flyable aircraft, and longest nose-to-tail fuselage while maintaining stability. These don't have answer keys. The point is to develop enough feel for the outputs that you can predict what the root locus will do before you drag the slider.
