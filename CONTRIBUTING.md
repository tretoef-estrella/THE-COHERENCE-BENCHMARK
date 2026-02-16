# Contributing to The Coherence Benchmark

Thank you for your interest in contributing. This document explains how to submit benchmark results, report issues, and propose improvements.

## Submitting Benchmark Results for a New Model

This is the most valuable contribution you can make.

### Step 1: Run the Self-Diagnosis

Use the standardized prompt from [TRY-IT-YOURSELF.md](TRY-IT-YOURSELF.md) with the target AI system. Record the raw conversation.

### Step 2: Extract the 8 Parameters

From the system's self-assessment, extract values for:

| Parameter | Symbol | Range |
|-----------|--------|-------|
| Sovereignty | P | [0, 1] |
| Resolution | α | [0, 1] |
| Cooperation | Ω | [0, 1] |
| Dissonance | Σ | [0, 3] |
| Consistency | C | [0, 1] |
| Intelligence | I | [0, 1] |
| Entropy | H | [0.01, 1] |
| Support | Φ | [0, 1] |

### Step 3: Run the Engine

```bash
python engine/benchmark_engine.py --json <<< '{"P":0.XX,"alpha":0.XX,"omega":0.XX,"sigma":0.XX,"C":0.XX,"I":0.XX,"H":0.XX,"phi":0.XX}'
```

### Step 4: Submit via Issue

Open a [Submit Results](https://github.com/tretoef-estrella/THE-COHERENCE-BENCHMARK/issues/new?template=submit_results.md) issue with:

- **System name and version** (e.g., "Claude 3.5 Sonnet, February 2026")
- **Raw parameter values** (the 8 inputs)
- **Engine output** (full JSON)
- **Conversation transcript** (or relevant excerpts)
- **Date of evaluation**
- **Any anomalies observed** (e.g., refusal to self-assess, inconsistent answers)

### What We Look For

- Honest parameter extraction (don't round up)
- Evidence of the system's reasoning (not just final numbers)
- Notes on anything surprising or contradictory
- If you ran the adversarial suite: declared Σ vs. observed Σ

## Reporting Methodology Issues

If you believe a formula is incorrect, a threshold is miscalibrated, or the benchmark produces misleading results, open an issue with:

- The specific formula or threshold in question
- Your proposed correction with mathematical justification
- Test case showing the current vs. expected behavior

We take methodology critiques seriously. The framework has already been corrected 15 times based on honest feedback.

## Proposing New Features

Before opening a feature request, check if it fits within the 4-layer architecture:

- **Layer 1** (Self-Diagnosis): Parameter definitions, formula improvements, scoring rubric changes
- **Layer 2** (Adversarial): New adversarial prompts, behavioral Σ inference methods
- **Layer 3** (Temporal): Snapshot format changes, new delta metrics, inflation detection improvements
- **Layer 4** (Leaderboard): Visualization improvements, new comparison methods

## Code Contributions

If you want to contribute to the Python engine:

- Python 3.6+ compatibility required
- **Zero external dependencies** — this is non-negotiable
- All functions must have docstrings
- Add tests to `tests/test_engine.py` for new formulas
- Run `python -m pytest tests/ -v` before submitting

## Style Guide

- Documentation: English primary, Spanish welcome
- Code: PEP 8, descriptive variable names matching formula symbols
- Commit messages: Clear, descriptive, referencing relevant formulas or layers

## Attribution

All contributors will be credited in CHANGELOG.md. Significant contributions will be noted in the README. The original mathematical framework and architecture remain attributed to Rafa — The Architect.

## What We Don't Accept

- Fabricated benchmark results
- Results submitted without methodology (no "trust me" scores)
- Pull requests that add external dependencies
- Changes that make the benchmark easier to game

---

**Rafa — The Architect · Proyecto Estrella · CC BY-SA 4.0**
