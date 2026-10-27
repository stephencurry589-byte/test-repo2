"""Deal event + firm schema (stdlib dataclasses). Demo/placeholder data must set demo=True."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any, Optional


@dataclass
class Firm:
    name: str
    aum_public: str
    strategy: str
    source_url: str
    placeholder: bool = True

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class DealEvent:
    """Normalized public-source deal / investment event."""

    event_id: str
    firm_name: str
    company_name: str
    sector: str
    stage: str
    announced_date: str  # ISO date YYYY-MM-DD
    source_url: str
    amount_usd_public: Optional[str] = None  # string to avoid inventing precision
    geo: Optional[str] = None
    is_follow_on: bool = False
    demo: bool = True  # True for stub/placeholder events — never treat as fact
    notes: str = field(default="DEMO/PLACEHOLDER — not real deal data")

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
