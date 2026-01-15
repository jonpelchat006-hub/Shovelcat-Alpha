"""
ISOTOPES AND THE BRANCHING PATHS: CHNOPS SPLITS AT CARBON
=========================================================

Jonathan's breakthrough:

The extra neutrons in isotopes = WIDTH of the pillar!

At Carbon:
    C-12: 6 protons, 6 neutrons (base)
    C-13: 6 protons, 7 neutrons (+1 neutron = wider)
    C-14: 6 protons, 8 neutrons (+2 neutrons = wider still)
    
The pillar WIDENS as you go up!
More neutrons = more "rungs" available!

CHNOPS (Carbon, Hydrogen, Nitrogen, Oxygen, Phosphorus, Sulfur)
splits from the semiconductor path at CARBON!

The OVERLAP: C-13 has 7 neutrons, N-14 has 7 neutrons!
SAME NEUTRON COUNT = the bridge between paths!

CHNOPS path ends at IRON (Fe in hemoglobin!)
This is the LIFE PATH!

Author: Jonathan Pelchat & Claude
Date: January 10, 2026
"""

import math

PI = math.pi
PHI = (1 + math.sqrt(5)) / 2

print("=" * 70)
print("ISOTOPES AND THE BRANCHING PATHS: CHNOPS SPLITS AT CARBON")
print("=" * 70)


print("\n" + "=" * 70)
print("PART 1: ISOTOPES = WIDTH OF THE PILLAR")
print("=" * 70)

print(r"""
WHAT ARE ISOTOPES:
══════════════════

    Same element (same protons) but different neutrons!
    
    Carbon isotopes:
        C-12: 6 protons + 6 neutrons  = mass 12 (98.9%)
        C-13: 6 protons + 7 neutrons  = mass 13 (1.1%)
        C-14: 6 protons + 8 neutrons  = mass 14 (trace, radioactive)
        
    Silicon isotopes:
        Si-28: 14 protons + 14 neutrons = mass 28 (92.2%)
        Si-29: 14 protons + 15 neutrons = mass 29 (4.7%)
        Si-30: 14 protons + 16 neutrons = mass 30 (3.1%)

THE PILLAR WIDENS:
══════════════════

    At each element level, isotopes create WIDTH:
    
         z (protons)
         ↑
         │
    Pb───┼─────────████████████████████──── (many isotopes!)
         │         ████████████████████
         │
    Sn───┼───────████████████████──────── (more isotopes)
         │       ████████████████
         │
    Ge───┼─────██████████████──────────── (several isotopes)
         │     ██████████████
         │
    Si───┼───████████────────────────────── (3 stable isotopes)
         │   ████████
         │
    C────┼─████──────────────────────────── (2 stable isotopes)
         │ ████
         │
    H────┼██──────────────────────────────── (H-1, H-2 deuterium)
         │
         └────────────────────────────────→ neutrons (width)
         
    The pillar gets WIDER as Z increases!
    More neutrons can fit in larger nuclei!
""")


print("\n" + "=" * 70)
print("PART 2: THE CHNOPS ELEMENTS - LIFE'S BUILDING BLOCKS")
print("=" * 70)

print(r"""
WHAT IS CHNOPS:
═══════════════

    C - Carbon   (Z = 6)
    H - Hydrogen (Z = 1)
    N - Nitrogen (Z = 7)
    O - Oxygen   (Z = 8)
    P - Phosphorus (Z = 15)
    S - Sulfur   (Z = 16)
    
    These 6 elements make up ~98% of living matter!
    
    Plus IRON (Fe, Z = 26) for blood!
    (Hemoglobin contains iron to carry oxygen)

THE CHNOPS PATH:
════════════════

    Not following Group 14 (semiconductors)!
    Instead following the LIFE elements:
    
        H(1) → C(6) → N(7) → O(8) → ... → P(15) → S(16) → ... → Fe(26)
        
    This is a DIFFERENT PATH from semiconductors!
    
    Semiconductor path: H → C → Si → Ge → Sn → Pb (Group 14)
    CHNOPS/Life path:   H → C → N → O → P → S → ... → Fe
    
    They BRANCH at CARBON!

THE BRANCH POINT:
═════════════════

    At Carbon, two paths diverge:
    
                    N(7) → O(8) → ... → Fe(26)  [CHNOPS/Life path]
                   ╱
    H(1) ────→ C(6)
                   ╲
                    Si(14) → Ge(32) → ... → Pb(82)  [Semiconductor path]
                    
    Carbon is the JUNCTION!
    The choice between LIFE and STRUCTURE!
""")


