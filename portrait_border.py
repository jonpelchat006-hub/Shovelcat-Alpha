"""
PORTRAIT BORDER SYSTEM
=======================

Every piece of content in the Shovelcat ecosystem wears its color address
as a visible border — a spectral fingerprint you can see at a glance.

The border encodes:
  1. COLOR SIGNATURE — which color dimensions this content lives in
  2. CRYSTALLIZATION STATE — how established/permanent the identity is
  3. DIMENSIONAL TIER — what scale this content operates at

BORDER RENDERING:
    - Top N colors by weight form the border bands
    - Band thickness proportional to color weight
    - Opacity/saturation controlled by crystallization state
    - Border style (dashed/solid/double) indicates crystallization level

SIGNPOST:
    A community's signpost is its logo/icon rendered with the dominant color
    and accented by secondary colors. The signpost crystallizes alongside
    the community name through VAPOR → GEL → CRYSTAL → DIAMOND.

PORTRAIT GALLERY:
    Users create art. Each piece gets a border computed from its content's
    color signature. Browsing the gallery, you see the spectral distribution
    of the entire community at a glance — lots of orange-cyan borders means
    a social art community, lots of orange-green means analytical creatives.

COLOR SPACE (hex values from subdomains.ts):
    RED     #dc2626  — Security / Existence
    ORANGE  #ea580c  — Art / Quantity
    GREEN   #16a34a  — Science / Structure
    BLUE    #2563eb  — Government / Temporal
    YELLOW  #d97706  — Explore / Motion
    CYAN    #0891b2  — Social / Relation
    VIOLET  #7c3aed  — Learn / Consciousness

Author: Jonathan Pelchat
Based on Shovelcat Theory — Color Buildings + Crystallization
"""

import math
from dataclasses import dataclass, field
from typing import Dict, List, Tuple, Optional
from enum import Enum

# =============================================================================
# CONSTANTS — matches subdomains.ts hex values
# =============================================================================

PHI = (1 + math.sqrt(5)) / 2
PHI_INV = PHI - 1  # ~0.618

COLOR_HEX = {
    "RED":    "#dc2626",
    "ORANGE": "#ea580c",
    "GREEN":  "#16a34a",
    "BLUE":   "#2563eb",
    "YELLOW": "#d97706",
    "CYAN":   "#0891b2",
    "VIOLET": "#7c3aed",
}

COLOR_LABELS = {
    "RED":    "Security",
    "ORANGE": "Art",
    "GREEN":  "Science",
    "BLUE":   "Government",
    "YELLOW": "Explore",
    "CYAN":   "Social",
    "VIOLET": "Learn",
}

# Border thickness in pixels at each crystallization level
BASE_BORDER_PX = {
    "vapor":   2,
    "gel":     3,
    "crystal": 4,
    "diamond": 6,
}

# Maximum number of color bands in a border
MAX_BORDER_BANDS = 4

# Minimum weight to appear as a visible border band
MIN_BAND_WEIGHT = 0.08


# =============================================================================
# CRYSTALLIZATION VISUAL PROPERTIES
# =============================================================================

class CrystalVisuals(Enum):
    """Visual properties tied to crystallization state."""
    VAPOR   = ("vapor",   0.30, 0.25, "dashed", "1 4")
    GEL     = ("gel",     0.60, 0.55, "solid",  "0")
    CRYSTAL = ("crystal", 0.85, 0.80, "solid",  "0")
    DIAMOND = ("diamond", 1.00, 1.00, "double", "0")

    def __init__(self, state_name, opacity, saturation, border_style, dash_array):
        self.state_name = state_name
        self.opacity = opacity
        self.saturation = saturation
        self.border_style = border_style
        self.dash_array = dash_array

    @property
    def glow(self) -> float:
        """Glow intensity — DIAMOND gets a subtle glow effect."""
        return {
            "vapor": 0.0,
            "gel": 0.0,
            "crystal": 0.3,
            "diamond": 0.8,
        }[self.state_name]

    @property
    def border_px(self) -> int:
        return BASE_BORDER_PX[self.state_name]


# =============================================================================
# COLOR BAND
# =============================================================================

