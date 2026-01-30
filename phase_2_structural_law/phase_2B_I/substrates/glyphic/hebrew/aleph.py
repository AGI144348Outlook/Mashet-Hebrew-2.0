from .schema import HEBREW_GLYPH_SCHEMA

ALEPH = {
    "glyph_id": "aleph",
    "glyph_set": "hebrew",
    "substrate_type": "glyph",

    "form_class": "composite",
    "directionality": "none",
    "closure": "open",

    "allowed_domains": ["air"],

    "allows_containment": False,
    "allows_adjacency": True,
    "allows_stacking": False,

    "status": "inert",

    "meaning": None,
    "phonetic": None,
    "numeric": None,
    "behavior": None,
}