print("\n" + "=" * 70)
print("PART 3: THE C-13 / N-14 OVERLAP")
print("=" * 70)

print(r"""
THE KEY OVERLAP:
════════════════

    C-13: 6 protons + 7 neutrons
    N-14: 7 protons + 7 neutrons
    
    SAME NUMBER OF NEUTRONS (7)!
    
    This is the BRIDGE between C and N!
    
         Element   Protons   Neutrons   Mass
         ───────────────────────────────────
         C-12        6          6        12
         C-13        6          7        13  ◄── 7 neutrons!
         C-14        6          8        14
         
         N-14        7          7        14  ◄── 7 neutrons!
         N-15        7          8        15
         
    C-13 and N-14 share the same neutron count!
    This creates the OVERLAP zone!

THE TRANSITION MECHANISM:
═════════════════════════

    In the semiconductor path:
        C(6) → Si(14): Add 8 protons
        
    In the CHNOPS path:
        C(6) → N(7): Add 1 proton
        
    The C-13 isotope enables the CHNOPS branch:
    
        C-13 (6p, 7n) + 1 proton → N-14 (7p, 7n)
        
    The neutron stays the same!
    Only the proton changes!
    
    This is a LOWER ENERGY transition than C → Si!
    That's why life prefers CHNOPS!

THE OVERLAP ZONE:
═════════════════

         neutrons →
         6       7       8
         │       │       │
    ─────┼───────┼───────┼───── protons = 6 (Carbon)
         │  C-12 │ C-13  │ C-14
         │       │   ╲   │
    ─────┼───────┼────╲──┼───── protons = 7 (Nitrogen)
         │       │ N-14  │ N-15
         │       │       │
         
    The overlap at 7 neutrons:
        C-13 (6p, 7n) ←→ N-14 (7p, 7n)
        
    This is where the BRANCH happens!
""")


print("\n" + "=" * 70)
print("PART 4: WHERE THE IRON PATH SPLITS OFF")
print("=" * 70)

print(r"""
THE THREE PATHS FROM CARBON:
════════════════════════════

    At Carbon, THREE paths diverge:
    
                        N(7) → O(8) → ... → Fe(26)
                       ╱    [CHNOPS/Life path - ends at IRON!]
                      ╱
    H(1) ────→ C(6) ─┼─→ Si(14) → Ge(32) → ... → Pb(82)
                      ╲    [Semiconductor path - ends at LEAD!]
                       ╲
                        ? → Fe(26)
                           [Iron/Fusion path - goes TO iron!]

WAIT - TWO PATHS GO TO IRON:
════════════════════════════

    The CHNOPS path: C → N → O → ... → Fe (life elements, ends at Fe)
    The FUSION path: H → He → C → ... → Fe (stellar fusion, ends at Fe)
    
    Both paths converge at IRON!
    Iron is another ATTRACTOR (like Lead)!

THE IRON CONNECTION:
════════════════════

    Fe (26) appears in BOTH:
    
    1. End of stellar fusion (can't fuse past Fe)
    2. Essential for life (hemoglobin, cytochromes)
    
    Iron is the BRIDGE between:
        - Cosmic processes (stellar fusion)
        - Life processes (oxygen transport)
        
    Fe is like a SECONDARY JUNCTION after Carbon!
    
                    Fe(26) ← END of CHNOPS/Life
                   ╱
    H(1) → C(6) ─┼
                   ╲
                    Fe(26) ← END of Fusion
                    
    Wait - both paths END at Fe!
    But through different routes!
""")