@dataclass
class ColorBand:
    """
    A single color band in a border.

    Represents one color dimension's contribution to the content's identity.
    Band thickness is proportional to weight relative to other bands.
    """
    color_name: str
    hex_value: str
    weight: float           # 0-1, from the color signature
    relative_thickness: float  # 0-1, share of total border width
    label: str              # Human-readable (e.g., "Art")

    def to_css_gradient_stop(self, start_pct: float, end_pct: float) -> str:
        """Generate a CSS linear-gradient color stop."""
        return f"{self.hex_value} {start_pct:.1f}%, {self.hex_value} {end_pct:.1f}%"


# =============================================================================
# SPECTRAL FINGERPRINT
# =============================================================================

@dataclass
class SpectralFingerprint:
    """
    The complete visual identity of a piece of content or community.

    Computes border bands, opacity, saturation, and rendering instructions
    from a color signature and crystallization state.
    """
    # Input
    color_weights: Dict[str, float]
    crystal_state: str = "vapor"  # vapor, gel, crystal, diamond

    # Computed
    bands: List[ColorBand] = field(default_factory=list)
    dominant_color: str = ""
    dominant_hex: str = ""

    def __post_init__(self):
        self._compute_bands()

    @property
    def visuals(self) -> CrystalVisuals:
        return {
            "vapor": CrystalVisuals.VAPOR,
            "gel": CrystalVisuals.GEL,
            "crystal": CrystalVisuals.CRYSTAL,
            "diamond": CrystalVisuals.DIAMOND,
        }[self.crystal_state]

    def _compute_bands(self):
        """Compute the visible border bands from color weights."""
        # Filter to significant weights
        significant = {
            c: w for c, w in self.color_weights.items()
            if w >= MIN_BAND_WEIGHT and c in COLOR_HEX
        }

        if not significant:
            # Fallback: use all colors equally
            significant = {c: 1.0 / len(COLOR_HEX) for c in COLOR_HEX}

        # Sort by weight descending, take top N
        sorted_colors = sorted(significant.items(), key=lambda x: -x[1])
        top_colors = sorted_colors[:MAX_BORDER_BANDS]

        # Normalize to relative thickness
        total = sum(w for _, w in top_colors)

        self.bands = []
        for color_name, weight in top_colors:
            self.bands.append(ColorBand(
                color_name=color_name,
                hex_value=COLOR_HEX[color_name],
                weight=weight,
                relative_thickness=weight / total if total > 0 else 0,
                label=COLOR_LABELS.get(color_name, color_name),
            ))

        # Set dominant
        if self.bands:
            self.dominant_color = self.bands[0].color_name
            self.dominant_hex = self.bands[0].hex_value

    # ─────────────────────────────────────────────────────────────────
    # CSS GENERATION
    # ─────────────────────────────────────────────────────────────────

    def to_css_border(self) -> Dict[str, str]:
        """
        Generate CSS properties for rendering this border.

        Returns a dict of CSS property → value pairs.
        For multi-color borders, uses a gradient background on a pseudo-element.
        """
        v = self.visuals
        px = v.border_px

        if len(self.bands) == 1:
            # Single color — simple border
            return {
                "border": f"{px}px {v.border_style} {self.bands[0].hex_value}",
                "opacity": str(v.opacity),
            }

        # Multi-color — gradient border using border-image
        stops = []
        pct = 0.0
        for band in self.bands:
            end_pct = pct + band.relative_thickness * 100
            stops.append(band.to_css_gradient_stop(pct, end_pct))
            pct = end_pct

        gradient = f"linear-gradient(90deg, {', '.join(stops)})"

        css = {
            "border-width": f"{px}px",
            "border-style": v.border_style,
            "border-image": f"{gradient} 1",
            "opacity": str(v.opacity),
        }

        # Add glow for CRYSTAL and DIAMOND
        if v.glow > 0:
            glow_color = self.dominant_hex
            glow_spread = int(v.glow * 8)
            css["box-shadow"] = f"0 0 {glow_spread}px {glow_color}"

        return css

    def to_css_string(self) -> str:
        """Generate a single CSS string."""
        props = self.to_css_border()
        return "; ".join(f"{k}: {v}" for k, v in props.items())

    def to_tailwind_classes(self) -> str:
        """
        Approximate as Tailwind CSS classes.
        Returns the closest standard classes (exact colors need custom config).
        """
        v = self.visuals
        px_class = {2: "border-2", 3: "border-[3px]", 4: "border-4", 6: "border-[6px]"}
        opacity_class = {0.30: "opacity-30", 0.60: "opacity-60", 0.85: "opacity-85", 1.0: "opacity-100"}
        style_class = {"dashed": "border-dashed", "solid": "border-solid", "double": "border-double"}

        classes = [
            px_class.get(v.border_px, "border-2"),
            style_class.get(v.border_style, "border-solid"),
            opacity_class.get(v.opacity, "opacity-100"),
        ]

        return " ".join(classes)

    # ─────────────────────────────────────────────────────────────────
    # SVG GENERATION (for signposts and portrait frames)
    # ─────────────────────────────────────────────────────────────────

    def to_svg_frame(self, width: int = 200, height: int = 200) -> str:
        """
        Generate an SVG frame element with gradient border bands.

        This is for rendering portrait borders and signpost frames
        in contexts where CSS gradients aren't available (e.g., canvas,
        server-side rendering, export).
        """
        v = self.visuals
        border_w = v.border_px * 2  # Double for SVG visibility

        # Build gradient stops
        svg_stops = []
        offset = 0
        for band in self.bands:
            end_offset = offset + band.relative_thickness
            svg_stops.append(
                f'<stop offset="{offset:.2f}" stop-color="{band.hex_value}" '
                f'stop-opacity="{v.opacity}"/>'
            )
            svg_stops.append(
                f'<stop offset="{end_offset:.2f}" stop-color="{band.hex_value}" '
                f'stop-opacity="{v.opacity}"/>'
            )
            offset = end_offset

        stops_xml = "\n      ".join(svg_stops)

        # Dash array for VAPOR
        dash_attr = f' stroke-dasharray="{v.dash_array}"' if v.dash_array != "0" else ""

        # Glow filter for CRYSTAL/DIAMOND
        glow_filter = ""
        glow_ref = ""
        if v.glow > 0:
            glow_filter = f"""
    <filter id="glow">
      <feGaussianBlur stdDeviation="{v.glow * 4:.1f}" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>"""
            glow_ref = ' filter="url(#glow)"'

        return f"""<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="borderGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      {stops_xml}
    </linearGradient>{glow_filter}
  </defs>
  <rect x="{border_w//2}" y="{border_w//2}"
        width="{width - border_w}" height="{height - border_w}"
        fill="none"
        stroke="url(#borderGrad)"
        stroke-width="{border_w}"{dash_attr}{glow_ref}
        rx="8"/>
</svg>"""

    # ─────────────────────────────────────────────────────────────────
    # ASCII RENDERING (for terminal/debug)
    # ─────────────────────────────────────────────────────────────────

    def to_ascii(self, content_label: str = "content", width: int = 40) -> str:
        """
        Render an ASCII portrait frame showing color bands.

        Used for terminal output and debugging.
        """
        v = self.visuals

        # Build band labels for top/bottom border
        band_labels = []
        for band in self.bands:
            chars = max(1, int(band.relative_thickness * (width - 4)))
            block = band.color_name[:chars].ljust(chars)
            band_labels.append(block)
        band_line = " ".join(band_labels)
        band_line = band_line[:width - 4].ljust(width - 4)

        # Border character based on state
        h_char = {
            "vapor": "-",
            "gel": "=",
            "crystal": "#",
            "diamond": "*",
        }[self.crystal_state]

        v_char = {
            "vapor": ":",
            "gel": "|",
            "crystal": "#",
            "diamond": "*",
        }[self.crystal_state]

        corner = {
            "vapor": ".",
            "gel": "+",
            "crystal": "#",
            "diamond": "*",
        }[self.crystal_state]

        top = corner + h_char * (width - 2) + corner
        bot = corner + h_char * (width - 2) + corner
        band = v_char + " " + band_line + " " + v_char
        empty = v_char + " " * (width - 2) + v_char

        # State indicator
        state_str = f"[{self.crystal_state.upper()} {v.opacity:.0%}]"
        state_line = v_char + state_str.center(width - 2) + v_char

        # Content label
        content_line = v_char + content_label.center(width - 2) + v_char

        # Dominant color
        dom_str = f"{self.dominant_color} dominant"
        dom_line = v_char + dom_str.center(width - 2) + v_char

        lines = [
            top,
            band,
            empty,
            content_line,
            dom_line,
            state_line,
            empty,
            band,
            bot,
        ]

        return "\n".join(lines)


