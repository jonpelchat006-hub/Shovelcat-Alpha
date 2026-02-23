"""
Coastline View — Spatial Rendering of the Ocean/Building/Lab City Model

The coastline is a 1D shore (wrapping) with 2D depth:
  - y < 0: Lab City (inland) — catgirl apartments, workspaces
  - y = 0: Shore — buildings sit here, one per color
  - y > 0: Ocean — users live here, depth = diversity of circuits

Rendering modes:
  - ASCII map: top-down view of coastline
  - CSS/SVG data: for the React frontend
  - Apartment cards: catgirl living situations
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple
import math

# ─── Constants ───────────────────────────────────────────────────────────

COLOR_DIMENSIONS = ["RED", "ORANGE", "YELLOW", "GREEN", "CYAN", "BLUE", "VIOLET"]

# Shore order: buildings left to right
BUILDING_POSITIONS = {
    "RED":    0.0 / 7,
    "ORANGE": 1.0 / 7,
    "YELLOW": 2.0 / 7,
    "GREEN":  3.0 / 7,
    "CYAN":   4.0 / 7,
    "BLUE":   5.0 / 7,
    "VIOLET": 6.0 / 7,
}

COLOR_CSS = {
    "RED":    "#e74c3c",
    "ORANGE": "#e67e22",
    "YELLOW": "#f1c40f",
    "GREEN":  "#2ecc71",
    "CYAN":   "#1abc9c",
    "BLUE":   "#3498db",
    "VIOLET": "#9b59b6",
}

ORGANISM_MARKERS = {
    "ELEMENT":  ".",
    "VIRUS":    "v",
    "BACTERIA": "o",
    "PLANT":    "T",
    "FISH":     "><",
    "RABBIT":   "r",
    "WOLF":     "W",
    "DOLPHIN":  "D",
    "OCTOPUS":  "8",
}

APARTMENT_ART = {
    "none":      "  ~  ",     # Waves (van life)
    "pod":       " [=] ",     # Small box
    "studio":    " [==]",     # Wider box
    "apartment": "[===]",     # Standard
    "house":     "/===\\",    # Peaked roof
    "compound":  "/[=]=\\",   # Multi-unit
    "penthouse": "^/===\\^",  # Elevated
    "estate":    "~/====\\~", # Waterfront
}


# ─── ASCII Coastline Map ────────────────────────────────────────────────

def render_coastline_ascii(
    coastline_data: Dict,
    width: int = 70,
    height: int = 25,
) -> str:
    """
    Render the coastline as an ASCII map.

    Layout (top to bottom):
      - Lab City (catgirl apartments)
      - Shore (buildings)
      - Ocean (user positions)

    coastline_data comes from ResidencyEngine.coastline_snapshot()
    """
    # Canvas
    canvas = [[' ' for _ in range(width)] for _ in range(height)]

    # Zones
    lab_start = 0
    lab_end = 6
    shore_line = 7
    ocean_start = 8
    ocean_end = height - 1

    # Draw zone separators
    for x in range(width):
        canvas[lab_end][x] = '─'
        canvas[shore_line][x] = '═'

    # Zone labels
    _place_text(canvas, 0, 0, "LAB CITY")
    _place_text(canvas, 0, shore_line, "SHORE")
    _place_text(canvas, 0, ocean_start, "OCEAN")

    # Draw buildings on shore
    for bdata in coastline_data.get("buildings", []):
        color = bdata["color"]
        pos = bdata["position"]
        x = int(pos * (width - 10)) + 5  # Margin
        x = min(x, width - 5)

        # Building marker
        short = color[:3]
        _place_text(canvas, x - 1, shore_line, f"[{short}]")

        # Resident count below
        count = bdata.get("resident_count", 0)
        if count > 0:
            _place_text(canvas, x, shore_line - 1, str(count))

    # Draw users in ocean
    for udata in coastline_data.get("user_positions", []):
        ux = udata["x"]
        uy = udata["y"]
        level = udata.get("organism_level", "ELEMENT")
        marker = ORGANISM_MARKERS.get(level, "?")

        # Map to canvas coordinates
        cx = int(ux * (width - 10)) + 5
        cy = ocean_start + int(uy * (ocean_end - ocean_start))
        cx = max(0, min(cx, width - len(marker)))
        cy = max(ocean_start, min(cy, ocean_end))

        _place_text(canvas, cx, cy, marker)

    # Draw catgirl apartments in lab city
    for apt in coastline_data.get("catgirl_apartments", []):
        ax = apt["x"]
        tier = apt.get("tier", "pod")
        art = APARTMENT_ART.get(tier, "[?]")

        cx = int(ax * (width - 10)) + 5
        cy = lab_start + 2 + min(3, int(abs(apt.get("y", 0)) * 5))
        cx = max(0, min(cx, width - len(art)))
        cy = max(lab_start, min(cy, lab_end - 1))

        _place_text(canvas, cx, cy, art)

    # Draw van lifers as waves in lab city
    van_count = coastline_data.get("van_lifers", 0)
    if van_count > 0:
        _place_text(canvas, width - 15, lab_start + 1, f"~{van_count} van life~")

    # Water effects in ocean
    for y in range(ocean_start + 1, ocean_end):
        for x in range(0, width, 8):
            if canvas[y][x] == ' ':
                depth = (y - ocean_start) / max(1, ocean_end - ocean_start)
                if depth > 0.5:
                    canvas[y][x] = '~'
                elif depth > 0.3:
                    canvas[y][min(x + 1, width - 1)] = '·'

    # Compile
    lines = []
    header = f"  COASTLINE — {coastline_data.get('total_users', 0)} entities"
    lines.append(header)
    lines.append("  " + "─" * (width - 4))
    for row in canvas:
        lines.append("  " + "".join(row))
    lines.append("  " + "─" * (width - 4))

    # Legend
    lines.append("  Legend: . Element  o Bacteria  T Plant  >< Fish  "
                 "r Rabbit  W Wolf  D Dolphin  8 Octopus")

    return "\n".join(lines)


def _place_text(canvas: List[List[str]], x: int, y: int, text: str):
    """Place text on canvas, clipping to bounds."""
    height = len(canvas)
    width = len(canvas[0]) if canvas else 0
    if y < 0 or y >= height:
        return
    for i, ch in enumerate(text):
        px = x + i
        if 0 <= px < width:
            canvas[y][px] = ch


# ─── Apartment Card ──────────────────────────────────────────────────────

def render_apartment_card(
    user_name: str,
    tier: str,
    building_color: str,
    organism_level: str,
    circuit_count: int,
    neighborhood: str,
) -> str:
    """Render a catgirl's apartment as a text card."""
    art = APARTMENT_ART.get(tier, "[?]")
    marker = ORGANISM_MARKERS.get(organism_level, "?")

    if tier == "none":
        return (
            f"┌─── {user_name}'s Catgirl ───┐\n"
            f"│  {art}                │\n"
            f"│  Van Life — no fixed  │\n"
            f"│  address in Lab City  │\n"
            f"│  [{marker}] {organism_level:<10}     │\n"
            f"│  Circuits: {circuit_count:<3}        │\n"
            f"└────────────────────────┘"
        )

    return (
        f"┌─── {user_name}'s Catgirl ───┐\n"
        f"│  {art:^20}  │\n"
        f"│  {tier.title():^20}  │\n"
        f"│  {neighborhood:^20}  │\n"
        f"│  near {building_color} building   │\n"
        f"│  [{marker}] {organism_level:<10}     │\n"
        f"│  Circuits: {circuit_count:<3}        │\n"
        f"└────────────────────────┘"
    )


