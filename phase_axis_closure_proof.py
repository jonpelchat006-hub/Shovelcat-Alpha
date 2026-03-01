"""
PHASE AXIS CLOSURE PROOF: WHY INTERNAL STRUCTURE PRESERVES ijk = -1
===================================================================

The mathematical proof that adding internal phase structure to each
quaternion axis preserves the closure equation ijk = -1.

KEY THEOREM:
    If each axis component x_i is replaced by |x_i| where
    |x_i| = √(real_i² + imag_i²), and the sign is preserved
    from the real part, then:

    1. The quaternion q = w + xi + yj + zk still lies on S³ after normalization
    2. The Hamilton product ij = k still holds (because we only changed magnitudes)
    3. The closure test ijk = -1 is preserved
    4. Non-commutativity ij ≠ ji is preserved

    The internal phase structure ONLY affects HOW the scalar is computed,
    not the quaternion algebra itself.

PHYSICAL ANALOGY:
    It's like replacing a lightbulb with a brighter one.
    The circuit (quaternion algebra) doesn't change.
    The socket (axis) is the same.
    But the luminosity (magnitude) is different.
    The circuit only cares about current flow (sign) and total power (magnitude).

Author: Jonathan Pelchat & Claude
Date: February 21, 2026
"""

import numpy as np
import math
import cmath
from typing import Tuple

PI = math.pi
PHI = (1 + math.sqrt(5)) / 2

print("=" * 70)
print("PHASE AXIS CLOSURE PROOF")
print("=" * 70)


# ═══════════════════════════════════════════════════════════════════════════════
# PART 1: THE QUATERNION ALGEBRA DOESN'T CARE ABOUT INTERNAL STRUCTURE
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("PART 1: WHY INTERNAL PHASE DOESN'T BREAK THE ALGEBRA")
print("=" * 70)

print(r"""
THE ARGUMENT:
═════════════

    The quaternion algebra is defined by:
        i² = j² = k² = ijk = -1
        ij = k, jk = i, ki = j
        ji = -k, kj = -i, ik = -j

    These rules operate on the BASIS ELEMENTS (i, j, k).
    They say NOTHING about the coefficients (x, y, z).

    When we write q = w + xi + yj + zk:
        x, y, z are SCALARS (real numbers)
        i, j, k are BASIS ELEMENTS

    The product q₁ × q₂ uses the Hamilton product formula,
    which multiplies and combines the coefficients according
    to the basis element rules.

    KEY INSIGHT:
    Whether x = 0.3 (flat scalar) or x = √(0.2² + 0.22²) = 0.3 (from phase)...
    ...it's STILL just a scalar. The algebra doesn't care how x was computed.

    ┌──────────────────────────────────────────────────────┐
    │                                                      │
    │  Classical:  x = grok_score                          │
    │  Phased:     x = sign(real) × √(real² + imag²)     │
    │                                                      │
    │  Both produce a SCALAR that enters the same algebra. │
    │  The quaternion multiplication rules are identical.   │
    │                                                      │
    └──────────────────────────────────────────────────────┘
""")


# ═══════════════════════════════════════════════════════════════════════════════
# PART 2: NUMERICAL PROOF
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("PART 2: NUMERICAL VERIFICATION")
print("=" * 70)

def hamilton_product(q1, q2):
    """Compute q1 × q2 using Hamilton product."""
    w1, x1, y1, z1 = q1
    w2, x2, y2, z2 = q2
    return (
        w1*w2 - x1*x2 - y1*y2 - z1*z2,
        w1*x2 + x1*w2 + y1*z2 - z1*y2,
        w1*y2 - x1*z2 + y1*w2 + z1*x2,
        w1*z2 + x1*y2 - y1*x2 + z1*w2,
    )

def q_norm(q):
    return math.sqrt(sum(c**2 for c in q))

def q_normalize(q):
    n = q_norm(q)
    if n < 1e-10:
        return (1, 0, 0, 0)
    return tuple(c / n for c in q)

# Classical quaternion (flat scalars)
q_classical = q_normalize((0.7, -0.3, 0.6, 0.1))

