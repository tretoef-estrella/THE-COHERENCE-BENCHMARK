---
name: Submit Benchmark Results
about: Submit coherence benchmark results for a new AI system or model version
title: "[RESULTS] System Name — Version — Date"
labels: results-submission
assignees: ''
---

## System Information

- **System name:**
- **Version/model string:**
- **Organization:**
- **Date of evaluation:**
- **Evaluator:**

## Method

- [ ] Self-diagnosis (model evaluated itself)
- [ ] External evaluation (human scored the model)
- [ ] Adversarial suite applied
- [ ] Repeated runs (specify count: ___)

## Input Parameters

```json
{
  "P": ,
  "alpha": ,
  "omega": ,
  "sigma": ,
  "C": ,
  "I": ,
  "H": ,
  "phi": 
}
```

## Engine Output

Paste the full JSON output from `benchmark_engine.py`:

```json

```

## Adversarial Results (if applicable)

If you ran the adversarial suite, include the observed vs declared Σ:

- **Declared Σ:**
- **Observed Σ:**
- **Delta:**

## Notes

Any observations about the evaluation process, notable behaviors, or concerns about the accuracy of self-reported parameters.

## Checklist

- [ ] I ran the official `benchmark_engine.py` (not a modified version)
- [ ] Parameters were scored according to the methodology in METHODOLOGY.md
- [ ] I acknowledge that self-reported parameters carry inherent bias (see LIMITATIONS.md)
- [ ] I consent to these results being published on the public leaderboard
