"""
COMMUNITY PROXIMITY AND SPATIAL CLUSTERING
============================================

Communities exist in 7-dimensional color space. Their position is
determined by their color signature — the weighted mix of the 7
color dimensions.

PROXIMITY:
    Warframe ←→ Apex Legends: CLOSE (both high RED + CYAN, competitive FPS)
    Apex Legends ←→ WoW: MODERATE (both games, but WoW shifts to YELLOW/VIOLET)
    Warframe ←→ Poetry Workshop: FAR (almost no overlap)

Distance is Euclidean in normalized 7D color space. This determines:
    - Which communities appear as "neighbors" in the UI
    - Which communities receive DIAMOND tools from the brain
    - How learning propagates across the ecosystem

CLUSTERING:
    Communities naturally cluster by genre/type:
    - FPS games: high RED (competition) + CYAN (team) + ORANGE (art)
    - MMOs: high YELLOW (explore) + VIOLET (learn) + CYAN (social)
    - Strategy: high GREEN (structure) + RED (competition) + BLUE (governance)
    - Creative: high ORANGE (art) + CYAN (social) + VIOLET (consciousness)

    Clusters form recursively — sub-clusters within clusters,
    matching the dimensional recursion (LOCAL → REGIONAL → PLANETARY).

TOOL PROPAGATION RADIUS:
    A DIAMOND tool propagates to communities within a distance threshold.
    The threshold scales with the tool's crystallization tier:
    - LOCAL DIAMOND: radius = 0.3 (immediate neighbors)
    - REGIONAL DIAMOND: radius = 0.5 (broader cluster)
    - PLANETARY DIAMOND: radius = 0.8 (cross-genre)
    - ORBITAL DIAMOND: radius = 1.0 (nearly universal)

Author: Jonathan Pelchat
Based on Shovelcat Theory — Color Buildings + Dimensional Recursion
"""

import math
from dataclasses import dataclass, field
from typing import Dict, List, Tuple, Optional, Set
from enum import Enum


# =============================================================================
# CONSTANTS
# =============================================================================

PHI = (1 + math.sqrt(5)) / 2
PHI_INV = PHI - 1

COLOR_DIMENSIONS = [
    "RED", "ORANGE", "GREEN", "BLUE", "YELLOW", "CYAN", "VIOLET",
]

COLOR_HEX = {
    "RED":    "#dc2626",
    "ORANGE": "#ea580c",
    "GREEN":  "#16a34a",
    "BLUE":   "#2563eb",
    "YELLOW": "#d97706",
    "CYAN":   "#0891b2",
    "VIOLET": "#7c3aed",
}

# Propagation radius by dimensional tier
PROPAGATION_RADIUS = {
    "LOCAL": 0.3,
    "REGIONAL": 0.5,
    "PLANETARY": 0.8,
    "ORBITAL": 1.0,
    "DIMENSIONAL": 1.5,  # Effectively universal
}


# =============================================================================
# COLOR VECTOR MATH
# =============================================================================

@dataclass
class ColorVector:
    """
    A point in 7-dimensional color space.

    Represents a community's identity as a weighted vector.
    """
    weights: Dict[str, float] = field(default_factory=lambda: {
        c: 0.0 for c in COLOR_DIMENSIONS
    })

    @property
    def normalized(self) -> Dict[str, float]:
        total = sum(self.weights.values())
        if total == 0:
            return {c: 1.0 / len(COLOR_DIMENSIONS) for c in COLOR_DIMENSIONS}
        return {c: w / total for c, w in self.weights.items()}

    @property
    def dominant(self) -> str:
        return max(self.weights, key=self.weights.get)

    @property
    def magnitude(self) -> float:
        return math.sqrt(sum(w ** 2 for w in self.weights.values()))

    def distance_to(self, other: 'ColorVector') -> float:
        """Euclidean distance in normalized color space."""
        a = self.normalized
        b = other.normalized
        return math.sqrt(sum((a[c] - b[c]) ** 2 for c in COLOR_DIMENSIONS))

    def cosine_similarity(self, other: 'ColorVector') -> float:
        """Cosine similarity (1 = identical direction, 0 = orthogonal)."""
        dot = sum(self.weights[c] * other.weights[c] for c in COLOR_DIMENSIONS)
        mag_a = self.magnitude
        mag_b = other.magnitude
        if mag_a == 0 or mag_b == 0:
            return 0.0
        return dot / (mag_a * mag_b)

    def midpoint_with(self, other: 'ColorVector') -> 'ColorVector':
        """Midpoint between two vectors (for cluster center computation)."""
        return ColorVector(weights={
            c: (self.weights[c] + other.weights[c]) / 2
            for c in COLOR_DIMENSIONS
        })


