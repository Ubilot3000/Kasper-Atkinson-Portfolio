---
layout: project
title: "Aircraft CFD Studies"
subtitle: "Four questions. Four answers..."
date: 2025-11-13
image: /assets/images/velocityZeroDegrees-2.png
starred: false
tags: [CFD, ANSYS Fluent, RANS, Aerodynamics, OpenVSP]
---

### Summary

For our 2026 Design Build Fly aircraft, the aerodynamic analysis only matters if the numbers are actually trustworthy. A drag polar built on shaky assumptions feeds bad lap times into the scoring model, and a bad scoring model means you optimize for the wrong plane. So before locking in any key parameters, I ran a series of CFD studies in ANSYS Fluent to answer some questions that couldn't be resolved analytically. Four came up. Each one produced a concrete design call.

The studies covered full-aircraft drag and wake characterization, landing gear fairing evaluation, wingtip endplate evaluation, and banner placement validation. Two of the studies led to building something. Two of them told us not to bother.

<div class="image-wrapper-large">
    <img src="{{ site.baseurl }}\assets\images\dragPolarM1.png" alt="drag-polar" class="project-image" style="width:100%;">
</div>

### Full-Aircraft Drag Polar

The drag polar is the foundation of everything downstream - lap time, scoring, sizing decisions. Getting a reliable $$C_{D_0}$$ required two independent methods: OpenVSP for a component-level parasitic drag buildup, and ANSYS Fluent for a full-aircraft simulation to cross-check it.

The CFD used a steady RANS formulation with a k-ω turbulence model. I ran simulations at several low angles of attack near cruise, extracted the lift and drag coefficients from each, and fit them to a parabolic polar:

$$
C_D = C_{D_0} + \frac{C_L^2}{\pi e AR}
$$

where $$e$$ is the Oswald efficiency factor and $$AR$$ is the wing aspect ratio. The fit gave $$C_{D_0} = 0.059$$, which matched the OpenVSP estimate closely. When two methods with completely different assumptions agree, that's about as much confidence as you can get without a wind tunnel.

With $$C_{D_0}$$ settled, I generated mission-specific drag polars for M1, M2, and M3. M1 and M2 came out nearly identical given how similar the aircraft configurations are. M3 adds banner drag on top, handled separately through the method described in the banner placement section.

### Landing Gear Fairings

The question was whether landing gear fairings reduced drag enough to justify the weight and build complexity. Not a lot of upfront intuition either way (we had never used them as a team), so I ran it.

The gear was modeled in Fluent at cruise, with and without fairings. Main gear drag dropped from 0.38 lbf to 0.37 lbf. That's a 2.6% reduction. Basically nothing. Lift jumped from 0.08 lbf to 0.27 lbf, a 238% increase, which looks good until you look at the fairing mass. The fairing design came in at a weight equivalent to 0.44 lbf of additional lift requirement, which nearly offset the benefit entirely. We decided fairings would not be for us.

<div class="image-row">
    <img src="{{ site.baseurl }}/assets/images/vectors-no-fairing.png" alt="nosecone-cad-1" class="project-image" style="width:20%">
    <img src="{{ site.baseurl }}/assets/images/vectors-fairing.png" alt="nosecone-cad-2" class="project-image" style="width:20%">
</div>

### Wingtip Endplates

Endplates reduce induced drag by raising the effective aspect ratio of the wing. The theory is solid, you see them on commercial jets, on Formula 1 cars, on everything where span efficiency matters. The question for a low-Reynolds-number competition aircraft is whether that benefit outweighs the manufacturing difficulties.

I evaluated three geometries: bare tip, a stadium-profile endplate, and an airfoil-profile endplate. The pressure contours from each run are shown below. The stadium and airfoil endplates did reduce the spanwise pressure gradient at the tip, but the effect on total drag was small at our operating $$C_L$$. The gain in effective span didn't offset the added complexity. No endplates. Knowing what not to build saves just as much time as knowing what to build.

<img src="{{ site.baseurl }}\assets\images\endplate_contours.jpeg" alt="endplate-cfd" class="project-image" style="width:100%;">

### Banner Wake Placement

This one was less about drag and more about whether Mission 3 would even work. The banner is towed on a rope below the tail. If the tow point sits inside the turbulent wake, the banner sees unsteady loading, deployment becomes unpredictable, and release gets messy. I reused the full-aircraft CFD model with the k-ω SST formulation. Turbulent regions were identified using an isosurface of turbulence kinetic energy at 5% of the freestream mean kinetic energy, which is a standard threshold for wake extent identification. I also extracted longitudinal midplane velocity contours to look at the full wake structure.

$$
k_{threshold} = 0.05 \times \frac{1}{2} U_\infty^2
$$

The result was reassuring. The turbulent region dissipates quickly downstream of the empennage and doesn't extend significantly below the fuselage centerline. There's a velocity deficit behind the aircraft - visible in the contours - but the elevated turbulence is gone well before the tow point. The banner hangs in comparatively uniform flow. Placement confirmed.

<img src="{{ site.baseurl }}\assets\images\velocityZeroDegrees-2.png" alt="wake-cfd" class="project-image" style="width:75%;">

### Takeaways

Each of these studies was scoped to answer one question with a yes or no. That constraint is what makes CFD useful on a student competition timeline; not running it to explore, but running it to decide. The drag polar anchored the scoring model. The fairing and endplate studies removed two items from the build list. The wake analysis cleared the banner configuration before the release mechanism was ever designed. Four decisions made before we touched a piece of balsa.