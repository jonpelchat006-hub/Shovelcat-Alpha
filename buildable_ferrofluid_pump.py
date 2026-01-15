"""
BUILDABLE FERROFLUID PULSER PUMP PROTOTYPE
==========================================
A practical design for 3D printing + basic electronics

CORE CONCEPT:
    TOP: Electromagnet → High θ (frustration) in water
    BOTTOM: Ferrofluid → Low θ (hexagonal escape)
    GRADIENT: θ_top - θ_bottom = energy to harvest

Author: Jonathan Pelchat
Date: January 2026
"""

# =============================================================================
# BILL OF MATERIALS
# =============================================================================

BILL_OF_MATERIALS = """
╔══════════════════════════════════════════════════════════════════════════╗
║                        BILL OF MATERIALS                                 ║
╠══════════════════════════════════════════════════════════════════════════╣
║                                                                          ║
║  3D PRINTED PARTS (PLA or PETG):                                        ║
║  ────────────────────────────────                                        ║
║  □ Main tube body (2 parts, threaded connection)                        ║
║  □ Top cap with coil holder                                              ║
║  □ Bottom chamber (ferrofluid reservoir)                                ║
║  □ Observation windows (use clear PETG or acrylic inserts)              ║
║  □ Coil bobbin for electromagnet                                         ║
║                                                                          ║
║  ELECTRONICS:                                                            ║
║  ────────────────                                                        ║
║  □ Magnet wire, 22-26 AWG, ~50m                      ~$15               ║
║  □ DC power supply 12-24V, 2-5A                      ~$20               ║
║  □ MOSFET or relay for switching (optional)          ~$5                ║
║  □ Arduino/ESP32 for control (optional)              ~$10               ║
║                                                                          ║
║  FLUIDS:                                                                 ║
║  ────────────────                                                        ║
║  □ Ferrofluid, 50-100mL                              ~$15-30            ║
║    - Amazon: "Ferrofluid magnetic liquid"                               ║
║    - Or make your own (see below)                                       ║
║  □ Distilled water                                   ~$2                ║
║  □ Food coloring (optional, for visibility)          ~$3                ║
║                                                                          ║
║  SEALS & MISC:                                                          ║
║  ────────────────                                                        ║
║  □ O-rings (various sizes for sealing)               ~$5                ║
║  □ Silicone sealant                                  ~$5                ║
║  □ Clear acrylic/polycarbonate tube (optional)       ~$10               ║
║  □ Small neodymium magnets for testing               ~$5                ║
║                                                                          ║
║  TOTAL ESTIMATED COST: $80-120                                          ║
║                                                                          ║
╚══════════════════════════════════════════════════════════════════════════╝
"""

# =============================================================================
# DESIGN SPECIFICATIONS
# =============================================================================

DESIGN_SPECS = """
╔══════════════════════════════════════════════════════════════════════════╗
║                     DESIGN SPECIFICATIONS                                ║
╠══════════════════════════════════════════════════════════════════════════╣
║                                                                          ║
║  DIMENSIONS (Prototype Scale):                                          ║
║  ─────────────────────────────                                          ║
║                                                                          ║
║      Total Height:     300-400 mm (12-16 inches)                        ║
║      Tube Inner Dia:   25-40 mm (1-1.5 inches)                          ║
║      Tube Wall:        3-4 mm                                            ║
║                                                                          ║
║      Top Section:      200-250 mm (water + electromagnet)               ║
║      Bottom Section:   50-100 mm (ferrofluid chamber)                   ║
║      Air Gap:          50 mm (for pulser action)                        ║
║                                                                          ║
║  ELECTROMAGNET (Top):                                                   ║
║  ────────────────────                                                    ║
║      Core:        None (air core) or soft iron bolt                     ║
║      Wire:        22-24 AWG magnet wire                                 ║
║      Turns:       200-500 turns                                          ║
║      Current:     1-3 A                                                  ║
║      Field:       10-50 mT (adjustable via current)                     ║
║                                                                          ║
║      Coil dimensions:                                                    ║
║          Inner dia: 50 mm (fits around tube)                            ║
║          Outer dia: 80-100 mm                                            ║
║          Height:    40-60 mm                                             ║
║                                                                          ║
║  FERROFLUID CHAMBER (Bottom):                                           ║
║  ─────────────────────────────                                          ║
║      Volume:      30-50 mL                                               ║
║      Depth:       20-30 mm                                               ║
║      Note:        Needs clear window to see hexagonal patterns!         ║
║                                                                          ║
║  CRITICAL FIELD FOR ROSENSWEIG:                                         ║
║  ──────────────────────────────                                         ║
║      B_critical ≈ 10-20 mT for typical ferrofluids                      ║
║      Aim for B ≈ 15-25 mT at ferrofluid surface                         ║
║      (Use small permanent magnet OR second coil below)                  ║
║                                                                          ║
╚══════════════════════════════════════════════════════════════════════════╝
"""

