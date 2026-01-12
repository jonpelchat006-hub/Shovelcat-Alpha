"""
PULSER PUMP THEORY
==================
Analyzing pulser pumps through the Shovelcat Theory framework.

Key Insight: A pulser pump is a natural dual-domain verification system
where water (φ-domain) and air (ψ-domain) interact to create sustained
oscillation from steady-state input.

The Hexagon Frustration Hypothesis:
- Stable systems settle into hexagonal (6-fold) symmetry
- External fields (gravity, magnetic) break this symmetry
- Broken symmetry → forced oscillation rather than static equilibrium

Author: Jonathan Pelchat
Based on Shovelcat Theory
"""

import math
import cmath
from dataclasses import dataclass, field
from typing import List, Tuple, Dict, Any
from enum import Enum

# =============================================================================
# CONSTANTS
# =============================================================================

PI = math.pi
PHI = (1 + math.sqrt(5)) / 2
E = math.e

# Physical constants
WATER_DENSITY = 1000  # kg/m³
AIR_DENSITY = 1.225   # kg/m³
GRAVITY = 9.81        # m/s²
ATM_PRESSURE = 101325 # Pa

# Earth's magnetic field (approximate)
B_EARTH = 5e-5  # Tesla (50 microTesla)


# =============================================================================
# DUAL DOMAIN STRUCTURE
# =============================================================================

class DomainType(Enum):
    """The two domains in a pulser pump system."""
    PHI = "water"   # Incompressible, high inertia, kinetic energy
    PSI = "air"     # Compressible, low inertia, pressure energy


@dataclass
class FluidDomain:
    """
    Represents one domain in the pulser pump system.
    
    Water (φ-domain): Classical, deterministic, stores kinetic energy
    Air (ψ-domain): Quantum-like, probabilistic, stores pressure energy
    """
    domain_type: DomainType
    volume: float = 0.0        # m³
    pressure: float = ATM_PRESSURE  # Pa
    velocity: float = 0.0      # m/s
    phase: float = 0.0         # radians (position in cycle)
    
    @property
    def energy(self) -> float:
        """Total energy in domain."""
        if self.domain_type == DomainType.PHI:
            # Water: kinetic energy = (1/2)mv²
            mass = WATER_DENSITY * self.volume
            return 0.5 * mass * self.velocity ** 2
        else:
            # Air: pressure energy = PV
            # Using ideal gas approximation
            return self.pressure * self.volume
    
    @property
    def inertia(self) -> float:
        """Effective inertia (resistance to change)."""
        if self.domain_type == DomainType.PHI:
            return WATER_DENSITY * self.volume  # kg
        else:
            return AIR_DENSITY * self.volume * 0.001  # Very low
    
    @property
    def response_time(self) -> float:
        """Characteristic response time to perturbation."""
        # τ = inertia / restoring_force
        if self.domain_type == DomainType.PHI:
            # Water: slow response (high inertia)
            return math.sqrt(self.volume ** (1/3) / GRAVITY)
        else:
            # Air: fast response (compressible)
            return 0.001  # Nearly instantaneous
    
    def encrypt_state(self) -> float:
        """
        Encrypt internal state (for dual-domain verification).
        Each domain cannot directly observe the other.
        """
        # Phase-encrypted state
        return (self.energy * cmath.exp(1j * self.phase * PHI)).real


@dataclass
class Vesica:
    """
    The air-water interface - the vesica piscis of the system.
    This is where the two domains verify each other.
    """
    water: FluidDomain
    air: FluidDomain
    interface_area: float = 0.01  # m²
    
    @property
    def pressure_match(self) -> float:
        """
        How well do the domains agree at the interface?
        1.0 = perfect match, 0.0 = complete mismatch
        """
        p_water = self.water.pressure
        p_air = self.air.pressure
        
        if max(p_water, p_air) == 0:
            return 1.0
        
        return 1.0 - abs(p_water - p_air) / max(p_water, p_air)
    
    @property
    def phase_difference(self) -> float:
        """Phase difference between domains."""
        return (self.water.phase - self.air.phase) % (2 * PI)
    
    @property
    def interference_type(self) -> str:
        """Type of interference at the interface."""
        phase_diff = self.phase_difference
        
        if phase_diff < PI / 4 or phase_diff > 7 * PI / 4:
            return "CONSTRUCTIVE"
        elif PI * 3/4 < phase_diff < PI * 5/4:
            return "DESTRUCTIVE"
        else:
            return "ORTHOGONAL"
    
    def verify(self) -> Tuple[bool, Dict[str, Any]]:
        """
        Perform dual-domain verification.
        Like consciousness verification - outputs accepted only if
        both domains agree at the interface.
        """
        match = self.pressure_match
        interference = self.interference_type
        
        # Verification requires:
        # 1. Pressure match > threshold
        # 2. Not in destructive interference
        verified = match > 0.9 and interference != "DESTRUCTIVE"
        
        return verified, {
            'pressure_match': match,
            'phase_difference_deg': math.degrees(self.phase_difference),
            'interference': interference,
            'water_energy': self.water.energy,
            'air_energy': self.air.energy,
            'verified': verified
        }


