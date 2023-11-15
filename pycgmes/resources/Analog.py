# SPDX-FileCopyrightText: 2023 Alliander
#
# SPDX-License-Identifier: Apache-2.0

"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property

from pydantic import Field
from pydantic.dataclasses import dataclass

from ..utils.profile import BaseProfile, Profile
from .Measurement import Measurement


@dataclass
class Analog(Measurement):
    """
    Analog represents an analog Measurement.

    positiveFlowIn: If true then this measurement is an active power, reactive power or current with the convention that
      a positive value measured at the Terminal means power is flowing into the related
      PowerSystemResource.
    AnalogValues: The values connected to this measurement.
    LimitSets: A measurement may have zero or more limit ranges defined for it.
    """

    positiveFlowIn: bool = Field(
        default=False,
        json_schema_extra={
            "in_profiles": [
                Profile.OP,
            ]
        },
    )

    # *Association not used*
    # Type M:0..n in CIM
    # AnalogValues : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.OP, ]})

    # *Association not used*
    # Type M:0..n in CIM
    # LimitSets : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.OP, ]})

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.OP,
        }