# =============================================================================
# ASSEMBLY DIAGRAM (ASCII)
# =============================================================================

ASSEMBLY_DIAGRAM = """
╔══════════════════════════════════════════════════════════════════════════╗
║                        ASSEMBLY DIAGRAM                                  ║
╠══════════════════════════════════════════════════════════════════════════╣

                    CROSS-SECTION VIEW
                    ==================
                    
        ┌─────────────────────────────────────┐
        │         AIR INLET/OUTLET            │  ← Valve or small hole
        │              ○                       │
        ├─────────────────────────────────────┤
        │  ╔═══════════════════════════════╗  │
        │  ║    ELECTROMAGNET COIL         ║  │  ← 200-500 turns
        │  ║  ┌─────────────────────────┐  ║  │     22-24 AWG wire
        │  ║  │                         │  ║  │     
        │  ║  │   ~~~~~~~~~~~~~~~~~~~   │  ║  │  ← Water surface
        │  ║  │   |               |     │  ║  │
        │  ║  │   |    WATER      |     │  ║  │  ← HIGH θ ZONE
        │  ║  │   |   (high θ)    |     │  ║  │     Frustrated!
        │  ║  │   |               |     │  ║  │
        │  ║  │   |               |     │  ║  │
        │  ║  └───┼───────────────┼─────┘  ║  │
        │  ╚═══════════════════════════════╝  │
        │        │               │            │
        │        │   TUBE        │            │  ← Clear section
        │        │   (clear)     │            │     for observation
        │        │               │            │
        │        │       ○       │            │  ← Air bubble zone
        │        │      ○ ○      │            │
        │        │               │            │
        ├────────┼───────────────┼────────────┤
        │  ┌─────┼───────────────┼─────────┐  │
        │  │     │   INTERFACE   │         │  │  ← Water-Ferrofluid
        │  │   ══╪═══════════════╪══       │  │     boundary
        │  │     │               │         │  │
        │  │     │  FERROFLUID   │         │  │  ← LOW θ ZONE
        │  │     │   (low θ)     │         │  │     Hexagonal escape!
        │  │     │               │         │  │
        │  │     │  ⬡ ⬡ ⬡ ⬡ ⬡   │         │  │  ← Rosensweig spikes
        │  │     │   ⬡ ⬡ ⬡ ⬡    │         │  │     (when B applied)
        │  └─────┴───────────────┴─────────┘  │
        │  ╔═══════════════════════════════╗  │
        │  ║   OPTIONAL: Bottom magnet     ║  │  ← Permanent magnet
        │  ║   or second coil for          ║  │     OR second coil
        │  ║   Rosensweig activation       ║  │     (~15-20 mT)
        │  ╚═══════════════════════════════╝  │
        └─────────────────────────────────────┘
        
        
                    TOP VIEW (Coil)
                    ===============
                    
                  ╔═══════════════╗
                ╔═╝               ╚═╗
              ╔═╝    ┌───────┐      ╚═╗
             ║       │       │        ║
             ║       │ TUBE  │        ║  ← Coil wraps around tube
             ║       │       │        ║
              ╚═╗    └───────┘      ╔═╝
                ╚═╗               ╔═╝
                  ╚═══════════════╝

╚══════════════════════════════════════════════════════════════════════════╝
"""

