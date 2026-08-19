from typing import Tuple
import matplotlib as mpl


def _to_hex(rgb: Tuple) -> str:
    normalized = tuple(x / 255.0 for x in rgb)
    return mpl.colors.rgb2hex(normalized)


def okabe_and_ito() -> dict:
    """Okabe & Ito (2008) colorblind-safe palette — the most widely recommended choice.

    8 colors, distinguishable under all common types of color vision deficiency.
    Reference: https://jfly.uni-koeln.de/color/
    """
    return {
        "black":       _to_hex((0, 0, 0)),
        "green":       _to_hex((0, 158, 115)),
        "blue":        _to_hex((0, 114, 178)),
        "lightblue":   _to_hex((86, 180, 233)),
        "yellow":      _to_hex((240, 228, 66)),
        "lightorange": _to_hex((230, 159, 0)),
        "orange":      _to_hex((213, 94, 0)),
        "lightpink":   _to_hex((204, 121, 167)),
    }


def accessible_colors() -> dict:
    """10-color accessible scheme from arXiv:2107.02270.

    A broader palette for cases where more than 8 colors are needed.
    Reference: https://doi.org/10.48550/arXiv.2107.02270
    """
    return {
        "blue":        _to_hex((63, 144, 218)),
        "orange":      _to_hex((255, 169, 14)),
        "purple":      _to_hex((131, 45, 182)),
        "red":         _to_hex((189, 31, 1)),
        "gray":        _to_hex((148, 164, 162)),
        "dark orange": _to_hex((231, 99, 0)),
        "light blue":  _to_hex((146, 218, 221)),
        "dark gray":   _to_hex((113, 117, 129)),
        "tan":         _to_hex((185, 172, 112)),
        "brown":       _to_hex((169, 107, 89)),
    }


def paul_tol_bright() -> dict:
    """Paul Tol's Bright palette — clean and vibrant, good for multiple categories.

    Reference: https://personal.sron.nl/~pault/
    """
    return {
        "grey":       _to_hex((187, 187, 187)),
        "blue":       _to_hex((60, 107, 159)),
        "green":      _to_hex((51, 117, 56)),
        "lightblue":  _to_hex((93, 168, 153)),
        "yellow":     _to_hex((201, 187, 88)),
        "rose":       _to_hex((235, 91, 108)),
        "pink":       _to_hex((160, 45, 108)),
    }


def paul_tol_muted() -> dict:
    """Paul Tol's Muted palette — softer tones, good for filled areas and backgrounds.

    Reference: https://personal.sron.nl/~pault/
    Also in: https://www.nceas.ucsb.edu/sites/default/files/2022-06/Colorblind Safe Color Schemes.pdf
    """
    return {
        "grey":         _to_hex((221, 221, 221)),
        "darkblue":     _to_hex((46, 37, 133)),
        "darkgreen":    _to_hex((51, 117, 56)),
        "lightgreen":   _to_hex((93, 168, 153)),
        "lightblue":    _to_hex((148, 203, 236)),
        "lightyellow":  _to_hex((220, 205, 125)),
        "lightred":     _to_hex((194, 106, 119)),
        "magnolia":     _to_hex((159, 74, 150)),
        "darkmagnolia": _to_hex((126, 41, 84)),
    }


def ibm_design_library() -> dict:
    """IBM Design Library colorblind-safe palette — 5 high-contrast colors.

    Reference: https://www.nceas.ucsb.edu/sites/default/files/2022-06/Colorblind Safe Color Schemes.pdf
    """
    return {
        "blue":   _to_hex((81, 131, 253)),
        "purple": _to_hex((103, 83, 236)),
        "pink":   _to_hex((216, 30, 114)),
        "orange": _to_hex((255, 84, 0)),
        "yellow": _to_hex((255, 167, 15)),
    }
