"""
Circuit Topology — Visual Rendering of Entity Circuit Bundles

Renders PathBundles as visual maps showing:
  - The social circuit ring (People→Hardware→Infra→Software→Content→People)
  - Each entity's circuit paths traced through the ring
  - +L (light) and -L (dark) polarity per path
  - Organism level badge and evolution progress
  - Convergence points where production meets user goals
  - Bundle comparison between two entities (shared infrastructure)

ASCII, SVG coordinate generation, and CSS style output for the
Shovelcat-AI production frontend.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple
import math

# ─── Constants ───────────────────────────────────────────────────────────

PHI = 1.618033988749895
PHI_INV = 0.6180339887498949
PI = math.pi
TAU = 2 * PI

COLOR_DIMENSIONS = ["RED", "ORANGE", "GREEN", "BLUE", "YELLOW", "CYAN", "VIOLET"]

# CSS color values for each domain
COLOR_CSS = {
    "RED":    "#e74c3c",
    "ORANGE": "#e67e22",
    "GREEN":  "#2ecc71",
    "BLUE":   "#3498db",
    "YELLOW": "#f1c40f",
    "CYAN":   "#1abc9c",
    "VIOLET": "#9b59b6",
}

# Organism level visual properties
ORGANISM_GLYPHS = {
    "ELEMENT":  "ite",   # mineral
    "VIRUS":    "vrs",   # parasitic
    "BACTERIA": "bct",   # single cell
    "PLANT":    "plt",   # rooted
    "FISH":     "fsh",   # mobile
    "RABBIT":   "rbt",   # social
    "WOLF":     "wlf",   # strategic
    "DOLPHIN":  "dph",   # bridging
    "OCTOPUS":  "oct",   # ecosystem
}

ORGANISM_EMOJI_MAP = {
    "ELEMENT":  "ite",
    "VIRUS":    "vrs",
    "BACTERIA": "bct",
    "PLANT":    "plt",
    "FISH":     "fsh",
    "RABBIT":   "rbt",
    "WOLF":     "wlf",
    "DOLPHIN":  "dph",
    "OCTOPUS":  "oct",
}

# Social circuit element positions on a ring (angles in radians)
ELEMENT_ANGLES = {
    "PEOPLE":         0,
    "HARDWARE":       TAU / 5,
    "INFRASTRUCTURE": 2 * TAU / 5,
    "SOFTWARE":       3 * TAU / 5,
    "CONTENT":        4 * TAU / 5,
}

ELEMENT_LABELS = {
    "PEOPLE":         "People",
    "HARDWARE":       "Hardware",
    "INFRASTRUCTURE": "Infra",
    "SOFTWARE":       "Software",
    "CONTENT":        "Content",
}


# ─── Ring Geometry ───────────────────────────────────────────────────────

@dataclass
class RingPoint:
    """A point on the social circuit ring."""
    x: float
    y: float
    angle: float
    element: str
    label: str


def ring_positions(center_x: float, center_y: float, radius: float) -> List[RingPoint]:
    """Calculate the 5 element positions on the circuit ring."""
    points = []
    for name, angle in ELEMENT_ANGLES.items():
        # Rotate so PEOPLE is at top (subtract π/2)
        adj_angle = angle - PI / 2
        x = center_x + radius * math.cos(adj_angle)
        y = center_y + radius * math.sin(adj_angle)
        points.append(RingPoint(
            x=x, y=y,
            angle=angle,
            element=name,
            label=ELEMENT_LABELS[name],
        ))
    return points


# ─── Circuit Path Rendering ─────────────────────────────────────────────

@dataclass
class RenderedArc:
    """A single arc segment in a rendered circuit."""
    start: RingPoint
    end: RingPoint
    color: str           # CSS color
    polarity: str        # "light" or "dark"
    opacity: float       # Health-based opacity
    stroke_width: float  # Value-based thickness
    is_complete: bool    # Part of a complete circuit?


@dataclass
class RenderedBundle:
    """Complete visual representation of an entity's circuit bundle."""
    entity_name: str
    organism_level: str
    organism_glyph: str
    arcs: List[RenderedArc]
    health_percent: float
    healthy_count: int
    total_count: int
    color_signature: Dict[str, float]
    evolution_progress: float   # 0.0 to 1.0 toward next level
    next_level: Optional[str]
    convergence_markers: List[Tuple[float, float, str]]  # (x, y, label)


