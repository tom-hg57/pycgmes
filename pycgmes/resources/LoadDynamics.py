# SPDX-FileCopyrightText: 2023 Alliander
#
# SPDX-License-Identifier: Apache-2.0

"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property

from pydantic.dataclasses import dataclass

from ..utils.profile import BaseProfile, Profile
from .IdentifiedObject import IdentifiedObject


@dataclass
class LoadDynamics(IdentifiedObject):
    """
    Load whose behaviour is described by reference to a standard model or by definition of a user-defined model. A
      standard feature of dynamic load behaviour modelling is the ability to associate the same behaviour to
      multiple energy consumers by means of a single load definition.  The load model is always applied to
      individual bus loads (energy consumers).

    EnergyConsumer: Energy consumer to which this dynamics load model applies.
    """

    # *Association not used*
    # Type M:0..n in CIM
    # EnergyConsumer : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.DY, ]})

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DY,
        }
