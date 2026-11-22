import csv
import logging
from dataclasses import dataclass
from pathlib import Path
from pprint import pprint

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class Ticker:
    symbol: str
    company_name: str
    sector: str
    asset_type: str


def load_tickers(path: Path) -> list[Ticker]:
    with path.open(newline="", encoding="utf-8") as file:
        data = csv.DictReader(file)

        tickers = [
            Ticker(
                symbol=row["symbol"].upper().strip(),
                company_name=row["company_name"].strip(),
                sector=row["sector"].strip(),
                asset_type=row["asset_type"].strip(),
            )
            for row in data
        ]

    if not tickers:
        raise ValueError(f"No tickers found in {path}")

    seen: set[str] = set()
    dupes: set[str] = set()

    for ticker in tickers:
        if ticker.symbol in seen:
            dupes.add(ticker.symbol)
        else:
            seen.add(ticker.symbol)

    if dupes:
        raise ValueError(f"Duplicate symbols in {path}: {', '.join(sorted(dupes))}")

    logger.info("Loaded %d tickers from %s", len(tickers), path)

    return tickers


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    pprint(load_tickers(Path("config/tickers_us.csv")))