def render_bundle(
    entity_name: str,
    organism_level: str,
    circuits: List[Dict],  # [{color_domain, light_phase, dark_phase, light_value, dark_value, is_complete, health_ratio}]
    convergence_points: List[Dict] = None,
    center_x: float = 200,
    center_y: float = 200,
    radius: float = 150,
    next_level: Optional[str] = None,
    next_level_threshold: int = 0,
    healthy_count: int = 0,
) -> RenderedBundle:
    """
    Render an entity's circuit bundle as visual arcs on the ring.

    Each circuit becomes a set of arcs (one per segment traversed).
    +L arcs are solid, -L arcs are dashed.
    Healthy circuits are full opacity, sick ones are faded.
    """
    ring = ring_positions(center_x, center_y, radius)
    arcs = []

    # Each circuit gets rendered as arcs around the ring
    for i, circuit in enumerate(circuits):
        color = COLOR_CSS.get(circuit["color_domain"].upper(), "#888")
        health = circuit.get("health_ratio", 0.5)
        is_complete = circuit.get("is_complete", False)

        # Offset radius slightly per circuit so they don't overlap
        offset = (i - len(circuits) / 2) * 3

        # Light arcs (+L)
        light_coverage = circuit.get("light_phase", 0) / TAU
        segments_lit = int(light_coverage * 5)
        for s in range(min(segments_lit, 5)):
            start_pt = ring[s]
            end_pt = ring[(s + 1) % 5]
            arcs.append(RenderedArc(
                start=RingPoint(
                    x=start_pt.x + offset * math.cos(start_pt.angle),
                    y=start_pt.y + offset * math.sin(start_pt.angle),
                    angle=start_pt.angle,
                    element=start_pt.element,
                    label=start_pt.label,
                ),
                end=RingPoint(
                    x=end_pt.x + offset * math.cos(end_pt.angle),
                    y=end_pt.y + offset * math.sin(end_pt.angle),
                    angle=end_pt.angle,
                    element=end_pt.element,
                    label=end_pt.label,
                ),
                color=color,
                polarity="light",
                opacity=min(1.0, health + 0.2) if is_complete else health * 0.6,
                stroke_width=max(1, circuit.get("light_value", 1) / 5),
                is_complete=is_complete,
            ))

        # Dark arcs (-L) — rendered as thinner, lower opacity
        dark_coverage = circuit.get("dark_phase", 0) / TAU
        segments_dark = int(dark_coverage * 5)
        for s in range(min(segments_dark, 5)):
            start_pt = ring[s]
            end_pt = ring[(s + 1) % 5]
            arcs.append(RenderedArc(
                start=start_pt,
                end=end_pt,
                color=color,
                polarity="dark",
                opacity=0.3,
                stroke_width=max(0.5, circuit.get("dark_value", 0.5) / 8),
                is_complete=False,
            ))

    # Convergence markers
    markers = []
    if convergence_points:
        for cp in convergence_points:
            element_name = cp.get("element", "PEOPLE")
            angle = ELEMENT_ANGLES.get(element_name, 0) - PI / 2
            marker_radius = radius + 20
            mx = center_x + marker_radius * math.cos(angle)
            my = center_y + marker_radius * math.sin(angle)
            label = cp.get("alignment_label", "?")
            markers.append((mx, my, label))

    # Color signature
    color_sig = {}
    for circuit in circuits:
        cd = circuit["color_domain"].upper()
        weight = circuit.get("health_ratio", 0.5) * circuit.get("light_phase", 0) / TAU
        color_sig[cd] = color_sig.get(cd, 0) + weight
    total_sig = sum(color_sig.values())
    if total_sig > 0:
        color_sig = {k: v / total_sig for k, v in color_sig.items()}

    # Evolution progress
    if next_level and next_level_threshold > 0:
        evolution_progress = min(1.0, healthy_count / next_level_threshold)
    else:
        evolution_progress = 1.0

    return RenderedBundle(
        entity_name=entity_name,
        organism_level=organism_level,
        organism_glyph=ORGANISM_GLYPHS.get(organism_level, "?"),
        arcs=arcs,
        health_percent=sum(c.get("health_ratio", 0.5) for c in circuits) / max(1, len(circuits)),
        healthy_count=healthy_count,
        total_count=len(circuits),
        color_signature=color_sig,
        evolution_progress=evolution_progress,
        next_level=next_level,
        convergence_markers=markers,
    )


