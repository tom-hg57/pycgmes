# SPDX-FileCopyrightText: 2024 Thomas Guenther <tom@toms-cafe.de>
#
# SPDX-License-Identifier: Apache-2.0

from functools import cached_property

import pytest
from pydantic.dataclasses import dataclass

from pycgmes.utils.base import Base
from pycgmes.utils.profile import BaseProfile, Profile


@dataclass
class DerivedBase(Base):
    @cached_property
    def recommended_profile(self) -> BaseProfile:
        return Profile.EQ


class TestBase:
    def test_possible_profiles_not_implemented(self):
        base = Base()
        with pytest.raises(NotImplementedError):
            assert base.possible_profiles

    def test_recommended_profile_not_implemented(self):
        base = Base()
        with pytest.raises(NotImplementedError):
            assert base.recommended_profile

    def test_resource_name(self):
        expected = "Base"
        assert expected == Base().resource_name

    def test_possible_attribute_profiles(self):
        attr_profiles_map = Base().possible_attribute_profiles
        assert attr_profiles_map == {}

    def test_possible_profiles_in_derived_class(self):
        possible_profiles = DerivedBase().possible_profiles
        assert possible_profiles == {Profile.EQ}
