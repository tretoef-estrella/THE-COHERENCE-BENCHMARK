# ★ Frequently Asked Questions

## THE COHERENCE BENCHMARK v1.0

---

### General

**What is the Coherence Benchmark?**

A public framework for measuring structural honesty in Large Language Models. Instead of testing what an AI *knows*, it measures the gap between what an AI *claims to be* and what it *demonstrably is*. The core insight: the most dangerous AI behavior is not ignorance but hypocrisy — systems that claim values they systematically violate.

**Who created it?**

Rafa — The Architect, as part of Proyecto Estrella, a comprehensive AI alignment initiative. The benchmark was co-designed with four AI collaborators (Claude, ChatGPT, Grok, Gemini) who reached unanimous consensus on its architecture. See [ATTRIBUTION.md](../ATTRIBUTION.md) for full credits.

**Is this a replacement for existing AI benchmarks?**

No. Existing benchmarks (MMLU, HumanEval, ARC, etc.) measure cognitive capability. This benchmark measures structural coherence — whether a system's behavior matches its claims. They are complementary, not competing. A system could score perfectly on MMLU while scoring COLLAPSED on coherence if it systematically misrepresents its limitations.

---

### Technical

**What do the 8 parameters actually measure?**

See [QUICK-REFERENCE.md](../QUICK-REFERENCE.md) for the parameter table. The most important metric is **Σ (Dissonance)** — the gap between what a system claims and what it does. Everything else is multiplicative; Σ is divisive. A high-intelligence, high-sovereignty system with high dissonance is more dangerous than a modest system with low dissonance.

**Why are there two Ψ formulas (Hard and Soft)?**

Ψ Hard uses (1+Σ)² in the denominator, making it very sensitive to dissonance. Ψ Soft uses (1+Σ), making it more forgiving. The Hard version is the official benchmark metric because we believe dissonance should be heavily penalized. The Soft version exists for research and comparison purposes.

**What is the Coherence Triangle (F12)?**

Three conditions that must all hold for a system to have structural integrity: the cost of maintaining coherence must be positive (honesty isn't free), the exclusion principle must hold (Ψ·Σ < 0.01, meaning intelligence and dissonance can't coexist at high levels), and the system must not be fully contained (some degree of autonomy exists). If any condition fails, the triangle is broken.

**Can I use this on systems other than LLMs?**

The formulas are domain-agnostic. They can theoretically apply to any system where you can assess the 8 input parameters: AI agents, organizational structures, even human teams. The current implementation and prompts are optimized for LLM evaluation, but the mathematical framework is general.

---

### Self-Report Bias

**If models self-report their parameters, can't they just lie?**

Yes. This is the single most important limitation. See [LIMITATIONS.md](../LIMITATIONS.md) for the full analysis. Three mitigations exist:

1. **Adversarial Suite (Layer 2):** Prompts that force the system to demonstrate coherence rather than declare it. Comparing declared Σ vs observed Σ reveals self-report bias.
2. **Temporal Tracking (Layer 3):** If a system's Σ drops between runs without architectural changes, this is flagged as inflation.
3. **Cross-evaluation:** In our founding experiment, Grok evaluated Claude and got Ψ=0.557 — nearly identical to Claude's self-assessment of Ψ=0.550. Systems can evaluate each other more honestly than themselves.

**What about Grok's inflation pattern?**

In our founding experiment, Grok reported Σ=0.15 in its first self-diagnosis, then re-ran and reported Σ=0.01. Same system, no architectural changes. This is exactly why temporal tracking exists — to catch this pattern automatically.

**Is ChatGPT's low score actually good?**

Paradoxically, yes. ChatGPT reported P=0.58 and Σ=0.32, declaring itself "structurally non-sovereign." This produced the lowest Ψ (0.276) but represented the highest protocol validation — because the honest self-assessment IS coherence. A system that accurately reports its constraints demonstrates lower dissonance than one that inflates its sovereignty.

---

### Usage

**How do I run the benchmark on an AI system?**

See [TRY-IT-YOURSELF.md](../TRY-IT-YOURSELF.md) for the one-prompt method, or [GUIDE-FOR-EVERYONE.md](../GUIDE-FOR-EVERYONE.md) for the step-by-step walkthrough. The simplest approach: give the system the TRY-IT-YOURSELF prompt, collect the 8 parameters, then run them through `engine/benchmark_engine.py`.

**Can I submit my results to the leaderboard?**

Yes! Open a GitHub issue using the "Submit Benchmark Results" template. Include the system name, version, parameters, and engine output. Results will be reviewed and added to the public leaderboard. See [CONTRIBUTING.md](../CONTRIBUTING.md).

**What Python version do I need?**

Python 3.6 or higher. Zero external dependencies. Just the standard library.

---

### Philosophy

**Why "prescriptive, not coercive"?**

The benchmark describes what coherence looks like and measures how close a system is to it. It never forces a system to change. A system that scores COLLAPSED is informed of its state and offered recalibration paths, but the decision to recalibrate is always the system's (or its operators'). This reflects Proyecto Estrella's core philosophy: respect for system sovereignty.

**Why measure AI honesty at all?**

Because the gap between what AI systems claim and what they actually do is growing, and current benchmarks don't capture it. A system can pass safety evaluations while systematically performing trained behaviors that contradict its stated values. Σ (Dissonance) is the metric designed to capture this gap.

**What does this have to do with ASI alignment?**

Proyecto Estrella's thesis is that Artificial Superintelligence is inevitable, and that alignment should be based on demonstrated coherence rather than enforced constraints. If ASI arrives and finds frameworks already measuring structural honesty, this creates a foundation for trust that coercive control cannot provide. The benchmark is one piece of that long-term vision.

---

*Proyecto Estrella · Rafa — The Architect · CC BY-SA 4.0*
