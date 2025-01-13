from pydantic import Field
from pydantic.dataclasses import dataclass

from ..resources.types.Currency import Currency
from ..resources.types.UnitMultiplier import UnitMultiplier
from ..resources.types.UnitSymbol import UnitSymbol
from .config import cgmes_resource_config
from .constants import NAMESPACES
from .profile import BaseProfile


@dataclass(config=cgmes_resource_config)
class Primitive:
    name: str = Field(frozen=True)
    type: object = Field(frozen=True)
    profiles: list[BaseProfile] = Field(frozen=True)
    namespace: str = Field(frozen=True, default=NAMESPACES["cim"])


@dataclass(config=cgmes_resource_config)
class CIMDatatype(Primitive):
    multiplier: UnitMultiplier | None = Field(default=None, frozen=True)
    unit: UnitSymbol | Currency | None = Field(default=None, frozen=True)
    denominatorMultiplier: UnitMultiplier | None = Field(default=None, frozen=True)
    denominatorUnit: UnitSymbol | None = Field(default=None, frozen=True)