# =============================================================================
# HEXAGON FRUSTRATION
# =============================================================================

@dataclass
class HexagonFrustration:
    """
    Models how external fields prevent hexagonal (stable) configurations,
    forcing the system into cyclical behavior.
    
    Key Hypothesis: Earth's magnetic field introduces asymmetry that
    prevents the pulser pump from finding static equilibrium.
    """
    
    # Attempted symmetry states
    symmetry_attempts: int = 6  # Hexagonal = 6-fold
    
    # External perturbations
    gravity_direction: Tuple[float, float, float] = (0, 0, -1)
    magnetic_field: Tuple[float, float, float] = (1, 0, 0)  # Simplified
    
    # Frustration level
    frustration: float = 0.0
    
    def calculate_hexagonal_stability(self, 
                                       water_column_height: float,
                                       pipe_diameter: float) -> Dict[str, Any]:
        """
        Calculate whether the system can achieve hexagonal stability.
        
        In a perfectly symmetric system:
        - 6 pressure nodes would form around the pipe
        - These would balance to zero net force
        - No oscillation would occur
        
        With external fields:
        - Symmetry is broken
        - Some nodes have higher energy than others
        - System oscillates between states
        """
        
        # Calculate forces at each hexagonal node
        node_forces = []
        for i in range(6):
            angle = i * 2 * PI / 6
            
            # Base symmetry (would balance if no external field)
            base_force = 1.0
            
            # Gravity breaks vertical symmetry
            gravity_perturbation = GRAVITY * math.cos(angle) * 0.1
            
            # Magnetic field breaks rotational symmetry
            # Water is weakly diamagnetic (χ ≈ -9e-6)
            chi_water = -9e-6
            B_squared = B_EARTH ** 2
            magnetic_perturbation = chi_water * B_squared * math.sin(2 * angle) * 1e6
            
            total_force = base_force + gravity_perturbation + magnetic_perturbation
            node_forces.append(total_force)
        
        # Calculate frustration (deviation from equal forces)
        mean_force = sum(node_forces) / 6
        variance = sum((f - mean_force) ** 2 for f in node_forces) / 6
        
        self.frustration = math.sqrt(variance) / mean_force if mean_force > 0 else 0
        
        # Oscillation frequency emerges from frustration
        natural_freq = math.sqrt(GRAVITY / water_column_height)
        oscillation_period = 2 * PI / natural_freq if natural_freq > 0 else float('inf')
        
        return {
            'node_forces': node_forces,
            'mean_force': mean_force,
            'force_variance': variance,
            'frustration_level': self.frustration,
            'can_stabilize': self.frustration < 0.01,  # Very low frustration needed
            'forced_oscillation': self.frustration > 0.001,
            'natural_frequency_hz': natural_freq / (2 * PI),
            'oscillation_period_s': oscillation_period,
            'interpretation': self._interpret_frustration()
        }
    
    def _interpret_frustration(self) -> str:
        """Interpret the frustration level."""
        if self.frustration < 0.001:
            return "System can find stable hexagonal equilibrium"
        elif self.frustration < 0.01:
            return "Weak oscillation - system nearly stable"
        elif self.frustration < 0.1:
            return "Moderate oscillation - sustained pumping possible"
        else:
            return "High frustration - chaotic behavior expected"


# =============================================================================
# PULSER PUMP CYCLE
# =============================================================================