# ─── ASCII Rendering ────────────────────────────────────────────────────

def ascii_ring(bundle: RenderedBundle, width: int = 60, height: int = 30) -> str:
    """
    Render a circuit bundle as ASCII art.

    Shows the 5-element ring with circuit arcs and organism badge.
    """
    # Create canvas
    canvas = [[' ' for _ in range(width)] for _ in range(height)]

    cx, cy = width // 2, height // 2
    rx, ry = width // 3, height // 3

    # Draw ring outline
    for angle_step in range(100):
        angle = angle_step * TAU / 100
        x = int(cx + rx * math.cos(angle))
        y = int(cy + ry * math.sin(angle))
        if 0 <= x < width and 0 <= y < height:
            if canvas[y][x] == ' ':
                canvas[y][x] = '·'

    # Place element labels
    for name, angle in ELEMENT_ANGLES.items():
        adj = angle - PI / 2
        x = int(cx + (rx + 2) * math.cos(adj))
        y = int(cy + (ry + 1) * math.sin(adj))
        label = ELEMENT_LABELS[name][:3].upper()
        for i, ch in enumerate(label):
            px = x + i - len(label) // 2
            if 0 <= px < width and 0 <= y < height:
                canvas[y][px] = ch

    # Draw circuit arcs (simplified — mark traversed segments)
    arc_chars = {'light': '═', 'dark': '─'}
    for arc in bundle.arcs:
        # Draw a line between start and end points (scaled to ASCII)
        sx = int(cx + rx * math.cos(arc.start.angle - PI / 2))
        sy = int(cy + ry * math.sin(arc.start.angle - PI / 2))
        ex = int(cx + rx * math.cos(arc.end.angle - PI / 2))
        ey = int(cy + ry * math.sin(arc.end.angle - PI / 2))

        # Bresenham-ish line
        steps = max(abs(ex - sx), abs(ey - sy), 1)
        char = arc_chars.get(arc.polarity, '·')
        for step in range(steps + 1):
            t = step / steps
            px = int(sx + t * (ex - sx))
            py = int(sy + t * (ey - sy))
            if 0 <= px < width and 0 <= py < height:
                canvas[py][px] = char

    # Place organism badge at center
    badge = f"[{bundle.organism_glyph}]"
    bx = cx - len(badge) // 2
    for i, ch in enumerate(badge):
        if 0 <= bx + i < width and 0 <= cy < height:
            canvas[cy][bx + i] = ch

    # Health indicator below badge
    health_str = f"{bundle.health_percent:.0%}"
    hx = cx - len(health_str) // 2
    for i, ch in enumerate(health_str):
        if 0 <= hx + i < width and 0 <= cy + 1 < height:
            canvas[cy + 1][hx + i] = ch

    # Circuit count
    count_str = f"{bundle.healthy_count}/{bundle.total_count}"
    countx = cx - len(count_str) // 2
    for i, ch in enumerate(count_str):
        if 0 <= countx + i < width and 0 <= cy + 2 < height:
            canvas[cy + 2][countx + i] = ch

    # Compile
    header = f"  {bundle.entity_name} — {bundle.organism_level}"
    lines = [header, "  " + "─" * (width - 4)]
    for row in canvas:
        lines.append("  " + "".join(row))
    lines.append("  " + "─" * (width - 4))

    # Color bar
    sig = bundle.color_signature
    bar_width = width - 6
    bar = "  ["
    for color in COLOR_DIMENSIONS:
        portion = sig.get(color, 0)
        chars = max(0, int(portion * bar_width))
        bar += color[0] * chars
    bar += " " * (bar_width - sum(max(0, int(sig.get(c, 0) * bar_width)) for c in COLOR_DIMENSIONS))
    bar += "]"
    lines.append(bar)

    # Evolution progress
    if bundle.next_level:
        prog = bundle.evolution_progress
        filled = int(prog * 20)
        evo_bar = f"  → {bundle.next_level}: [{'█' * filled}{'░' * (20 - filled)}] {prog:.0%}"
        lines.append(evo_bar)

    return "\n".join(lines)


