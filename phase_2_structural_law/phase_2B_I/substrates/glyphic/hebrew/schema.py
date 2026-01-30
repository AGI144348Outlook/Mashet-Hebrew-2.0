"""
Inert Hebrew Glyph Schema
Phase: 2B-I
Status: Declarative only
"""

HEBREW_GLYPH_SCHEMA = {
    "glyph_id": str,            # Unique identifier (e.g. "aleph")
    "glyph_set": "hebrew",       # Fixed substrate family
    "substrate_type": "glyph",   # Glyphic, not icon, not operator

    # Structural classification only
    "form_class": str,           # e.g. linear, enclosed, open, composite
    "directionality": str,       # e.g. none, left, right, bilateral
    "closure": str,              # open / closed / mixed

    # Domain labels (non-operative)
    "allowed_domains": list,     # e.g. ["earth", "water", "air", "fire"]

    # Structural constraints
    "allows_containment": bool,  # Can this glyph host others? (label only)
    "allows_adjacency": bool,    # Can it sit next to others?
    "allows_stacking": bool,     # Can it be layered?

    # Lifecycle state
    "status": "inert",            # Locked at Phase 2B-I

    # Explicit prohibitions (defensive)
    "meaning": None,
    "phonetic": None,
    "numeric": None,
    "behavior": None,
}