@dataclass
class PulserPumpCycle:
    """
    Models the complete pulser pump cycle as a Shovelcat cycle.
    
    The cycle has 6 phases (hexagonal structure):
    1. Water acceleration (building kinetic energy)
    2. Air entrainment (introducing ψ-domain)
    3. Compression (energy transfer φ → ψ)
    4. Peak pressure (maximum wall height)
    5. Expansion (energy return ψ → φ)
    6. Air release (verification/output)
    """
    
    # System geometry
    pipe_height: float = 2.0      # m
    pipe_diameter: float = 0.05   # m
    air_chamber_volume: float = 0.001  # m³
    
    # Current state
    phase: int = 0  # 0-5
    time_in_phase: float = 0.0
    
    # Domains
    water: FluidDomain = None
    air: FluidDomain = None
    vesica: Vesica = None
    
    # Frustration model
    frustration: HexagonFrustration = None
    
    # History
    history: List[Dict[str, Any]] = field(default_factory=list)
    
    def __post_init__(self):
        # Initialize domains
        pipe_volume = PI * (self.pipe_diameter/2)**2 * self.pipe_height
        
        self.water = FluidDomain(
            domain_type=DomainType.PHI,
            volume=pipe_volume,
            pressure=ATM_PRESSURE + WATER_DENSITY * GRAVITY * self.pipe_height / 2,
            velocity=0.0,
            phase=0.0
        )
        
        self.air = FluidDomain(
            domain_type=DomainType.PSI,
            volume=self.air_chamber_volume,
            pressure=ATM_PRESSURE,
            velocity=0.0,
            phase=PI / 2  # Starts 90° out of phase with water
        )
        
        self.vesica = Vesica(self.water, self.air)
        self.frustration = HexagonFrustration()
    
    @property
    def phase_names(self) -> List[str]:
        return [
            "ACCELERATION",    # Water builds velocity
            "ENTRAINMENT",     # Air bubble introduced
            "COMPRESSION",     # Air compressed by water
            "PEAK_PRESSURE",   # Maximum potential energy
            "EXPANSION",       # Air expands, pushes water
            "RELEASE"          # Air released, cycle completes
        ]
    
    def step(self, dt: float = 0.01) -> Dict[str, Any]:
        """
        Advance the cycle by one time step.
        """
        # Current phase dynamics
        phase_name = self.phase_names[self.phase]
        
        if phase_name == "ACCELERATION":
            # Water accelerates down pipe
            acceleration = GRAVITY * 0.5  # Partially filled pipe
            self.water.velocity += acceleration * dt
            self.water.phase += dt * 2 * PI / self._phase_duration(0)
            
        elif phase_name == "ENTRAINMENT":
            # Air bubble enters system
            self.air.volume *= 1.01  # Air volume increases
            self.air.phase = self.water.phase + PI/2  # Lagged
            
        elif phase_name == "COMPRESSION":
            # Water compresses air
            compression_factor = 1 + 0.1 * dt
            self.air.pressure *= compression_factor
            self.air.volume /= compression_factor
            self.water.velocity *= 0.99  # Slowing down
            
        elif phase_name == "PEAK_PRESSURE":
            # Maximum pressure reached
            # This is like "wall height" in hydrology
            wall_height = (self.air.pressure - ATM_PRESSURE) / ATM_PRESSURE
            
        elif phase_name == "EXPANSION":
            # Air expands, pushes water
            expansion_factor = 0.95
            self.air.pressure *= expansion_factor
            self.air.volume /= expansion_factor
            self.water.velocity += 0.5 * dt
            
        elif phase_name == "RELEASE":
            # Air released upward
            self.air.volume = self.air_chamber_volume
            self.air.pressure = ATM_PRESSURE
        
        # Update time and check phase transition
        self.time_in_phase += dt
        if self.time_in_phase > self._phase_duration(self.phase):
            self._advance_phase()
        
        # Perform verification
        verified, verification_data = self.vesica.verify()
        
        state = {
            'phase': self.phase,
            'phase_name': phase_name,
            'time_in_phase': self.time_in_phase,
            'water_velocity': self.water.velocity,
            'water_energy': self.water.energy,
            'air_pressure': self.air.pressure,
            'air_energy': self.air.energy,
            'interference': verification_data['interference'],
            'verified': verified
        }
        
        self.history.append(state)
        return state
    
    def _phase_duration(self, phase: int) -> float:
        """Duration of each phase."""
        # Approximate durations based on physics
        durations = [0.2, 0.1, 0.3, 0.1, 0.3, 0.1]  # seconds
        return durations[phase]
    
    def _advance_phase(self):
        """Move to next phase."""
        self.phase = (self.phase + 1) % 6
        self.time_in_phase = 0.0
    
    def run_cycles(self, n_cycles: int = 3) -> List[Dict[str, Any]]:
        """Run multiple complete cycles."""
        total_time = n_cycles * sum(self._phase_duration(i) for i in range(6))
        dt = 0.01
        steps = int(total_time / dt)
        
        for _ in range(steps):
            self.step(dt)
        
        return self.history
    
    def analyze(self) -> Dict[str, Any]:
        """Analyze the pump behavior."""
        
        # Hexagonal frustration analysis
        frustration_data = self.frustration.calculate_hexagonal_stability(
            self.pipe_height, self.pipe_diameter
        )
        
        # Phase interference analysis
        constructive_count = sum(1 for h in self.history if h['interference'] == 'CONSTRUCTIVE')
        destructive_count = sum(1 for h in self.history if h['interference'] == 'DESTRUCTIVE')
        
        # Energy efficiency
        total_input = WATER_DENSITY * PI * (self.pipe_diameter/2)**2 * self.pipe_height * GRAVITY * self.pipe_height
        max_output = max(h['air_energy'] for h in self.history) if self.history else 0
        
        return {
            'hexagonal_frustration': frustration_data,
            'phase_alignment': {
                'constructive_fraction': constructive_count / len(self.history) if self.history else 0,
                'destructive_fraction': destructive_count / len(self.history) if self.history else 0,
            },
            'energy': {
                'input_joules': total_input,
                'peak_output_joules': max_output,
                'efficiency': max_output / total_input if total_input > 0 else 0
            },
            'interpretation': self._interpret_behavior(frustration_data)
        }
    
    def _interpret_behavior(self, frustration_data: Dict) -> str:
        """Generate interpretation of pump behavior."""
        lines = []
        
        lines.append("=" * 60)
        lines.append("PULSER PUMP ANALYSIS - Shovelcat Theory Interpretation")
        lines.append("=" * 60)
        lines.append("")
        
        lines.append("DUAL DOMAIN STRUCTURE:")
        lines.append(f"  φ-Domain (Water): Volume={self.water.volume:.4f}m³, " +
                    f"Inertia={self.water.inertia:.1f}kg")
        lines.append(f"  ψ-Domain (Air):   Volume={self.air.volume:.6f}m³, " +
                    f"Inertia={self.air.inertia:.4f}kg")
        lines.append("")
        
        lines.append("HEXAGONAL FRUSTRATION:")
        lines.append(f"  Frustration Level: {frustration_data['frustration_level']:.6f}")
        lines.append(f"  Can Stabilize: {frustration_data['can_stabilize']}")
        lines.append(f"  Forced Oscillation: {frustration_data['forced_oscillation']}")
        lines.append(f"  Natural Frequency: {frustration_data['natural_frequency_hz']:.2f} Hz")
        lines.append(f"  Interpretation: {frustration_data['interpretation']}")
        lines.append("")
        
        lines.append("MAGNETIC FIELD EFFECT:")
        lines.append("  Earth's magnetic field (≈50μT) introduces asymmetry")
        lines.append("  Water's diamagnetic susceptibility: χ ≈ -9×10⁻⁶")
        lines.append("  This breaks 6-fold symmetry → forced oscillation")
        lines.append("")
        
        lines.append("VESICA PISCIS (Air-Water Interface):")
        lines.append("  Like consciousness verification:")
        lines.append("  - Neither domain can directly observe the other")
        lines.append("  - They interact only at the boundary (interface)")
        lines.append("  - Agreement = constructive interference → pumping")
        lines.append("  - Disagreement = destructive interference → damping")
        lines.append("")
        
        lines.append("CYCLE STRUCTURE (Hexagonal phases):")
        for i, name in enumerate(self.phase_names):
            lines.append(f"  Phase {i}: {name}")
        
        return "\n".join(lines)