# ─── CSS Style Generation ───────────────────────────────────────────────

def organism_badge_style(level: str) -> Dict:
    """
    CSS style object for the organism level badge.
    Suitable for React inline styles.
    """
    level_colors = {
        "ELEMENT":  {"bg": "#95a5a6", "fg": "#2c3e50", "border": "none"},
        "VIRUS":    {"bg": "#e74c3c", "fg": "#fff",    "border": "1px dashed #c0392b"},
        "BACTERIA": {"bg": "#f39c12", "fg": "#2c3e50", "border": "1px solid #e67e22"},
        "PLANT":    {"bg": "#27ae60", "fg": "#fff",    "border": "2px solid #2ecc71"},
        "FISH":     {"bg": "#3498db", "fg": "#fff",    "border": "2px solid #2980b9"},
        "RABBIT":   {"bg": "#e67e22", "fg": "#fff",    "border": "2px solid #d35400"},
        "WOLF":     {"bg": "#8e44ad", "fg": "#fff",    "border": "3px solid #9b59b6"},
        "DOLPHIN":  {"bg": "#1abc9c", "fg": "#fff",    "border": "3px double #16a085"},
        "OCTOPUS":  {"bg": "#2c3e50", "fg": "#f1c40f", "border": "3px double #f39c12"},
    }
    config = level_colors.get(level, level_colors["ELEMENT"])
    return {
        "backgroundColor": config["bg"],
        "color": config["fg"],
        "border": config["border"],
        "borderRadius": "12px",
        "padding": "4px 12px",
        "fontSize": "0.85rem",
        "fontWeight": "600",
        "display": "inline-flex",
        "alignItems": "center",
        "gap": "4px",
    }


def circuit_arc_svg_path(
    start_angle: float,
    end_angle: float,
    radius: float,
    cx: float,
    cy: float,
) -> str:
    """Generate SVG arc path data for a circuit segment."""
    # Adjust so PEOPLE is at top
    sa = start_angle - PI / 2
    ea = end_angle - PI / 2

    sx = cx + radius * math.cos(sa)
    sy = cy + radius * math.sin(sa)
    ex = cx + radius * math.cos(ea)
    ey = cy + radius * math.sin(ea)

    # Large arc flag
    diff = ea - sa
    if diff < 0:
        diff += TAU
    large = 1 if diff > PI else 0

    return f"M {sx:.1f} {sy:.1f} A {radius:.1f} {radius:.1f} 0 {large} 1 {ex:.1f} {ey:.1f}"


def bundle_to_svg_data(bundle: RenderedBundle) -> Dict:
    """
    Convert a rendered bundle to SVG-compatible data.
    Returns dict of paths, markers, and text elements.
    """
    cx, cy, r = 200, 200, 150
    ring = ring_positions(cx, cy, r)

    svg_paths = []
    for arc in bundle.arcs:
        path_d = circuit_arc_svg_path(
            arc.start.angle, arc.end.angle, r, cx, cy
        )
        svg_paths.append({
            "d": path_d,
            "stroke": arc.color,
            "strokeWidth": arc.stroke_width,
            "opacity": arc.opacity,
            "strokeDasharray": "8 4" if arc.polarity == "dark" else "none",
            "fill": "none",
        })

    # Element labels
    labels = []
    for pt in ring:
        labels.append({
            "x": pt.x,
            "y": pt.y,
            "text": pt.label,
            "element": pt.element,
        })

    # Convergence markers
    markers = []
    for mx, my, label in bundle.convergence_markers:
        markers.append({"x": mx, "y": my, "label": label})

    return {
        "viewBox": "0 0 400 400",
        "paths": svg_paths,
        "labels": labels,
        "markers": markers,
        "center": {"x": cx, "y": cy},
        "radius": r,
        "badge": {
            "level": bundle.organism_level,
            "glyph": bundle.organism_glyph,
            "style": organism_badge_style(bundle.organism_level),
        },
    }


# ─── Bundle Comparison ───────────────────────────────────────────────────

