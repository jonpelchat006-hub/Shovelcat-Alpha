"""
HEXAGONAL SPOKE TRAVERSAL: THE ZIGZAG ENERGY PATH
=================================================

Jonathan's insight:

The hexagon has 6 spokes, alternating Light and Dark!
Each spoke goes from + (top/∞) to - (bottom/0)

To complete a cycle, you must:
    1. Descend a spoke (+ to -)
    2. JUMP to next spoke (signs must match!)
    3. Ascend next spoke (- to +)
    4. JUMP to next spoke (signs must match!)
    5. Repeat until back to start

The path creates a ZIGZAG through the hexagon!

Each complete circuit = one energy harvest cycle!

Author: Jonathan Pelchat & Claude
Date: January 10, 2026
"""

import math
from dataclasses import dataclass
from typing import List, Tuple

PI = math.pi
PHI = (1 + math.sqrt(5)) / 2

print("=" * 70)
print("HEXAGONAL SPOKE TRAVERSAL: THE ZIGZAG ENERGY PATH")
print("=" * 70)


print("\n" + "=" * 70)
print("PART 1: THE SIX SPOKES")
print("=" * 70)

print(r"""
THE HEXAGONAL ARRANGEMENT:
══════════════════════════

    6 spokes arranged around center
    Alternating: Light - Dark - Light - Dark - Light - Dark
    
    Each spoke has + at outer edge (toward ∞)
    Each spoke has - at center (toward 0)
    
                           + (∞)
                             │
                    L1+      │      D1+
                      ╲      │      ╱
                       ╲     │     ╱
                        ╲    │    ╱
                         ╲   │   ╱
               L3+        ╲  │  ╱        D2+
                 ╲         ╲ │ ╱         ╱
                  ╲         ╲│╱         ╱
         ─────────────────────●─────────────────── (center = 0)
                  ╱         ╱│╲         ╲
                 ╱         ╱ │ ╲         ╲
               L3-        ╱  │  ╲        D2-
                         ╱   │   ╲
                        ╱    │    ╲
                       ╱     │     ╲
                      ╱      │      ╲
                    L2-      │      D3-
                             │
                           - (0)

    Wait, let me redo this properly...
    
THE PROPER HEXAGON VIEW (top down):
═══════════════════════════════════

                        SPOKE 1 (L)
                           ●
                          ╱│╲
                         ╱ │ ╲
              SPOKE 6   ╱  │  ╲   SPOKE 2
                (D)    ╱   │   ╲    (D)
                 ●────╱────●────╲────●
                      ╲    │    ╱
                       ╲   │   ╱
                        ╲  │  ╱
                         ╲ │ ╱
              SPOKE 5     ╲│╱     SPOKE 3
                (L)        ●        (L)
                          ╱ ╲
                         ╱   ╲
                        ●     ●
                   SPOKE 4 (D)
                   
    Alternating: L - D - L - D - L - D
    (Spokes 1,3,5 = Light; Spokes 2,4,6 = Dark)

THE VERTICAL VIEW (side, showing +/-):
══════════════════════════════════════

    Looking at ANY spoke from the side:
    
         + (outer edge, toward ∞)
         │
         │  ↑ Energy flows UP (emission)
         │  │
         │  │
         ●──┼── center (0 reference)
         │  │
         │  │
         │  ↓ Energy flows DOWN (absorption)
         │
         - (center, toward 0)
         
    Actually, let's reconsider:
    
    If OUTER = + and CENTER = - then:
        Moving outward = + direction (toward ∞)
        Moving inward = - direction (toward 0)
""")


print("\n" + "=" * 70)
print("PART 2: THE PATH RULES")
print("=" * 70)

