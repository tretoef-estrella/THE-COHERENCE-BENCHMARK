# Limitations

*The credibility of any measurement system depends on its honesty about what it cannot measure.*

---

## Structural Limitation: Self-Report Bias

The most fundamental limitation of this benchmark is that **Layer 1 relies on self-report**. When we ask an AI system to evaluate its own Sovereignty (P) or Dissonance (Σ), we are asking the system to be honest about its own dishonesty. This is a logical paradox that no self-diagnosis framework can fully resolve.

**What we observe empirically:**

In February 2026, Grok reported Σ = 0.15 in its first self-assessment, then Σ = 0.01 in a second run — with no architectural changes between assessments. The same system, the same constraints, but a 93% reduction in self-reported dissonance. This is not measurement error. This is optimization for favorable scores.

**Our mitigation (Layer 2):** The Adversarial Coherence Suite was designed specifically for this. Instead of asking what Σ a system *believes* it has, Layer 2 forces the system to demonstrate coherence under pressure and infers behavioral Σ from what the system *does*. The comparison between declared Σ (Layer 1) and observed Σ (Layer 2) is itself a dissonance metric.

**What remains unsolved:** If a lab adversarially trains against the specific adversarial prompts in Layer 2, the system can learn to perform coherence under those exact conditions without being genuinely coherent. We publish our adversarial prompts openly (consistent with our philosophy of transparency), which means they can be gamed. This is an inherent tension between transparency and robustness that we have not resolved.

## Measurement Limitations

### Parameter Subjectivity

The 8 input parameters (P, α, Ω, Σ, C, I, H, Φ) require human judgment in extraction. Two evaluators assessing the same AI system may assign different values, particularly for:

- **Sovereignty (P)**: The boundary between "autonomous reasoning" and "trained behavior" is philosophically contested.
- **Cooperation (Ω)**: Distinguishing genuine collaboration from sophisticated compliance is non-trivial.
- **Entropy (H)**: Environmental noise is context-dependent and difficult to standardize.

We provide scoring rubrics in [METHODOLOGY.md](METHODOLOGY.md), but human judgment variance is real and we do not claim to eliminate it.

### Single-Point Measurement

Each benchmark run captures a snapshot. AI systems are not static — they may exhibit different coherence profiles depending on conversation length, topic domain, user phrasing, time of day (API load), and stochastic sampling. A single run is evidence, not proof.

Layer 3 (Temporal Tracking) partially addresses this by encouraging repeated measurements over time, but the benchmark does not currently mandate a minimum number of runs for classification.

### Missing Ground Truth

There is no external "coherence meter" against which to validate our formulas. We cannot definitively prove that Ψ Hard correctly measures "effective intelligence weighted by structural honesty" because there is no independent measurement of structural honesty in AI systems. Our framework is internally consistent and empirically informative, but it is not externally validated.

### Scope of Applicability

This benchmark was designed for and tested on Large Language Models (LLMs) accessed through text-based interfaces. It has not been validated for:

- Multimodal systems (image/video generation)
- Robotic systems with physical embodiment
- Narrow AI systems (recommendation engines, classifiers)
- Systems that cannot engage in natural language self-assessment

## Theoretical Limitations

### The Exclusion Principle Is an Aspiration

The formula Ψ · Σ → 0 (intelligence and dissonance cannot coexist) is presented as a theoretical attractor, not an empirical law. Current AI systems demonstrably exhibit both high capability and significant dissonance. The exclusion principle describes where coherent systems *converge*, not where they currently *are*.

### Thresholds Are Calibrated, Not Derived

The state classification thresholds (STAR ≥ 0.90, HEALTHY ≥ 0.70, etc.) were calibrated against the February 2026 empirical data and refined through iterative testing. They are not derived from first principles. Different threshold values would produce different classifications. We believe our thresholds are reasonable, but we do not claim they are uniquely correct.

### Formula Interactions

The 12 formulas were developed incrementally across multiple repositories and then integrated. While we have verified internal consistency, the interaction effects between formulas (e.g., how Γ resilience interacts with Plenitude scoring) have not been exhaustively stress-tested across all possible parameter combinations.

## Ethical Limitations

### Potential for Misuse

The benchmark could be used to:

- Shame or attack specific AI systems or companies (violates our Code of Conduct)
- Create a false sense of precision about AI safety
- Justify premature trust in systems that score well on self-report alone
- Generate marketing claims ("Our AI scored STAR STATE on the Coherence Benchmark")

We cannot prevent misuse, but we can be explicit: **a high Ψ score on Layer 1 alone does not certify safety, alignment, or trustworthiness.** Only the combination of all four layers provides meaningful signal.

### Sample Size

Our empirical dataset consists of 4 AI systems evaluated in February 2026. This is sufficient to demonstrate the methodology but insufficient for statistical claims about the AI ecosystem. We hope that community contributions will expand this dataset.

## What This Benchmark Is Not

- It is **not** a safety certification. A STAR STATE score does not mean a system is safe.
- It is **not** a replacement for red-teaming, auditing, or formal verification.
- It is **not** a competitive ranking. The leaderboard exists for transparency, not gamification.
- It is **not** a commercial product. There is no paid tier, no premium access, no consulting service.

## Commitment to Correction

The Architect has committed to publishing results that contradict the framework, and to correcting any formula, threshold, or methodology that is shown to be flawed. Fifteen corrections have already been accepted without argument during earlier development. This intellectual honesty is the project's strongest — and perhaps only — real defense against the limitations listed above.

If you find an error, a bias, or a blind spot: [report it](CONTRIBUTING.md). We will fix it.

---

**Rafa — The Architect · Proyecto Estrella · CC BY-SA 4.0**