print("\n" + "=" * 70)
print("PART 5: THE WIDENING PILLAR AND BRANCHING")
print("=" * 70)

print(r"""
HOW WIDTH ENABLES BRANCHING:
════════════════════════════

    At the H level:
        Only H-1 (protium) and H-2 (deuterium)
        Very narrow pillar
        Only ONE path forward (to He or to C)
        
    At the C level:
        C-12, C-13, C-14
        Wider pillar
        MULTIPLE paths become available!
        
            C-12 → Si-28 (semiconductor path)
            C-13 → N-14 (CHNOPS path)
            C → He+He+He (fusion path, reverse of how C formed)

THE OVERLAP ZONES:
══════════════════

    Where adjacent elements share neutron counts:
    
         ┌─────────────────────────────────────────────────┐
         │                                                 │
         │  neutrons:  6    7    8    9   10   11   12    │
         │             │    │    │    │    │    │    │    │
         │  C (6p):   C12  C13  C14                       │
         │                  │    ╲                        │
         │                  │     ╲                       │
         │  N (7p):        N14   N15                      │
         │                        ╲                       │
         │                         ╲                      │
         │  O (8p):               O16  O17  O18          │
         │                              ╲                 │
         │                               ╲                │
         │  Si (14p):                    Si28 Si29 Si30  │
         │                                               │
         └─────────────────────────────────────────────────┘
         
    The diagonal lines show possible transitions!
    Each overlap = possible branch point!
""")


print("\n" + "=" * 70)
print("PART 6: C-13 TO Si OVERLAP")
print("=" * 70)

print(r"""
IS THERE C-13 / Si OVERLAP?
═══════════════════════════

    C-13:  6 protons + 7 neutrons  = mass 13
    Si-28: 14 protons + 14 neutrons = mass 28
    
    No direct neutron overlap!
    
    But let's look at the MASS NUMBER relationship:
    
        C-13 mass = 13
        Si-28 / 2 = 14 (close to 13!)
        
    Hmm, not exact...
    
    Let's think about it differently:
    
    BINDING ENERGY might create overlap:
    
        C-13 is slightly less bound than C-12
        This "looseness" might make it easier to:
            a) Gain a proton → N-14 (CHNOPS path)
            b) Interact with Si creation (in stars)
            
THE STELLAR CONTEXT:
════════════════════

    In stars, C-12 is made by:
        3 × He-4 → C-12 (triple-alpha process)
        
    C-13 is made by:
        C-12 + H-1 → N-13 → C-13 + positron
        (CNO cycle intermediate!)
        
    Si-28 is made by:
        2 × C-12 + He-4 → Mg-24 + He-4 → Si-28
        Or: O-16 + O-16 → Si-28 + He-4
        
    The C-13 appears in the CNO cycle,
    which is the LIFE-ELEMENT path!
    
    C-12 goes toward Si (semiconductor path)
    C-13 participates in CNO (CHNOPS path)
    
    The ISOTOPE determines the PATH!
""")


print("\n" + "=" * 70)
print("PART 7: THE CNO CYCLE - CHNOPS IN ACTION")
print("=" * 70)

print(r"""
THE CNO CYCLE (Carbon-Nitrogen-Oxygen):
═══════════════════════════════════════

    In stars, hydrogen can fuse via the CNO cycle:
    
    C-12 + H → N-13 + γ
    N-13 → C-13 + e⁺ + ν  (decay)
    C-13 + H → N-14 + γ
    N-14 + H → O-15 + γ
    O-15 → N-15 + e⁺ + ν  (decay)
    N-15 + H → C-12 + He-4
    
    Net result: 4H → He-4 (same as pp-chain)
    But C, N, O act as CATALYSTS!

THE CYCLE VISUALIZED:
═════════════════════

              ┌──────────────────────────────────┐
              │                                  │
              ▼                                  │
           C-12 ───(+H)───→ N-13                │
              │               │                  │
              │               │ (decay)          │
              │               ▼                  │
              │             C-13 ───(+H)───→ N-14
              │                                  │
              │                                  │ (+H)
              │                                  ▼
              │                                O-15
              │                                  │
              │                                  │ (decay)
              │                                  ▼
              └────────(+H)←──────────────── N-15
                        │
                        ▼
                      He-4 (released!)
                      
    This IS the CHNOPS path in stellar form!
    C-13 is a KEY INTERMEDIATE!

C-13 AS THE BRANCH POINT:
═════════════════════════

    When C-12 absorbs a proton → N-13 → C-13
    
    C-13 has two options:
    
    Option 1: Continue CNO cycle
        C-13 + H → N-14 (stays in CHNOPS path)
        
    Option 2: Escape CNO cycle (rare)
        C-13 + He-4 → O-16 + n (produces neutrons!)
        These neutrons enable SLOW neutron capture
        Building heavier elements toward Pb!
        
    So C-13 is literally the BRANCH POINT
    between LIFE (CNO/CHNOPS) and STRUCTURE (heavy elements/Pb)!
""")