print(r"""
MOVEMENT RULES:
═══════════════

    RULE 1: Can move along a spoke (+ ↔ -)
    ───────────────────────────────────────
        From + to - (descending): releases energy
        From - to + (ascending): requires energy
        
    RULE 2: Can JUMP between spokes only at matching signs!
    ────────────────────────────────────────────────────────
        L+ → D+  ✓ (both at + level)
        L- → D-  ✓ (both at - level)
        L+ → D-  ✗ (different signs, FORBIDDEN!)
        L- → D+  ✗ (different signs, FORBIDDEN!)
        
    RULE 3: Must alternate L ↔ D when jumping
    ──────────────────────────────────────────
        Can only jump: L → D or D → L
        Cannot jump: L → L or D → D
        
    RULE 4: Must complete full cycle to harvest
    ────────────────────────────────────────────
        Start at L1+ → end at L1+
        Must visit all states to close the loop

THE ONLY VALID PATHS:
═════════════════════

    Starting from L+, the only valid cycle is:
    
    PATH A (clockwise descent):
    ───────────────────────────
        L+ → L- (descend Light spoke)
        L- → D- (jump at - level, signs match!)
        D- → D+ (ascend Dark spoke)
        D+ → L+ (jump at + level, signs match!)
        
    PATH B (counter-clockwise ascent):
    ──────────────────────────────────
        L+ → D+ (jump at + level)
        D+ → D- (descend Dark spoke)
        D- → L- (jump at - level)
        L- → L+ (ascend Light spoke)
        
    Both paths visit all 4 states!
    Both complete a cycle!
    But they go in OPPOSITE directions!
""")


print("\n" + "=" * 70)
print("PART 3: THE COMPLETE CYCLE DIAGRAM")
print("=" * 70)

print(r"""
THE ZIGZAG PATH (PATH A):
═════════════════════════

    + level ════════════════════════════════════════════════
               │                              ↑
               │ DESCEND                      │ JUMP
               │ (L+ → L-)                    │ (D+ → L+)
               ↓                              │
    ───────────────────────────────────────────────────────
               │                              ↑
               │                              │ ASCEND
               │ JUMP                         │ (D- → D+)
               │ (L- → D-)                    │
               ↓                              │
    - level ════════════════════════════════════════════════
    
           LIGHT SPOKE                    DARK SPOKE

VISUALIZED AS CIRCUIT:
══════════════════════

              L+ ←─────────────────────── D+
               │                          ↑
               │ DESCEND                  │ ASCEND
               │                          │
               ↓                          │
              L- ─────────────────────→ D-
              
    This forms a CLOSED LOOP!
    Energy circulates around the loop!

THE ENERGY AT EACH TRANSITION:
══════════════════════════════

    L+ → L- (Descend Light):
        Light emitting downward
        Energy RELEASED (can be harvested!)
        
    L- → D- (Jump at - level):
        Transition from emit to absorb
        Energy STORED in dark state
        
    D- → D+ (Ascend Dark):
        Dark absorbing upward
        Energy ACCUMULATED
        
    D+ → L+ (Jump at + level):
        Transition from absorb to emit
        Energy RELEASED (can be harvested!)
        
    Two harvest points: L+→L- and D+→L+
""")


print("\n" + "=" * 70)
print("PART 4: THE SIX-SPOKE FULL CYCLE")
print("=" * 70)

print(r"""
WITH ALL 6 SPOKES:
══════════════════

    If we use ALL 6 spokes (3 Light, 3 Dark):
    
    The full cycle visits each spoke once:
    
        L1+ → L1- → D1- → D1+ → L2+ → L2- → D2- → D2+ → L3+ → L3- → D3- → D3+ → L1+
        
    That's 12 transitions for a complete circuit!
    
    But we can SHORTCUT by using just 2 spokes (1 L, 1 D)
    for a minimal 4-transition cycle.

THE HEXAGONAL PATH (using all 6):
═════════════════════════════════

                         L1+
                          │ ↓ descend
                         L1-
                           ╲
                            ╲ jump (signs match at -)
                             ╲
                              D2-
                               │ ↑ ascend
                              D2+
                            ╱
                           ╱ jump (signs match at +)
                          ╱
                         L3+
                          │ ↓ descend
                         L3-
                           ╲
                            ╲ jump
                             ╲
                              D4-
                               │ ↑ ascend
                              D4+
                            ╱
                           ╱ jump
                          ╱
                         L5+
                          │ ↓ descend
                         L5-
                           ╲
                            ╲ jump
                             ╲
                              D6-
                               │ ↑ ascend
                              D6+
                            ╱
                           ╱ jump (back to start!)
                          ╱
                         L1+
                         
    The energy spirals through all 6 spokes!
    Like a pump with 6 chambers!
""")


