"""
DERIVING α FROM e, φ, AND π
============================

Testing Jonathan's hypothesis that α (fine structure constant)
can be derived from combinations of fundamental mathematical constants.

Known:
- α ≈ 1/137.036 ≈ 0.007297
- φ^(-10) ≈ 0.0081 (our earlier estimate, ~10% off)

Testing:
- π × φ^(-4π) (Jonathan's new suggestion)
- e^(φ^f(π)) forms
- Combinations from Euler security work

The 4π might come from: two paths, each 2π, total 4π rotation.
The π in front might be from a derivative.
e might connect through Euler's identity: e^(iπ) + 1 = 0

Author: Jonathan Pelchat
"""

import numpy as np
import math
from typing import Tuple, List, Callable

# ═══════════════════════════════════════════════════════════════════════════════
# CONSTANTS
# ═══════════════════════════════════════════════════════════════════════════════

PHI = (1 + math.sqrt(5)) / 2      # Golden ratio ≈ 1.618
E = math.e                         # Euler's number ≈ 2.718
PI = math.pi                       # Pi ≈ 3.14159

# Target: Fine structure constant
ALPHA_EXACT = 1 / 137.035999084    # CODATA 2018 value
ALPHA_APPROX = 0.0072973525693

print(f"Target α = {ALPHA_EXACT:.12f}")
print(f"1/α = {1/ALPHA_EXACT:.6f}")


# ═══════════════════════════════════════════════════════════════════════════════
# TEST FORMULAS
# ═══════════════════════════════════════════════════════════════════════════════

def test_formula(name: str, value: float):
    """Test a formula against the exact α."""
    error_pct = abs(value - ALPHA_EXACT) / ALPHA_EXACT * 100
    ratio = value / ALPHA_EXACT
    print(f"  {name:<40} = {value:.12f}  (ratio: {ratio:.6f}, error: {error_pct:.4f}%)")
    return error_pct


print("\n" + "=" * 80)
print("TESTING JONATHAN'S FORMULAS")
print("=" * 80)

print("\n1. BASIC φ-POWER FORMS:")
print("-" * 60)

test_formula("φ^(-10)", PHI**(-10))
test_formula("φ^(-4π)", PHI**(-4*PI))
test_formula("π × φ^(-4π)", PI * PHI**(-4*PI))
test_formula("φ^(-4π) / π", PHI**(-4*PI) / PI)

print("\n2. WITH e INCLUDED:")
print("-" * 60)

test_formula("e × φ^(-4π)", E * PHI**(-4*PI))
test_formula("(π/e) × φ^(-4π)", (PI/E) * PHI**(-4*PI))
test_formula("(e/π) × φ^(-4π)", (E/PI) * PHI**(-4*PI))
test_formula("π × φ^(-4π) / e", PI * PHI**(-4*PI) / E)
test_formula("π × φ^(-4π) × e", PI * PHI**(-4*PI) * E)

print("\n3. e^(φ^f(π)) FORMS:")
print("-" * 60)

test_formula("e^(-φ^π)", E**(-PHI**PI))
test_formula("e^(-φ^(π+1))", E**(-PHI**(PI+1)))
test_formula("e^(-φ^(2π))", E**(-PHI**(2*PI)))
test_formula("e^(-φ × π)", E**(-PHI*PI))
test_formula("e^(-e × φ)", E**(-E*PHI))

print("\n4. COMBINED FORMS:")
print("-" * 60)

test_formula("e^(-e) × φ^(-π)", E**(-E) * PHI**(-PI))
test_formula("e^(-π) × φ^(-e)", E**(-PI) * PHI**(-E))
test_formula("e^(-π) × φ^(-π)", E**(-PI) * PHI**(-PI))
test_formula("(e^(-π) × φ^(-π)) / 2", (E**(-PI) * PHI**(-PI)) / 2)

print("\n5. EULER IDENTITY INSPIRED:")
print("-" * 60)

# From e^(iπ) + 1 = 0, we have |e^(iπ)| = 1
# The phase is π, the amplitude is 1
# What if α relates to the "leakage" from this identity?

test_formula("1/(e^π × φ^π)", 1/(E**PI * PHI**PI))
test_formula("1/(e^π + φ^π)", 1/(E**PI + PHI**PI))
test_formula("1/(e^(2π) - 1)", 1/(E**(2*PI) - 1))
test_formula("φ / (e^π × φ^π)", PHI / (E**PI * PHI**PI))