# ─── User Position Detail ───────────────────────────────────────────────

def render_user_position(
    user_name: str,
    position_x: float,
    position_y: float,
    home_color: str,
    organism_level: str,
    residencies: List[Dict],
    spectrum: Dict[str, float],
) -> str:
    """Detailed view of a user's position on the coastline."""
    lines = []
    lines.append(f"╔═══ {user_name} ═══╗")
    lines.append(f"║ Position: shore {position_x:.2f}, depth {position_y:.2f}")
    lines.append(f"║ Home ocean: {home_color}")
    lines.append(f"║ Level: {organism_level}")
    lines.append(f"║")

    # Spectrum bar
    bar_width = 30
    lines.append(f"║ Spectrum:")
    for color in COLOR_DIMENSIONS:
        weight = spectrum.get(color, 0)
        filled = int(weight * bar_width)
        bar = "█" * filled + "░" * (bar_width - filled)
        lines.append(f"║   {color[:3]:>3} [{bar}] {weight:.1%}")

    # Residencies
    if residencies:
        lines.append(f"║")
        lines.append(f"║ Residencies:")
        for res in residencies:
            status = res.get("type", "stranger")
            community = res.get("community", "?")
            completion = res.get("completion", 0)
            icon = {"resident": "●", "commuter": "◐", "visitor": "○", "stranger": "·"}.get(status, "?")
            lines.append(f"║   {icon} {community}: {status} ({completion:.0%})")

    lines.append(f"╚{'═' * (max(len(l) for l in lines) - 2)}╝")
    return "\n".join(lines)