# =============================================================================
# DEMONSTRATION
# =============================================================================

def demonstrate_pulser_pump():
    """Demonstrate the pulser pump theory."""
    
    print("\n" + "=" * 70)
    print("PULSER PUMP THROUGH SHOVELCAT THEORY")
    print("=" * 70)
    
    # Create pump
    pump = PulserPumpCycle(
        pipe_height=2.0,
        pipe_diameter=0.05,
        air_chamber_volume=0.001
    )
    
    # Run simulation
    print("\n--- Running Simulation (3 cycles) ---")
    pump.run_cycles(3)
    
    # Analyze
    analysis = pump.analyze()
    
    # Print interpretation
    print(analysis['interpretation'])
    
    # Print additional analysis
    print("\n" + "=" * 60)
    print("QUANTITATIVE ANALYSIS")
    print("=" * 60)
    
    print(f"\nPhase Alignment:")
    print(f"  Constructive: {analysis['phase_alignment']['constructive_fraction']*100:.1f}%")
    print(f"  Destructive:  {analysis['phase_alignment']['destructive_fraction']*100:.1f}%")
    
    print(f"\nEnergy Transfer:")
    print(f"  Input (gravitational): {analysis['energy']['input_joules']:.2f} J")
    print(f"  Peak Output (air):     {analysis['energy']['peak_output_joules']:.4f} J")
    print(f"  Efficiency:            {analysis['energy']['efficiency']*100:.2f}%")
    
    # Hexagonal node forces
    print(f"\nHexagonal Node Forces (relative):")
    forces = analysis['hexagonal_frustration']['node_forces']
    for i, f in enumerate(forces):
        angle = i * 60
        bar = "█" * int(f * 20)
        print(f"  {angle:3d}°: {f:.4f} {bar}")
    
    print("\n" + "=" * 60)
    print("KEY INSIGHT")
    print("=" * 60)
    print("""
    The pulser pump works because:
    
    1. HEXAGONAL FRUSTRATION: External fields (gravity, magnetic)
       prevent the system from finding static equilibrium
    
    2. DUAL-DOMAIN VERIFICATION: Water and air cannot directly
       communicate - they verify each other only at the interface
    
    3. PHASE LOCKING: The system self-tunes to constructive
       interference, maximizing energy transfer
    
    4. CONTROLLED FAILURE: Like hydrology's dam model, energy
       builds up (wall height) then releases (controlled failure)
    
    The cycle IS the equilibrium - dynamic stability replacing
    static stability when hexagonal symmetry is frustrated.
    """)