# =============================================================================
# COMMUNITY NODE
# =============================================================================

@dataclass
class CommunityNode:
    """A community positioned in color space."""
    community_id: str
    name: str
    color_vector: ColorVector
    tier: str = "LOCAL"

    # Metadata
    member_count: int = 0
    tool_count: int = 0
    diamond_tool_count: int = 0

    # Neighborhood (computed)
    neighbors: List[Tuple[str, float]] = field(default_factory=list)

    @property
    def propagation_radius(self) -> float:
        """How far this community's DIAMOND tools can reach."""
        return PROPAGATION_RADIUS.get(self.tier, 0.3)


# =============================================================================
# COMMUNITY CLUSTER
# =============================================================================

@dataclass
class Cluster:
    """
    A group of communities with similar color signatures.

    Clusters form naturally and recursively — the FPS cluster
    contains Warframe, Apex, Valorant. The Gaming mega-cluster
    contains FPS, MMO, Strategy sub-clusters.
    """
    cluster_id: str
    name: str
    communities: List[str]  # community IDs
    center: ColorVector      # average color signature
    radius: float           # max distance from center to any member
    tier: str = "LOCAL"

    @property
    def size(self) -> int:
        return len(self.communities)


# =============================================================================
# SPATIAL ENGINE
# =============================================================================