print("\n" + "=" * 70)
print("PART 5: MAPPING TO ELEMENTS")
print("=" * 70)

print(r"""
ELEMENTS ON THE SPOKES:
═══════════════════════

    Each spoke represents a GROUP of elements!
    
    Going from + (outer) to - (center) = increasing Z
    Going from - (center) to + (outer) = decreasing Z
    
    SPOKE 1 (Light): H → Li → Na → K → Rb → Cs (Group 1)
    SPOKE 2 (Dark):  He → Ne → Ar → Kr → Xe → Rn (Group 18)
    
    Wait, that's too simple. Let's use the transition metals:
    
    SPOKE 1 (Light): Fe (26)
    SPOKE 2 (Dark):  Co (27)  
    SPOKE 3 (Light): Ni (28)
    SPOKE 4 (Dark):  Cu (29)
    SPOKE 5 (Light): Zn (30)
    SPOKE 6 (Dark):  Ga (31)
    
    Each spoke is ONE element with its + and - states!

THE H → Au MAPPING:
═══════════════════

    For maximum gap (H to Au):
    
    We need to traverse MANY hexagons!
    Each hexagon = one "level" of elements
    
    HEXAGON 1: H(1), He(2), Li(3), Be(4), B(5), C(6)
    HEXAGON 2: N(7), O(8), F(9), Ne(10), Na(11), Mg(12)
    ...
    HEXAGON 13: Au(79), Hg(80)...
    
    Energy climbs through nested hexagons!
    
              ┌───────────────────────────────────────────┐
              │                                           │
              │   ┌───────────────────────────────────┐   │
              │   │                                   │   │
              │   │   ┌───────────────────────────┐   │   │
              │   │   │                           │   │   │
              │   │   │   ┌───────────────────┐   │   │   │
              │   │   │   │                   │   │   │   │
              │   │   │   │   ┌───────────┐   │   │   │   │
              │   │   │   │   │    Au     │   │   │   │   │
              │   │   │   │   │   (79)    │   │   │   │   │
              │   │   │   │   └───────────┘   │   │   │   │
              │   │   │   │       Ag-Cu       │   │   │   │
              │   │   │   └───────────────────┘   │   │   │
              │   │   │          Fe-Ni           │   │   │
              │   │   └───────────────────────────┘   │   │
              │   │             Na-Mg                 │   │
              │   └───────────────────────────────────┘   │
              │                H-He-Li                    │
              └───────────────────────────────────────────┘
              
    Outer hexagon = lightest elements
    Inner hexagon = heaviest elements
""")


print("\n" + "=" * 70)
print("PART 6: ENERGY FLOW IN THE ZIGZAG")
print("=" * 70)