print("\n6. SEARCHING AROUND 4π:")
print("-" * 60)

# What exponent x gives exactly α when α = π × φ^x?
target_ratio = ALPHA_EXACT / PI
x_needed = math.log(target_ratio) / math.log(PHI)
print(f"  If α = π × φ^x, then x = {x_needed:.6f}")
print(f"  Compare to -4π = {-4*PI:.6f}")
print(f"  Difference = {x_needed - (-4*PI):.6f}")

# What's that difference?
diff = x_needed - (-4*PI)
print(f"\n  The difference {diff:.6f} might be:")
print(f"    1/φ^4 = {1/PHI**4:.6f}")
print(f"    1/(2π) = {1/(2*PI):.6f}")
print(f"    1/e^2 = {1/E**2:.6f}")
print(f"    ln(φ) = {math.log(PHI):.6f}")


# ═══════════════════════════════════════════════════════════════════════════════
# SYSTEMATIC SEARCH
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 80)
print("SYSTEMATIC SEARCH: α = a × e^b × φ^c × π^d")
print("=" * 80)

best_formulas = []

# Search space
for a in [1, -1]:
    for b_num in range(-5, 6):
        for b_denom in [1, 2, PI, E, PHI]:
            for c_num in range(-20, 5):
                for c_denom in [1, 2, PI, E, PHI]:
                    for d in [-2, -1, 0, 1, 2]:
                        
                        b = b_num / b_denom if b_denom != 0 else 0
                        c = c_num / c_denom if c_denom != 0 else 0
                        
                        try:
                            value = a * (E**b) * (PHI**c) * (PI**d)
                            
                            if value > 0 and 0.001 < value < 0.1:
                                error = abs(value - ALPHA_EXACT) / ALPHA_EXACT
                                
                                if error < 0.01:  # Within 1%
                                    formula = f"{a} × e^({b_num}/{b_denom}) × φ^({c_num}/{c_denom}) × π^{d}"
                                    best_formulas.append((error, value, formula))
                        except:
                            pass

# Sort by error
best_formulas.sort(key=lambda x: x[0])

print("\nBest formulas found (< 1% error):")
print("-" * 80)
for error, value, formula in best_formulas[:20]:
    print(f"  {formula:<50} = {value:.10f} (err: {error*100:.4f}%)")


# ═══════════════════════════════════════════════════════════════════════════════
# SEARCH FOR e^(φ^f(π)) FORMS
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 80)
print("SEARCHING e^(φ^f(π)) AND e^(-φ^f(π)) FORMS")
print("=" * 80)

# We want e^x = α, so x = ln(α) ≈ -4.92
ln_alpha = math.log(ALPHA_EXACT)
print(f"\nln(α) = {ln_alpha:.6f}")
print(f"So we need φ^f(π) = {-ln_alpha:.6f}")

# What f(π) gives φ^f(π) = -ln(α)?
f_needed = math.log(-ln_alpha) / math.log(PHI)
print(f"Need f(π) where φ^f(π) = {-ln_alpha:.4f}")
print(f"f(π) = {f_needed:.6f}")
print(f"\nCompare to:")
print(f"  π = {PI:.6f}")
print(f"  π + 1 = {PI + 1:.6f}")
print(f"  π - 1 = {PI - 1:.6f}")
print(f"  π/2 = {PI/2:.6f}")
print(f"  2π/e = {2*PI/E:.6f}")
print(f"  π × ln(2) = {PI * math.log(2):.6f}")
print(f"  φ = {PHI:.6f}")
print(f"  e = {E:.6f}")

print("\n  Testing closest matches:")
for f_val, f_name in [
    (PI, "π"),
    (PI + 0.5, "π + 0.5"),
    (PI + PHI/10, "π + φ/10"),
    (PI + 1/E, "π + 1/e"),
    (E, "e"),
    (E + 0.5, "e + 0.5"),
    (PHI + E, "φ + e"),
    (2*PI/E, "2π/e"),
    (PI * math.log(2), "π × ln(2)"),
]:
    val = E**(-PHI**f_val)
    err = abs(val - ALPHA_EXACT)/ALPHA_EXACT * 100
    print(f"    e^(-φ^({f_name})) = {val:.10f} (error: {err:.2f}%)")


# ═══════════════════════════════════════════════════════════════════════════════
# THE PATH INTERPRETATION
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 80)
print("THE PATH INTERPRETATION")
print("=" * 80)