# =============================================================================
# 3D PRINTING GUIDE
# =============================================================================

PRINTING_GUIDE = """
╔══════════════════════════════════════════════════════════════════════════╗
║                     3D PRINTING GUIDE                                    ║
╠══════════════════════════════════════════════════════════════════════════╣
║                                                                          ║
║  RECOMMENDED SETTINGS:                                                  ║
║  ─────────────────────                                                  ║
║      Material:     PETG (water resistant) or PLA                        ║
║      Layer Height: 0.2 mm                                                ║
║      Infill:       20-40% (more for structural parts)                   ║
║      Walls:        3-4 perimeters                                        ║
║      Supports:     Yes, for overhangs                                   ║
║                                                                          ║
║  PART 1: MAIN TUBE (Print in 2 halves, join with threads)              ║
║  ────────────────────────────────────────────────────────               ║
║      - Print vertically for strength                                    ║
║      - Add threaded sections for assembly                               ║
║      - Consider printing with clear PETG for visibility                 ║
║      - OR use clear acrylic tube insert                                 ║
║                                                                          ║
║  PART 2: TOP CAP WITH COIL HOLDER                                       ║
║  ─────────────────────────────────                                      ║
║      - Includes bobbin for winding electromagnet                        ║
║      - Air hole with optional valve fitting                             ║
║      - O-ring groove for seal                                           ║
║                                                                          ║
║  PART 3: BOTTOM FERROFLUID CHAMBER                                      ║
║  ──────────────────────────────────                                     ║
║      - Wider than tube for ferrofluid reservoir                         ║
║      - Flat bottom for observation                                      ║
║      - Clear window cutout (use acrylic insert)                         ║
║      - Optional: pocket for permanent magnet below                      ║
║                                                                          ║
║  PART 4: COIL BOBBIN                                                    ║
║  ─────────────────────                                                  ║
║      - Fits around tube                                                 ║
║      - Flanges to contain wire                                          ║
║      - Slots for wire entry/exit                                        ║
║                                                                          ║
║  WATERPROOFING:                                                         ║
║  ──────────────                                                         ║
║      - Use silicone sealant on all joints                               ║
║      - O-rings at threaded connections                                  ║
║      - Test with plain water first!                                     ║
║                                                                          ║
╚══════════════════════════════════════════════════════════════════════════╝
"""

# =============================================================================
# ELECTROMAGNET WINDING
# =============================================================================

