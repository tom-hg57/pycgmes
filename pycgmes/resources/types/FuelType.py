"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from enum import Enum


class FuelType(str, Enum):
    """
    Type of fuel.
    """

    coal = "coal"  # Generic coal, not including lignite type.  # noqa: E501, E741, RUF003
    oil = "oil"  # Oil.  # noqa: E501, E741, RUF003
    gas = "gas"  # Natural gas.  # noqa: E501, E741, RUF003
    lignite = "lignite"  # The fuel is lignite coal.  Note that this is a special type of coal, so the other enum of coal is reserved for hard coal types or if the exact type of coal is not known.  # noqa: E501, E741, RUF003
    hardCoal = "hardCoal"  # Hard coal.  # noqa: E501, E741, RUF003
    oilShale = "oilShale"  # Oil Shale.  # noqa: E501, E741, RUF003
    brownCoalLignite = "brownCoalLignite"  # Brown coal lignite.  # noqa: E501, E741, RUF003
    coalDerivedGas = "coalDerivedGas"  # Coal derived gas.  # noqa: E501, E741, RUF003
    peat = "peat"  # Peat.  # noqa: E501, E741, RUF003
    other = "other"  # Any fuel type not included in the rest of the enumerated value.  # noqa: E501, E741, RUF003