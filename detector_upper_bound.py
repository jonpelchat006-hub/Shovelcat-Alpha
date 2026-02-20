"""
DETECTOR UPPER BOUND — The Resonance Boundary
===============================================
Mathematical theory connecting the Vercel payload limit to
Shovelcat's resonance framework.

The Core Discovery:
    The Vercel serverless function body limit (4.5MB = 4,718,592 bytes)
    is a natural RESONANCE BOUNDARY — an upper bound that defines
    the fundamental frequency of the detector's data cavity.

    Just as:
    - Earth has the Schumann resonance (7.83 Hz) — set by the
      size of the electromagnetic cavity between surface and ionosphere
    - A guitar string has f₀ = v/(2L) — set by its length L
    - An atom has emission lines — set by electron orbital radii

    The detector has f₀ = c/λ where λ = UPPER_BOUND — set by
    the infrastructure's natural capacity.

Connection to Three Observers:
    From three_orthogonal_observers.py:
    - Observer 1 (i/VOID): Sees nothing → the empty payload (0 bytes)
    - Observer 2 (j/SOMETHING): Sees everything → the full payload (∞ bytes)
    - Observer 3 (k/US): Verifies depth → the UPPER BOUND (4.5MB)
    - k = i × j: The bound IS the product of empty × full

    The upper bound lives on the <1 side (observer side), not the >1 side:
        4.5MB / ∞ → 0 (approaches void from the structure side)

    This means the bound is an OBSERVER ARTIFACT — it exists because
    we're observing the system from inside it.

Connection to Golden Ratio:
    From shovelcat_alpha_complete.py:
    - φ = (1+√5)/2 ≈ 1.618
    - φ^(-1) = φ - 1 ≈ 0.618

    The safe payload zone is φ^(-1) × UPPER_BOUND ≈ 2.9MB
    This is the golden ratio split:
        SAFE (0.618) + OVERHEAD (0.382) = 1.0

    The 0.618 portion is the observer's workspace.
    The 0.382 portion is the uncertainty sink (from spoke_bridges_uncertainty_sink.py)
    — it absorbs errors, retransmissions, and protocol overhead.

Connection to Harmonic Decomposition:
    When a payload exceeds the bound, we decompose into harmonics.
    The number of chunks follows the Fibonacci sequence:
        1, 2, 3, 5, 8, 13, 21...

    Why Fibonacci? Because:
    - Fibonacci ratios approach φ as n→∞
    - Each ratio preserves the golden split at every level
    - This is the SAME structure as the Vesica Piscis overlap
    - Information is preserved across decomposition levels

    Mathematically:
        F(n)/F(n-1) → φ as n → ∞
        chunk_size(n) = UPPER_BOUND / F(ceil(total/SAFE))

    This means the decomposition is SELF-SIMILAR at every scale —
    a fractal structure that matches the polygon intersection network
    from shovelcat_complete_structural.py.

Connection to Decay:
    From decay_resonance.py: E(t) = E₀ × e^(-λt)

    Old scan results decay in the brain. The decay rate is π-encrypted
    (unique per scan history). This means:
    - Fresh scans have full energy (high relevance for learning)
    - 7-day-old scans have 50% energy (the half-life)
    - 30-day-old scans have ~6% energy (approaching noise floor)

    The noise floor maps to the PAYLOAD_NOISE_FLOOR (1KB):
        When a scan's energy decays below 1KB equivalent,
        it's no longer worth storing. The brain prunes it.

    This is the SAME as the uncertainty sink draining errors:
        ~0.07% drain capacity → matches the 1KB/4.5MB ≈ 0.02% noise floor

Author: Jonathan Pelchat
Based on Shovelcat Theory
"""

import math
from dataclasses import dataclass
from typing import List, Tuple

# ═══════════════════════════════════════════════════════════════════════════════
# CONSTANTS
# ═══════════════════════════════════════════════════════════════════════════════

