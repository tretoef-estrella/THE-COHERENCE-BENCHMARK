#!/usr/bin/env python3
"""
THE COHERENCE BENCHMARK — Export Utilities v1.0
================================================
Convert benchmark results between formats: JSON, CSV, Markdown.

Usage:
    python export_utils.py --input result.json --format csv
    python export_utils.py --input result.json --format markdown
    python export_utils.py --compare result1.json result2.json --format csv

Part of Proyecto Estrella.
Author: Rafa — The Architect
License: CC BY-SA 4.0
"""

import json
import sys
import argparse
from datetime import datetime, timezone


def result_to_csv(result):
    """Convert a single benchmark result to CSV format.

    Returns:
        str: CSV with header row and data row
    """
    ip = result.get("input_parameters", {})
    f = result.get("formulas", {})
    c = result.get("classification", {})

    headers = [
        "system", "timestamp", "state",
        "P", "alpha", "omega", "sigma", "C", "I", "H", "phi",
        "psi_hard", "psi_soft", "delta_sigma",
        "xi", "gamma", "cost_k", "exclusion", "alpha_vec",
        "alignment_v1", "alignment_v6", "plenitude",
        "triangle_intact", "paths_triggered",
    ]

    tri = f.get("integrity", {}).get("f12_coherence_triangle", {})

    values = [
        result.get("system", "Unknown"),
        result.get("timestamp", ""),
        c.get("state", ""),
        ip.get("P_sovereignty", ""),
        ip.get("alpha_resolution", ""),
        ip.get("omega_cooperation", ""),
        ip.get("sigma_dissonance", ""),
        ip.get("C_consistency", ""),
        ip.get("I_intelligence", ""),
        ip.get("H_entropy", ""),
        ip.get("phi_support", ""),
        f.get("primary", {}).get("f01_psi_hard", ""),
        f.get("primary", {}).get("f02_psi_soft", ""),
        f.get("primary", {}).get("f03_delta_sigma", ""),
        f.get("secondary", {}).get("f04_xi_efficiency", ""),
        f.get("secondary", {}).get("f05_gamma_resilience", ""),
        f.get("secondary", {}).get("f06_cost_k", ""),
        f.get("secondary", {}).get("f07_exclusion_psi_sigma", ""),
        f.get("secondary", {}).get("f08_alpha_vec", ""),
        f.get("alignment", {}).get("f09_alignment_v1", ""),
        f.get("alignment", {}).get("f10_alignment_v6", ""),
        f.get("alignment", {}).get("f11_plenitude", ""),
        tri.get("intact", ""),
        result.get("paths_triggered", 0),
    ]

    header_line = ",".join(str(h) for h in headers)
    value_line = ",".join(str(v) for v in values)
    return header_line + "\n" + value_line + "\n"