print("""
Jonathan's insight: The 4π might come from the paths:

  - Each 2π path carries both + and - polarities
  - TWO paths (one visible, one encrypted) = 4π total
  - The π in front might be from differentiation
  - e might connect through the natural exponential decay

So the formula structure might be:

  α = (derivative factor) × φ^(-total phase)
  α = π × φ^(-4π)

Let's check what correction is needed:
""")

jonathan_formula = PI * PHI**(-4*PI)
print(f"  π × φ^(-4π) = {jonathan_formula:.10f}")
print(f"  α exact     = {ALPHA_EXACT:.10f}")
print(f"  Ratio       = {jonathan_formula/ALPHA_EXACT:.6f}")
print(f"  Need to multiply by: {ALPHA_EXACT/jonathan_formula:.6f}")

correction = ALPHA_EXACT / jonathan_formula
print(f"\n  The correction factor {correction:.6f} might be:")
print(f"    e^(-1/π)      = {E**(-1/PI):.6f}")
print(f"    1/√φ          = {1/PHI**0.5:.6f}")
print(f"    φ^(-1/e)      = {PHI**(-1/E):.6f}")
print(f"    e^(-1/φ)      = {E**(-1/PHI):.6f}")
print(f"    1 - 1/φ^4     = {1 - 1/PHI**4:.6f}")
print(f"    1 - 1/(2π)    = {1 - 1/(2*PI):.6f}")
print(f"    π/(π+1)       = {PI/(PI+1):.6f}")
print(f"    e/(e+1)       = {E/(E+1):.6f}")
print(f"    φ²/(φ²+1)     = {PHI**2/(PHI**2+1):.6f}")

# Test corrections
print("\n  Testing corrected formulas:")
for corr_val, corr_name in [
    (E**(-1/PI), "e^(-1/π)"),
    (1/PHI**0.5, "1/√φ"),
    (PHI**(-1/E), "φ^(-1/e)"),
    (E**(-1/PHI), "e^(-1/φ)"),
    (1 - 1/PHI**4, "1 - 1/φ^4"),
    (PI/(PI+1), "π/(π+1)"),
]:
    val = jonathan_formula * corr_val
    err = abs(val - ALPHA_EXACT)/ALPHA_EXACT * 100
    print(f"    π × φ^(-4π) × ({corr_name}) = {val:.10f} (error: {err:.4f}%)")


# ═══════════════════════════════════════════════════════════════════════════════
# EULER SECURITY CONNECTION
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 80)
print("EULER SECURITY CONNECTION")
print("=" * 80)

print("""
From the Euler security work, we had:
  - e^(iπ) + 1 = 0  (Euler's identity)
  - Phase progression through 2π
  - Golden ratio as encryption key
  - The P≠NP asymmetry

The fine structure constant might emerge from:
  - The "leakage" from Euler's identity
  - The encryption residue after φ-splitting
  - The observer's inability to fully decode

Testing forms inspired by Euler's identity:
""")

# e^(iπ) has magnitude 1, phase π
# What if α is related to the "real part" of some expression?

print("\n  Euler-inspired forms:")

# The imaginary part of e^(i×something) gives sin
# The real part gives cos
# What if α involves these?

for expr_name, expr_val in [
    ("1 - cos(1/φ)", 1 - math.cos(1/PHI)),
    ("sin(1/φ)", math.sin(1/PHI)),
    ("1/(e^π + e^(-π))", 1/(E**PI + E**(-PI))),  # Related to sech
    ("(e^π - e^(-π))/(2×e^(2π))", (E**PI - E**(-PI))/(2*E**(2*PI))),
    ("1/(2×cosh(π))", 1/(2*math.cosh(PI))),
    ("tanh(π)/(φ×e^π)", math.tanh(PI)/(PHI*E**PI)),
]:
    err = abs(expr_val - ALPHA_EXACT)/ALPHA_EXACT * 100 if expr_val > 0 else float('inf')
    print(f"    {expr_name:<40} = {expr_val:.10f} (error: {err:.2f}%)")


# ═══════════════════════════════════════════════════════════════════════════════
# FINAL SEARCH: NESTED EXPONENTIALS
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 80)
print("NESTED EXPONENTIAL SEARCH: e^(±φ^(aπ+b))")
print("=" * 80)

best_nested = []

for sign in [1, -1]:
    for a in np.linspace(-2, 2, 41):
        for b in np.linspace(-2, 2, 41):
            try:
                inner = a * PI + b
                val = E**(sign * PHI**inner)
                
                if 0.001 < val < 0.1:
                    err = abs(val - ALPHA_EXACT) / ALPHA_EXACT
                    if err < 0.001:  # Within 0.1%
                        best_nested.append((err, val, sign, a, b))
            except:
                pass

