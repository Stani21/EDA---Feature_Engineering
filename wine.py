"""Explore and visualize the Red Wine Quality dataset."""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


PAIRPLOT_FEATURES = ["alcohol", "volatile acidity", "citric acid", "sulphates"]


def load_data(data_path: Path) -> pd.DataFrame:
    """Load the semicolon-separated dataset and remove duplicate rows."""
    if not data_path.is_file():
        raise FileNotFoundError(f"Dataset not found: {data_path}")

    data = pd.read_csv(data_path, sep=";")
    if "quality" not in data.columns:
        raise ValueError("The dataset must contain a 'quality' column.")

    duplicate_count = int(data.duplicated().sum())
    if duplicate_count:
        data = data.drop_duplicates().copy()
    print(f"Removed duplicate rows: {duplicate_count}")
    return data


def print_summary(data: pd.DataFrame) -> None:
    """Print useful dataset details and the feature correlation matrix."""
    print("\nDataset preview:")
    print(data.head())
    print("\nDataset information:")
    data.info()
    print(f"\nDataset shape: {data.shape[0]} rows x {data.shape[1]} columns")
    quality_values = sorted(int(value) for value in data["quality"].unique())
    print(f"\nQuality values: {quality_values}")
    print(f"\nMissing values by column:\n{data.isna().sum()}")
    print(f"\nCorrelation matrix:\n{data.corr(numeric_only=True).round(2)}")


def create_plots(data: pd.DataFrame, output_dir: Path, show: bool) -> None:
    """Save the main exploratory plots to the output directory."""
    output_dir.mkdir(parents=True, exist_ok=True)
    sns.set_theme(style="whitegrid", palette="colorblind")

    quality_order = sorted(data["quality"].unique())

    fig, ax = plt.subplots(figsize=(8, 5))
    sns.countplot(data=data, x="quality", order=quality_order, ax=ax)
    ax.set(title="Red Wine Quality Counts", xlabel="Quality", ylabel="Number of wines")
    fig.tight_layout()
    fig.savefig(output_dir / "quality_counts.png", dpi=150)

    fig, ax = plt.subplots(figsize=(8, 5))
    sns.histplot(data=data, x="quality", discrete=True, kde=True, ax=ax)
    ax.set(title="Distribution of Wine Quality", xlabel="Quality", ylabel="Number of wines")
    fig.tight_layout()
    fig.savefig(output_dir / "quality_distribution.png", dpi=150)

    fig, ax = plt.subplots(figsize=(11, 8))
    sns.heatmap(
        data.corr(numeric_only=True),
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        center=0,
        ax=ax,
    )
    ax.set_title("Feature Correlation Heatmap")
    fig.tight_layout()
    fig.savefig(output_dir / "correlation_heatmap.png", dpi=150)

    pair_grid = sns.pairplot(
        data,
        vars=PAIRPLOT_FEATURES,
        hue="quality",
        corner=True,
        plot_kws={"alpha": 0.6, "s": 20},
    )
    pair_grid.figure.suptitle("Selected Features by Wine Quality", y=1.02)
    pair_grid.savefig(output_dir / "pairplot.png", dpi=150, bbox_inches="tight")

    fig, ax = plt.subplots(figsize=(8, 5))
    sns.scatterplot(
        data=data,
        x="alcohol",
        y="pH",
        hue="quality",
        palette="colorblind",
        ax=ax,
    )
    ax.set(title="Alcohol vs pH by Wine Quality")
    fig.tight_layout()
    fig.savefig(output_dir / "alcohol_vs_ph.png", dpi=150)

    print(f"\nSaved plots to: {output_dir.resolve()}")
    if show:
        plt.show()
    plt.close("all")


def main() -> None:
    project_dir = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(
        description="Summarize and plot the Red Wine Quality dataset."
    )
    parser.add_argument(
        "--data",
        type=Path,
        default=project_dir / "winequality-red.csv",
        help="Path to the semicolon-separated CSV dataset.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=project_dir / "outputs",
        help="Directory where plot images will be saved.",
    )
    parser.add_argument(
        "--no-show",
        action="store_true",
        help="Save plots without opening interactive windows.",
    )
    args = parser.parse_args()

    data = load_data(args.data)
    print_summary(data)
    create_plots(data, args.output_dir, show=not args.no_show)


if __name__ == "__main__":
    main()