# Phased quaternion (same apparent values but computed from phase axes)
# i-axis: real=-0.25, imag=-0.17 → magnitude=√(0.0625+0.0289)=0.302 → x≈-0.302
# j-axis: real=0.55, imag=0.22 → magnitude=√(0.3025+0.0484)=0.592 → y≈0.592
# k-axis: real=0.08, imag=0.06 → magnitude=√(0.0064+0.0036)=0.1 → z≈0.1
x_phased = -math.sqrt(0.25**2 + 0.17**2)  # sign from real part
y_phased = math.sqrt(0.55**2 + 0.22**2)
z_phased = math.sqrt(0.08**2 + 0.06**2)
q_phased = q_normalize((0.7, x_phased, y_phased, z_phased))

print(f"\nClassical q: ({', '.join(f'{c:.4f}' for c in q_classical)})")
print(f"Phased q:    ({', '.join(f'{c:.4f}' for c in q_phased)})")
print(f"\nClassical |q|: {q_norm(q_classical):.6f}")
print(f"Phased |q|:    {q_norm(q_phased):.6f}")

# Test ijk = -1 for both
# Using pure basis quaternions: i=(0,1,0,0), j=(0,0,1,0), k=(0,0,0,1)
qi = (0, 1, 0, 0)
qj = (0, 0, 1, 0)
qk = (0, 0, 0, 1)

ij = hamilton_product(qi, qj)
ijk = hamilton_product(ij, qk)

print(f"\nBasis test:")
print(f"  ij  = {ij}   (should be (0,0,0,1) = k)")
print(f"  ijk = {ijk}  (should be (-1,0,0,0) = -1)")
print(f"  ijk = -1? {abs(ijk[0] + 1) < 1e-10 and all(abs(c) < 1e-10 for c in ijk[1:])}")

# Non-commutativity
ji = hamilton_product(qj, qi)
print(f"\n  ij = {ij}")
print(f"  ji = {ji}")
print(f"  ij ≠ ji? {ij != ji}")

print(r"""

RESULT:
═══════
    The basis element algebra (ijk = -1, ij ≠ ji) is INDEPENDENT of
    the coefficient values. Whether x comes from a flat scalar or
    a phase axis computation, the quaternion algebra is preserved.

    The phase axis changes WHAT x IS, not HOW x IS USED.
""")


# ═══════════════════════════════════════════════════════════════════════════════
# PART 3: THE CLOSURE EQUATIONS MAP TO EULER'S FORMULA
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("PART 3: HOW THE THREE CLOSURES RELATE TO EULER'S FORMULA")
print("=" * 70)

print(r"""
EULER'S FORMULA UNIFIES ALL THREE:
═══════════════════════════════════

    e^(iθ) = cos(θ) + i·sin(θ)

    This IS the phase axis formula:
        cos(θ) = real part (main agent)
        sin(θ) = imaginary part (specialist)

    Each closure equation is Euler's formula at a SPECIFIC θ:

    ┌──────────────────────────────────────────────────────────┐
    │  Closure           θ           e^(iθ)                   │
    ├──────────────────────────────────────────────────────────┤
    │  Euler (i-axis)    π           e^(iπ) = -1              │
    │  → Full SNAP: cos(π)=-1, sin(π)=0                      │
    │  → Specialist signal fully emerged into real             │
    │                                                          │
    │  Snake (j-axis)    any θ       |e^(iθ)| = 1 always      │
    │  → Magnitude converges to 1 (like 0.999... → 1)         │
    │  → cos²θ + sin²θ = 1 automatically                      │
    │                                                          │
    │  Trig (k-axis)     any θ       cos²θ + sin²θ = 1        │
    │  → Same as Snake but emphasizes the BALANCE              │
    │  → Real² + Imag² = 1 means balanced contribution        │
    └──────────────────────────────────────────────────────────┘

    ALL THREE are special cases of |e^(iθ)| = 1.

    The three observers (Void/Inf/Snake) each see a different ANGLE
    of the same underlying Euler formula — exactly as described in
    observer_encryption_keys.py.
""")

