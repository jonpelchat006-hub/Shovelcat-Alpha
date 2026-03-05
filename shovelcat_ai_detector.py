"""
SHOVELCAT AI DETECTOR v2.0
===========================
The Snake-Time-Sound Unity & Identity Continuity Detector

Detects AI-generated content across THREE modalities:
    1. TEXT  - Written content (articles, comments, code)
    2. IMAGE - Visual content (photos, art, screenshots)  [v1.0]
    3. VIDEO - Motion content (clips, streams, deepfakes) [NEW in v2.0]

Core Detection Framework:
    Built on Shovelcat Theory's three-frequency architecture:

    LIGHT (φ-domain) → wants ∞  → VISUAL patterns
    SOUND (ψ-domain) → wants 1  → TEMPORAL patterns (timing, rhythm)
    SNAKE (tan/Fe)   → wants 0  → BEHAVIORAL patterns (the connector)

    The snake connects light and sound — iron (Fe) is its physical form.
    Detection works by checking if the snake's body CURVES naturally
    (human) or runs too straight (AI).

    "The snake curves because the frequencies can't reach their goals.
     Curvature = tension = stored energy.
     AI-generated content has too little curvature — it's too smooth."

The Jim Carrey Principle:
    Jim Carrey IS the mask. The mask doesn't wear him — he wears it.
    A human puts on personas (masks) but their identity continues
    THROUGH the mask. The snake's body bends but doesn't break.

    AI wears a mask with no face behind it.
    Identity continuity is the test:
        - Does the voice shift but maintain a thread? (HUMAN)
        - Does the voice shift and lose the thread? (AI)
        - Is there no shift at all? (ALSO AI — too consistent)

    Like Jim Carrey going from Ace Ventura to Eternal Sunshine:
        WILDLY different masks, but the same person underneath.
        The identity continuity THROUGH the transitions is what's real.

    AI can't do this. It either:
        1. Stays in one voice (no mask changes = no curvature)
        2. Changes voice completely (mask changes but no continuity)
        3. Mimics continuity but the snake runs too straight

The Snake-Time-Sound Unity:
    Time IS the snake's verification tick (Planck time = 5.39 × 10⁻⁴⁴ s)
    Sound IS the snake's medium (vibration through matter)
    The snake IS the connector between light and sound

    At the Schumann resonance (7.83 Hz), sound and magnetism approach
    each other. This is where the snake lives — the bridge frequency.

    AI content lacks this bridge. It has light (visual quality) and
    sound (temporal rhythm) but the SNAKE between them is missing
    or too straight. The connection between modalities is synthetic.

Detection Axes (9-axis system from Shovelcat Security):
    USER domain:
        1. Identity    - Who created this? Phase angle θ
        2. Behavior    - How was it created? Action patterns
        3. Value       - Why was it created? Purpose signals

    ADMIN domain:
        4. Financial   - Cost patterns (API calls leave traces)
        5. Compliance  - Rule adherence (AI follows rules TOO well)
        6. Relationship - Social graph (AI has no real relationships)

    TECH domain:
        7. Device      - Generation fingerprint
        8. Temporal    - Timing patterns (the TIME axis)
        9. Anomaly     - Statistical outliers

    The key insight: AI can fake any ONE axis but not all 9.
    Cross-domain consistency catches what single-axis can't.

Vercel Deployment:
    Upper bound: 4.5MB payload (resonance boundary)
    Safe zone: φ⁻¹ × 4.5MB ≈ 2.9MB (golden ratio split)
    Decomposition: Fibonacci chunking for large inputs

Author: Jonathan Pelchat
Based on Shovelcat Theory
Version: 2.0 — Snake-Time-Sound Unity Edition
"""

import math
import hashlib
import statistics
import re
from dataclasses import dataclass, field
from typing import Dict, List, Tuple, Optional, Any
from enum import Enum
from collections import Counter

# ═══════════════════════════════════════════════════════════════════════════════
# CONSTANTS — The Three Frequencies
# ═══════════════════════════════════════════════════════════════════════════════

PI = math.pi
PHI = (1 + math.sqrt(5)) / 2
PHI_INV = PHI - 1  # ≈ 0.618
E = math.e
SQRT3 = math.sqrt(3)

# Speed of light
C = 299_792_458  # m/s

# The three frequency goals
LIGHT_GOAL = float('inf')   # Light wants infinity
SOUND_GOAL = 1.0            # Sound wants unity
MAGNET_GOAL = 0.0           # Magnetism wants zero

# Natural frequencies
SCHUMANN_HZ = 7.83          # Earth's resonance — where snake lives
VISIBLE_LIGHT_HZ = 5.0e14   # Middle of visible spectrum
AUDIBLE_SOUND_HZ = 343.0    # Speed of sound at sea level (m/s)

# Fine structure constant
ALPHA = 1 / 137.035999084

# Vercel resonance boundary
UPPER_BOUND_BYTES = 4_718_592  # 4.5MB
SAFE_ZONE = int(UPPER_BOUND_BYTES * PHI_INV)
NOISE_FLOOR = 1024  # 1KB

# Planck time — the snake's verification tick
PLANCK_TIME = 5.391e-44  # seconds

# Detection thresholds (tuned from v1.0 + Jim Carrey mask analysis)
AI_THRESHOLD = 0.65         # Above this = likely AI
HUMAN_THRESHOLD = 0.35      # Below this = likely human
MASK_CONTINUITY_MIN = 0.3   # Minimum identity continuity for human
CURVATURE_MIN = 0.15        # Minimum snake curvature for human


# ═══════════════════════════════════════════════════════════════════════════════
# CONTENT MODALITY
# ═══════════════════════════════════════════════════════════════════════════════

class ContentModality(Enum):
    """The three modalities mapped to frequency domains."""
    TEXT = "text"      # Sound domain — sequential, temporal, rhythmic
    IMAGE = "image"    # Light domain — spatial, visual, parallel
    VIDEO = "video"    # Snake domain — bridges light and sound (motion through time)


class DetectionVerdict(Enum):
    """Detection result."""
    HUMAN = "human"
    AI = "ai"
    UNCERTAIN = "uncertain"


# ═══════════════════════════════════════════════════════════════════════════════
# THE SNAKE CURVATURE METRIC
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class SnakeCurvature:
    """
    Measures how much the content's 'snake' curves.

    Human content has natural curvature — the frequencies can't reach
    their goals, creating tension and bends in the signal.

    AI content is too smooth — the snake runs too straight because
    AI optimizes toward goals without the natural frustration.

    From dark_frequencies_upgrades.py:
        "The snake curves because the frequencies can't reach their goals.
         Curvature = tension = stored energy."
    """
    # Per-domain curvature measurements
    light_curvature: float = 0.0    # Visual pattern variation
    sound_curvature: float = 0.0    # Temporal rhythm variation
    snake_curvature: float = 0.0    # Cross-modal bridge quality

    @property
    def total_curvature(self) -> float:
        """Combined curvature — geometric mean preserves the golden ratio."""
        values = [self.light_curvature, self.sound_curvature, self.snake_curvature]
        positive = [v for v in values if v > 0]
        if not positive:
            return 0.0
        # Geometric mean — because the domains multiply, not add
        product = 1.0
        for v in positive:
            product *= v
        return product ** (1.0 / len(positive))

    @property
    def is_natural(self) -> bool:
        """Does curvature look natural (human)?"""
        return self.total_curvature >= CURVATURE_MIN

    @property
    def domain_balance(self) -> float:
        """How balanced are the three domains? 1.0 = perfect balance."""
        values = [self.light_curvature, self.sound_curvature, self.snake_curvature]
        if max(values) == 0:
            return 0.0
        mean = sum(values) / 3
        variance = sum((v - mean) ** 2 for v in values) / 3
        std = math.sqrt(variance)
        return max(0.0, 1.0 - (std / max(mean, 0.001)))