# =============================================================================
# SIGNPOST
# =============================================================================

@dataclass
class Signpost:
    """
    A community's signpost — its visual identity marker.

    The signpost is the community's logo/icon rendered with its dominant
    color and accented by secondary colors. It crystallizes alongside
    the community name.
    """
    community_name: str
    fingerprint: SpectralFingerprint
    icon_type: str = "default"  # Could be custom icon, uploaded logo, etc.

    def to_ascii(self, width: int = 30) -> str:
        """Render the signpost as ASCII art."""
        v = self.fingerprint.visuals
        dom = self.fingerprint.dominant_color

        # Signpost pole
        pole = "  |  "

        # Name plate — width scales with crystallization
        plate_w = min(width, 10 + len(self.community_name) + 4)

        h = {
            "vapor": "~",
            "gel": "-",
            "crystal": "=",
            "diamond": "#",
        }[self.fingerprint.crystal_state]

        top = " " + h * plate_w
        bot = " " + h * plate_w

        # Color indicator line
        bands_str = " ".join(
            f"{b.color_name[:3]}" for b in self.fingerprint.bands[:3]
        )

        name_line = f" {h} {self.community_name.center(plate_w - 4)} {h}"
        color_line = f" {h} {bands_str.center(plate_w - 4)} {h}"
        state_line = f" {h} {self.fingerprint.crystal_state.upper().center(plate_w - 4)} {h}"

        return "\n".join([
            top,
            name_line,
            color_line,
            state_line,
            bot,
            pole,
            pole,
        ])