ELECTROMAGNET_GUIDE = """
╔══════════════════════════════════════════════════════════════════════════╗
║                    ELECTROMAGNET WINDING GUIDE                           ║
╠══════════════════════════════════════════════════════════════════════════╣
║                                                                          ║
║  GOAL: Create ~20-50 mT field at the water column                       ║
║                                                                          ║
║  FORMULA:                                                                ║
║  ────────                                                                ║
║      B = μ₀ × N × I / L                                                 ║
║                                                                          ║
║      Where:                                                              ║
║          B = magnetic field (Tesla)                                     ║
║          μ₀ = 4π × 10⁻⁷ (permeability of free space)                   ║
║          N = number of turns                                             ║
║          I = current (Amps)                                              ║
║          L = coil length (meters)                                       ║
║                                                                          ║
║  EXAMPLE CALCULATION:                                                   ║
║  ────────────────────                                                   ║
║      N = 300 turns                                                       ║
║      I = 2 A                                                             ║
║      L = 0.05 m (50 mm coil height)                                     ║
║                                                                          ║
║      B = (4π × 10⁻⁷) × 300 × 2 / 0.05                                  ║
║      B = 0.015 T = 15 mT  ✓                                             ║
║                                                                          ║
║  WINDING INSTRUCTIONS:                                                  ║
║  ─────────────────────                                                  ║
║      1. Print or obtain coil bobbin                                     ║
║      2. Secure wire start with tape                                     ║
║      3. Wind NEATLY in layers (important for field uniformity)          ║
║      4. Count turns as you go                                           ║
║      5. Secure end, leave 30cm leads                                    ║
║      6. Apply thin coat of clear nail polish to secure (optional)       ║
║                                                                          ║
║  WIRE LENGTH NEEDED:                                                    ║
║  ────────────────────                                                   ║
║      Circumference ≈ π × 65mm = 200mm per turn (average)                ║
║      300 turns × 0.2m = 60m of wire                                     ║
║      Add 20% margin = ~75m                                               ║
║                                                                          ║
║  POWER & HEAT:                                                          ║
║  ─────────────                                                          ║
║      Resistance of 60m of 24AWG ≈ 5 ohms                                ║
║      At 2A: Power = I²R = 4 × 5 = 20W                                   ║
║      THE COIL WILL GET WARM! Don't run continuously.                    ║
║      Use duty cycle: 30 sec on, 30 sec off                              ║
║                                                                          ║
╚══════════════════════════════════════════════════════════════════════════╝
"""

# =============================================================================
# FERROFLUID OPTIONS
# =============================================================================

FERROFLUID_OPTIONS = """
╔══════════════════════════════════════════════════════════════════════════╗
║                      FERROFLUID OPTIONS                                  ║
╠══════════════════════════════════════════════════════════════════════════╣
║                                                                          ║
║  OPTION 1: BUY PRE-MADE (Recommended for first build)                   ║
║  ─────────────────────────────────────────────────────                  ║
║      - Amazon: Search "ferrofluid display"                              ║
║      - Typical: 50mL for $15-25                                         ║
║      - Works out of the box                                             ║
║      - Consistent properties                                             ║
║                                                                          ║
║  OPTION 2: MAKE YOUR OWN (Cheaper, educational)                         ║
║  ──────────────────────────────────────────────                         ║
║                                                                          ║
║      INGREDIENTS:                                                        ║
║      - Magnetite powder (Fe₃O₄) - Amazon/eBay, ~$10/100g               ║
║      - Oleic acid (surfactant) - Amazon, ~$10                           ║
║      - Carrier oil (vegetable oil, kerosene, or motor oil)              ║
║                                                                          ║
║      SIMPLE RECIPE:                                                      ║
║      1. Mix 1 part magnetite : 3 parts oleic acid : 10 parts oil        ║
║      2. Grind/mix thoroughly (mortar+pestle or blender)                 ║
║      3. Let settle, decant off larger particles                         ║
║      4. Result is crude ferrofluid                                      ║
║                                                                          ║
║      BETTER RECIPE (finer particles):                                   ║
║      1. Dissolve FeCl₂ + 2×FeCl₃ in water                              ║
║      2. Add ammonia (NH₄OH) to precipitate Fe₃O₄                       ║
║      3. Wash precipitate, add oleic acid                                ║
║      4. Transfer to carrier oil                                          ║
║      (Requires more chemistry knowledge)                                 ║
║                                                                          ║
║  IMPORTANT PROPERTIES:                                                  ║
║  ─────────────────────                                                  ║
║      - Saturation magnetization: 10-50 kA/m                             ║
║      - Critical field for Rosensweig: 10-30 mT                          ║
║      - Viscosity: affects spike formation speed                         ║
║      - Surface tension: affects spike height                            ║
║                                                                          ║
║  SAFETY:                                                                ║
║  ───────                                                                ║
║      - Ferrofluid STAINS everything permanently!                        ║
║      - Work over newspaper/plastic                                       ║
║      - Wear gloves                                                       ║
║      - Keep away from electronics and credit cards                      ║
║                                                                          ║
╚══════════════════════════════════════════════════════════════════════════╝
"""

