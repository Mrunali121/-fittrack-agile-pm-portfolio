"""
Generates the Sprint 2 burndown chart for the FitTrack case study.

This is the actual script used to produce 06-sprint-burndown-chart.png —
included in the repo so the chart's data and annotations are transparent
and reproducible, not just a static image.

Usage:
    pip install matplotlib
    python generate_burndown_chart.py
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Sprint 2 was a 10-working-day sprint committed at 21 story points.
days = list(range(0, 11))
ideal = [21 - (21 / 10) * d for d in days]

# Actual burndown: the team held pace even through the Day 6 scope-change
# request (see 03-sprint-planning/sprint-02-plan.md) because it was deferred
# rather than absorbed mid-sprint.
actual = [21, 19, 17, 15.5, 13, 11, 11, 8, 5, 2, 0]


def build_chart(output_path: str = "06-sprint-burndown-chart.png") -> None:
    fig, ax = plt.subplots(figsize=(9, 5.5))

    ax.plot(days, ideal, linestyle="--", color="#9aa0a6",
            label="Ideal burndown", linewidth=2)
    ax.plot(days, actual, marker="o", color="#2563eb",
            label="Actual burndown", linewidth=2.5)

    ax.annotate(
        "Day 6: Scope-creep request\n(streak freeze) — deferred to\n"
        "Sprint 3 to protect sprint goal",
        xy=(6, 11), xytext=(6.3, 16.5),
        arrowprops=dict(arrowstyle="->", color="#d97706"),
        fontsize=9, color="#92400e",
        bbox=dict(boxstyle="round,pad=0.4", fc="#fef3c7", ec="#d97706"),
    )

    ax.set_title("Sprint 2 Burndown — FitTrack MVP", fontsize=14, fontweight="bold")
    ax.set_xlabel("Sprint Day")
    ax.set_ylabel("Story Points Remaining")
    ax.set_xticks(days)
    ax.set_ylim(0, 23)
    ax.grid(True, linestyle=":", alpha=0.5)
    ax.legend(loc="upper right")

    fig.tight_layout()
    fig.savefig(output_path, dpi=150)
    print(f"Saved {output_path}")


if __name__ == "__main__":
    build_chart()