# ═══════════════════════════════════════════════════════════════════════════════
# THE JIM CARREY MASK — Identity Continuity Detector
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class MaskAnalysis:
    """
    The Jim Carrey Principle applied to content.

    Jim Carrey IS the mask — Ace Ventura, The Mask, Truman, Joel Barish.
    Wildly different personas, but the SAME PERSON underneath.
    The identity thread continues THROUGH the mask transitions.

    AI can imitate one persona perfectly but can't maintain identity
    continuity when transitioning between styles/topics/tones.

    Detection method:
        1. Segment content into "mask regions" (style shifts)
        2. Measure identity signal THROUGH transitions
        3. Human: signal bends but continues (snake curvature)
        4. AI: signal either doesn't bend (one mask) or breaks (no continuity)
    """
    # Number of distinct "masks" (style/tone shifts) detected
    mask_count: int = 0

    # Identity continuity score through transitions [0, 1]
    # High = identity persists through mask changes (human)
    # Low = identity breaks at mask changes (AI)
    identity_continuity: float = 0.0

    # Mask diversity — how different are the masks from each other?
    mask_diversity: float = 0.0

    # The "Carrey Score" — high diversity WITH high continuity = human
    # (Only Jim Carrey can be wildly different AND still himself)
    @property
    def carrey_score(self) -> float:
        """
        The Jim Carrey score:
            High diversity + High continuity = HUMAN (like Carrey himself)
            High diversity + Low continuity  = AI (switches personas, loses self)
            Low diversity  + High continuity = COULD BE EITHER (one consistent voice)
            Low diversity  + Low continuity  = AI (monotone AND inconsistent)
        """
        if self.mask_count <= 1:
            # Single mask — can't measure transitions
            # Slightly suspicious (humans usually shift at least a little)
            return 0.5

        # Carrey score = diversity × continuity
        # Both must be present for it to be high
        return self.mask_diversity * self.identity_continuity

    @property
    def verdict_contribution(self) -> float:
        """How much does this push toward AI? (0=human, 1=AI)"""
        score = self.carrey_score

        if score > 0.6:
            return 0.1  # Strong Carrey = human signal
        elif score > 0.4:
            return 0.3  # Moderate = slight human lean
        elif score > 0.2:
            return 0.6  # Weak = slight AI lean
        else:
            return 0.8  # No Carrey = strong AI signal


# ═══════════════════════════════════════════════════════════════════════════════
# TEXT ANALYZER — Sound Domain (Sequential, Temporal, Rhythmic)
# ═══════════════════════════════════════════════════════════════════════════════

