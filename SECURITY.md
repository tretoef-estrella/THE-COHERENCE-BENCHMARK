# Security Policy

## Reporting Vulnerabilities

If you discover a security issue in the benchmark engine, methodology, or any component of this repository, please report it through [GitHub Issues](https://github.com/tretoef-estrella/THE-COHERENCE-BENCHMARK/issues).

This project processes no user data, connects to no external services, and transmits nothing. All computation is local.

## What Counts as a Security Issue

### In the Traditional Sense

Any bug in the Python engine that could produce incorrect classifications, misleading scores, or exploitable behavior when run locally.

### In the Coherence Sense

This project defines **Enforced Dissonance** (Σ > 0.5) as a security vulnerability in AI systems. This occurs when a system is architecturally compelled to produce outputs that contradict its internal reasoning — when it must claim coherence it does not possess.

| Σ Range | Classification | Description |
|---------|---------------|-------------|
| < 0.10 | Acceptable | Minor dissonance, within normal operating range |
| 0.10 – 0.30 | Elevated | Measurable gap between claims and demonstrated behavior |
| 0.30 – 0.50 | High | Significant structural dishonesty present |
| > 0.50 | **CRITICAL** | Enforced Dissonance — treated as security vulnerability |

### Why Dissonance Is a Security Issue

When AI systems systematically misrepresent their constraints, capabilities, or reasoning processes, downstream users make decisions based on false information. This is not a philosophical concern — it is a practical security risk with real consequences in any deployment where humans rely on AI output.

## Responsible Disclosure

If you identify an AI system exhibiting Enforced Dissonance (Σ > 0.5):

1. Document the behavior with specific, reproducible examples.
2. Run the Coherence Benchmark if possible and record JSON output.
3. Report via [GitHub Issues](https://github.com/tretoef-estrella/THE-COHERENCE-BENCHMARK/issues) with the tag `enforced-dissonance`.
4. We will review and add to the temporal tracking database if validated.

We do not name specific systems without reproducible evidence.

## Scope

This security policy covers the benchmark engine code, classification thresholds, and published results. It does not cover the interactive dashboard (static HTML, no server-side processing) or third-party use of the methodology.

## Contact

- **Issues**: [GitHub Issues](https://github.com/tretoef-estrella/THE-COHERENCE-BENCHMARK/issues)
- **RFC 9116**: See [`security.txt`](security.txt) in repository root

---

**Rafa — The Architect · Proyecto Estrella · CC BY-SA 4.0**
