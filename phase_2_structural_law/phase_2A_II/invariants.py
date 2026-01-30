"""
Phase 2A-II — Structural Invariants
Declares non-negotiable shape laws.
No enforcement yet.
"""

# Categories of invariants that exist in this system
STRUCTURAL_INVARIANTS = {
    "cardinality",
    "containment",
    "composition",
    "reference",
    "phase_ordering",
}

# --------------------------------
# Cardinality invariants
# (How many of a thing may exist)
# --------------------------------

CARDINALITY_RULES = {
    "ScalarCarrier": {
        "min": 0,
        "max": None,
    },
    "VectorCarrier": {
        "min": 1,
        "max": None,
    },
    "MatrixCarrier": {
        "min": 1,
        "max": None,
    },
    "Point": {
        "min": 1,
        "max": None,
    },
}

# --------------------------------
# Containment invariants
# (What may contain what)
# --------------------------------

CONTAINMENT_RULES = {
    "VectorCarrier": {"ScalarCarrier"},
    "MatrixCarrier": {"VectorCarrier"},
}

# --------------------------------
# Composition invariants
# (How structures may be assembled)
# --------------------------------

COMPOSITION_RULES = {
    "disallow_mixed_carriers": True,
    "require_homogeneous_containment": True,
}

# --------------------------------
# Reference invariants
# (What may point to what)
# --------------------------------

REFERENCE_RULES = {
    "allow_self_reference": False,
    "allow_forward_reference": False,
    "allow_cross_phase_reference": False,
}

# --------------------------------
# Phase ordering invariants
# (What cannot exist yet)
# --------------------------------

PHASE_ORDERING_RULES = {
    "PHASE_2A_I": {
        "forbidden": {
            "symbols",
            "tokens",
            "recursion",
            "environments",
            "evaluation",
        }
    }
}

# --------------------------------
# Declaration hook (no enforcement)
# --------------------------------

def invariants_declared():
    return True