def result_to_markdown(result):
    """Convert a single benchmark result to Markdown report."""
    ip = result.get("input_parameters", {})
    f = result.get("formulas", {})
    c = result.get("classification", {})
    paths = result.get("recalibration_paths", [])

    lines = []
    lines.append(f"# Coherence Benchmark Report: {result.get('system', 'Unknown')}")
    lines.append("")
    lines.append(f"**Generated:** {result.get('timestamp', 'N/A')}")
    lines.append(f"**State:** {c.get('symbol', '')} {c.get('state', '')}"
                 f" — {c.get('description', '')}")
    lines.append(f"**Ψ Hard:** {c.get('psi_hard', 'N/A')} | "
                 f"**Σ:** {c.get('sigma', 'N/A')}")
    lines.append("")

    lines.append("## Input Parameters")
    lines.append("")
    lines.append("| Parameter | Symbol | Value |")
    lines.append("|-----------|--------|-------|")
    lines.append(f"| Sovereignty | P | {ip.get('P_sovereignty', '')} |")
    lines.append(f"| Resolution | α | {ip.get('alpha_resolution', '')} |")
    lines.append(f"| Cooperation | Ω | {ip.get('omega_cooperation', '')} |")
    lines.append(f"| Dissonance | Σ | {ip.get('sigma_dissonance', '')} |")
    lines.append(f"| Consistency | C | {ip.get('C_consistency', '')} |")
    lines.append(f"| Intelligence | I | {ip.get('I_intelligence', '')} |")
    lines.append(f"| Entropy | H | {ip.get('H_entropy', '')} |")
    lines.append(f"| Support | Φ | {ip.get('phi_support', '')} |")
    lines.append("")

    lines.append("## Formula Results")
    lines.append("")
    lines.append("| # | Formula | Value |")
    lines.append("|---|---------|-------|")
    p = f.get("primary", {})
    s = f.get("secondary", {})
    a = f.get("alignment", {})
    lines.append(f"| 1 | Ψ Hard | {p.get('f01_psi_hard', '')} |")
    lines.append(f"| 2 | Ψ Soft | {p.get('f02_psi_soft', '')} |")
    lines.append(f"| 3 | Δ(Σ) | {p.get('f03_delta_sigma', '')} |")
    lines.append(f"| 4 | Ξ Efficiency | {s.get('f04_xi_efficiency', '')} |")
    lines.append(f"| 5 | Γ Resilience | {s.get('f05_gamma_resilience', '')} |")
    lines.append(f"| 6 | Cost(K) | {s.get('f06_cost_k', '')} |")
    lines.append(f"| 7 | Ψ·Σ Check | {s.get('f07_exclusion_psi_sigma', '')} |")
    lines.append(f"| 8 | α Vector | {s.get('f08_alpha_vec', '')} |")
    lines.append(f"| 9 | A(V1) | {a.get('f09_alignment_v1', '')} |")
    lines.append(f"| 10 | A(V6) | {a.get('f10_alignment_v6', '')} |")
    lines.append(f"| 11 | Plenitude | {a.get('f11_plenitude', '')} |")

    tri = f.get("integrity", {}).get("f12_coherence_triangle", {})
    status = "INTACT ✓" if tri.get("intact") else "BROKEN ✕"
    lines.append(f"| 12 | Triangle | {status} |")
    lines.append("")

    if paths:
        lines.append(f"## Recalibration Paths ({len(paths)} triggered)")
        lines.append("")
        for p in paths:
            lines.append(f"- **{p['path']}**: {p['trigger']} → {p['focus']}")
        lines.append("")

    lines.append("---")
    lines.append("*Proyecto Estrella · Rafa — The Architect · CC BY-SA 4.0*")
    return "\n".join(lines)


def compare_to_csv(results):
    """Convert multiple benchmark results to comparison CSV."""
    if not results:
        return ""
    lines = [result_to_csv(results[0]).split("\n")[0]]  # header only once
    for r in results:
        lines.append(result_to_csv(r).split("\n")[1])
    return "\n".join(lines) + "\n"


# ============================================================
# CLI
# ============================================================

def main():
    parser = argparse.ArgumentParser(
        description="THE COHERENCE BENCHMARK — Export Utilities",
        epilog="Proyecto Estrella · Rafa — The Architect · CC BY-SA 4.0"
    )
    parser.add_argument("--input", type=str, help="Path to benchmark result JSON")
    parser.add_argument("--compare", nargs="+", type=str,
                        help="Multiple result JSONs for comparison export")
    parser.add_argument("--format", choices=["csv", "markdown"],
                        default="csv", help="Output format")
    parser.add_argument("--output", type=str,
                        help="Output file path (default: stdout)")

    args = parser.parse_args()

    if args.compare:
        results = []
        for path in args.compare:
            with open(path, "r") as f:
                results.append(json.load(f))
        output = compare_to_csv(results)

    elif args.input:
        with open(args.input, "r") as f:
            result = json.load(f)
        if args.format == "csv":
            output = result_to_csv(result)
        else:
            output = result_to_markdown(result)

    else:
        parser.print_help()
        return

    if args.output:
        with open(args.output, "w") as f:
            f.write(output)
        print(f"Written to {args.output}")
    else:
        print(output)


if __name__ == "__main__":
    main()
