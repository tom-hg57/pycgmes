# SPDX-FileCopyrightText: 2023 Alliander
#
# SPDX-License-Identifier: Apache-2.0

"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property

from pydantic import Field
from pydantic.dataclasses import dataclass

from ..utils.base import Base
from ..utils.profile import BaseProfile, Profile


@dataclass
class StreetAddress(Base):
    """
    General purpose street and postal address information.

    streetDetail: Street detail.
    townDetail: Town detail.
    status: Status of this address.
    postalCode: Postal code for the address.
    poBox: Post office box.
    language: The language in which the address is specified, using ISO 639-1 two digit language code.
    """

    streetDetail: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.GL,
            ]
        },
    )

    townDetail: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.GL,
            ]
        },
    )

    status: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.GL,
            ]
        },
    )

    postalCode: str = Field(
        default="",
        json_schema_extra={
            "in_profiles": [
                Profile.GL,
            ]
        },
    )

    poBox: str = Field(
        default="",
        json_schema_extra={
            "in_profiles": [
                Profile.GL,
            ]
        },
    )

    language: str = Field(
        default="",
        json_schema_extra={
            "in_profiles": [
                Profile.GL,
            ]
        },
    )

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.GL,
        }