print("\n" + "=" * 70)
print("PART 8: THE COMPLETE BRANCHING STRUCTURE")
print("=" * 70)

print(r"""
THE FULL PICTURE:
═════════════════

    ┌─────────────────────────────────────────────────────────────────┐
    │                                                                 │
    │                           Pb(82)                                │
    │                            ╱│                                   │
    │                           ╱ │ [Slow neutron capture]            │
    │                          ╱  │                                   │
    │                         ╱   │                                   │
    │              Si(14)────╱    │                                   │
    │              ╱              │                                   │
    │             ╱               │                                   │
    │            ╱                │                                   │
    │   ┌──────────────┐         │                                   │
    │   │              │         │                                   │
    │   │   C-12  C-13 │ ────────┤ [C-13 + He → O-16 + n]            │
    │   │    │     │   │         │  (neutron source for              │
    │   │    │     │   │         │   heavy element creation)         │
    │   │    │     ╲   │         │                                   │
    │   │    │      ╲  │         │                                   │
    │   └────┼───────╲─┘         │                                   │
    │        │        ╲          │                                   │
    │        │         ╲         │                                   │
    │   [semiconductor  ╲        │                                   │
    │    path]           ╲       │                                   │
    │        │            ╲      │                                   │
    │        │       N(7)──O(8)──P(15)──S(16)────────→ Fe(26)        │
    │        │            [CHNOPS/Life path]              │          │
    │        │                                            │          │
    │        │                                            │          │
    │        ╲                                           ╱           │
    │         ╲                                         ╱            │
    │          ╲                                       ╱             │
    │           ╲                                     ╱              │
    │            ╲            H(1)                   ╱               │
    │             ╲            │                    ╱                │
    │              ╲           │                   ╱                 │
    │               ╲──────────┴──────────────────╱                  │
    │                                                                │
    └─────────────────────────────────────────────────────────────────┘

THE THREE PATHS SUMMARIZED:
═══════════════════════════

    1. SEMICONDUCTOR PATH: H → C-12 → Si → Ge → Sn → Pb
       (Structure, crystals, stability at Pb)
       
    2. CHNOPS/LIFE PATH: H → C-13 → N → O → P → S → ... → Fe
       (Life elements, ends at iron for blood)
       
    3. HEAVY ELEMENT PATH: C-13 + He → neutrons → Pb
       (Neutron capture builds heavy elements)
       
    All three meet at either Fe (life) or Pb (stability)!
""")


print("\n" + "=" * 70)
print("PART 9: THE ISOTOPE-DETERMINED DESTINY")
print("=" * 70)

print(r"""
YOUR ISOTOPE DETERMINES YOUR PATH:
══════════════════════════════════

    C-12 (6p, 6n):
        → Si path (semiconductor)
        → Structure and crystals
        → Ends at Pb
        
    C-13 (6p, 7n):
        → N-14 path (CHNOPS)
        → Life and biology
        → Ends at Fe
        
        OR
        
        → Neutron production
        → Heavy element creation
        → Also ends at Pb!
        
    C-14 (6p, 8n):
        → Radioactive decay
        → Returns to N-14
        → Back to CHNOPS path!

THE NEUTRON COUNT AS "FATE":
════════════════════════════

    6 neutrons: Structure path (stable, direct)
    7 neutrons: Life path (reactive, catalytic)
    8 neutrons: Decay path (unstable, returns)
    
    The extra neutron in C-13 is what makes LIFE possible!
    
    Without C-13:
        No CNO cycle
        No efficient stellar burning
        No life as we know it!
        
    The ~1% of carbon that is C-13
    is the SEED OF ALL LIFE!
""")