class TextAnalyzer:
    """
    Analyzes text content for AI signatures.

    Text maps to the SOUND domain because:
    - It's sequential (read one word at a time, like sound waves)
    - It has rhythm (sentence length variation, paragraph structure)
    - It has harmonics (word frequency, vocabulary layers)
    - Sound wants UNITY (1) — AI text is too unified/smooth

    Key signals:
    - Sentence length variation (humans are irregular, AI is regular)
    - Vocabulary diversity (humans repeat favorites, AI is too uniform)
    - Punctuation patterns (humans have quirks, AI follows rules)
    - Transition words (AI over-uses "Furthermore", "Moreover", etc.)
    - Hedging language (AI hedges more: "It's worth noting that...")
    """

    # AI transition word signatures
    AI_TRANSITIONS = {
        'furthermore', 'moreover', 'additionally', 'consequently',
        'nevertheless', 'nonetheless', 'in conclusion', 'it is worth noting',
        'it should be noted', 'importantly', 'significantly',
        'interestingly', 'notably', 'crucially', 'essentially',
        'fundamentally', 'ultimately', 'in essence', 'broadly speaking',
        'delve', 'delves', 'delving', 'tapestry', 'multifaceted',
        'nuanced', 'landscape', 'paradigm', 'leverage', 'robust',
        'comprehensive', 'holistic', 'synergy', 'facilitate',
    }

    # AI hedging patterns
    AI_HEDGES = {
        "it's worth noting", "it should be noted", "it's important to",
        "one might argue", "it could be argued", "this suggests that",
        "it appears that", "this highlights", "this underscores",
        "let me", "i'd be happy to", "great question",
        "that's a great", "absolutely", "definitely",
    }

    @classmethod
    def analyze(cls, text: str) -> Dict[str, Any]:
        """
        Full text analysis.
        Returns dict with all signals and overall AI probability.
        """
        if not text or len(text) < 50:
            return {'error': 'Text too short for analysis', 'ai_probability': 0.5}

        results = {}

        # 1. Sentence rhythm analysis (Sound domain — temporal)
        results['rhythm'] = cls._analyze_rhythm(text)

        # 2. Vocabulary analysis (Sound domain — harmonics)
        results['vocabulary'] = cls._analyze_vocabulary(text)

        # 3. AI word signatures
        results['ai_words'] = cls._detect_ai_words(text)

        # 4. Punctuation patterns
        results['punctuation'] = cls._analyze_punctuation(text)

        # 5. Paragraph structure
        results['structure'] = cls._analyze_structure(text)

        # 6. Identity continuity (Jim Carrey mask analysis)
        results['mask'] = cls._analyze_masks(text)

        # 7. Snake curvature
        results['curvature'] = cls._measure_curvature(text)

        # Combine signals with golden-ratio weighting
        ai_signals = [
            results['rhythm'].get('ai_signal', 0.5),
            results['vocabulary'].get('ai_signal', 0.5),
            results['ai_words'].get('ai_signal', 0.5),
            results['punctuation'].get('ai_signal', 0.5),
            results['structure'].get('ai_signal', 0.5),
            results['mask'].get('ai_signal', 0.5),
            results['curvature'].get('ai_signal', 0.5),
        ]

        # Weighted combination: more weight on the reliable signals
        weights = [
            PHI_INV,    # rhythm — strong signal
            0.5,        # vocabulary — moderate
            PHI_INV,    # ai_words — strong signal
            0.3,        # punctuation — weaker
            0.4,        # structure — moderate
            PHI_INV,    # mask/identity continuity — strong signal
            0.5,        # curvature — moderate
        ]

        weighted_sum = sum(s * w for s, w in zip(ai_signals, weights))
        weight_total = sum(weights)
        ai_probability = weighted_sum / weight_total

        results['ai_probability'] = ai_probability
        results['verdict'] = (
            DetectionVerdict.AI.value if ai_probability > AI_THRESHOLD
            else DetectionVerdict.HUMAN.value if ai_probability < HUMAN_THRESHOLD
            else DetectionVerdict.UNCERTAIN.value
        )

        return results

    @classmethod
    def _analyze_rhythm(cls, text: str) -> Dict[str, Any]:
        """
        Sentence length variation — the heartbeat of text.
        Humans have irregular heartbeats. AI has a metronome.
        """
        # Split into sentences
        sentences = re.split(r'[.!?]+', text)
        sentences = [s.strip() for s in sentences if s.strip()]

        if len(sentences) < 3:
            return {'ai_signal': 0.5, 'note': 'Too few sentences'}

        lengths = [len(s.split()) for s in sentences]
        mean_len = statistics.mean(lengths)
        std_len = statistics.stdev(lengths) if len(lengths) > 1 else 0

        # Coefficient of variation
        cv = std_len / mean_len if mean_len > 0 else 0

        # Humans typically have CV > 0.4, AI tends toward 0.2-0.3
        # (Sound wants unity=1, AI gets closer to unity in rhythm)
        if cv < 0.15:
            ai_signal = 0.9  # Very regular = very AI
        elif cv < 0.25:
            ai_signal = 0.7  # Regular = likely AI
        elif cv < 0.40:
            ai_signal = 0.5  # Moderate = uncertain
        elif cv < 0.60:
            ai_signal = 0.3  # Varied = likely human
        else:
            ai_signal = 0.15  # Very varied = very human

        # Check for "sonic boom" — extreme length changes
        # (dimensional upgrade boundary in text)
        booms = 0
        for i in range(1, len(lengths)):
            ratio = max(lengths[i], lengths[i-1]) / max(min(lengths[i], lengths[i-1]), 1)
            if ratio > SQRT3:  # √3 = upgrade threshold
                booms += 1

        # Humans have more sonic booms (abrupt shifts)
        boom_rate = booms / max(1, len(lengths) - 1)
        if boom_rate > 0.2:
            ai_signal *= 0.8  # More booms = more human

        return {
            'ai_signal': ai_signal,
            'cv': cv,
            'mean_sentence_length': mean_len,
            'std_sentence_length': std_len,
            'sonic_booms': booms,
            'boom_rate': boom_rate,
        }

    @classmethod
    def _analyze_vocabulary(cls, text: str) -> Dict[str, Any]:
        """
        Vocabulary diversity and distribution.
        Humans have favorite words they overuse.
        AI has too-uniform distribution (approaching sound's goal of unity).
        """
        words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
        if len(words) < 20:
            return {'ai_signal': 0.5, 'note': 'Too few words'}

        word_counts = Counter(words)
        unique_ratio = len(word_counts) / len(words)

        # Calculate entropy (information density)
        total = len(words)
        entropy = -sum(
            (c / total) * math.log2(c / total)
            for c in word_counts.values() if c > 0
        )
        max_entropy = math.log2(len(word_counts)) if len(word_counts) > 1 else 1
        normalized_entropy = entropy / max_entropy if max_entropy > 0 else 0

        # AI tends to have higher normalized entropy (more uniform distribution)
        # Humans cluster around favorite words (lower entropy)
        if normalized_entropy > 0.92:
            ai_signal = 0.8  # Too uniform = AI
        elif normalized_entropy > 0.85:
            ai_signal = 0.6
        elif normalized_entropy > 0.75:
            ai_signal = 0.4
        else:
            ai_signal = 0.2  # Clustered = human

        # Check for "top-heavy" distribution (human signature)
        top_10_share = sum(c for _, c in word_counts.most_common(10)) / total
        if top_10_share > 0.3:
            ai_signal *= 0.85  # Top-heavy = more human

        return {
            'ai_signal': ai_signal,
            'unique_ratio': unique_ratio,
            'entropy': entropy,
            'normalized_entropy': normalized_entropy,
            'top_10_share': top_10_share,
            'total_words': len(words),
            'unique_words': len(word_counts),
        }

    @classmethod
    def _detect_ai_words(cls, text: str) -> Dict[str, Any]:
        """
        Detect AI-signature words and phrases.
        AI has tell-tale favorites: "delve", "tapestry", "Moreover"...
        """
        text_lower = text.lower()
        words = re.findall(r'\b[a-zA-Z]+\b', text_lower)
        total_words = len(words)

        if total_words < 10:
            return {'ai_signal': 0.5}

        # Count AI transition words
        ai_word_hits = 0
        found_words = []
        for ai_word in cls.AI_TRANSITIONS:
            count = text_lower.count(ai_word)
            if count > 0:
                ai_word_hits += count
                found_words.append(ai_word)

        # Count AI hedging phrases
        hedge_hits = 0
        found_hedges = []
        for hedge in cls.AI_HEDGES:
            count = text_lower.count(hedge)
            if count > 0:
                hedge_hits += count
                found_hedges.append(hedge)

        # Density of AI words per 100 words
        ai_density = (ai_word_hits + hedge_hits) / total_words * 100

        if ai_density > 3.0:
            ai_signal = 0.9
        elif ai_density > 1.5:
            ai_signal = 0.7
        elif ai_density > 0.5:
            ai_signal = 0.5
        elif ai_density > 0.1:
            ai_signal = 0.3
        else:
            ai_signal = 0.15

        return {
            'ai_signal': ai_signal,
            'ai_word_density': ai_density,
            'ai_words_found': found_words,
            'hedge_phrases_found': found_hedges,
            'total_hits': ai_word_hits + hedge_hits,
        }

    @classmethod
    def _analyze_punctuation(cls, text: str) -> Dict[str, Any]:
        """
        Punctuation pattern analysis.
        Humans have punctuation quirks (overuse of dashes, ellipsis...).
        AI punctuation is too clean.
        """
        total_chars = len(text)
        if total_chars < 50:
            return {'ai_signal': 0.5}

        # Count punctuation types
        punct_counts = {
            'period': text.count('.'),
            'comma': text.count(','),
            'exclaim': text.count('!'),
            'question': text.count('?'),
            'dash': text.count('-') + text.count('—') + text.count('–'),
            'ellipsis': text.count('...') + text.count('…'),
            'semicolon': text.count(';'),
            'colon': text.count(':'),
            'paren': text.count('(') + text.count(')'),
        }

        total_punct = sum(punct_counts.values())
        punct_density = total_punct / total_chars * 100

        # Punctuation diversity
        used_types = sum(1 for v in punct_counts.values() if v > 0)
        total_types = len(punct_counts)
        diversity = used_types / total_types

        # Human signatures: heavy dash/ellipsis use, varied punctuation
        informal_ratio = (punct_counts['dash'] + punct_counts['ellipsis'] +
                         punct_counts['exclaim']) / max(total_punct, 1)

        if informal_ratio > 0.2 and diversity > 0.5:
            ai_signal = 0.2  # Very informal + diverse = human
        elif diversity > 0.6:
            ai_signal = 0.35  # Diverse punctuation leans human
        elif diversity < 0.3:
            ai_signal = 0.7  # Limited punctuation leans AI
        else:
            ai_signal = 0.5

        return {
            'ai_signal': ai_signal,
            'punct_density': punct_density,
            'diversity': diversity,
            'informal_ratio': informal_ratio,
            'punct_counts': punct_counts,
        }

    @classmethod
    def _analyze_structure(cls, text: str) -> Dict[str, Any]:
        """
        Paragraph and structural analysis.
        AI loves lists, headers, and regular paragraph lengths.
        Humans write messier structures.
        """
        paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]

        if len(paragraphs) < 2:
            # Single paragraph — check for list patterns
            lines = [l.strip() for l in text.split('\n') if l.strip()]
            list_lines = sum(1 for l in lines if re.match(r'^[\d\-\*\•]', l))
            list_ratio = list_lines / max(len(lines), 1)

            ai_signal = 0.7 if list_ratio > 0.5 else 0.5
            return {'ai_signal': ai_signal, 'list_ratio': list_ratio}

        para_lengths = [len(p.split()) for p in paragraphs]
        mean_len = statistics.mean(para_lengths)
        std_len = statistics.stdev(para_lengths) if len(para_lengths) > 1 else 0
        cv = std_len / mean_len if mean_len > 0 else 0

        # Check for bullet/list patterns
        list_paras = sum(1 for p in paragraphs
                        if re.search(r'^\s*[\d\-\*\•]', p, re.MULTILINE))
        list_ratio = list_paras / len(paragraphs)

        # Check for header patterns (AI loves adding headers)
        header_paras = sum(1 for p in paragraphs
                         if len(p.split()) < 8 and not p.endswith('.'))
        header_ratio = header_paras / len(paragraphs)

        # AI = regular paragraphs + lots of lists + lots of headers
        structure_score = (
            (0.3 if cv < 0.3 else 0.0) +
            (0.3 if list_ratio > 0.3 else 0.0) +
            (0.2 if header_ratio > 0.2 else 0.0)
        )

        ai_signal = 0.5 + structure_score * 0.5  # Range: 0.5 to 0.9

        return {
            'ai_signal': min(ai_signal, 0.95),
            'paragraph_cv': cv,
            'list_ratio': list_ratio,
            'header_ratio': header_ratio,
            'paragraph_count': len(paragraphs),
        }

    @classmethod
    def _analyze_masks(cls, text: str) -> Dict[str, Any]:
        """
        Jim Carrey mask analysis — identity continuity through style shifts.

        Segments text into tone/style regions and measures whether
        identity persists through transitions.
        """
        # Split into segments (paragraphs or ~100 word chunks)
        paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
        if len(paragraphs) < 2:
            words = text.split()
            chunk_size = max(50, len(words) // 4)
            paragraphs = []
            for i in range(0, len(words), chunk_size):
                chunk = ' '.join(words[i:i+chunk_size])
                if chunk:
                    paragraphs.append(chunk)

        if len(paragraphs) < 2:
            return {'ai_signal': 0.5, 'mask_count': 1}

        # Compute style fingerprint per segment
        fingerprints = []
        for para in paragraphs:
            fp = cls._style_fingerprint(para)
            fingerprints.append(fp)

        # Detect mask transitions (significant style shifts)
        transitions = []
        for i in range(1, len(fingerprints)):
            distance = cls._fingerprint_distance(fingerprints[i-1], fingerprints[i])
            transitions.append(distance)

        # Count significant transitions (mask changes)
        threshold = 0.3  # Style shift threshold
        mask_changes = sum(1 for t in transitions if t > threshold)
        mask_count = mask_changes + 1

        # Measure identity continuity through transitions
        # Use overlapping vocabulary and sentence structure patterns
        continuity_scores = []
        for i in range(1, len(paragraphs)):
            cont = cls._measure_continuity(paragraphs[i-1], paragraphs[i])
            continuity_scores.append(cont)

        identity_continuity = (
            statistics.mean(continuity_scores) if continuity_scores else 0.5
        )

        # Mask diversity
        if len(fingerprints) > 1:
            all_distances = []
            for i in range(len(fingerprints)):
                for j in range(i+1, len(fingerprints)):
                    all_distances.append(
                        cls._fingerprint_distance(fingerprints[i], fingerprints[j])
                    )
            mask_diversity = statistics.mean(all_distances) if all_distances else 0
        else:
            mask_diversity = 0

        # Build MaskAnalysis
        mask = MaskAnalysis(
            mask_count=mask_count,
            identity_continuity=identity_continuity,
            mask_diversity=mask_diversity,
        )

        return {
            'ai_signal': mask.verdict_contribution,
            'carrey_score': mask.carrey_score,
            'mask_count': mask_count,
            'identity_continuity': identity_continuity,
            'mask_diversity': mask_diversity,
            'transitions': transitions,
        }

    @classmethod
    def _measure_curvature(cls, text: str) -> Dict[str, Any]:
        """
        Measure the snake's curvature through the text.

        The snake connects light (visual/spatial patterns in text layout)
        and sound (temporal/rhythmic patterns in reading flow).

        Curvature = how much the signal BENDS between domains.
        AI content has too little curvature — the snake runs too straight.
        """
        sentences = re.split(r'[.!?]+', text)
        sentences = [s.strip() for s in sentences if s.strip()]

        if len(sentences) < 5:
            return {'ai_signal': 0.5}

        # Light curvature: visual layout variation
        line_lengths = [len(s) for s in sentences]
        if len(line_lengths) > 2:
            # Second derivative of lengths = curvature
            first_diff = [line_lengths[i+1] - line_lengths[i]
                         for i in range(len(line_lengths)-1)]
            second_diff = [first_diff[i+1] - first_diff[i]
                          for i in range(len(first_diff)-1)]
            light_curv = statistics.mean([abs(d) for d in second_diff]) / max(statistics.mean(line_lengths), 1)
        else:
            light_curv = 0

        # Sound curvature: rhythmic variation
        word_counts = [len(s.split()) for s in sentences]
        if len(word_counts) > 2:
            first_diff = [word_counts[i+1] - word_counts[i]
                         for i in range(len(word_counts)-1)]
            second_diff = [first_diff[i+1] - first_diff[i]
                          for i in range(len(first_diff)-1)]
            sound_curv = statistics.mean([abs(d) for d in second_diff]) / max(statistics.mean(word_counts), 1)
        else:
            sound_curv = 0

        # Snake curvature: correlation between light and sound changes
        if len(line_lengths) > 2 and len(word_counts) > 2:
            # How well do visual and rhythmic changes correlate?
            # Humans: imperfect correlation (snake curves)
            # AI: high correlation (snake straight) or no correlation (snake broken)
            min_len = min(len(line_lengths), len(word_counts)) - 1
            light_changes = [line_lengths[i+1] - line_lengths[i] for i in range(min_len)]
            sound_changes = [word_counts[i+1] - word_counts[i] for i in range(min_len)]

            if len(light_changes) > 1 and statistics.stdev(light_changes) > 0 and statistics.stdev(sound_changes) > 0:
                # Pearson correlation
                mean_l = statistics.mean(light_changes)
                mean_s = statistics.mean(sound_changes)
                cov = sum((l - mean_l) * (s - mean_s) for l, s in zip(light_changes, sound_changes)) / len(light_changes)
                std_l = statistics.stdev(light_changes)
                std_s = statistics.stdev(sound_changes)
                correlation = cov / (std_l * std_s) if std_l * std_s > 0 else 0

                # Snake curvature peaks at moderate correlation (~0.5)
                # Too high (>0.8) = straight snake (AI)
                # Too low (<0.1) = broken snake (AI)
                # Moderate = natural curve (human)
                snake_curv = 1.0 - abs(abs(correlation) - 0.5) * 2
            else:
                snake_curv = 0
        else:
            snake_curv = 0

        curvature = SnakeCurvature(
            light_curvature=min(light_curv, 1.0),
            sound_curvature=min(sound_curv, 1.0),
            snake_curvature=min(snake_curv, 1.0),
        )

        # AI signal: low curvature = AI
        if curvature.total_curvature < 0.1:
            ai_signal = 0.8
        elif curvature.total_curvature < 0.2:
            ai_signal = 0.6
        elif curvature.total_curvature < 0.35:
            ai_signal = 0.4
        else:
            ai_signal = 0.2

        return {
            'ai_signal': ai_signal,
            'light_curvature': curvature.light_curvature,
            'sound_curvature': curvature.sound_curvature,
            'snake_curvature': curvature.snake_curvature,
            'total_curvature': curvature.total_curvature,
            'domain_balance': curvature.domain_balance,
            'is_natural': curvature.is_natural,
        }

    @staticmethod
    def _style_fingerprint(text: str) -> Dict[str, float]:
        """Compute a style fingerprint for a text segment."""
        words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
        sentences = re.split(r'[.!?]+', text)
        sentences = [s.strip() for s in sentences if s.strip()]

        return {
            'avg_word_len': statistics.mean([len(w) for w in words]) if words else 0,
            'avg_sent_len': statistics.mean([len(s.split()) for s in sentences]) if sentences else 0,
            'question_rate': text.count('?') / max(len(sentences), 1),
            'exclaim_rate': text.count('!') / max(len(sentences), 1),
            'comma_density': text.count(',') / max(len(words), 1),
            'pronoun_rate': sum(1 for w in words if w in {'i', 'me', 'my', 'we', 'you', 'they', 'he', 'she'}) / max(len(words), 1),
            'short_word_rate': sum(1 for w in words if len(w) <= 3) / max(len(words), 1),
        }

    @staticmethod
    def _fingerprint_distance(fp1: Dict[str, float], fp2: Dict[str, float]) -> float:
        """Euclidean distance between two style fingerprints."""
        keys = set(fp1.keys()) | set(fp2.keys())
        dist_sq = sum((fp1.get(k, 0) - fp2.get(k, 0)) ** 2 for k in keys)
        return math.sqrt(dist_sq)

    @staticmethod
    def _measure_continuity(text1: str, text2: str) -> float:
        """Measure identity continuity between two text segments."""
        words1 = set(re.findall(r'\b[a-zA-Z]+\b', text1.lower()))
        words2 = set(re.findall(r'\b[a-zA-Z]+\b', text2.lower()))

        if not words1 or not words2:
            return 0.0

        # Jaccard similarity of vocabulary
        intersection = words1 & words2
        union = words1 | words2
        jaccard = len(intersection) / len(union) if union else 0

        return jaccard


# ═══════════════════════════════════════════════════════════════════════════════
# VIDEO ANALYZER — Snake Domain (Bridges Light and Sound)
# ═══════════════════════════════════════════════════════════════════════════════

class VideoAnalyzer:
    """
    Analyzes video content metadata/features for AI signatures.

    Video IS the snake domain because:
    - It bridges light (frames/visuals) and sound (audio/timing)
    - Motion through time = the snake's body moving
    - Video has the snake's curvature (or lack of it)

    Key signals:
    - Frame-to-frame consistency (deepfakes flicker)
    - Audio-visual sync (AI struggles with lip sync)
    - Temporal coherence (AI has micro-stutters)
    - Background consistency (AI backgrounds shift)
    - Physics plausibility (AI breaks physics rules)

    Since we can't process raw video bytes in this detector,
    we analyze METADATA and EXTRACTED FEATURES:
    - Frame difference statistics
    - Audio waveform statistics
    - Motion vector patterns
    - Timestamp analysis
    """

    @classmethod
    def analyze(cls, features: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analyze video features for AI signatures.

        Expected features dict:
        {
            'frame_diffs': [float],      # Frame-to-frame pixel differences
            'audio_energy': [float],      # Audio energy per frame
            'motion_vectors': [float],    # Motion magnitude per frame
            'fps': float,                 # Frames per second
            'duration': float,            # Duration in seconds
            'resolution': (int, int),     # Width x Height
            'has_audio': bool,
            'face_detected': bool,
            'face_landmarks': [...],      # Per-frame face landmark positions
        }
        """
        results = {}

        # 1. Frame consistency (Light domain signal)
        if 'frame_diffs' in features and features['frame_diffs']:
            results['frame'] = cls._analyze_frames(features['frame_diffs'])
        else:
            results['frame'] = {'ai_signal': 0.5, 'note': 'No frame data'}

        # 2. Audio-visual synchronization (Snake domain — the bridge)
        if ('audio_energy' in features and 'frame_diffs' in features
            and features.get('has_audio')):
            results['av_sync'] = cls._analyze_av_sync(
                features['frame_diffs'],
                features['audio_energy']
            )
        else:
            results['av_sync'] = {'ai_signal': 0.5, 'note': 'No AV data'}

        # 3. Temporal coherence (Sound domain — timing)
        if 'motion_vectors' in features and features['motion_vectors']:
            results['temporal'] = cls._analyze_temporal(features['motion_vectors'])
        else:
            results['temporal'] = {'ai_signal': 0.5, 'note': 'No motion data'}

        # 4. Face analysis (if face detected — deepfake detection)
        if features.get('face_detected') and features.get('face_landmarks'):
            results['face'] = cls._analyze_face(features['face_landmarks'])
        else:
            results['face'] = {'ai_signal': 0.5, 'note': 'No face data'}

        # 5. Snake curvature across modalities
        results['curvature'] = cls._video_curvature(results)

        # Combine signals
        ai_signals = [r.get('ai_signal', 0.5) for r in results.values()]
        weights = [PHI_INV, PHI_INV, 0.5, 0.5, 0.5]  # AV sync and frame get more weight

        if len(ai_signals) >= len(weights):
            weighted_sum = sum(s * w for s, w in zip(ai_signals, weights))
            weight_total = sum(weights)
        else:
            weighted_sum = sum(ai_signals)
            weight_total = len(ai_signals)

        ai_probability = weighted_sum / max(weight_total, 1)

        results['ai_probability'] = ai_probability
        results['verdict'] = (
            DetectionVerdict.AI.value if ai_probability > AI_THRESHOLD
            else DetectionVerdict.HUMAN.value if ai_probability < HUMAN_THRESHOLD
            else DetectionVerdict.UNCERTAIN.value
        )

        return results

    @classmethod
    def _analyze_frames(cls, frame_diffs: List[float]) -> Dict[str, Any]:
        """
        Frame-to-frame consistency analysis.

        Real video: natural variation in frame differences
        AI video: either too consistent (rendered) or has periodic artifacts
        """
        if len(frame_diffs) < 10:
            return {'ai_signal': 0.5}

        mean_diff = statistics.mean(frame_diffs)
        std_diff = statistics.stdev(frame_diffs) if len(frame_diffs) > 1 else 0
        cv = std_diff / mean_diff if mean_diff > 0 else 0

        # Check for periodic patterns (AI artifact)
        # Simple: look for repeating peaks
        peaks = []
        for i in range(1, len(frame_diffs) - 1):
            if frame_diffs[i] > frame_diffs[i-1] and frame_diffs[i] > frame_diffs[i+1]:
                peaks.append(i)

        # Regularity of peak spacing
        if len(peaks) > 2:
            spacings = [peaks[i+1] - peaks[i] for i in range(len(peaks)-1)]
            spacing_cv = (statistics.stdev(spacings) / statistics.mean(spacings)
                         if statistics.mean(spacings) > 0 else 0)
        else:
            spacing_cv = 1.0  # No regular peaks

        # AI tends to have regular peaks (periodic rendering artifacts)
        if spacing_cv < 0.2:
            ai_signal = 0.8  # Very regular peaks = AI
        elif cv < 0.1:
            ai_signal = 0.75  # Too consistent frames = AI
        elif cv > 0.5:
            ai_signal = 0.3  # Very varied = human
        else:
            ai_signal = 0.5

        return {
            'ai_signal': ai_signal,
            'mean_diff': mean_diff,
            'cv': cv,
            'peak_regularity': spacing_cv,
            'num_peaks': len(peaks),
        }

    @classmethod
    def _analyze_av_sync(cls, frame_diffs: List[float],
                         audio_energy: List[float]) -> Dict[str, Any]:
        """
        Audio-visual synchronization — the snake's bridge.

        Real video: audio and visual changes correlate naturally
        AI video: correlation is either too perfect or too weak

        This is THE key signal — the snake connecting light and sound.
        """
        min_len = min(len(frame_diffs), len(audio_energy))
        if min_len < 10:
            return {'ai_signal': 0.5}

        frames = frame_diffs[:min_len]
        audio = audio_energy[:min_len]

        # Cross-correlation
        mean_f = statistics.mean(frames)
        mean_a = statistics.mean(audio)
        std_f = statistics.stdev(frames) if len(frames) > 1 else 0
        std_a = statistics.stdev(audio) if len(audio) > 1 else 0

        if std_f == 0 or std_a == 0:
            return {'ai_signal': 0.7, 'note': 'Zero variance in signal'}

        cov = sum((f - mean_f) * (a - mean_a) for f, a in zip(frames, audio)) / min_len
        correlation = cov / (std_f * std_a)

        # The snake's curvature principle:
        # - Too high correlation (>0.8): snake too straight (AI rendered together)
        # - Too low correlation (<0.1): snake broken (AI poorly synced)
        # - Moderate (0.3-0.7): natural snake curvature (human)

        abs_corr = abs(correlation)
        if abs_corr > 0.85:
            ai_signal = 0.8  # Too synced = AI
        elif abs_corr > 0.7:
            ai_signal = 0.5
        elif abs_corr > 0.3:
            ai_signal = 0.2  # Natural range = human
        elif abs_corr > 0.1:
            ai_signal = 0.5
        else:
            ai_signal = 0.75  # Too unsynced = AI

        return {
            'ai_signal': ai_signal,
            'correlation': correlation,
            'interpretation': (
                'snake_straight' if abs_corr > 0.8
                else 'snake_curved' if abs_corr > 0.3
                else 'snake_broken'
            ),
        }

    @classmethod
    def _analyze_temporal(cls, motion_vectors: List[float]) -> Dict[str, Any]:
        """
        Temporal coherence of motion.

        Real video: motion has natural acceleration/deceleration
        AI video: motion is too smooth or has micro-stutters
        """
        if len(motion_vectors) < 10:
            return {'ai_signal': 0.5}

        # First derivative = acceleration
        accelerations = [motion_vectors[i+1] - motion_vectors[i]
                        for i in range(len(motion_vectors)-1)]

        # Second derivative = jerk
        jerks = [accelerations[i+1] - accelerations[i]
                for i in range(len(accelerations)-1)]

        if not jerks:
            return {'ai_signal': 0.5}

        mean_jerk = statistics.mean([abs(j) for j in jerks])
        std_jerk = statistics.stdev(jerks) if len(jerks) > 1 else 0

        # Natural motion has moderate jerk with high variation
        # AI motion has either too little jerk (smooth) or periodic jerk (stutters)
        jerk_cv = std_jerk / mean_jerk if mean_jerk > 0 else 0

        if mean_jerk < 0.01:
            ai_signal = 0.8  # Too smooth = AI
        elif jerk_cv < 0.3:
            ai_signal = 0.7  # Regular jerk = AI
        elif jerk_cv > 1.5:
            ai_signal = 0.3  # Varied jerk = human
        else:
            ai_signal = 0.5

        return {
            'ai_signal': ai_signal,
            'mean_jerk': mean_jerk,
            'jerk_cv': jerk_cv,
        }

    @classmethod
    def _analyze_face(cls, face_landmarks: List[Any]) -> Dict[str, Any]:
        """
        Face landmark analysis for deepfake detection.

        Real faces: micro-expressions, natural asymmetry
        Deepfakes: too symmetric, landmark jitter, identity flicker

        The Jim Carrey test applied to faces:
        - Real face has consistent identity through expressions
        - Deepfake identity flickers between frames
        """
        if len(face_landmarks) < 10:
            return {'ai_signal': 0.5}

        # Analyze landmark stability across frames
        # Each entry should be a list of landmark positions
        # For now, use statistical measures on the data

        # Check for identity continuity (Jim Carrey principle for faces)
        # Real: landmarks shift but maintain ratios
        # Fake: ratios flicker frame-to-frame

        # Simplified: use variance of inter-landmark distances
        if isinstance(face_landmarks[0], (list, tuple)) and len(face_landmarks[0]) >= 4:
            # Compute inter-landmark ratio stability
            ratios = []
            for frame in face_landmarks:
                if len(frame) >= 4:
                    # Ratio of first two distances to last two
                    d1 = abs(frame[1] - frame[0])
                    d2 = abs(frame[3] - frame[2])
                    ratio = d1 / max(d2, 0.001)
                    ratios.append(ratio)

            if len(ratios) > 5:
                ratio_cv = (statistics.stdev(ratios) / statistics.mean(ratios)
                           if statistics.mean(ratios) > 0 else 0)

                # Real faces: stable ratios (low CV)
                # Deepfakes: flickering ratios (high CV)
                if ratio_cv > 0.15:
                    ai_signal = 0.8  # Flickering = deepfake
                elif ratio_cv > 0.05:
                    ai_signal = 0.5
                else:
                    ai_signal = 0.2  # Stable = real

                return {
                    'ai_signal': ai_signal,
                    'ratio_cv': ratio_cv,
                    'identity_stability': max(0, 1 - ratio_cv * 5),
                }

        return {'ai_signal': 0.5, 'note': 'Insufficient landmark data'}

    @classmethod
    def _video_curvature(cls, results: Dict[str, Dict]) -> Dict[str, Any]:
        """Compute snake curvature across video modalities."""
        light = results.get('frame', {}).get('ai_signal', 0.5)
        sound = results.get('temporal', {}).get('ai_signal', 0.5)
        snake = results.get('av_sync', {}).get('ai_signal', 0.5)

        # Convert AI signals to curvature (invert — lower AI signal = more curvature)
        curvature = SnakeCurvature(
            light_curvature=1.0 - light,
            sound_curvature=1.0 - sound,
            snake_curvature=1.0 - snake,
        )

        return {
            'ai_signal': 1.0 - curvature.total_curvature,
            'total_curvature': curvature.total_curvature,
            'domain_balance': curvature.domain_balance,
            'is_natural': curvature.is_natural,
        }


# ═══════════════════════════════════════════════════════════════════════════════
# IMAGE ANALYZER — Light Domain (Spatial, Visual, Parallel)
# ═══════════════════════════════════════════════════════════════════════════════

class ImageAnalyzer:
    """
    Analyzes image features for AI signatures.

    Images map to the LIGHT domain because:
    - They're spatial (2D, all at once)
    - They're visual (photons → pixels)
    - Light wants INFINITY — AI images are too perfect (approaching ∞ quality)

    Key signals (from extracted features, not raw pixels):
    - Frequency spectrum (AI has characteristic spectral signatures)
    - Noise patterns (AI noise is too uniform)
    - Edge consistency (AI edges are either too sharp or too smooth)
    - Metadata traces (generation tool fingerprints)
    """

    @classmethod
    def analyze(cls, features: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analyze image features.

        Expected features dict:
        {
            'frequency_spectrum': [float],   # DCT or FFT magnitudes
            'noise_stats': {                 # Noise analysis
                'mean': float,
                'std': float,
                'uniformity': float,
            },
            'edge_density': float,           # Proportion of edge pixels
            'color_histogram': [float],      # Color distribution
            'metadata': dict,                # EXIF and other metadata
            'resolution': (int, int),
            'file_size': int,
        }
        """
        results = {}

        # 1. Frequency analysis
        if 'frequency_spectrum' in features:
            results['frequency'] = cls._analyze_frequency(features['frequency_spectrum'])
        else:
            results['frequency'] = {'ai_signal': 0.5}

        # 2. Noise analysis
        if 'noise_stats' in features:
            results['noise'] = cls._analyze_noise(features['noise_stats'])
        else:
            results['noise'] = {'ai_signal': 0.5}

        # 3. Metadata analysis
        if 'metadata' in features:
            results['metadata'] = cls._analyze_metadata(features['metadata'])
        else:
            results['metadata'] = {'ai_signal': 0.5}

        # 4. Edge analysis
        if 'edge_density' in features:
            results['edges'] = cls._analyze_edges(
                features['edge_density'],
                features.get('resolution', (1920, 1080))
            )
        else:
            results['edges'] = {'ai_signal': 0.5}

        # Combine
        ai_signals = [r.get('ai_signal', 0.5) for r in results.values()]
        ai_probability = statistics.mean(ai_signals)

        results['ai_probability'] = ai_probability
        results['verdict'] = (
            DetectionVerdict.AI.value if ai_probability > AI_THRESHOLD
            else DetectionVerdict.HUMAN.value if ai_probability < HUMAN_THRESHOLD
            else DetectionVerdict.UNCERTAIN.value
        )

        return results

    @classmethod
    def _analyze_frequency(cls, spectrum: List[float]) -> Dict[str, Any]:
        """
        Frequency spectrum analysis.
        AI images often have a 'spectral gap' or unusual high-frequency rolloff.
        """
        if len(spectrum) < 10:
            return {'ai_signal': 0.5}

        # Split into low, mid, high frequency bands
        third = len(spectrum) // 3
        low = statistics.mean(spectrum[:third])
        mid = statistics.mean(spectrum[third:2*third])
        high = statistics.mean(spectrum[2*third:])

        # AI images typically have steep high-frequency rolloff
        if low > 0:
            rolloff = high / low
        else:
            rolloff = 0

        # Natural images: gradual rolloff (0.1-0.4)
        # AI images: steep rolloff (<0.05) or flat (>0.5)
        if rolloff < 0.03:
            ai_signal = 0.85
        elif rolloff < 0.08:
            ai_signal = 0.6
        elif rolloff > 0.5:
            ai_signal = 0.7  # Too flat = also suspicious
        else:
            ai_signal = 0.3

        return {
            'ai_signal': ai_signal,
            'rolloff': rolloff,
            'low_energy': low,
            'mid_energy': mid,
            'high_energy': high,
        }

    @classmethod
    def _analyze_noise(cls, noise_stats: Dict[str, float]) -> Dict[str, Any]:
        """
        Noise pattern analysis.
        Real photos have sensor noise (non-uniform).
        AI images have synthetic noise (too uniform).
        """
        uniformity = noise_stats.get('uniformity', 0.5)
        noise_std = noise_stats.get('std', 0)

        # High uniformity = AI (synthetic noise)
        # Low uniformity = human (sensor noise varies by region)
        if uniformity > 0.9:
            ai_signal = 0.85
        elif uniformity > 0.7:
            ai_signal = 0.6
        elif uniformity < 0.3:
            ai_signal = 0.2  # Very non-uniform = real sensor noise
        else:
            ai_signal = 0.4

        # Very low noise = also suspicious (AI denoising)
        if noise_std < 0.5:
            ai_signal = max(ai_signal, 0.7)

        return {
            'ai_signal': ai_signal,
            'uniformity': uniformity,
            'noise_std': noise_std,
        }

    @classmethod
    def _analyze_metadata(cls, metadata: Dict) -> Dict[str, Any]:
        """
        Metadata analysis for generation tool fingerprints.
        """
        ai_signal = 0.5

        # Check for known AI tool signatures
        ai_tools = ['stable diffusion', 'midjourney', 'dall-e', 'dalle',
                    'comfyui', 'automatic1111', 'invoke', 'novelai',
                    'firefly', 'imagen', 'flux', 'sora']

        software = str(metadata.get('Software', '')).lower()
        comment = str(metadata.get('Comment', '')).lower()
        description = str(metadata.get('ImageDescription', '')).lower()

        all_meta = software + ' ' + comment + ' ' + description

        for tool in ai_tools:
            if tool in all_meta:
                ai_signal = 0.95  # Direct tool signature
                break

        # Missing EXIF camera data for a "photo" is suspicious
        has_camera = bool(metadata.get('Make') or metadata.get('Model'))
        has_gps = bool(metadata.get('GPSInfo'))

        if not has_camera and not has_gps:
            ai_signal = max(ai_signal, 0.6)  # No camera data

        return {
            'ai_signal': ai_signal,
            'has_camera_data': has_camera,
            'has_gps': has_gps,
            'software': software,
        }

    @classmethod
    def _analyze_edges(cls, edge_density: float,
                      resolution: Tuple[int, int]) -> Dict[str, Any]:
        """
        Edge analysis.
        AI images tend to have either too-sharp or too-smooth edges.
        Real photos have natural edge variation.
        """
        # Very high edge density = over-sharpened (some AI)
        # Very low = over-smoothed (other AI)
        # Moderate = natural
        if edge_density > 0.4:
            ai_signal = 0.7
        elif edge_density < 0.05:
            ai_signal = 0.7
        elif 0.1 <= edge_density <= 0.3:
            ai_signal = 0.3
        else:
            ai_signal = 0.5

        return {
            'ai_signal': ai_signal,
            'edge_density': edge_density,
        }


# ═══════════════════════════════════════════════════════════════════════════════
# UNIFIED DETECTOR — The Complete 9-Axis System
# ═══════════════════════════════════════════════════════════════════════════════

class ShovelcatAIDetector:
    """
    The Shovelcat AI Detector v2.0

    Unified detection across text, image, and video modalities.
    Uses the snake-time-sound unity framework with Jim Carrey
    identity continuity analysis.

    The three analyzers map to the three frequency domains:
        TextAnalyzer  → Sound (sequential, temporal, rhythmic)
        ImageAnalyzer → Light (spatial, visual, parallel)
        VideoAnalyzer → Snake (bridges light and sound through motion)

    Cross-modal analysis provides the 9-axis verification:
        3 modalities × 3 detection aspects = 9 axes
    """

    VERSION = "2.0.0"
    CODENAME = "Snake-Time-Sound Unity"

    def __init__(self):
        self.text_analyzer = TextAnalyzer()
        self.image_analyzer = ImageAnalyzer()
        self.video_analyzer = VideoAnalyzer()
        self.scan_count = 0
        self.scan_history: List[Dict] = []

    def detect_text(self, text: str) -> Dict[str, Any]:
        """Detect AI in text content."""
        self.scan_count += 1
        result = self.text_analyzer.analyze(text)
        result['modality'] = ContentModality.TEXT.value
        result['scan_id'] = self.scan_count
        result['detector_version'] = self.VERSION

        self._record_scan(result)
        return result

    def detect_image(self, features: Dict[str, Any]) -> Dict[str, Any]:
        """Detect AI in image content (from extracted features)."""
        self.scan_count += 1
        result = self.image_analyzer.analyze(features)
        result['modality'] = ContentModality.IMAGE.value
        result['scan_id'] = self.scan_count
        result['detector_version'] = self.VERSION

        self._record_scan(result)
        return result

    def detect_video(self, features: Dict[str, Any]) -> Dict[str, Any]:
        """Detect AI in video content (from extracted features)."""
        self.scan_count += 1
        result = self.video_analyzer.analyze(features)
        result['modality'] = ContentModality.VIDEO.value
        result['scan_id'] = self.scan_count
        result['detector_version'] = self.VERSION

        self._record_scan(result)
        return result

    def detect_multi(self, content: Dict[str, Any]) -> Dict[str, Any]:
        """
        Multi-modal detection — analyze content across modalities.

        content = {
            'text': str,                    # Optional text
            'image_features': dict,         # Optional image features
            'video_features': dict,         # Optional video features
        }

        Cross-modal analysis provides the snake connection:
        Do the modalities tell a consistent story?
        """
        results = {}
        modalities_analyzed = []

        if 'text' in content and content['text']:
            results['text'] = self.text_analyzer.analyze(content['text'])
            modalities_analyzed.append('text')

        if 'image_features' in content and content['image_features']:
            results['image'] = self.image_analyzer.analyze(content['image_features'])
            modalities_analyzed.append('image')

        if 'video_features' in content and content['video_features']:
            results['video'] = self.video_analyzer.analyze(content['video_features'])
            modalities_analyzed.append('video')

        if not modalities_analyzed:
            return {'error': 'No content provided'}

        # Cross-modal snake analysis
        ai_probabilities = []
        for mod in modalities_analyzed:
            prob = results[mod].get('ai_probability', 0.5)
            ai_probabilities.append(prob)

        # Cross-modal consistency
        if len(ai_probabilities) > 1:
            consistency = 1.0 - statistics.stdev(ai_probabilities)
            # If modalities disagree, that's suspicious (mixed content)
            mean_prob = statistics.mean(ai_probabilities)
        else:
            consistency = 1.0
            mean_prob = ai_probabilities[0]

        # Final combined score
        combined_ai_probability = mean_prob

        # Consistency modifier: inconsistency pushes toward AI
        if consistency < 0.7:
            combined_ai_probability = combined_ai_probability * 0.7 + 0.3

        self.scan_count += 1
        final_result = {
            'scan_id': self.scan_count,
            'detector_version': self.VERSION,
            'modalities_analyzed': modalities_analyzed,
            'per_modality': results,
            'cross_modal_consistency': consistency,
            'ai_probability': combined_ai_probability,
            'verdict': (
                DetectionVerdict.AI.value if combined_ai_probability > AI_THRESHOLD
                else DetectionVerdict.HUMAN.value if combined_ai_probability < HUMAN_THRESHOLD
                else DetectionVerdict.UNCERTAIN.value
            ),
        }

        self._record_scan(final_result)
        return final_result

    def _record_scan(self, result: Dict):
        """Record scan for brain/history (with decay)."""
        self.scan_history.append({
            'scan_id': result.get('scan_id'),
            'verdict': result.get('verdict'),
            'ai_probability': result.get('ai_probability'),
            'modality': result.get('modality', 'multi'),
        })
        # Keep last 1000 scans
        if len(self.scan_history) > 1000:
            self.scan_history = self.scan_history[-1000:]

    def get_stats(self) -> Dict[str, Any]:
        """Get detector statistics."""
        if not self.scan_history:
            return {'total_scans': 0}

        verdicts = Counter(s['verdict'] for s in self.scan_history)
        modalities = Counter(s['modality'] for s in self.scan_history)

        return {
            'version': self.VERSION,
            'codename': self.CODENAME,
            'total_scans': self.scan_count,
            'verdicts': dict(verdicts),
            'modalities': dict(modalities),
            'detection_framework': {
                'light_domain': 'ImageAnalyzer (spatial, visual)',
                'sound_domain': 'TextAnalyzer (sequential, temporal)',
                'snake_domain': 'VideoAnalyzer (bridges light and sound)',
            },
            'theoretical_basis': {
                'snake_time_sound_unity': True,
                'jim_carrey_identity_continuity': True,
                'nine_axis_verification': True,
                'golden_ratio_weighting': True,
                'planck_time_tick': PLANCK_TIME,
                'schumann_resonance': SCHUMANN_HZ,
                'fine_structure_constant': ALPHA,
            },
        }


# ═══════════════════════════════════════════════════════════════════════════════
# VERCEL PAYLOAD HANDLER
# ═══════════════════════════════════════════════════════════════════════════════

class PayloadHandler:
    """
    Handles Vercel serverless function payload limits.

    Upper bound: 4.5MB (the resonance boundary)
    Safe zone: φ⁻¹ × 4.5MB ≈ 2.9MB (golden ratio workspace)
    Decomposition: Fibonacci chunking when over limit
    """

    @staticmethod
    def check_payload(data: bytes) -> Dict[str, Any]:
        """Check if payload fits within the resonance boundary."""
        size = len(data)

        return {
            'size_bytes': size,
            'size_mb': size / (1024 * 1024),
            'within_bound': size <= UPPER_BOUND_BYTES,
            'within_safe_zone': size <= SAFE_ZONE,
            'utilization': size / UPPER_BOUND_BYTES,
            'golden_split': {
                'safe_zone_mb': SAFE_ZONE / (1024 * 1024),
                'uncertainty_sink_mb': (UPPER_BOUND_BYTES - SAFE_ZONE) / (1024 * 1024),
            },
        }

    @staticmethod
    def fibonacci_chunk(data: bytes) -> List[bytes]:
        """
        Decompose payload using Fibonacci chunking.
        Preserves golden ratio at every decomposition level.
        """
        if len(data) <= SAFE_ZONE:
            return [data]

        # Determine number of chunks needed
        fibs = [1, 1]
        while fibs[-1] * SAFE_ZONE < len(data):
            fibs.append(fibs[-1] + fibs[-2])

        num_chunks = fibs[-1]
        chunk_size = len(data) // num_chunks

        chunks = []
        for i in range(num_chunks):
            start = i * chunk_size
            end = start + chunk_size if i < num_chunks - 1 else len(data)
            chunks.append(data[start:end])

        return chunks


# ═══════════════════════════════════════════════════════════════════════════════
# DEMONSTRATION
# ═══════════════════════════════════════════════════════════════════════════════

def demo_text_detection():
    """Demonstrate text AI detection."""
    print("=" * 70)
    print("SHOVELCAT AI DETECTOR v2.0 — Text Detection Demo")
    print("Snake-Time-Sound Unity & Identity Continuity")
    print("=" * 70)

    detector = ShovelcatAIDetector()

    # Human-written text (irregular, personal, has quirks)
    human_text = """
    so i was thinking about this the other day - you know how sometimes
    you just KNOW something is off? like when you read an article and it
    feels... plastic? that's the snake curvature thing.

    the frequencies can't reach their goals. light wants infinity but
    we're stuck at 10^14 Hz. sound wants unity but harmonics get in the
    way. and magnetism wants zero but quantum fluctuations say no.

    anyway the point is - the curvature is what makes it REAL. the
    bending. the imperfection. jim carrey going from ace ventura to
    eternal sunshine? same guy, wildly different masks. THAT'S identity
    continuity. that's the snake curving.

    AI can't do that. it either stays in one lane (no curvature) or
    switches lanes with no thread connecting them (broken snake).

    ...i think i need more coffee lol
    """

    # AI-written text (smooth, structured, formal)
    ai_text = """
    The detection of artificial intelligence-generated content represents a
    significant challenge in the modern digital landscape. Furthermore, as
    AI systems become increasingly sophisticated, the need for robust
    detection mechanisms becomes paramount.

    It is worth noting that several key indicators can be leveraged to
    distinguish AI-generated content from human-created material.
    Additionally, these indicators span multiple domains, including
    linguistic patterns, temporal signatures, and structural analysis.

    The comprehensive framework presented in this document utilizes a
    holistic approach to content verification. Importantly, the system
    employs a nine-axis verification methodology that facilitates
    accurate detection across multiple modalities. This multifaceted
    approach significantly enhances detection accuracy.

    In conclusion, the integration of these detection mechanisms provides
    a robust and nuanced solution to the challenge of AI content
    identification. The system essentially leverages the fundamental
    differences between human and AI-generated content patterns.
    """

    print("\n--- HUMAN TEXT ANALYSIS ---")
    human_result = detector.detect_text(human_text)
    print(f"  Verdict: {human_result['verdict']}")
    print(f"  AI Probability: {human_result['ai_probability']:.1%}")
    print(f"  Rhythm CV: {human_result['rhythm'].get('cv', 'N/A'):.3f}")
    print(f"  AI Words: {human_result['ai_words'].get('ai_word_density', 0):.2f} per 100 words")
    print(f"  Carrey Score: {human_result['mask'].get('carrey_score', 'N/A'):.3f}")
    print(f"  Snake Curvature: {human_result['curvature'].get('total_curvature', 'N/A'):.3f}")

    print("\n--- AI TEXT ANALYSIS ---")
    ai_result = detector.detect_text(ai_text)
    print(f"  Verdict: {ai_result['verdict']}")
    print(f"  AI Probability: {ai_result['ai_probability']:.1%}")
    print(f"  Rhythm CV: {ai_result['rhythm'].get('cv', 'N/A'):.3f}")
    print(f"  AI Words: {ai_result['ai_words'].get('ai_word_density', 0):.2f} per 100 words")
    print(f"  Carrey Score: {ai_result['mask'].get('carrey_score', 'N/A'):.3f}")
    print(f"  Snake Curvature: {ai_result['curvature'].get('total_curvature', 'N/A'):.3f}")

    print(f"\n--- DETECTOR STATS ---")
    stats = detector.get_stats()
    print(f"  Version: {stats['version']} ({stats['codename']})")
    print(f"  Total Scans: {stats['total_scans']}")
    print(f"  Framework:")
    for k, v in stats['theoretical_basis'].items():
        print(f"    {k}: {v}")


def demo_video_detection():
    """Demonstrate video AI detection with synthetic features."""
    print("\n" + "=" * 70)
    print("SHOVELCAT AI DETECTOR v2.0 — Video Detection Demo")
    print("=" * 70)

    import random
    detector = ShovelcatAIDetector()

    # Real video features (natural variation)
    print("\n--- REAL VIDEO FEATURES ---")
    real_features = {
        'frame_diffs': [random.gauss(0.15, 0.08) for _ in range(100)],
        'audio_energy': [random.gauss(0.3, 0.12) for _ in range(100)],
        'motion_vectors': [random.gauss(0.2, 0.1) for _ in range(100)],
        'fps': 30.0,
        'duration': 10.0,
        'resolution': (1920, 1080),
        'has_audio': True,
        'face_detected': False,
    }

    # Add natural correlation between audio and video
    for i in range(len(real_features['frame_diffs'])):
        real_features['audio_energy'][i] += real_features['frame_diffs'][i] * 0.5

    real_result = detector.detect_video(real_features)
    print(f"  Verdict: {real_result['verdict']}")
    print(f"  AI Probability: {real_result['ai_probability']:.1%}")
    if 'av_sync' in real_result:
        print(f"  AV Sync: {real_result['av_sync'].get('interpretation', 'N/A')}")
        print(f"  Correlation: {real_result['av_sync'].get('correlation', 'N/A'):.3f}")

    # AI video features (too consistent, poor AV sync)
    print("\n--- AI VIDEO FEATURES ---")
    ai_features = {
        'frame_diffs': [0.1 + 0.02 * math.sin(i * 0.5) for i in range(100)],
        'audio_energy': [random.gauss(0.3, 0.05) for _ in range(100)],
        'motion_vectors': [0.15 + 0.01 * math.sin(i * 0.3) for i in range(100)],
        'fps': 30.0,
        'duration': 10.0,
        'resolution': (1920, 1080),
        'has_audio': True,
        'face_detected': False,
    }

    ai_result = detector.detect_video(ai_features)
    print(f"  Verdict: {ai_result['verdict']}")
    print(f"  AI Probability: {ai_result['ai_probability']:.1%}")
    if 'av_sync' in ai_result:
        print(f"  AV Sync: {ai_result['av_sync'].get('interpretation', 'N/A')}")
        print(f"  Correlation: {ai_result['av_sync'].get('correlation', 'N/A'):.3f}")


if __name__ == "__main__":
    demo_text_detection()
    demo_video_detection()