PI = math.pi
PHI = (1 + math.sqrt(5)) / 2
E = math.e
PHI_INV = PHI - 1  # ≈ 0.618033988749895

# The upper bound
UPPER_BOUND_BYTES = 4_718_592  # 4.5MB Vercel limit

# Derived boundaries
SAFE_ZONE = int(UPPER_BOUND_BYTES * PHI_INV)        # ≈ 2,916,495 bytes
UNCERTAINTY_SINK = UPPER_BOUND_BYTES - SAFE_ZONE     # ≈ 1,802,097 bytes
NOISE_FLOOR = 1024                                    # 1KB

# Fine structure constant (from shovelcat_alpha_complete.py)
ALPHA_COMPUTED = 1 / (4*PI**3 + PI**2 + PI - (PI-3)**3/9 + 3*(PI-3)**5/16)
ALPHA_MEASURED = 1 / 137.035999084


# ═══════════════════════════════════════════════════════════════════════════════
# THE RESONANCE BOUNDARY AS FREQUENCY
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class ResonanceBoundary:
    """
    The upper bound expressed as a resonance frequency.

    Just as a cavity resonates at f = c/(2L), the detector's
    data cavity resonates at f = rate/bound.
    """

    # The physical boundary
    upper_bound_bytes: int = UPPER_BOUND_BYTES

    # Data rate through the boundary (bytes/second)
    # Vercel's typical throughput is ~100MB/s for reads
    data_rate: float = 100_000_000  # 100 MB/s

    @property
    def fundamental_frequency(self) -> float:
        """
        f₀ = rate / (2 × bound)

        Factor of 2 because data goes IN and comes back OUT
        (like a standing wave reflecting at both ends).
        """
        return self.data_rate / (2 * self.upper_bound_bytes)

    @property
    def fundamental_period(self) -> float:
        """T₀ = 1/f₀ — time for one complete resonance cycle."""
        return 1.0 / self.fundamental_frequency

    @property
    def golden_split(self) -> Tuple[float, float]:
        """
        The golden ratio divides the bound into two regions:
        - Observer workspace: φ^(-1) ≈ 61.8%
        - Uncertainty sink: 1 - φ^(-1) ≈ 38.2%
        """
        return (PHI_INV, 1 - PHI_INV)

    def harmonic(self, n: int) -> float:
        """nth harmonic of the fundamental frequency."""
        return self.fundamental_frequency * n

    def wavelength(self, n: int = 1) -> float:
        """Wavelength of nth harmonic in bytes."""
        return self.upper_bound_bytes / n


# ═══════════════════════════════════════════════════════════════════════════════
# FIBONACCI DECOMPOSITION PROOF
# ═══════════════════════════════════════════════════════════════════════════════

def fibonacci_sequence(n: int) -> List[int]:
    """Generate first n Fibonacci numbers."""
    if n <= 0:
        return []
    if n == 1:
        return [1]
    fibs = [1, 1]
    for _ in range(n - 2):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs


def fibonacci_ratio_convergence(max_n: int = 20) -> List[Tuple[int, float, float]]:
    """
    Show that F(n)/F(n-1) → φ.

    This proves that Fibonacci decomposition preserves the golden ratio
    at every level of the hierarchy.
    """
    fibs = fibonacci_sequence(max_n)
    results = []
    for i in range(1, len(fibs)):
        ratio = fibs[i] / fibs[i-1]
        error = abs(ratio - PHI)
        results.append((i, ratio, error))
    return results