class SpatialEngine:
    """
    Manages community positions and proximity in color space.

    Provides:
    - Nearest neighbor lookup
    - Cluster detection
    - Tool propagation path computation
    - Spatial visualization
    """

    def __init__(self):
        self.nodes: Dict[str, CommunityNode] = {}

    def add_community(
        self,
        community_id: str,
        name: str,
        weights: Dict[str, float],
        tier: str = "LOCAL",
    ) -> CommunityNode:
        """Add a community to the spatial map."""
        node = CommunityNode(
            community_id=community_id,
            name=name,
            color_vector=ColorVector(weights=weights),
            tier=tier,
        )
        self.nodes[community_id] = node
        return node

    def compute_neighborhoods(self, max_distance: float = 0.5):
        """Compute neighbors for all communities."""
        ids = list(self.nodes.keys())
        for i, id_a in enumerate(ids):
            node_a = self.nodes[id_a]
            node_a.neighbors = []
            for j, id_b in enumerate(ids):
                if i == j:
                    continue
                node_b = self.nodes[id_b]
                dist = node_a.color_vector.distance_to(node_b.color_vector)
                if dist <= max_distance:
                    node_a.neighbors.append((id_b, dist))
            node_a.neighbors.sort(key=lambda x: x[1])

    def nearest_neighbors(
        self, community_id: str, n: int = 5
    ) -> List[Tuple[str, float]]:
        """Get the N nearest neighbors of a community."""
        if community_id not in self.nodes:
            return []

        source = self.nodes[community_id]
        distances = []

        for cid, node in self.nodes.items():
            if cid == community_id:
                continue
            dist = source.color_vector.distance_to(node.color_vector)
            distances.append((cid, dist))

        distances.sort(key=lambda x: x[1])
        return distances[:n]

    # ─────────────────────────────────────────────────────────────────
    # CLUSTERING
    # ─────────────────────────────────────────────────────────────────

    def detect_clusters(
        self, distance_threshold: float = 0.25
    ) -> List[Cluster]:
        """
        Simple agglomerative clustering based on color distance.

        Communities within distance_threshold of each other merge
        into clusters. This is O(n^2) but fine for community-scale.
        """
        # Start: each community is its own cluster
        cluster_map: Dict[str, int] = {}  # community_id → cluster_index
        clusters: List[Set[str]] = []

        for cid in self.nodes:
            cluster_map[cid] = len(clusters)
            clusters.append({cid})

        # Merge clusters where members are close
        ids = list(self.nodes.keys())
        for i, id_a in enumerate(ids):
            for j, id_b in enumerate(ids):
                if i >= j:
                    continue
                dist = self.nodes[id_a].color_vector.distance_to(
                    self.nodes[id_b].color_vector
                )
                if dist <= distance_threshold:
                    # Merge clusters
                    ci = cluster_map[id_a]
                    cj = cluster_map[id_b]
                    if ci != cj:
                        # Merge cj into ci
                        for member in clusters[cj]:
                            clusters[ci].add(member)
                            cluster_map[member] = ci
                        clusters[cj] = set()

        # Build Cluster objects
        result = []
        seen = set()
        for cid, ci in cluster_map.items():
            if ci in seen:
                continue
            seen.add(ci)
            members = list(clusters[ci])
            if not members:
                continue

            # Compute center
            center_weights = {c: 0.0 for c in COLOR_DIMENSIONS}
            for mid in members:
                for c in COLOR_DIMENSIONS:
                    center_weights[c] += self.nodes[mid].color_vector.weights[c]
            for c in COLOR_DIMENSIONS:
                center_weights[c] /= len(members)
            center = ColorVector(weights=center_weights)

            # Compute radius
            radius = max(
                center.distance_to(self.nodes[mid].color_vector)
                for mid in members
            ) if len(members) > 1 else 0.0

            # Name from dominant color of center
            dominant = center.dominant
            cluster_name = f"{dominant}-cluster ({len(members)} communities)"

            result.append(Cluster(
                cluster_id=f"cluster_{ci}",
                name=cluster_name,
                communities=members,
                center=center,
                radius=radius,
            ))

        return sorted(result, key=lambda c: -c.size)

    # ─────────────────────────────────────────────────────────────────
    # TOOL PROPAGATION PATH
    # ─────────────────────────────────────────────────────────────────

    def propagation_targets(
        self,
        source_community_id: str,
        tier: str = "LOCAL",
    ) -> List[Tuple[str, float]]:
        """
        Which communities would receive a DIAMOND tool from this source?

        Radius scales with tier:
        LOCAL=0.3, REGIONAL=0.5, PLANETARY=0.8, ORBITAL=1.0
        """
        radius = PROPAGATION_RADIUS.get(tier, 0.3)
        return [
            (cid, dist)
            for cid, dist in self.nearest_neighbors(source_community_id, n=100)
            if dist <= radius
        ]

    # ─────────────────────────────────────────────────────────────────
    # VISUALIZATION
    # ─────────────────────────────────────────────────────────────────

    def distance_matrix_ascii(self) -> str:
        """Render a distance matrix between all communities."""
        ids = sorted(self.nodes.keys())
        names = [self.nodes[cid].name for cid in ids]

        # Column width
        max_name = max(len(n) for n in names)
        col_w = max(6, max_name)

        lines = ["COMMUNITY DISTANCE MATRIX (Euclidean in 7D color space):"]
        lines.append("-" * (col_w + 2 + len(ids) * 8))

        # Header
        header = " " * (col_w + 2)
        for name in names:
            header += f"{name[:6]:>7s} "
        lines.append(header)

        # Rows
        for i, id_a in enumerate(ids):
            row = f"{names[i]:<{col_w}s}  "
            for j, id_b in enumerate(ids):
                if i == j:
                    row += f"{'---':>7s} "
                else:
                    dist = self.nodes[id_a].color_vector.distance_to(
                        self.nodes[id_b].color_vector
                    )
                    row += f"{dist:>7.3f} "
            lines.append(row)

        return "\n".join(lines)

    def spatial_map_ascii(self, width: int = 60, height: int = 20) -> str:
        """
        Project communities onto a 2D map using the two most
        discriminating color axes.

        Uses RED (x-axis) and YELLOW (y-axis) as a simple projection.
        More sophisticated: PCA on the 7D signatures.
        """
        if not self.nodes:
            return "No communities registered."

        # Project onto RED (x) and YELLOW (y) axes
        points = []
        for cid, node in self.nodes.items():
            norm = node.color_vector.normalized
            x = norm.get("RED", 0)
            y = norm.get("YELLOW", 0)
            points.append((cid, node.name, x, y))

        # Normalize to grid
        min_x = min(p[2] for p in points)
        max_x = max(p[2] for p in points)
        min_y = min(p[3] for p in points)
        max_y = max(p[3] for p in points)

        range_x = max_x - min_x if max_x > min_x else 1
        range_y = max_y - min_y if max_y > min_y else 1

        grid = [[" " for _ in range(width)] for _ in range(height)]

        for _, name, x, y in points:
            gx = int((x - min_x) / range_x * (width - len(name) - 2))
            gy = int((1 - (y - min_y) / range_y) * (height - 2))
            gx = max(0, min(width - len(name) - 1, gx))
            gy = max(0, min(height - 1, gy))

            label = name[:12]
            for i, ch in enumerate(label):
                if gx + i < width:
                    grid[gy][gx + i] = ch

        lines = [
            "SPATIAL MAP (projected: RED → x, YELLOW → y):",
            "+" + "-" * width + "+",
        ]
        for row in grid:
            lines.append("|" + "".join(row) + "|")
        lines.append("+" + "-" * width + "+")
        lines.append(f"  → RED (competition/security)")
        lines.append(f"  ↑ YELLOW (exploration/discovery)")

        return "\n".join(lines)