# ─── CSS Data for React ─────────────────────────────────────────────────

def coastline_css_data(coastline_data: Dict) -> Dict:
    """
    Convert coastline snapshot to CSS-compatible rendering data.
    For use in Shovelcat-AI React components.
    """
    # Building markers
    buildings = []
    for bdata in coastline_data.get("buildings", []):
        color = bdata["color"]
        buildings.append({
            "color": color,
            "cssColor": COLOR_CSS.get(color, "#888"),
            "left": f"{bdata['position'] * 100:.1f}%",
            "label": color[:3],
            "residents": bdata.get("resident_count", 0),
        })

    # User dots
    users = []
    for udata in coastline_data.get("user_positions", []):
        color = udata.get("home_color", "RED")
        users.append({
            "id": udata["user_id"],
            "name": udata["name"],
            "left": f"{udata['x'] * 100:.1f}%",
            "top": f"{(1 - udata['y']) * 50 + 50:.1f}%",  # Ocean is bottom half
            "color": COLOR_CSS.get(color, "#888"),
            "level": udata.get("organism_level", "ELEMENT"),
            "marker": ORGANISM_MARKERS.get(udata.get("organism_level", "ELEMENT"), "."),
            "isVanLife": udata.get("is_van_life", True),
        })

    # Apartment markers (Lab City, top section)
    apartments = []
    for apt in coastline_data.get("catgirl_apartments", []):
        color = apt.get("building_color", "RED")
        apartments.append({
            "userId": apt["user_id"],
            "left": f"{apt['x'] * 100:.1f}%",
            "top": f"{(1 - abs(apt.get('y', 0.3))) * 25:.1f}%",  # Lab city is top 25%
            "tier": apt["tier"],
            "color": COLOR_CSS.get(color, "#888"),
            "neighborhood": apt.get("neighborhood", ""),
        })

    return {
        "buildings": buildings,
        "users": users,
        "apartments": apartments,
        "stats": {
            "totalUsers": coastline_data.get("total_users", 0),
            "vanLifers": coastline_data.get("van_lifers", 0),
        },
        "zones": {
            "labCity": {"top": "0%", "height": "25%", "label": "Lab City"},
            "shore": {"top": "25%", "height": "5%", "label": "Shore"},
            "ocean": {"top": "30%", "height": "70%", "label": "Ocean"},
        },
    }


# ─── Example ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    # Sample coastline data (normally from ResidencyEngine.coastline_snapshot())
    sample_data = {
        "buildings": [
            {"color": c, "position": BUILDING_POSITIONS[c], "resident_count": i + 1}
            for i, c in enumerate(COLOR_DIMENSIONS)
        ],
        "user_positions": [
            {"user_id": "u1", "name": "Alex", "x": 0.18, "y": 0.3,
             "home_color": "ORANGE", "organism_level": "PLANT", "is_van_life": False,
             "apartment_tier": "studio"},
            {"user_id": "u2", "name": "Sam", "x": 0.45, "y": 0.2,
             "home_color": "GREEN", "organism_level": "FISH", "is_van_life": False,
             "apartment_tier": "apartment"},
            {"user_id": "u3", "name": "Ghost", "x": 0.7, "y": 0.85,
             "home_color": "BLUE", "organism_level": "ELEMENT", "is_van_life": True,
             "apartment_tier": "none"},
        ],
        "catgirl_apartments": [
            {"user_id": "u1", "x": 0.18, "y": -0.3, "tier": "studio",
             "building_color": "ORANGE", "neighborhood": "orange district"},
            {"user_id": "u2", "x": 0.45, "y": -0.35, "tier": "apartment",
             "building_color": "GREEN", "neighborhood": "green district"},
        ],
        "van_lifers": 1,
        "total_users": 3,
    }

    print(render_coastline_ascii(sample_data))
    print()

    print(render_apartment_card("Alex", "studio", "ORANGE", "PLANT", 3, "orange district"))
    print()

    print(render_user_position(
        "Alex", 0.18, 0.3, "ORANGE", "PLANT",
        [
            {"type": "resident", "community": "warframe_hub", "completion": 1.0},
            {"type": "commuter", "community": "cancer_research", "completion": 0.6},
        ],
        {"RED": 0.10, "ORANGE": 0.30, "YELLOW": 0.08, "GREEN": 0.25,
         "CYAN": 0.10, "BLUE": 0.10, "VIOLET": 0.07},
    ))