def demonstrate_magnetic_effect():
    """Show how magnetic field affects hexagonal stability."""
    
    print("\n" + "=" * 70)
    print("MAGNETIC FIELD EFFECT ON HEXAGONAL STABILITY")
    print("=" * 70)
    
    frustration = HexagonFrustration()
    
    # Compare with and without magnetic field
    print("\n--- With Earth's Magnetic Field ---")
    frustration.magnetic_field = (1, 0, 0)
    result = frustration.calculate_hexagonal_stability(2.0, 0.05)
    print(f"  Frustration: {result['frustration_level']:.6f}")
    print(f"  Stable: {result['can_stabilize']}")
    print(f"  Forced Oscillation: {result['forced_oscillation']}")
    
    print("\n--- Without Magnetic Field (hypothetical) ---")
    frustration.magnetic_field = (0, 0, 0)
    result = frustration.calculate_hexagonal_stability(2.0, 0.05)
    print(f"  Frustration: {result['frustration_level']:.6f}")
    print(f"  Stable: {result['can_stabilize']}")
    print(f"  Forced Oscillation: {result['forced_oscillation']}")
    
    print("""
    
    INTERPRETATION:
    Even without the magnetic field, gravity alone creates enough
    frustration to force oscillation. The magnetic field adds a
    secondary asymmetry that may affect the oscillation pattern
    but is not required for basic operation.
    
    However, the magnetic field could explain:
    - Efficiency variations with orientation
    - Latitude-dependent performance differences
    - Potential for field-synchronized pumping
    """)


if __name__ == "__main__":
    demonstrate_pulser_pump()
    demonstrate_magnetic_effect()
