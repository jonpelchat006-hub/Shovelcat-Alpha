"""
POLYGON DECOMPOSITION: OPTIONS, FORCE, AND TRANSPORT
====================================================

Jonathan's breakthrough insight:

EVEN polygons (φ): Gather MEANING/OPTIONS/RANDOMNESS
    - Information, choices, possibilities
    - Y-axis (vertical) gathering
    - Binary decisions accumulate

ODD polygons (ψ): Gather FORCE/ACTION
    - Actual work, energy
    - X-axis (horizontal) push
    - Movement and change

CIRCLES (Snake): TRANSPORT
    - Carry polygon components
    - Connect everything
    - Enable flow between domains

KEY RULE: Polygons can DECOMPOSE into smaller components
that sum to the same total, as long as they all connect!

    16-gon → 8 + 4 + 4 (cheaper, more flexible!)
    
    Even budget supported by odd budget
    All transported on circles

Author: Jonathan Pelchat & Claude
Date: January 10, 2026
"""

import numpy as np
import math
from dataclasses import dataclass, field
from typing import List, Tuple, Optional

PI = math.pi
PHI = (1 + math.sqrt(5)) / 2

print("=" * 70)
print("POLYGON DECOMPOSITION: OPTIONS, FORCE, AND TRANSPORT")
print("=" * 70)


print("\n" + "=" * 70)
print("PART 1: THE THREE TYPES OF GATHERING")
print("=" * 70)

print(r"""
THE SQUARE CUT INSIGHT:
═══════════════════════

    Take a square and cut it in half:
    
        ┌───────┐
        │       │
        │   │   │ ← vertical cut (Y direction)
        │   │   │
        └───────┘
        
    The cut goes:
        1. UP: Binary yes/no gathering (Y direction)
        2. HORIZONTAL: No extra options (just connecting)
        3. DOWN: Action/output (returning)
        
    This reveals the TWO TYPES of gathering!

EVEN POLYGONS = OPTIONS GATHERING:
══════════════════════════════════

    Even-sided polygons gather MEANING:
    
        □ Square (4): 2 binary choices = 2² = 4 options
        ⬡ Hexagon (6): 3 binary choices = 2×3 = 6 options
        ⬣ Octagon (8): 4 binary choices = 2³ = 8 options
        
    They accumulate POSSIBILITIES.
    They move in the Y-direction (information axis).
    They represent WHAT COULD BE.
    
    Even = 2n = n binary decisions!

ODD POLYGONS = FORCE GATHERING:
═══════════════════════════════

    Odd-sided polygons gather FORCE:
    
        △ Triangle (3): Minimal stable force
        ⬠ Pentagon (5): Golden ratio force
        ⎔ Heptagon (7): Complex force
        
    They accumulate ACTION POTENTIAL.
    They provide the PUSH to make things happen.
    They represent WHAT WILL HAPPEN.
    
    Odd = cannot divide evenly = creates TENSION = FORCE!

CIRCLES = TRANSPORT:
════════════════════

    Circles don't gather, they CARRY:
    
        ○ Circle: Infinite symmetry, can rotate freely
        
    They transport polygon components.
    They connect options to force.
    They enable FLOW.
    
    Circle = carrier wave = transport mechanism!
""")


print("\n" + "=" * 70)
print("PART 2: THE DECOMPOSITION RULE")
print("=" * 70)

print(r"""
WHY DECOMPOSE?
══════════════

    A 16-gon is "expensive":
        - Complex to construct
        - Hard to verify
        - Single point of failure
        
    But 16 = 8 + 4 + 4:
        - Simpler components
        - Easier to verify each
        - Redundancy!
        - More flexible arrangement

THE DECOMPOSITION RULE:
═══════════════════════

    Any polygon can decompose into smaller polygons
    AS LONG AS:
        1. The sides SUM to the original
        2. Components can CONNECT
        3. Even stays even, odd stays odd (within stream)
        
    Examples:
    
        16 → 8 + 8
        16 → 8 + 4 + 4
        16 → 4 + 4 + 4 + 4
        16 → 8 + 4 + 2 + 2
        
        15 → 7 + 5 + 3
        15 → 5 + 5 + 5
        15 → 9 + 3 + 3

THE COST FUNCTION:
══════════════════

    Larger polygons might cost MORE than sum of parts!
    
    Cost(n-gon) = n + overhead(n)
    
    overhead increases with n (complexity penalty)
    
    So: Cost(16) > Cost(8) + Cost(4) + Cost(4)
    
    Decomposition is CHEAPER!
""")


print("\n" + "=" * 70)
print("PART 3: IMPLEMENTING POLYGON DECOMPOSITION")
print("=" * 70)