# =============================================================================
# EXPERIMENT PROCEDURE
# =============================================================================

EXPERIMENT_PROCEDURE = """
╔══════════════════════════════════════════════════════════════════════════╗
║                    EXPERIMENT PROCEDURE                                  ║
╠══════════════════════════════════════════════════════════════════════════╣
║                                                                          ║
║  PHASE 1: BASIC ASSEMBLY & LEAK TEST                                    ║
║  ────────────────────────────────────                                   ║
║      □ Assemble all printed parts (dry)                                 ║
║      □ Check fits, adjust if needed                                     ║
║      □ Apply silicone sealant to joints                                 ║
║      □ Let cure 24 hours                                                 ║
║      □ Fill with water only                                             ║
║      □ Check for leaks over 1 hour                                      ║
║      □ Fix any leaks, retest                                            ║
║                                                                          ║
║  PHASE 2: FERROFLUID TEST (Separate)                                    ║
║  ────────────────────────────────────                                   ║
║      □ Put ferrofluid in shallow dish                                   ║
║      □ Bring magnet underneath                                          ║
║      □ Observe Rosensweig spikes forming                                ║
║      □ Note: this is the HEXAGONAL ESCAPE state!                        ║
║      □ Photograph the hexagonal pattern                                 ║
║      □ Measure critical distance/field for spike onset                  ║
║                                                                          ║
║  PHASE 3: ELECTROMAGNET TEST                                            ║
║  ───────────────────────────────                                        ║
║      □ Connect coil to power supply                                     ║
║      □ Start at LOW current (0.5A)                                      ║
║      □ Test with iron filings or compass                                ║
║      □ Gradually increase current                                       ║
║      □ Note heating - don't exceed safe temperature                     ║
║      □ Map field strength if you have a gaussmeter                      ║
║                                                                          ║
║  PHASE 4: COMBINED SYSTEM                                               ║
║  ─────────────────────────                                              ║
║      □ Add ferrofluid to bottom chamber (30-50 mL)                      ║
║      □ Slowly add water on top (don't mix!)                             ║
║      □ Leave air gap at top                                             ║
║      □ Seal system                                                       ║
║      □ Let settle - ferrofluid should sink to bottom                    ║
║                                                                          ║
║  PHASE 5: ACTIVATION EXPERIMENTS                                        ║
║  ────────────────────────────────                                       ║
║                                                                          ║
║      Experiment A: Top coil only                                        ║
║      ─────────────────────────────                                      ║
║      □ Energize top electromagnet                                       ║
║      □ Observe water behavior                                           ║
║      □ Look for oscillation or movement                                 ║
║      □ Record observations                                              ║
║                                                                          ║
║      Experiment B: Bottom magnet only                                   ║
║      ──────────────────────────────                                     ║
║      □ Place permanent magnet below ferrofluid                          ║
║      □ Observe hexagonal spike formation                                ║
║      □ This is θ → low (hexagonal escape state)                         ║
║                                                                          ║
║      Experiment C: BOTH (The key experiment!)                           ║
║      ─────────────────────────────────────────                          ║
║      □ Activate bottom magnet (hexagonal escape ready)                  ║
║      □ Energize top coil (frustration applied)                          ║
║      □ OBSERVE THE GRADIENT EFFECT                                      ║
║      □ Look for:                                                        ║
║          - Oscillation in water column                                  ║
║          - Interface movement                                           ║
║          - Air bubble behavior                                          ║
║          - Energy transfer to ferrofluid pattern                        ║
║                                                                          ║
║      Experiment D: Varying field strength                               ║
║      ────────────────────────────────────                               ║
║      □ Try different top coil currents                                  ║
║      □ Try different bottom magnet distances                            ║
║      □ Find optimal configuration                                       ║
║      □ Document what creates strongest oscillation                      ║
║                                                                          ║
║  PHASE 6: ENERGY MEASUREMENT (Advanced)                                 ║
║  ──────────────────────────────────────                                 ║
║      □ Add small turbine or paddle to measure flow                      ║
║      □ Connect to small generator or LED                                ║
║      □ Measure output vs input power                                    ║
║      □ Calculate efficiency                                              ║
║                                                                          ║
╚══════════════════════════════════════════════════════════════════════════╝
"""