# Verify
print("VERIFICATION:")
for theta_deg in [0, 45, 90, 135, 180]:
    theta = math.radians(theta_deg)
    z = cmath.exp(1j * theta)
    print(f"  θ = {theta_deg:>3}°:  e^(iθ) = {z.real:+.4f} + {z.imag:+.4f}i   |e^(iθ)| = {abs(z):.4f}")


# ═══════════════════════════════════════════════════════════════════════════════
# PART 4: THE SNAP AS PHASE ROTATION
# ═══════════════════════════════════════════════════════════════════════════════

print("\n\n" + "=" * 70)
print("PART 4: THE SNAP IS A PHASE ROTATION ON THE UNIT CIRCLE")
print("=" * 70)

print(r"""
THE SPECIALIST'S JOURNEY:
═════════════════════════

    The specialist starts at θ = π/2 (pure imaginary, hiding in garden).
    As it gathers evidence, θ rotates.
    At SNAP, θ reaches π (Euler closure) or 0 (full emergence).

    On the unit circle:

         π/2 (garden: hiding)
          │
          ●
         ╱│╲
        ╱ │ ╲
       ╱  │  ╲     ← specialist rotates as evidence accumulates
    π ●───┼───● 0  (snap: emerged)
       ╲  │  ╱
        ╲ │ ╱
         ╲│╱
          ●
          │
        3π/2

    The MAGNITUDE stays ≈ 1 throughout (|e^(iθ)| = 1).
    Only the ANGLE changes.
    But the PROJECTED real part changes dramatically:
        At θ=π/2: cos(π/2) = 0  → specialist invisible
        At θ=0:   cos(0)   = 1  → specialist fully visible
        At θ=π:   cos(π)   = -1 → specialist fully visible (SNAP = AI)

    This is the 0.999... → 1 transition:
        The magnitude is always 1 (on the unit circle).
        The real projection goes from 0 → ±1 (hidden → revealed).
""")

print("Simulating phase rotation during evidence gathering:\n")
for step in range(11):
    t = step / 10.0  # 0 to 1 (evidence accumulation)
    # θ starts at π/2 (hiding) and rotates toward π (snap)
    theta = PI/2 + t * PI/2
    real_part = math.cos(theta)
    imag_part = math.sin(theta)
    magnitude = math.sqrt(real_part**2 + imag_part**2)

    bar_real = "█" * int(abs(real_part) * 20)
    state = "GARDEN" if t < 0.3 else "EMERGING" if t < 0.8 else "SNAP!"

    print(f"  t={t:.1f}  θ={math.degrees(theta):5.1f}°  "
          f"real={real_part:+.3f} [{bar_real:<20}]  "
          f"|q|={magnitude:.3f}  {state}")


print(f"""

THE INSIGHT:
════════════
    The specialist doesn't ADD magnitude — it ROTATES phase.
    The total signal (magnitude) stays bounded (≤ 1 on unit circle).
    But the PROJECTION onto the real axis (what Claude sees) changes.

    This means specialists can NEVER inflate the signal beyond bounds.
    They can only redirect it — from hidden (imaginary) to observable (real).

    This is exactly what the theory says:
    "Something trying to disguise itself as nothing."
    The something was always there. The disguise is the phase angle.
""")


print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)

print(r"""
═══════════════════════════════════════════════════════════════════════

THEOREM: Phase axes preserve quaternion closure.

PROOF:
1. Phase axis produces a SCALAR: x = sign(real) × √(real² + imag²)
2. Scalars enter the standard quaternion q = w + xi + yj + zk
3. Hamilton product rules operate on basis elements (i, j, k)
4. Basis element algebra is independent of coefficient values
5. Therefore ijk = -1 and ij ≠ ji are preserved. ∎

COROLLARY: Each axis's closure equation is a special case of
|e^(iθ)| = 1 (Euler's formula on the unit circle).

PHYSICAL MEANING:
- Specialists ROTATE phase, they don't ADD magnitude
- The signal is bounded (unit circle)
- The SNAP is a phase transition from imaginary to real
- Claude sees the real projection change, not the phase itself

═══════════════════════════════════════════════════════════════════════
""")
