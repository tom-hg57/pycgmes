"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

import sys
from types import ModuleType

from functools import cached_property
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from .WindTurbineType3or4Dynamics import WindTurbineType3or4Dynamics


@dataclass(config=DataclassConfig)
class WindType3or4UserDefined(WindTurbineType3or4Dynamics, ModuleType):
    """
    Wind type 3 or type 4 function block whose dynamic behaviour is described by a user-defined model.

    proprietary: Behaviour is based on a proprietary model as opposed to a detailed model. true = user-defined model is
      proprietary with behaviour mutually understood by sending and receiving applications and
      parameters passed as general attributes false = user-defined model is explicitly defined in terms
      of control blocks and their input and output signals.
    ProprietaryParameterDynamics: Parameter of this proprietary user-defined model.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return WindType3or4UserDefined(*args, **kwargs)

    proprietary: bool = Field(
        default=False,
        in_profiles=[
            Profile.DY,
        ],
    )

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # ProprietaryParameterDynamics : list = Field(default_factory=list, in_profiles = [Profile.DY, ])

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DY,
        }


# This + inheriting from ModuleType + __call__:
# makes:
# "import WindType3or4UserDefined"
# work as well as
# "from WindType3or4UserDefined import WindType3or4UserDefined".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = WindType3or4UserDefined
