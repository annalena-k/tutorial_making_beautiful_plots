from typing import Tuple
import matplotlib as mpl


def _to_hex(rgb: Tuple) -> str:
    normalized = tuple(x / 255.0 for x in rgb)
    return mpl.colors.rgb2hex(normalized)


def okabe_and_ito() -> dict:
    """Okabe & Ito colorblind-safe palette — the most widely recommended choice.

    8 colors distinguishable under all common types of color vision deficiency
    (deuteranopia, protanopia, tritanopia) and in greyscale.

    Key names and hex values from the original CUD specification.
    Reference: Okabe & Ito (2008). https://jfly.uni-koeln.de/color/ (orig. 2002)
    """
    return {
        "black":          _to_hex((0,   0,   0)),    # #000000
        "orange":         _to_hex((230, 159, 0)),    # #E69F00
        "sky_blue":       _to_hex((86,  180, 233)),  # #56B4E9
        "bluish_green":   _to_hex((0,   158, 115)),  # #009E73
        "yellow":         _to_hex((240, 228, 66)),   # #F0E442
        "blue":           _to_hex((0,   114, 178)),  # #0072B2
        "vermillion":     _to_hex((213, 94,  0)),    # #D55E00
        "reddish_purple": _to_hex((204, 121, 167)),  # #CC79A7
    }


def accessible_colors() -> dict:
    """10-color accessible scheme from Chatterjee et al. (2021).

    A broader palette when more than 8 categories are needed.
    Reference: Petroff (2021). https://arxiv.org/abs/2107.02270
    """
    return {
        "blue":       _to_hex((63,  144, 218)),
        "orange":     _to_hex((255, 169, 14)),
        "purple":     _to_hex((131, 45,  182)),
        "red":        _to_hex((189, 31,  1)),
        "gray":       _to_hex((148, 164, 162)),
        "dark_orange":_to_hex((231, 99,  0)),
        "light_blue": _to_hex((146, 218, 221)),
        "dark_gray":  _to_hex((113, 117, 129)),
        "tan":        _to_hex((185, 172, 112)),
        "brown":      _to_hex((169, 107, 89)),
    }


def paul_tol_bright() -> dict:
    """Paul Tol's Bright palette — vivid, high-contrast, good for scatter plots and lines.

    7 colors. Official values from Paul Tol's notes (2021).
    Reference: https://personal.sron.nl/~pault/data/colourschemes.pdf
    """
    return {
        "blue":   _to_hex((68,  119, 170)),  # #4477AA
        "cyan":   _to_hex((102, 204, 238)),  # #66CCEE
        "green":  _to_hex((34,  136, 51)),   # #228833
        "yellow": _to_hex((204, 187, 68)),   # #CCBB44
        "red":    _to_hex((238, 102, 119)),  # #EE6677
        "purple": _to_hex((170, 51,  119)),  # #AA3377
        "grey":   _to_hex((187, 187, 187)),  # #BBBBBB
    }


def paul_tol_muted() -> dict:
    """Paul Tol's Muted palette — softer tones, good for filled areas.

    10 colors. Official values from Paul Tol's notes (2021).
    Reference: https://personal.sron.nl/~pault/data/colourschemes.pdf
    """
    return {
        "indigo":    _to_hex((51,  34,  136)),  # #332288
        "cyan":      _to_hex((136, 204, 238)),  # #88CCEE
        "teal":      _to_hex((68,  170, 153)),  # #44AA99
        "green":     _to_hex((17,  119, 51)),   # #117733
        "olive":     _to_hex((153, 153, 51)),   # #999933
        "sand":      _to_hex((221, 204, 119)),  # #DDCC77
        "rose":      _to_hex((204, 102, 119)),  # #CC6677
        "wine":      _to_hex((136, 34,  85)),   # #882255
        "purple":    _to_hex((170, 68,  153)),  # #AA4499
        "pale_grey": _to_hex((221, 221, 221)),  # #DDDDDD
    }