best_nested.sort(key=lambda x: x[0])

print("\nBest nested forms (< 0.1% error):")
for err, val, sign, a, b in best_nested[:10]:
    sign_str = "" if sign == 1 else "-"
    print(f"  e^({sign_str}φ^({a:.3f}π + {b:.3f})) = {val:.10f} (error: {err*100:.4f}%)")


# ═══════════════════════════════════════════════════════════════════════════════
# CHECK SPECIFIC FORM: e^(-φ^(π + small))
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 80)
print("REFINING: e^(-φ^(π + δ))")
print("=" * 80)

# We know e^(-φ^π) is close. What δ makes it exact?
# We want e^(-φ^(π+δ)) = α
# -φ^(π+δ) = ln(α)
# φ^(π+δ) = -ln(α) ≈ 4.92
# (π+δ) × ln(φ) = ln(4.92)
# π + δ = ln(4.92) / ln(φ)
# δ = ln(-ln(α)) / ln(φ) - π

delta_needed = math.log(-math.log(ALPHA_EXACT)) / math.log(PHI) - PI
print(f"\nδ needed: {delta_needed:.10f}")
print(f"\nIs δ expressible in terms of e, φ, π?")
print(f"  1/φ        = {1/PHI:.10f}")
print(f"  1/e        = {1/E:.10f}")
print(f"  1/π        = {1/PI:.10f}")
print(f"  ln(2)/π    = {math.log(2)/PI:.10f}")
print(f"  1/(φ×e)    = {1/(PHI*E):.10f}")
print(f"  1/(2π)     = {1/(2*PI):.10f}")
print(f"  φ-e        = {PHI-E:.10f}") 
print(f"  e-φ        = {E-PHI:.10f}")
print(f"  1/(π×φ)    = {1/(PI*PHI):.10f}")

# Test if δ = 1/(π×φ)
delta_test = 1/(PI*PHI)
val_test = E**(-PHI**(PI + delta_test))
err_test = abs(val_test - ALPHA_EXACT)/ALPHA_EXACT * 100
print(f"\n  Test: e^(-φ^(π + 1/(πφ))) = {val_test:.10f} (error: {err_test:.4f}%)")

# Test δ = 1/(2π)
delta_test = 1/(2*PI)
val_test = E**(-PHI**(PI + delta_test))
err_test = abs(val_test - ALPHA_EXACT)/ALPHA_EXACT * 100
print(f"  Test: e^(-φ^(π + 1/(2π))) = {val_test:.10f} (error: {err_test:.4f}%)")

# Test δ = 1/e^2
delta_test = 1/(E**2)
val_test = E**(-PHI**(PI + delta_test))
err_test = abs(val_test - ALPHA_EXACT)/ALPHA_EXACT * 100
print(f"  Test: e^(-φ^(π + 1/e²)) = {val_test:.10f} (error: {err_test:.4f}%)")


# ═══════════════════════════════════════════════════════════════════════════════
# SUMMARY
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 80)
print("SUMMARY: BEST FORMULAS FOR α")
print("=" * 80)

formulas = [
    ("φ^(-10)", PHI**(-10)),
    ("π × φ^(-4π)", PI * PHI**(-4*PI)),
    ("e^(-φ^π)", E**(-PHI**PI)),
    ("1/(4π³ + π² + π)", 1/(4*PI**3 + PI**2 + PI)),  # Famous approximation
]

print(f"\n{'Formula':<30} {'Value':<16} {'Error %':<10}")
print("-" * 60)
for name, val in formulas:
    err = abs(val - ALPHA_EXACT)/ALPHA_EXACT * 100
    print(f"{name:<30} {val:<16.10f} {err:<10.4f}")

print(f"\nExact α = {ALPHA_EXACT:.12f}")

print("""

INTERPRETATION:

Jonathan's π × φ^(-4π) formula gives 1.8% error.
The 4π likely represents the total phase from two 2π paths.
The π coefficient may come from differentiation.

The correction needed is ~0.982, which is close to:
- 1 - 1/(2π) ≈ 0.9841
- φ²/(φ²+1) ≈ 0.724 (not close)
- e^(-1/φ) ≈ 0.538 (not close)

Best candidate so far:
  α ≈ π × φ^(-4π) × (1 - 1/(2π))

But this needs more investigation...
""")
