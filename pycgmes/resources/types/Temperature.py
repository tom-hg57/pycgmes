"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from ...utils.datatypes import CIMDatatype
from ...utils.profile import Profile
from .UnitMultiplier import UnitMultiplier
from .UnitSymbol import UnitSymbol


Temperature = CIMDatatype(
    name="Temperature",
    type=float,
    multiplier=UnitMultiplier.none,
    unit=UnitSymbol.degC,
    profiles=[
        Profile.DY,
        Profile.SC,
    ],
)

"""
Value of temperature in degrees Celsius.
"""