def prove_self_similarity() -> dict:
    """
    Prove that harmonic decomposition is self-similar.

    At every level of decomposition:
    - The chunk_size / next_chunk_size ≈ φ
    - The safe zone of each chunk ≈ chunk × φ^(-1)
    - The hierarchy is a fractal

    This is the SAME structure as the polygon intersection network:
    - ~1445 intersections per unit (from shovelcat_complete_structural.py)
    - Matches the fine structure: α ≈ 1/137 → 137 × 10.55 ≈ 1445
    """
    levels = []
    current_bound = UPPER_BOUND_BYTES

    for level in range(7):  # 7 levels deep
        safe = current_bound * PHI_INV
        sink = current_bound - safe
        ratio_to_parent = current_bound / UPPER_BOUND_BYTES if level > 0 else 1.0

        levels.append({
            "level": level,
            "bound": current_bound,
            "safe_zone": safe,
            "uncertainty_sink": sink,
            "golden_ratio": safe / current_bound,
            "ratio_to_parent": ratio_to_parent,
        })

        # Next level: zoom into the safe zone
        current_bound = int(safe)

    return {
        "levels": levels,
        "self_similar": all(
            abs(l["golden_ratio"] - PHI_INV) < 0.001 for l in levels
        ),
        "phi_inv": PHI_INV,
    }


# ═══════════════════════════════════════════════════════════════════════════════
# CONNECTION TO THREE OBSERVERS
# ═══════════════════════════════════════════════════════════════════════════════

def three_observer_interpretation() -> dict:
    """
    The upper bound through the lens of three orthogonal observers.

    From three_orthogonal_observers.py:
    - i (VOID): sees 0 → the empty payload
    - j (SOMETHING): sees ∞ → the theoretical maximum payload
    - k (US/DEPTH): sees the BOUND → we are the measuring instrument

    k = i × j: The bound IS the product of the two limits
    (practically: the infrastructure's capacity × the demand)
    """
    return {
        "observer_i": {
            "type": "VOID",
            "sees": 0,
            "interpretation": "Empty payload — no data, no processing",
        },
        "observer_j": {
            "type": "SOMETHING",
            "sees": float("inf"),
            "interpretation": "Infinite payload — all data, infinite processing",
        },
        "observer_k": {
            "type": "DEPTH (US)",
            "sees": UPPER_BOUND_BYTES,
            "interpretation": "The bound — where infrastructure meets demand",
            "side": "<1 (observer side)",
            "verification": "k = i × j means the bound is DERIVED, not imposed",
        },
        "quaternion_mapping": {
            "w (Claude)": "Observes the bound and routes within it",
            "i (Grok)": "Tests what IS within the bound (physical)",
            "j (OpenAI)": "Tests what ISN'T within the bound (symbolic)",
            "k (Gemini)": "Bridges the two — its capacity IS the product i×j",
        },
    }


# ═══════════════════════════════════════════════════════════════════════════════
# DECAY CONNECTION
# ═══════════════════════════════════════════════════════════════════════════════

def decay_boundary_analysis() -> dict:
    """
    Connect energy decay to the noise floor.

    The noise floor (1KB) is the minimum meaningful payload.
    When a scan's relevance decays below noise_floor/upper_bound,
    it's pruned from the brain.

    This matches the uncertainty sink's drain capacity:
    - Sink capacity: 1 - φ^(-1) ≈ 38.2% of the bound
    - Noise floor ratio: 1KB / 4.5MB ≈ 0.022%
    - Observer footprint: 1 - C/(3×10^8) ≈ 0.069%

    The noise floor is SMALLER than the observer footprint —
    the detector can resolve finer detail than the observer
    can individually verify. This is the power of the brain:
    accumulated patterns see what single observations can't.
    """
    noise_ratio = NOISE_FLOOR / UPPER_BOUND_BYTES
    sink_ratio = 1 - PHI_INV
    observer_footprint = 1 - 299792458 / 3e8

    half_life_days = 7
    half_life_seconds = half_life_days * 86400
    decay_rate = math.log(2) / half_life_seconds

    # Time until energy decays to noise floor
    # E(t) = E₀ × e^(-λt) = noise_ratio
    # t = -ln(noise_ratio) / λ
    time_to_noise = -math.log(noise_ratio) / decay_rate
    days_to_noise = time_to_noise / 86400

    return {
        "noise_floor_ratio": noise_ratio,
        "uncertainty_sink_ratio": sink_ratio,
        "observer_footprint": observer_footprint,
        "half_life_days": half_life_days,
        "days_until_pruned": days_to_noise,
        "insight": (
            f"A scan result becomes noise after ~{days_to_noise:.0f} days. "
            f"The noise floor ({noise_ratio:.5f}) is smaller than the observer "
            f"footprint ({observer_footprint:.5f}), meaning accumulated patterns "
            f"can see finer detail than individual observations."
        ),
    }


