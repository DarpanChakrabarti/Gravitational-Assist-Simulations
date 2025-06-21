# 🚀 Gravitational Assist Simulations

This repository contains all Python code and supporting files used in the paper:  
**"Gravitational Assist: Computational Modeling and Analysis"**  
by **Darpan Chakrabarti**, Indian Institute of Science, Bengaluru.

The project models hyperbolic flybys and gravitational assist maneuvers based on Newtonian mechanics. It includes analytical derivations, mission-specific simulations (Cassini and Galileo I), and parameter sensitivity visualizations.

---

## 📁 Contents

| File/Folder                  | Description |
|-----------------------------|-------------|
| `trajectory_simulation.py`  | Plots a conic-section hyperbolic trajectory (Figure 3) |
| `cassini_flyby.py`          | Simulates Cassini-Earth flyby (Figure 4a) |
| `galileo_flyby.py`          | Simulates Galileo I-Earth flyby (Figure 4b) |
| `compare_flybys.py`         | Overlays both flyby trajectories (Figure 4c) |
| `deflection_vs_b.py`        | Plots deflection angle vs. impact parameter (Figure 5a) |
| `deflection_vs_vinf.py`     | Plots deflection angle vs. asymptotic velocity (Figure 5b) |
| `requirements.txt`          | Lists required Python libraries (NumPy, Matplotlib) |
| `figures/` (optional)       | Contains example output plots (if included) |
| `README.md`                 | You're reading it! Project overview and instructions. |

---

## ▶️ Getting Started

### 🔧 Requirements

- Python 3.6+
- `numpy`
- `matplotlib`

Install dependencies using:

```bash
pip install -r requirements.txt