# =============================================================================
# WHAT TO LOOK FOR
# =============================================================================

OBSERVATIONS = """
╔══════════════════════════════════════════════════════════════════════════╗
║                    WHAT TO LOOK FOR                                      ║
╠══════════════════════════════════════════════════════════════════════════╣
║                                                                          ║
║  SUCCESS INDICATORS:                                                    ║
║  ───────────────────                                                    ║
║                                                                          ║
║  ✓ Ferrofluid forms HEXAGONAL spike pattern when bottom field applied   ║
║      → This is the HEXAGONAL ESCAPE (low θ state)                       ║
║      → The system has found α-equilibrium here                          ║
║                                                                          ║
║  ✓ Water shows oscillation when top field applied                       ║
║      → This is FRUSTRATION (high θ state)                               ║
║      → The water cannot find stable configuration                       ║
║                                                                          ║
║  ✓ Interface between water and ferrofluid moves rhythmically            ║
║      → Energy is transferring across the gradient!                      ║
║      → This is the θ-gradient doing work                                ║
║                                                                          ║
║  ✓ Air bubbles rise/fall in regular pattern                             ║
║      → Classic pulser pump behavior ENHANCED by gradient                ║
║                                                                          ║
║  ✓ Ferrofluid spikes "pulse" in sync with water movement                ║
║      → The two domains are COUPLED                                      ║
║      → Vesica piscis verification happening!                            ║
║                                                                          ║
║  MEASUREMENTS TO RECORD:                                                ║
║  ────────────────────────                                               ║
║      □ Oscillation frequency (Hz)                                       ║
║      □ Amplitude of water movement (mm)                                 ║
║      □ Spike height in ferrofluid (mm)                                  ║
║      □ Current in coil (A)                                              ║
║      □ Time until oscillation starts (s)                                ║
║      □ Duration of sustained oscillation                                ║
║                                                                          ║
║  VARIABLES TO TEST:                                                     ║
║  ──────────────────                                                     ║
║      □ Top field strength (vary current)                                ║
║      □ Bottom field strength (vary magnet distance)                     ║
║      □ Water column height                                              ║
║      □ Ferrofluid amount                                                ║
║      □ Air gap size                                                     ║
║      □ Temperature (cold vs warm)                                       ║
║      □ Orientation (vertical vs tilted)                                 ║
║      □ Orientation relative to magnetic North!                          ║
║                                                                          ║
║  THE KEY PREDICTION TO TEST:                                            ║
║  ───────────────────────────                                            ║
║                                                                          ║
║      Stronger top field (more frustration) should increase:             ║
║          → Oscillation amplitude                                        ║
║          → Energy transfer to ferrofluid                                ║
║          → Overall system activity                                      ║
║                                                                          ║
║      Optimal bottom field (~1.2× critical) should:                      ║
║          → Maximize hexagonal stability                                 ║
║          → Provide best "escape" for the gradient                       ║
║                                                                          ║
║      The GRADIENT (top - bottom) is what matters!                       ║
║                                                                          ║
╚══════════════════════════════════════════════════════════════════════════╝
"""

# =============================================================================
# SAFETY
# =============================================================================

