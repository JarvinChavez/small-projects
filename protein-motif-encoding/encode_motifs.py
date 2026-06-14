"""Encode UniProt motif regions into fixed-length numeric tensors for analysis."""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

BASE = Path(__file__).resolve().parent
DATA_PATH = BASE / "data" / "sample_motif_regions.csv"
OUTPUT_PATH = BASE / "data" / "encoded_motif_tensor.csv"
MAX_LENGTH = 100
NGRAM_SIZE = 2


def extract_ngrams(sequence: str, n: int = NGRAM_SIZE) -> list[str]:
    return [
        sequence[i : i + n]
        for i in range(len(sequence) - n + 1)
        if "." not in sequence[i : i + n]
    ]


def build_vocabulary(regions: pd.Series) -> dict[str, int]:
    tokens: set[str] = set()
    for region in regions.dropna():
        tokens.update(extract_ngrams(region))
    return {token: idx + 1 for idx, token in enumerate(sorted(tokens))}


def encode_sequence(sequence: str, token_to_index: dict[str, int]) -> list[int]:
    indices = [token_to_index.get(token, 0) for token in extract_ngrams(sequence)]
    if len(indices) < MAX_LENGTH:
        indices.extend([0] * (MAX_LENGTH - len(indices)))
    return indices[:MAX_LENGTH]


def encode_motif_regions(csv_path: Path = DATA_PATH) -> tuple[np.ndarray, pd.DataFrame]:
    df = pd.read_csv(csv_path)
    region_col = "Motif_Region" if "Motif_Region" in df.columns else "sequence"
    vocabulary = build_vocabulary(df[region_col])
    encoded = df[region_col].dropna().apply(lambda s: encode_sequence(s, vocabulary))
    tensor = np.stack(encoded.to_list())
    encoded_df = pd.DataFrame(tensor)
    return tensor, encoded_df


def main() -> None:
    tensor, encoded_df = encode_motif_regions()
    encoded_df.to_csv(OUTPUT_PATH, index=False)
    print(f"Encoded shape: {tensor.shape}")
    print(f"Wrote: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