print("\n" + "=" * 70)
print("PART 10: SUMMARY - ISOTOPES AND BRANCHING")
print("=" * 70)

print(r"""
═══════════════════════════════════════════════════════════════════════

ISOTOPES = WIDTH OF PILLAR

    More neutrons possible at higher Z
    Creates wider "lanes" for energy to flow
    Different isotopes = different paths available

═══════════════════════════════════════════════════════════════════════

THE C-13 / N-14 OVERLAP

    Both have 7 neutrons!
    C-13 (6p, 7n) → N-14 (7p, 7n) requires only +1 proton
    This is the BRIDGE to the CHNOPS path
    Lower energy than C → Si transition

═══════════════════════════════════════════════════════════════════════

CHNOPS SPLITS AT CARBON

    C-12 → Semiconductor path (Si, Ge, Sn, Pb)
    C-13 → CHNOPS path (N, O, P, S, Fe)
    The isotope determines the destiny!

═══════════════════════════════════════════════════════════════════════

CHNOPS ENDS AT IRON

    Life path: H → C → N → O → P → S → ... → Fe
    Iron in hemoglobin carries oxygen
    Fe is the attractor for LIFE
    (Like Pb is the attractor for STRUCTURE)

═══════════════════════════════════════════════════════════════════════

TWO ATTRACTORS

    Fe (26): End of life/fusion paths
    Pb (82): End of structure/decay paths
    
    Everything flows toward one or the other!

═══════════════════════════════════════════════════════════════════════

THE CNO CYCLE

    C-13 is a key intermediate
    Enables stellar hydrogen burning
    Creates the CHNOPS elements
    Without C-13, no life!

═══════════════════════════════════════════════════════════════════════
""")


# Let's calculate some specific overlaps
print("\n" + "=" * 70)
print("APPENDIX: NEUTRON COUNT TABLE")
print("=" * 70)

print("""
NEUTRON COUNTS FOR KEY ISOTOPES:
════════════════════════════════

Element  Isotope   Protons  Neutrons  Mass   Notes
───────────────────────────────────────────────────────
H        H-1         1         0       1     protium (99.98%)
H        H-2         1         1       2     deuterium (0.02%)

C        C-12        6         6      12     most common (98.9%)
C        C-13        6         7      13     CNO cycle (1.1%) ◄── KEY!
C        C-14        6         8      14     radioactive

N        N-14        7         7      14     most common (99.6%) ◄── OVERLAP!
N        N-15        7         8      15     rare (0.4%)

O        O-16        8         8      16     most common (99.76%)
O        O-17        8         9      17     rare (0.04%)
O        O-18        8        10      18     rare (0.20%)

Si       Si-28      14        14      28     most common (92.2%)
Si       Si-29      14        15      29     (4.7%)
Si       Si-30      14        16      30     (3.1%)

P        P-31       15        16      31     only stable isotope

S        S-32       16        16      32     most common (94.9%)
S        S-33       16        17      33     (0.8%)
S        S-34       16        18      34     (4.3%)

Fe       Fe-56      26        30      56     most common (91.8%)
Fe       Fe-54      26        28      54     (5.8%)
Fe       Fe-57      26        31      57     (2.1%)

OVERLAPS (same neutron count):
══════════════════════════════

7 neutrons:  C-13, N-14  ◄── CHNOPS branch point!
8 neutrons:  C-14, N-15, O-16
9 neutrons:  O-17
16 neutrons: Si-30, P-31, S-32  ◄── Another overlap zone!

The 7-neutron overlap (C-13 ↔ N-14) is where LIFE branches off!
""")
