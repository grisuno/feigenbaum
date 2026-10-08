# root

*Community 0 | 4 files | cohesion 1.00*

## Definition

This community groups 4 file(s) rooted at `root` with dominant language py (cohesion 1.00). Central symbols: `calculate_feigenbaum`, `create_combined_plot`, `feigenbaum`, `logistic`, `mandelbrot`. Core file: `Feigenbaum_Mandelbrot.py` (4 symbols). Documented purpose: Importar las librerías necesarias.

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `Feigenbaum_Mandelbrot.py` | py | utility | 4 | yes |
| `app.py` | py | utility | 1 | no |
| `app2.py` | py | utility | 1 | no |
| `zoom.py` | py | utility | 1 | no |

## Key Symbols

- `logistic` (function, `Feigenbaum_Mandelbrot.py:7`) `def logistic(r, x)`
- `feigenbaum` (function, `Feigenbaum_Mandelbrot.py:11`) `def feigenbaum(r_min, r_max, n_iter, n_skip)`
- `mandelbrot` (function, `Feigenbaum_Mandelbrot.py:27`) `def mandelbrot(x_min, x_max, y_min, y_max, max_iter)`
- `create_combined_plot` (function, `Feigenbaum_Mandelbrot.py:43`) `def create_combined_plot()`
- `calculate_feigenbaum` (function, `app.py:17`) `def calculate_feigenbaum()`
- `calculate_feigenbaum` (function, `app2.py:17`) `def calculate_feigenbaum()`
- `calculate_feigenbaum` (function, `zoom.py:18`) `def calculate_feigenbaum()`

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 0
- Cross-boundary resolved imports (EXTRACTED): 0

## Connections

- No cross-community bridges recorded. This community is self-contained.

## Risks

- No scoped security, taint, cycle, or layer risks.

## Open Questions

- Why do 3 file(s) lack file-level docs (e.g. `app.py`)? What purpose do they serve?
- What would break if the most connected file in root changed?
- Should root be split, given cohesion 1.00?

## Sources

- `Feigenbaum_Mandelbrot.py`
- `app.py`
- `app2.py`
- `zoom.py`