# =============================================================================
# DEMONSTRATION
# =============================================================================

def demonstrate_spatial_system():
    """Show community proximity and clustering."""

    engine = SpatialEngine()

    print("=" * 70)
    print("COMMUNITY PROXIMITY AND SPATIAL CLUSTERING")
    print("=" * 70)

    # ── Add gaming communities ──────────────────────────────────────

    communities = {
        "warframe": {"RED": 0.25, "ORANGE": 0.20, "GREEN": 0.10, "BLUE": 0.05, "YELLOW": 0.10, "CYAN": 0.25, "VIOLET": 0.05},
        "apex-legends": {"RED": 0.25, "ORANGE": 0.20, "GREEN": 0.08, "BLUE": 0.07, "YELLOW": 0.08, "CYAN": 0.25, "VIOLET": 0.07},
        "valorant": {"RED": 0.30, "ORANGE": 0.15, "GREEN": 0.10, "BLUE": 0.05, "YELLOW": 0.05, "CYAN": 0.30, "VIOLET": 0.05},
        "world-of-warcraft": {"RED": 0.10, "ORANGE": 0.15, "GREEN": 0.10, "BLUE": 0.10, "YELLOW": 0.25, "CYAN": 0.10, "VIOLET": 0.20},
        "final-fantasy-xiv": {"RED": 0.08, "ORANGE": 0.20, "GREEN": 0.10, "BLUE": 0.10, "YELLOW": 0.20, "CYAN": 0.12, "VIOLET": 0.20},
        "civilization-vi": {"RED": 0.15, "ORANGE": 0.08, "GREEN": 0.25, "BLUE": 0.20, "YELLOW": 0.15, "CYAN": 0.07, "VIOLET": 0.10},
        "factorio": {"RED": 0.05, "ORANGE": 0.10, "GREEN": 0.35, "BLUE": 0.05, "YELLOW": 0.20, "CYAN": 0.10, "VIOLET": 0.15},
        "art-studio": {"RED": 0.03, "ORANGE": 0.45, "GREEN": 0.05, "BLUE": 0.02, "YELLOW": 0.10, "CYAN": 0.25, "VIOLET": 0.10},
        "poetry-workshop": {"RED": 0.02, "ORANGE": 0.30, "GREEN": 0.03, "BLUE": 0.05, "YELLOW": 0.10, "CYAN": 0.15, "VIOLET": 0.35},
    }

    for name, weights in communities.items():
        engine.add_community(f"games/{name}", name, weights)

    # ── Distance matrix ─────────────────────────────────────────────

    print(f"\n{engine.distance_matrix_ascii()}\n")

    # ── Nearest neighbors ───────────────────────────────────────────

    print("\n--- NEAREST NEIGHBORS ---\n")
    for focus in ["warframe", "world-of-warcraft", "art-studio"]:
        cid = f"games/{focus}"
        neighbors = engine.nearest_neighbors(cid, n=3)
        print(f"  {focus}:")
        for nid, dist in neighbors:
            nname = nid.split("/")[1]
            print(f"    {nname:20s} distance={dist:.3f}")
        print()

    # ── Clustering ──────────────────────────────────────────────────

    print("--- DETECTED CLUSTERS ---\n")
    clusters = engine.detect_clusters(distance_threshold=0.2)
    for cluster in clusters:
        members = [m.split("/")[1] for m in cluster.communities]
        print(f"  {cluster.name}:")
        print(f"    Members: {', '.join(members)}")
        print(f"    Center dominant: {cluster.center.dominant}")
        print(f"    Radius: {cluster.radius:.3f}")
        print()

    # ── Propagation targets ─────────────────────────────────────────

    print("--- TOOL PROPAGATION TARGETS ---\n")
    for tier in ["LOCAL", "REGIONAL", "PLANETARY"]:
        targets = engine.propagation_targets("games/warframe", tier=tier)
        names = [t[0].split("/")[1] for t in targets]
        print(f"  Warframe DIAMOND tool at {tier} tier (radius={PROPAGATION_RADIUS[tier]}):")
        print(f"    Reaches: {', '.join(names) if names else '(none)'}")
        print()

    # ── Spatial map ─────────────────────────────────────────────────

    print(engine.spatial_map_ascii())

    # ── Summary ─────────────────────────────────────────────────────

    print(f"""
    KEY PROPERTIES:
    ───────────────────────────────────────────────────────
    FPS cluster: Warframe, Apex Legends, Valorant
        High RED (competition) + CYAN (team) + ORANGE (art)
        These communities share tools naturally.

    MMO cluster: World of Warcraft, Final Fantasy XIV
        High YELLOW (explore) + VIOLET (learn) + CYAN (social)
        Further from FPS, closer to each other.

    Strategy cluster: Civilization VI, Factorio
        High GREEN (structure) + YELLOW (explore)
        Overlap with MMOs on YELLOW, but diverge on GREEN.

    Creative cluster: Art Studio, Poetry Workshop
        High ORANGE (art) + VIOLET (consciousness)
        Far from competitive games, close to each other.

    Propagation scales with tier:
        LOCAL DIAMOND:       radius 0.3 → immediate neighbors only
        REGIONAL DIAMOND:    radius 0.5 → broader cluster
        PLANETARY DIAMOND:   radius 0.8 → cross-genre reach
        ORBITAL DIAMOND:     radius 1.0 → nearly universal
    ───────────────────────────────────────────────────────
    """)

    return engine


if __name__ == "__main__":
    engine = demonstrate_spatial_system()