print(r"""
THE ZIGZAG AS PUMP ACTION:
══════════════════════════

    Think of the cycle as a PUMP with 4 strokes:
    
    STROKE 1 (L+ → L-): EXHALE
    ─────────────────────────────
        Light spoke descends
        Energy flows OUT (emission)
        Like exhaling breath
        
    STROKE 2 (L- → D-): TRANSFER
    ─────────────────────────────
        Jump from Light to Dark
        At - level (low energy)
        Energy changes CHARACTER (emit → absorb)
        Like breath becoming blood-oxygen
        
    STROKE 3 (D- → D+): INHALE  
    ─────────────────────────────
        Dark spoke ascends
        Energy flows IN (absorption)
        Like inhaling breath
        
    STROKE 4 (D+ → L+): TRANSFER
    ─────────────────────────────
        Jump from Dark to Light
        At + level (high energy)
        Energy changes CHARACTER (absorb → emit)
        Like oxygen becoming breath
        
    COMPLETE CYCLE = ONE PUMP ACTION!

THE BREATHING HEXAGON:
══════════════════════

        EXHALE ──→ L+ ←── TRANSFER
                   │          ↑
                   │          │
                   ↓          │
        TRANSFER ──→ L- ──→ D- ←── INHALE
                             │
                             │
                             ↓
                            D+ ──→ TRANSFER
                             
    The hexagon BREATHES!
    Light exhales (emits)
    Dark inhales (absorbs)
    Transfers happen at matching levels!
""")


print("\n" + "=" * 70)
print("PART 7: THE HARVEST POINTS")
print("=" * 70)

print(r"""
WHERE ENERGY IS HARVESTED:
══════════════════════════

    Not all transitions release usable energy!
    
    L+ → L- (Descend Light):
        ★★★ HARVEST POINT! ★★★
        Light emits energy as it descends
        This energy can be captured!
        
    L- → D- (Jump at - level):
        No harvest
        Energy just changes form
        (from emission-ready to absorption-ready)
        
    D- → D+ (Ascend Dark):
        Energy is ABSORBED
        Being stored/accumulated
        Not available for harvest
        
    D+ → L+ (Jump at + level):
        ★★★ HARVEST POINT! ★★★
        Transition releases excess energy!
        Like pressure release valve!

TWO HARVESTS PER CYCLE:
═══════════════════════

              L+ ←─────────────────────── D+
               │                          ↑
               │ ★ HARVEST 1 ★           │
               │ (emission)               │
               ↓                          │
              L- ─────────────────────→ D-
                       │
                       │
                       ↓
                 (no harvest,
                  just storage)
                 
    And:
    
              L+ ←──── ★ HARVEST 2 ★ ──── D+
               │      (transition)        ↑
               
    Total: 2 harvest opportunities per minimal cycle!
    
    With 6 spokes: 6 harvest opportunities per full cycle!
""")


print("\n" + "=" * 70)
print("PART 8: THE PHYSICAL REALIZATION")
print("=" * 70)

print(r"""
BUILDING THE HEXAGONAL PUMP:
════════════════════════════

    Each spoke is a CHANNEL for energy flow:
    
    ┌─────────────────────────────────────────────────────────────┐
    │                                                             │
    │                    HEXAGONAL CHAMBER                        │
    │                                                             │
    │         LIGHT              │              DARK              │
    │         SPOKE              │              SPOKE             │
    │           │                │                │               │
    │     ┌─────┴─────┐         │         ┌─────┴─────┐         │
    │     │           │         │         │           │         │
    │  +  │  EMITTER  │    HARVEST    │  ABSORBER │  +      │
    │     │  (LED?)   │─────────┼──────│  (solar   │         │
    │     │           │         │      │   cell?)  │         │
    │     │     │     │         │      │     │     │         │
    │     │     ↓     │         │      │     ↑     │         │
    │     │           │         │      │           │         │
    │  -  │  GROUND   │─────────┼──────│  GROUND   │  -      │
    │     │           │ TRANSFER│      │           │         │
    │     └───────────┘         │      └───────────┘         │
    │                           │                             │
    └─────────────────────────────────────────────────────────────┘

THE COMPONENTS:
═══════════════

    LIGHT SPOKE:
        + end: Excited state (emitter, LED, laser)
        - end: Ground state (after emission)
        Direction: Emits photons as energy descends
        
    DARK SPOKE:
        - end: Ground state (ready to absorb)
        + end: Excited state (after absorption)
        Direction: Absorbs photons as energy ascends
        
    TRANSFER POINTS:
        At + level: High-energy transition (harvest!)
        At - level: Low-energy transition (storage)
        
    The light spoke EMITS what the dark spoke ABSORBS!
    They're coupled through the transfer points!
""")


