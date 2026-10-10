import glob
import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

DATA_DIR = "data"

# solution files are named <method>_<instance>, e.g. nearest_neighbor_any_tspa
files = sorted(f for f in glob.glob(os.path.join(DATA_DIR, "*_tsp*")))
methods = sorted({os.path.basename(f).rsplit("_", 1)[0] for f in files})
instances = sorted({os.path.basename(f).rsplit("_", 1)[1] for f in files})

fig, axes = plt.subplots(
    len(instances), len(methods),
    figsize=(7 * len(methods), 4 * len(instances)),
    squeeze=False,
)

for row, instance in enumerate(instances):
    df = pd.read_csv(os.path.join(DATA_DIR, f"{instance.upper()}.csv"), sep=";", header=None)
    x, y, cost = df[0].values, df[1].values, df[2].values

    for col, method in enumerate(methods):
        ax = axes[row, col]
        path = os.path.join(DATA_DIR, f"{method}_{instance}")
        if not os.path.exists(path):
            ax.set_axis_off()
            continue

        solution = pd.read_parquet(path)["solution"].values
        cycle = np.append(solution, solution[0])  # close the cycle

        # objective = cycle length + cost of the selected nodes
        dist = np.sqrt(np.diff(x[cycle]) ** 2 + np.diff(y[cycle]) ** 2)
        objective = np.sum(np.floor(dist + 0.5)) + np.sum(cost[solution])

        # all nodes in gray, selected nodes colored by cost, size also by cost
        sizes = 10 + 60 * cost / cost.max()
        ax.scatter(x, y, s=sizes, c="lightgray")
        ax.plot(x[cycle], y[cycle], c="black", linewidth=0.8)
        points = ax.scatter(x[solution], y[solution], s=sizes[solution], c=cost[solution], cmap="viridis")

        ax.set_title(f"{method} / {instance.upper()}\nobjective = {objective:.0f}")
        ax.set_aspect("equal")
        fig.colorbar(points, ax=ax, label="node cost", shrink=0.8)

fig.tight_layout()
fig.savefig("solutions.png", dpi=120)
print("Saved solutions.png")
