"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

import sys
from types import ModuleType

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from .GeneratingUnit import GeneratingUnit


@dataclass(config=DataclassConfig)
class HydroGeneratingUnit(GeneratingUnit, ModuleType):
    """
    A generating unit whose prime mover is a hydraulic turbine (e.g., Francis, Pelton, Kaplan).

    energyConversionCapability: Energy conversion capability for generating.
    dropHeight: The height water drops from the reservoir mid-point to the turbine.
    turbineType: Type of turbine.
    HydroPowerPlant: The hydro generating unit belongs to a hydro power plant.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return HydroGeneratingUnit(*args, **kwargs)

    energyConversionCapability: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQ,
        ],
    )

    dropHeight: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    turbineType: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQ,
        ],
    )

    HydroPowerPlant: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQ,
        ],
    )

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.EQ,
            Profile.SSH,
        }


# This + inheriting from ModuleType + __call__:
# makes:
# "import HydroGeneratingUnit"
# work as well as
# "from HydroGeneratingUnit import HydroGeneratingUnit".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = HydroGeneratingUnit