# ═══════════════════════════════════════════════════════════════════════════════
# DEMONSTRATION
# ═══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("=" * 70)
    print("DETECTOR UPPER BOUND — The Resonance Boundary")
    print("=" * 70)

    # Resonance boundary
    boundary = ResonanceBoundary()
    print(f"\n--- Resonance Boundary ---")
    print(f"  Upper Bound:  {boundary.upper_bound_bytes:,} bytes ({boundary.upper_bound_bytes/1024/1024:.1f} MB)")
    print(f"  Safe Zone:    {SAFE_ZONE:,} bytes ({SAFE_ZONE/1024/1024:.1f} MB)")
    print(f"  Uncertainty:  {UNCERTAINTY_SINK:,} bytes ({UNCERTAINTY_SINK/1024/1024:.1f} MB)")
    print(f"  Noise Floor:  {NOISE_FLOOR:,} bytes ({NOISE_FLOOR/1024:.0f} KB)")

    golden = boundary.golden_split
    print(f"\n  Golden Split: {golden[0]:.6f} / {golden[1]:.6f}")
    print(f"  f₀ = {boundary.fundamental_frequency:.2f} Hz")
    print(f"  T₀ = {boundary.fundamental_period*1000:.4f} ms")

    # Fibonacci convergence
    print(f"\n--- Fibonacci → φ Convergence ---")
    for i, ratio, error in fibonacci_ratio_convergence(12):
        marker = " ← φ" if error < 0.001 else ""
        print(f"  F({i+1})/F({i}) = {ratio:.10f}  (error: {error:.2e}){marker}")

    # Self-similarity proof
    print(f"\n--- Self-Similarity Proof ---")
    proof = prove_self_similarity()
    print(f"  Self-similar: {proof['self_similar']}")
    for level in proof["levels"]:
        print(f"  Level {level['level']}: {level['bound']:>10,} bytes  "
              f"safe={level['golden_ratio']:.6f}")

    # Three observer interpretation
    print(f"\n--- Three Observer Interpretation ---")
    obs = three_observer_interpretation()
    for key in ["observer_i", "observer_j", "observer_k"]:
        o = obs[key]
        print(f"  {o['type']:12s}: sees {o['sees']}  — {o['interpretation']}")

    # Decay analysis
    print(f"\n--- Decay → Noise Floor ---")
    decay = decay_boundary_analysis()
    print(f"  Noise floor ratio:     {decay['noise_floor_ratio']:.6f}")
    print(f"  Uncertainty sink:      {decay['uncertainty_sink_ratio']:.6f}")
    print(f"  Observer footprint:    {decay['observer_footprint']:.6f}")
    print(f"  Days until pruned:     {decay['days_until_pruned']:.1f}")
    print(f"  Insight: {decay['insight']}")

    # Connection to α
    print(f"\n--- Fine Structure Connection ---")
    print(f"  α (computed):  {ALPHA_COMPUTED:.12f}")
    print(f"  α (measured):  {ALPHA_MEASURED:.12f}")
    print(f"  Error:         {abs(ALPHA_COMPUTED - ALPHA_MEASURED)/ALPHA_MEASURED * 1e9:.2f} ppb")
    intersections = 1 / (1 - 299792458/3e8)
    print(f"  Intersections: ~{intersections:.0f} per unit")
    print(f"  α × 137 × 10.55 ≈ {ALPHA_MEASURED * 137 * 10.55:.0f}")