# =============================================================================
# PORTRAIT
# =============================================================================

@dataclass
class Portrait:
    """
    A user-created piece of content with its spectral border.

    The portrait sits in a community and gets a border computed from
    where it lives in color space. Browsing a gallery of portraits,
    you see the spectral distribution of the entire community.
    """
    portrait_id: str
    creator_id: str
    community_id: str
    title: str
    content_type: str  # "image", "text", "diagram", "video"

    # The color signature of THIS specific content
    # (may differ from the community's overall signature)
    fingerprint: SpectralFingerprint

    created_at: str = ""

    def to_gallery_card(self, card_width: int = 36) -> str:
        """Render as a gallery card with border and metadata."""
        frame = self.fingerprint.to_ascii(
            content_label=self.title,
            width=card_width,
        )
        meta = f"  by {self.creator_id} | {self.content_type}"
        return frame + "\n" + meta


# =============================================================================
# GALLERY
# =============================================================================

@dataclass
class Gallery:
    """
    A collection of portraits in a community space.

    Provides aggregate color analysis — what's the community actually
    producing? This feeds back into behavioral drift detection.
    """
    community_id: str
    portraits: List[Portrait] = field(default_factory=list)

    def aggregate_signature(self) -> Dict[str, float]:
        """
        Compute the aggregate color signature across all portraits.

        This is the community's ACTUAL behavioral signature —
        what people are creating, not what the identity says they are.
        Used for SNAP drift detection.
        """
        if not self.portraits:
            return {c: 0.0 for c in COLOR_HEX}

        aggregate = {c: 0.0 for c in COLOR_HEX}
        for portrait in self.portraits:
            for color, weight in portrait.fingerprint.color_weights.items():
                if color in aggregate:
                    aggregate[color] += weight

        # Normalize
        total = sum(aggregate.values())
        if total > 0:
            aggregate = {c: w / total for c, w in aggregate.items()}

        return aggregate

    def color_distribution_ascii(self, width: int = 50) -> str:
        """ASCII bar chart of aggregate color distribution."""
        sig = self.aggregate_signature()

        lines = [f"Gallery Color Distribution ({len(self.portraits)} portraits):"]
        lines.append("-" * width)

        for color in ["RED", "ORANGE", "GREEN", "BLUE", "YELLOW", "CYAN", "VIOLET"]:
            weight = sig.get(color, 0)
            bar_len = int(weight * (width - 15))
            bar = "#" * bar_len
            label = COLOR_LABELS.get(color, color)
            lines.append(f"  {label:10s} {bar} {weight:.1%}")

        lines.append("-" * width)
        return "\n".join(lines)


# =============================================================================
# DEMONSTRATION
# =============================================================================