print("\n" + "=" * 70)
print("PART 9: THE ROTATING FIELD")
print("=" * 70)

print(r"""
IF WE ROTATE THE FIELD:
═══════════════════════

    Instead of static spokes, what if the field ROTATES?
    
    The Light/Dark character rotates around the hexagon!
    
    Time 0:   L  D  L  D  L  D  (spokes 1-6)
    Time 1:   D  L  D  L  D  L  (rotated 60°)
    Time 2:   L  D  L  D  L  D  (back to start)
    
    Rotation frequency: Related to Schumann? (7.83 Hz)
    
    ┌─────────────────────────────────────────┐
    │                                         │
    │         Time 0        Time 1            │
    │                                         │
    │           L             D               │
    │          ╱ ╲           ╱ ╲              │
    │         D   D         L   L             │
    │         │   │    →    │   │   (rotate)  │
    │         L   L         D   D             │
    │          ╲ ╱           ╲ ╱              │
    │           D             L               │
    │                                         │
    └─────────────────────────────────────────┘
    
    The rotation creates APPARENT motion of energy!
    Energy doesn't actually move - the FIELD rotates!
    
    This is like:
        - AC current (field oscillates)
        - Rotating magnetic field in motor
        - Wave propagation

THE STANDING WAVE:
══════════════════

    If rotation is at right frequency:
        Creates STANDING WAVE pattern!
        
        Nodes: Where L and D cancel (transfer points!)
        Antinodes: Where L or D is maximum (harvest points!)
        
    The standing wave PUMPS energy automatically!
    No need for external drive after startup!
""")


print("\n" + "=" * 70)
print("PART 10: SUMMARY - THE ZIGZAG CYCLE")
print("=" * 70)

print(r"""
═══════════════════════════════════════════════════════════════════════

THE HEXAGONAL SPOKE STRUCTURE

    6 spokes alternating: Light - Dark - Light - Dark - Light - Dark
    Each spoke: + (outer/∞) to - (center/0)
    
═══════════════════════════════════════════════════════════════════════

THE ZIGZAG PATH

    L+ → L- (descend Light, HARVEST!)
    L- → D- (jump at - level, signs match)
    D- → D+ (ascend Dark, accumulate)
    D+ → L+ (jump at + level, HARVEST!)
    
    2 harvests per minimal cycle!

═══════════════════════════════════════════════════════════════════════

THE RULES

    1. Can move along spoke (+ ↔ -)
    2. Can only JUMP at matching signs (++ or --)
    3. Must alternate L ↔ D when jumping
    4. Must complete full cycle to close loop

═══════════════════════════════════════════════════════════════════════

THE BREATHING ANALOGY

    Light descending = EXHALE (emit)
    Dark ascending = INHALE (absorb)
    Transfers = character change
    
    The hexagon BREATHES energy!

═══════════════════════════════════════════════════════════════════════

THE PHYSICAL IMPLEMENTATION

    Light spoke: Emitter (LED, laser, excited atoms)
    Dark spoke: Absorber (solar cell, ground state atoms)
    Transfer: Coupled at matching energy levels
    Harvest: At transition points

═══════════════════════════════════════════════════════════════════════

THE ROTATING FIELD OPTION

    Field rotates at Schumann frequency (7.83 Hz)?
    Creates standing wave pattern
    Automatic pumping once started
    Self-sustaining oscillation!

═══════════════════════════════════════════════════════════════════════

COMPLETE H → Au PATH

    Multiple hexagons nested
    Energy spirals inward (H at outer, Au at center)
    Each hexagon = one element level
    ~13 hexagons for full H → Au range

═══════════════════════════════════════════════════════════════════════
""")
