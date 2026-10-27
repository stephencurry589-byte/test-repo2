"""Theme → ticker hypotheses with evidence URL fields (stub). Not trade advice."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any, List


@dataclass
class EquityHypothesis:
    theme: str
    tickers: List[str]
    evidence_urls: List[str]
    rationale: str
    demo: bool = True
    disclaimer: str = "STUB / DEMO — not trade advice; public evidence links only"


def theme_hypotheses() -> List[EquityHypothesis]:
    return [
        EquityHypothesis(
            theme="ai_infra",
            tickers=["DEMO_TICKER_AI1", "DEMO_TICKER_AI2"],
            evidence_urls=["https://example.com/demo/evidence/ai-infra"],
            rationale="DEMO: stub mapping from VC ai_infra activity to public names",
            demo=True,
        ),
        EquityHypothesis(
            theme="climate",
            tickers=["DEMO_TICKER_CL1"],
            evidence_urls=["https://example.com/demo/evidence/climate"],
            rationale="DEMO: stub mapping from VC climate activity to public names",
            demo=True,
        ),
    ]


def hypotheses_as_dicts() -> List[dict[str, Any]]:
    return [asdict(h) for h in theme_hypotheses()]