def ibm_design_library() -> dict:
    """IBM Design Library colorblind-safe palette — 5 high-contrast colors.

    Optimized for colorblind accessibility by IBM's design team.
    Reference: https://www.ibm.com/design/language/color/
    """
    return {
        "blue":    _to_hex((100, 143, 255)),  # #648FFF
        "purple":  _to_hex((120, 94,  240)),  # #785EF0
        "magenta": _to_hex((220, 38,  127)),  # #DC267F
        "orange":  _to_hex((254, 97,  0)),    # #FE6100
        "gold":    _to_hex((255, 176, 0)),    # #FFB000
    }


def nceas_two_color_pairs() -> dict:
    """Two-color categorical pairs designed for colorblind accessibility.

    8 pairs curated by Alexandra Phillips for NCEAS (2022). Values verified by
    pixel-sampling the published PDF swatches.

    Each value is a list [color_1_hex, color_2_hex].
    Reference: https://www.nceas.ucsb.edu/sites/default/files/2022-06/Colorblind%20Safe%20Color%20Schemes.pdf
    """
    return {
        "yellow_blue":    [_to_hex((253, 179, 56)),   _to_hex((2,   81,  150))],
        "tan_turquoise":  [_to_hex((227, 190, 107)),  _to_hex((61,  177, 166))],
        "orange_purple":  [_to_hex((235, 97,  35)),   _to_hex((81,  40,  136))],
        "green_purple":   [_to_hex((41,  94,  17)),   _to_hex((88,  9,   79))],
        "blue_red":       [_to_hex((47,  103, 177)),  _to_hex((191, 44,  35))],
        "blue_pink":      [_to_hex((16,  85,  154)),  _to_hex((219, 76,  119))],
        "yellow_pink":    [_to_hex((244, 179, 1)),    _to_hex((219, 16,  72))],
        "brown_blue":     [_to_hex((106, 74,  60)),   _to_hex((15,  101, 161))],
    }


def nceas_blue_to_red() -> list:
    """Divergent blue-to-red colormap (9 stops) from Alexandra Phillips / NCEAS (2022).

    Suitable for data with a meaningful midpoint (e.g. anomalies, correlations).
    Returns a list of 9 hex strings ordered from blue → near-white → red.

    Reference: https://www.nceas.ucsb.edu/sites/default/files/2022-06/Colorblind%20Safe%20Color%20Schemes.pdf
    """
    return [
        _to_hex((16,  101, 171)),  # dark blue
        _to_hex((58,  147, 195)),  # medium blue
        _to_hex((142, 196, 222)),  # light blue
        _to_hex((209, 229, 240)),  # pale blue
        _to_hex((249, 240, 249)),  # near-white center
        _to_hex((254, 219, 199)),  # pale salmon
        _to_hex((246, 164, 130)),  # salmon
        _to_hex((215, 95,  76)),   # medium red
        _to_hex((179, 21,  41)),   # dark red
    ]


def nceas_purple_to_green() -> list:
    """Divergent purple-to-green colormap (9 stops) from Alexandra Phillips / NCEAS (2022).

    An alternative to blue-to-red for deuteranopia-safe divergent data.
    Returns a list of 9 hex strings ordered from purple → near-white → green.

    Reference: https://www.nceas.ucsb.edu/sites/default/files/2022-06/Colorblind%20Safe%20Color%20Schemes.pdf
    """
    return [
        _to_hex((116, 40,  129)),  # dark purple
        _to_hex((152, 110, 172)),  # medium purple
        _to_hex((195, 164, 207)),  # light purple
        _to_hex((229, 212, 232)),  # pale purple
        _to_hex((249, 240, 249)),  # near-white center
        _to_hex((217, 241, 213)),  # pale green
        _to_hex((173, 212, 160)),  # light green
        _to_hex((92,  174, 99)),   # medium green
        _to_hex((27,  121, 57)),   # dark green
    ]
