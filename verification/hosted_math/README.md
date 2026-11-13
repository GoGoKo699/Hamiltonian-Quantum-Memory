# Actual hosted mathematics

The [read-only capture workflow](../../.github/workflows/hosted-math.yml) checks the mathematical expressions rendered by GitHub at the exact source commit proposed by a pull request from this repository. It visits every tracked Markdown page at widths 1440 and 760 pixels, compares the accessible MathML with the pinned source, checks expression counts and supported relations, and retains full-page screenshots and HTML alongside the report.

The workflow uploads an artifact named `hosted-math-<full-source-commit>` for 14 days. Its `hosted-report.json`, per-page receipts and screenshots are observations of that source revision. A successful scientific reproduction run, local Markdown inventory or an earlier screenshot is not a substitute for this hosted report. Screenshots still need visual review: the automated comparison does not certify complete layout quality or scientific correctness.

The collector and text checker use the pinned implementations identified by these SHA-256 values:

| File | SHA-256 |
| --- | --- |
| `capture_hosted_math.cjs` | `c96f5c769ef62711137fc4d75e110cfb40c0db149c87590cdfb463b69a648b54` |
| `check_rendered_math.py` | `edbc2d72af94e96b78166d74b66fcea150134f2f3ebaaea121e9057768e1dbfe` |

The workflow structure was adapted from the inspected `hosted-math.yml` at Quantum-Memory-Calibration commit `213dcbf5013bf7ea63f796e6288ef24963281b23`. The helper implementations are unchanged. This repository-specific adaptation restricts the job to same-repository pull requests and disables npm lifecycle scripts during package installation.

## Permissions and limits

The job grants only `contents: read`. It checks out the exact pull-request head with credential persistence disabled. It does not request secrets, store authentication state, use signed-in browser sessions, publish pages, edit repository contents or change repository settings. All actions are pinned by their inspected full commit identifiers; Playwright and MathJax use explicit package versions. Installation downloads the browser and runtime on the disposable runner; it does not assert a frozen transitive npm dependency graph.

The browser is anonymous and read-only. It rejects redirects away from the exact pinned GitHub URL and reports access failures, transport failures, rendering failures and policy denials distinctly. Capture artifacts can contain only the public pages actually visited in that anonymous session. No private-account screenshots are requested by this workflow.

The workflow is a capture route, not a record that captures already passed. Inspect its actual run and source-bound artifact before claiming hosted verification. Failed reports and partial captures remain failed evidence. A changed mathematical source requires another capture at the corresponding revision.
