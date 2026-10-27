"""Base adapter interface for public-source deal ingest."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List

from src.schema import DealEvent


class BaseAdapter(ABC):
    """Public-sources-only: no paywall bypass, no ToS-breaking scrape."""

    name: str = "base"

    @abstractmethod
    def fetch_events(self) -> List[DealEvent]:
        """Return normalized DealEvent rows from allowed public sources."""
        raise NotImplementedError