def compare_bundles_ascii(
    bundle_a: RenderedBundle,
    bundle_b: RenderedBundle,
    shared_segment_count: int = 0,
) -> str:
    """
    Side-by-side ASCII comparison of two entity bundles.
    Shows shared infrastructure between them.
    """
    lines = []
    col = 30

    def pad(s: str, w: int = col) -> str:
        return s[:w].ljust(w)

    lines.append(pad(f"  {bundle_a.entity_name}") + " | " + pad(f"  {bundle_b.entity_name}"))
    lines.append(pad("  " + "─" * (col - 2)) + " | " + pad("  " + "─" * (col - 2)))

    lines.append(
        pad(f"  Level: {bundle_a.organism_level}") + " | " +
        pad(f"  Level: {bundle_b.organism_level}")
    )
    lines.append(
        pad(f"  Circuits: {bundle_a.healthy_count}/{bundle_a.total_count}") + " | " +
        pad(f"  Circuits: {bundle_b.healthy_count}/{bundle_b.total_count}")
    )
    lines.append(
        pad(f"  Health: {bundle_a.health_percent:.0%}") + " | " +
        pad(f"  Health: {bundle_b.health_percent:.0%}")
    )

    # Color signatures comparison
    lines.append(pad("  Colors:") + " | " + pad("  Colors:"))
    for color in COLOR_DIMENSIONS:
        va = bundle_a.color_signature.get(color, 0)
        vb = bundle_b.color_signature.get(color, 0)
        bar_a = "#" * int(va * 20)
        bar_b = "#" * int(vb * 20)
        lines.append(
            pad(f"    {color[:3]}: {bar_a}") + " | " +
            pad(f"    {color[:3]}: {bar_b}")
        )

    # Shared infrastructure
    lines.append("")
    lines.append(f"  Shared segments: {shared_segment_count}")
    if shared_segment_count > 0:
        lines.append(f"  These entities share infrastructure — potential for collaboration")

    return "\n".join(lines)


# ─── Evolution Timeline ─────────────────────────────────────────────────

def evolution_timeline_ascii(
    level_history: List[Tuple[float, str]],
    entity_name: str,
) -> str:
    """
    Render an entity's evolution history as an ASCII timeline.
    Shows organism level transitions over time.
    """
    if not level_history:
        return f"  {entity_name}: No evolution history"

    levels_order = ["ELEMENT", "VIRUS", "BACTERIA", "PLANT", "FISH",
                    "RABBIT", "WOLF", "DOLPHIN", "OCTOPUS"]

    lines = [f"  {entity_name} — Evolution Timeline", "  " + "─" * 50]

    max_tier = 0
    for _, level in level_history:
        if level in levels_order:
            max_tier = max(max_tier, levels_order.index(level))

    # Draw timeline
    for tier_idx in range(max_tier, -1, -1):
        level_name = levels_order[tier_idx]
        glyph = ORGANISM_GLYPHS.get(level_name, "?")

        # Check if entity reached this level
        reached = any(l == level_name for _, l in level_history)

        if reached:
            # Find when
            ts = next(t for t, l in level_history if l == level_name)
            lines.append(f"  {glyph:>3}  ●──── {level_name}")
        else:
            lines.append(f"  {glyph:>3}  │")

    lines.append(f"       ╵ start")

    return "\n".join(lines)


# ─── Example ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    # Render a sample bundle
    sample_circuits = [
        {
            "color_domain": "ORANGE",
            "light_phase": TAU,
            "dark_phase": TAU * 0.4,
            "light_value": 50,
            "dark_value": 15,
            "is_complete": True,
            "health_ratio": 0.77,
        },
        {
            "color_domain": "GREEN",
            "light_phase": TAU,
            "dark_phase": TAU * 0.2,
            "light_value": 40,
            "dark_value": 5,
            "is_complete": True,
            "health_ratio": 0.89,
        },
        {
            "color_domain": "CYAN",
            "light_phase": TAU * 0.6,
            "dark_phase": 0,
            "light_value": 20,
            "dark_value": 0,
            "is_complete": False,
            "health_ratio": 1.0,
        },
    ]

    bundle = render_bundle(
        entity_name="Alex",
        organism_level="PLANT",
        circuits=sample_circuits,
        healthy_count=2,
        next_level="FISH",
        next_level_threshold=4,
    )

    print(ascii_ring(bundle))
    print()

    # SVG data
    svg = bundle_to_svg_data(bundle)
    print(f"SVG: {len(svg['paths'])} arcs, {len(svg['labels'])} labels")
    print(f"Badge: {svg['badge']['level']} [{svg['badge']['glyph']}]")