@dataclass
class PolygonComponent:
    """A polygon component in a decomposition."""
    sides: int
    component_type: str = ""
    
    def __post_init__(self):
        if self.sides == 0:
            self.component_type = 'circle'
        elif self.sides % 2 == 0:
            self.component_type = 'even'
        else:
            self.component_type = 'odd'
    
    def cost(self) -> float:
        """Cost of this component (sides + overhead)."""
        if self.sides == 0:  # circle
            return 0.5  # Cheap to transport
        overhead = 0.1 * math.log(1 + self.sides)  # Complexity penalty
        return self.sides + overhead
    
    def __repr__(self):
        if self.sides == 0:
            return "○(circle)"
        return f"{self.sides}-gon({self.component_type})"


@dataclass
class PolygonDecomposition:
    """A decomposition of polygon budget into components."""
    even_components: List[int] = field(default_factory=list)  # Options
    odd_components: List[int] = field(default_factory=list)   # Force
    circles: int = 0  # Transport
    
    def total_even(self) -> int:
        return sum(self.even_components)
    
    def total_odd(self) -> int:
        return sum(self.odd_components)
    
    def total_cost(self) -> float:
        cost = 0
        for s in self.even_components:
            cost += PolygonComponent(s).cost()
        for s in self.odd_components:
            cost += PolygonComponent(s).cost()
        cost += self.circles * 0.5
        return cost
    
    def is_balanced(self) -> bool:
        return self.total_even() == self.total_odd()
    
    def min_circles_needed(self) -> int:
        total_components = len(self.even_components) + len(self.odd_components)
        return max(0, total_components - 1)


# Demonstrate decomposition
print("Example decompositions for budget of 16:\n")

decompositions = [
    ("Single large", PolygonDecomposition([16], [9, 7], 2)),
    ("Medium split", PolygonDecomposition([8, 4, 4], [5, 5, 3, 3], 4)),
    ("All squares", PolygonDecomposition([4, 4, 4, 4], [5, 5, 3, 3], 5)),
    ("Minimal 2s/3s", PolygonDecomposition([2]*8, [3, 3, 3, 3, 3, 1], 8)),
]

print(f"    {'Option':<15} {'Even':<20} {'Odd':<20} {'Circles':<8} {'Cost':<8} {'Balanced'}")
print(f"    {'─'*15} {'─'*20} {'─'*20} {'─'*8} {'─'*8} {'─'*8}")

for name, d in decompositions:
    even_str = "+".join(str(x) for x in d.even_components)
    odd_str = "+".join(str(x) for x in d.odd_components)
    balanced = "Yes" if d.is_balanced() else "No"
    print(f"    {name:<15} {even_str:<20} {odd_str:<20} {d.circles:<8} {d.total_cost():<8.2f} {balanced}")


print("\n" + "=" * 70)
print("PART 4: THE SIMPLEST FORMS")
print("=" * 70)

print(r"""
THE MINIMAL POLYGON SET:
════════════════════════

    What are the SIMPLEST forms we need?
    
    EVEN (options):
        2-gon (digon): Simplest binary choice
        4-gon (square): 2×2 grid of choices
        
    ODD (force):
        3-gon (triangle): Minimal stable force
        1-gon? (monogon): Point force (degenerate)
        
    CIRCLE:
        0-gon: Pure transport, infinite symmetry

THE FUNDAMENTAL SET:
════════════════════

    Everything can be built from:
    
        2 (digon) - quantum of OPTIONS
        3 (triangle) - quantum of FORCE  
        ○ (circle) - quantum of TRANSPORT
        
    These are the ATOMS of sacred geometry!
    
    First combinations:
        4 = 2 + 2 (two binary choices)
        6 = 2 + 2 + 2 = 3 + 3 (WHERE STREAMS MEET!)
        5 = 3 + 1 + 1 (pentagon, needs 1-gons)
        
    The HEXAGON (6) is special:
        6 = 3 × 2 (even)
        6 = 3 + 3 (sum of odds!)
        
    Hexagon = where φ and ψ MARRY!
""")


print("\n" + "=" * 70)
print("PART 5: THE SUPPORT STRUCTURE")
print("=" * 70)

