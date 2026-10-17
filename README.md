# DFT_Python-Tools

Python scripts for post-processing density functional theory (DFT) calculations from Quantum ESPRESSO.

## QuantumEspresso_Proj: orbital-projected band structure

`graph-matplot.py` plots a band structure coloured by atomic-orbital character. It reads the projected files written by `projwfc.x`, so each band is shaded by its weight on a given atom and orbital.

The example data are for a Ga–As system along the M–Γ–K–M path. The script draws six panels:

| Panel | Projection |
|---|---|
| 1 | Ga *s* |
| 2 | Ga *p<sub>x</sub>* + *p<sub>y</sub>* |
| 3 | Ga *p<sub>z</sub>* |
| 4 | As *s* |
| 5 | As *p<sub>x</sub>* + *p<sub>y</sub>* |
| 6 | As *p<sub>z</sub>* |

### Input files

| File | Content | Columns |
|---|---|---|
| `no-soc.dat` | Band structure (no spin–orbit coupling), drawn as black lines | k-path coordinate, E (eV) |
| `total.dat` | Total projected DOS along the k-path | ik, E (eV), dos(E), pdos(E) |
| `Ga-s.dat`, `As-s.dat` | *s*-orbital projections | ik, E (eV), ldos(E), pdos(E) |
| `Ga-p.dat`, `As-p.dat` | *p*-orbital projections | ik, E (eV), ldos(E), then one pdos(E) column for each of the three *p* orbitals |

### Workflow

1. Run an SCF calculation with `pw.x`.
2. Run a `bands` calculation along your high-symmetry path with `pw.x`, then `bands.x` to get the band file (`no-soc.dat` here).
3. Run `projwfc.x` with `kresolveddos = .true.` to get k-resolved projections for each atom and orbital.
4. Copy the projected files next to the script and run:

```bash
python graph-matplot.py
```

The figure is saved as `pBand.pdf`.

### Adapting it to your system

Edit these values at the top of the script:

- `ef`: the reference energy in eV. In the example it is the valence band maximum (−3.1982 eV), so the y-axis reads *E* − *E*<sub>VBM</sub>.
- `x0 = 1 + (x0*50.085589298)`: the factor that converts the `bands.x` path coordinate into k-point index. It depends on your path length and number of k-points.
- `kpts` and `labels`: the k-point indices of the high-symmetry points and their names.
- `plt.ylim(-2, 2)`: the energy window.

## Requirements

- Python 3
- NumPy
- Matplotlib

## License

MIT. See [LICENSE](LICENSE).