def demonstrate_portrait_system():
    """Show the portrait border system in action."""

    print("=" * 60)
    print("PORTRAIT BORDER SYSTEM — DEMONSTRATION")
    print("=" * 60)

    # ── 1. Community signpost ───────────────────────────────────────

    print("\n--- SIGNPOSTS AT DIFFERENT CRYSTALLIZATION LEVELS ---\n")

    apex_weights = {
        "RED": 0.20, "ORANGE": 0.30, "GREEN": 0.08,
        "BLUE": 0.07, "YELLOW": 0.08, "CYAN": 0.20, "VIOLET": 0.07,
    }

    for state in ["vapor", "gel", "crystal", "diamond"]:
        fp = SpectralFingerprint(color_weights=apex_weights, crystal_state=state)
        signpost = Signpost(community_name="Apex Legends Hub", fingerprint=fp)
        print(signpost.to_ascii())
        print()

    # ── 2. Portrait borders ─────────────────────────────────────────

    print("\n--- PORTRAITS WITH DIFFERENT COLOR SIGNATURES ---\n")

    # Fan art (Art + Social)
    fan_art = Portrait(
        portrait_id="p001",
        creator_id="artist_42",
        community_id="games/apex-legends",
        title="Wraith Fan Art",
        content_type="image",
        fingerprint=SpectralFingerprint(
            color_weights={
                "RED": 0.05, "ORANGE": 0.45, "GREEN": 0.03,
                "BLUE": 0.02, "YELLOW": 0.05, "CYAN": 0.35, "VIOLET": 0.05,
            },
            crystal_state="gel",
        ),
    )
    print(fan_art.to_gallery_card())
    print()

    # Strategy diagram (Art + Science)
    strategy = Portrait(
        portrait_id="p002",
        creator_id="analyst_7",
        community_id="games/apex-legends",
        title="Drop Zone Analysis",
        content_type="diagram",
        fingerprint=SpectralFingerprint(
            color_weights={
                "RED": 0.10, "ORANGE": 0.25, "GREEN": 0.35,
                "BLUE": 0.05, "YELLOW": 0.15, "CYAN": 0.05, "VIOLET": 0.05,
            },
            crystal_state="crystal",
        ),
    )
    print(strategy.to_gallery_card())
    print()

    # Tutorial (Learn + Art)
    tutorial = Portrait(
        portrait_id="p003",
        creator_id="coach_99",
        community_id="games/apex-legends",
        title="Movement Guide",
        content_type="video",
        fingerprint=SpectralFingerprint(
            color_weights={
                "RED": 0.05, "ORANGE": 0.20, "GREEN": 0.10,
                "BLUE": 0.03, "YELLOW": 0.12, "CYAN": 0.10, "VIOLET": 0.40,
            },
            crystal_state="vapor",
        ),
    )
    print(tutorial.to_gallery_card())
    print()

    # ── 3. Gallery aggregate ────────────────────────────────────────

    print("\n--- GALLERY AGGREGATE ---\n")

    gallery = Gallery(
        community_id="games/apex-legends",
        portraits=[fan_art, strategy, tutorial],
    )
    print(gallery.color_distribution_ascii())

    # ── 4. CSS output ───────────────────────────────────────────────

    print("\n--- CSS BORDER OUTPUT ---\n")

    for name, portrait in [("Fan Art", fan_art), ("Strategy", strategy), ("Tutorial", tutorial)]:
        css = portrait.fingerprint.to_css_string()
        tw = portrait.fingerprint.to_tailwind_classes()
        print(f"  {name}:")
        print(f"    CSS:      {css}")
        print(f"    Tailwind: {tw}")
        print()

    # ── 5. SVG frame ────────────────────────────────────────────────

    print("\n--- SVG FRAME (Diamond state) ---\n")

    diamond_fp = SpectralFingerprint(
        color_weights=apex_weights,
        crystal_state="diamond",
    )
    print(diamond_fp.to_svg_frame(width=120, height=120))

    # ── Summary ─────────────────────────────────────────────────────

    print("\n" + "=" * 60)
    print("BORDER PROPERTIES BY CRYSTALLIZATION STATE")
    print("=" * 60)
    print(f"""
    State     Px  Style   Opacity  Saturation  Glow   Dash
    -------   --  ------  -------  ----------  -----  --------
    VAPOR      2  dashed   30%      25%         none   "1 4"
    GEL        3  solid    60%      55%         none   none
    CRYSTAL    4  solid    85%      80%         0.3    none
    DIAMOND    6  double  100%     100%         0.8    none

    Band selection: Top {MAX_BORDER_BANDS} colors above {MIN_BAND_WEIGHT:.0%} weight
    Thickness: proportional to relative weight within selected bands
    Gradient: left-to-right, strongest color first

    The border IS the content's color address.
    You can SEE the community's character before reading a word.
    """)

    return gallery


if __name__ == "__main__":
    gallery = demonstrate_portrait_system()