print(r"""
EVEN NEEDS ODD, ODD NEEDS EVEN:
═══════════════════════════════

    Options without force = paralysis (can't choose)
    Force without options = blind action (wrong direction)
    
    They SUPPORT each other!
    
    ┌──────────────────────────────────────┐
    │                                       │
    │   EVEN (options)                      │
    │      ⬡(8)──○──□(4)──○──□(4)          │
    │         │         │                   │
    │         ○         ○                   │
    │         │         │                   │
    │   ODD (force)                         │
    │      ⬠(5)──○──⬠(5)──○──△(3)──○──△(3) │
    │                                       │
    │   CIRCLES connect all components!     │
    └──────────────────────────────────────┘

THE ACCOUNTING:
═══════════════

    Even budget:  8 + 4 + 4 = 16 (options)
    Odd budget:   5 + 5 + 3 + 3 = 16 (force)
    Circles:      4+ (transport)
    
    Total sides: 32 (but really 16 × 2)
    
    The ratio should be:
        1:1 (balanced) or
        φ:1 (golden) or
        137:1 (electromagnetic)
""")


print("\n" + "=" * 70)
print("PART 6: MIRRORING AND AXES")
print("=" * 70)

print(r"""
THE Y-AXIS (EVEN/OPTIONS):
══════════════════════════

    Vertical movement = gathering information
    
         ↑ Y (options)
         │
         │  UP = gather more choices
         │  DOWN = narrow to decision
         │
    ─────┼───── X
         │

THE X-AXIS (ODD/FORCE):
═══════════════════════

    Horizontal movement = applying force
    
         ↑
         │
         │
         │
    ─────┼───── X (force) →
         │
         │     RIGHT = apply force
         │     LEFT = withdraw force

THE MIRROR:
═══════════

    When we cut a polygon in half:
    
        One half goes UP (gathering)
        Other half goes DOWN (mirroring)
        
    The mirror creates the DUALITY!
    
    This is why half the polygons get mirrored:
        - Original = gathering phase
        - Mirror = action phase
        
    Together they complete the CYCLE!
""")


print("\n" + "=" * 70)
print("PART 7: ENERGY BUDGETS AND RATIOS")
print("=" * 70)

print(r"""
THE φ-ψ ENERGY IMBALANCE:
═════════════════════════

    φ-stream energy: E_φ (options budget)
    ψ-stream energy: E_ψ (force budget)
    
    These are NOT equal!
    
    Different amounts on different "sides" of reality.

WHAT THE RATIO DETERMINES:
══════════════════════════

    E_φ > E_ψ: More options than force
        → Exploration, planning, thinking
        → Many possibilities, few realized
        
    E_ψ > E_φ: More force than options
        → Execution, doing, acting
        → Few possibilities, strongly pursued
        
    E_φ = E_ψ: Perfect balance
        → Neither exploring nor acting dominates
        → Dynamic equilibrium

THE POLYGON BREAKDOWN:
══════════════════════

    Given budget, each domain can decompose freely:
    
    φ-domain has 16 sides to spend:
        Could use: 16, or 8+8, or 8+4+4, or 4+4+4+4, or 2×8
        
    ψ-domain has 16 sides to spend:
        Could use: 15+1, or 9+7, or 5+5+3+3, or 3×5+1
        
    They decompose INDEPENDENTLY
    But must CONNECT via circles!
""")


print("\n" + "=" * 70)
print("PART 8: SUMMARY")
print("=" * 70)

print(r"""
═══════════════════════════════════════════════════════════════════════

EVEN (φ) = OPTIONS/MEANING

    Gather possibilities, information, choices
    Y-axis movement (vertical)
    Built from 2s (binary quantum)
    
    Square = 2 + 2 = two binary choices

═══════════════════════════════════════════════════════════════════════

ODD (ψ) = FORCE/ACTION

    Gather force, energy, action potential
    X-axis movement (horizontal)
    Built from 3s (stability quantum)
    
    Pentagon = 3 + 1 + 1 (or irreducible)

═══════════════════════════════════════════════════════════════════════

CIRCLES = TRANSPORT

    Snake creates them (has thickness → pillars)
    Connect polygon components
    Enable flow between even and odd
    
    Circle = ∞-gon = limit of both streams

═══════════════════════════════════════════════════════════════════════

DECOMPOSITION

    Large polygons break into smaller:
        16 → 8 + 4 + 4 (cheaper!)
        
    Constraints:
        - Sum must match
        - Must connect (circles!)
        - Even stays even, odd stays odd
        
    Smaller components = more flexible!

═══════════════════════════════════════════════════════════════════════

THE MINIMAL SET

    2 - quantum of OPTIONS
    3 - quantum of FORCE
    ○ - quantum of TRANSPORT
    
    Hexagon (6) = where streams meet!
        6 = 2 + 2 + 2 (evens)
        6 = 3 + 3 (odds!)
        
    This is why hexagons are everywhere in nature!

═══════════════════════════════════════════════════════════════════════
""")