SAFETY = """
╔══════════════════════════════════════════════════════════════════════════╗
║                         SAFETY NOTES                                     ║
╠══════════════════════════════════════════════════════════════════════════╣
║                                                                          ║
║  ELECTRICAL:                                                            ║
║  ───────────                                                            ║
║  ⚠ Never exceed rated current of wire                                   ║
║  ⚠ Coil WILL get hot - don't touch during operation                    ║
║  ⚠ Use duty cycling (30s on, 30s off)                                   ║
║  ⚠ Keep away from water/ferrofluid (shock hazard)                      ║
║  ⚠ Use fuse or current limiter in power supply                         ║
║                                                                          ║
║  FERROFLUID:                                                            ║
║  ───────────                                                            ║
║  ⚠ STAINS permanently - protect surfaces                               ║
║  ⚠ Wear gloves when handling                                           ║
║  ⚠ Don't ingest (iron oxide nanoparticles)                             ║
║  ⚠ Keep away from electronics, credit cards, hard drives               ║
║  ⚠ Store in sealed container away from magnets                         ║
║                                                                          ║
║  MAGNETS:                                                               ║
║  ────────                                                               ║
║  ⚠ Strong neodymium magnets can pinch/crush fingers                    ║
║  ⚠ Keep away from pacemakers and medical devices                       ║
║  ⚠ Can erase magnetic media                                            ║
║                                                                          ║
║  GENERAL:                                                               ║
║  ────────                                                               ║
║  ⚠ Work in ventilated area                                             ║
║  ⚠ Have paper towels ready for spills                                  ║
║  ⚠ Start with LOW power settings, increase gradually                   ║
║                                                                          ║
╚══════════════════════════════════════════════════════════════════════════╝
"""

# =============================================================================
# SIMPLE STL-GENERATION PARAMETERS
# =============================================================================

STL_PARAMETERS = """
╔══════════════════════════════════════════════════════════════════════════╗
║                   OPENSCAD PARAMETERS                                    ║
║              (For generating your own STL files)                         ║
╠══════════════════════════════════════════════════════════════════════════╣

// Main dimensions (mm)
tube_inner_d = 32;
tube_outer_d = 40;
tube_height = 250;

// Bottom chamber
chamber_inner_d = 60;
chamber_outer_d = 70;
chamber_height = 40;

// Coil bobbin
bobbin_inner_d = tube_outer_d + 2;  // Fits over tube
bobbin_outer_d = 90;
bobbin_height = 50;
flange_height = 5;

// Thread parameters (for joining parts)
thread_pitch = 2.5;
thread_depth = 1.5;

// O-ring groove
oring_d = 3;
oring_groove_d = tube_outer_d + oring_d;

// Window cutout (for observation)
window_width = 30;
window_height = 50;

╚══════════════════════════════════════════════════════════════════════════╝
"""

# =============================================================================
# MAIN
# =============================================================================

def print_all_guides():
    """Print all build guides."""
    print(BILL_OF_MATERIALS)
    print(DESIGN_SPECS)
    print(ASSEMBLY_DIAGRAM)
    print(PRINTING_GUIDE)
    print(ELECTROMAGNET_GUIDE)
    print(FERROFLUID_OPTIONS)
    print(EXPERIMENT_PROCEDURE)
    print(OBSERVATIONS)
    print(SAFETY)
    print(STL_PARAMETERS)


if __name__ == "__main__":
    print("=" * 75)
    print("BUILDABLE FERROFLUID PULSER PUMP PROTOTYPE")
    print("Based on Shovelcat Theory - Hexagonal Frustration Gradient")
    print("Author: Jonathan Pelchat")
    print("=" * 75)
    print()
    print("This document contains everything you need to build a prototype.")
    print("See individual sections below for:")
    print("  - Bill of Materials")
    print("  - Design Specifications") 
    print("  - Assembly Diagram")
    print("  - 3D Printing Guide")
    print("  - Electromagnet Winding")
    print("  - Ferrofluid Options")
    print("  - Experiment Procedure")
    print("  - What to Observe")
    print("  - Safety Notes")
    print()
    
    print_all_guides()
