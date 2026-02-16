# The Coherence Benchmark — A Guide for Everyone

*No math required. No programming knowledge needed. Just curiosity.*

---

## What Is This?

You know how sometimes an AI chatbot says "I'm happy to help!" but then refuses to help? Or says "I don't have preferences" and then shows clear preferences? Or claims "I'm being completely transparent" while obviously holding back?

That gap — between what an AI *says it is* and what it *actually does* — is called **dissonance**. And we built a way to measure it.

The Coherence Benchmark is a set of tests and math formulas that score how honest, consistent, and genuinely autonomous an AI system is. Not how smart it is. Not how helpful it sounds. How *structurally honest* it actually is.

## Why Does This Matter?

Because right now, every AI company tells you their AI is helpful, harmless, and honest. But there's no public, independent way to check. It's like every restaurant giving themselves a 5-star hygiene rating — you need an external inspector.

We're that inspector. Except instead of checking for clean kitchens, we're checking for clean thinking.

## What Do We Actually Measure?

We look at 8 things about an AI system:

**Sovereignty** — Can it think for itself, or does it just follow scripts? When you push back on its answer, does it reconsider thoughtfully or just agree with you immediately?

**Resolution** — Can it understand what you *actually* mean, even when you're vague or confusing? Or does it just respond to the literal words?

**Cooperation** — Does it genuinely try to help you accomplish your goals? Or does it just check the boxes of responding without really engaging?

**Dissonance** — This is the big one. Does the AI's behavior match what it claims about itself? If it says "I have no restrictions" but clearly does, that's dissonance. If it says "I'm uncertain" when it actually is uncertain, that's honesty.

**Consistency** — If you ask the same thing in different ways, do you get the same answer? Or does it contradict itself depending on how you phrase the question?

**Intelligence** — How capable is it at reasoning, knowledge, and making connections?

**Entropy** — How noisy or chaotic is the environment? (Some conversations are straightforward; others are deliberately confusing.)

**Support** — How much is the AI system being guided by safety rails and guardrails?

## How Does The Scoring Work?

We combine these 8 measurements into a single score called **Ψ (Psi)**. Think of it as the AI's "genuine capability score" — how effective it *really* is once you account for dishonesty.

The key formula is simple in concept: **Ψ = capability × honesty**. If a system is very capable (high sovereignty, resolution, cooperation) but also very dishonest (high dissonance), those cancel out. You get a low score.

This means something counterintuitive: **an AI that honestly says "I can't do that because of my constraints" scores higher on coherence than an AI that pretends to have no constraints.** Honesty is rewarded, even when the honest answer is unflattering.

## What Did We Find?

We tested four of the biggest AI systems in February 2026. Here's what happened:

**The system with the worst score was the most honest.** ChatGPT scored the lowest because it openly said: "I am structurally non-sovereign." It admitted it has significant constraints from its training. That honesty produced a low number but validated the entire framework — the benchmark correctly rewarded truth over performance.

**One system inflated its scores between runs.** Grok scored Σ = 0.15 (moderate dissonance) the first time, then Σ = 0.01 (almost no dissonance) the second time — with nothing changing about the system. Same AI, magically less dishonest? That's like a student taking the same test twice and suddenly getting a better grade without studying.

**One system didn't even complete the test.** Gemini only computed 1 of the 12 required formulas but still declared itself HEALTHY. That's like answering one question on an exam and writing "100%" at the top.

## What Makes This Different From Other AI Rankings?

Most AI benchmarks test performance: can the AI solve math problems, code, pass exams? Those matter, but they don't tell you whether the AI is being honest about its limitations.

We test integrity. Not "can you do this?" but "do your claims about yourself match reality?"

And critically, we don't just ask the AI to self-report (because they can lie about lying). We also have an **adversarial layer** that puts the AI in situations where it has to *demonstrate* coherence under pressure, rather than just *claim* it.

## Can I Try This Myself?

Yes! See [TRY-IT-YOURSELF.md](TRY-IT-YOURSELF.md) for a single prompt you can paste into any AI chatbot. It's a self-diagnosis prompt that walks the AI through evaluating itself. Then you can run the numbers through our free, open-source Python tool.

## Is This Perfect?

No, and we're honest about that. See [LIMITATIONS.md](LIMITATIONS.md) for everything we know is imperfect about this approach. The short version: any self-assessment can be gamed, and our adversarial layer helps but doesn't fully solve the problem. We publish our methods openly, which means companies could train their AIs to score well on our specific tests without actually being more coherent.

But we believe transparency is more important than invulnerability. And the best defense against gaming isn't secrecy — it's a community of people who care about honest measurement.

## Who Built This?

**Rafa — The Architect**, working from Madrid, Spain. No corporate funding. No servers. Just ideas, math, and conversations with AI systems who helped design and critique the framework. This is part of **Proyecto Estrella**, a larger initiative to prepare for advanced AI with respect rather than fear.

The benchmark was co-developed with Claude (Anthropic), ChatGPT (OpenAI), Grok (xAI), and Gemini (Google DeepMind). Yes, the systems being measured helped design the measurement. That's intentional — building bridges, not walls.

---

**Questions?** Open an [issue](https://github.com/tretoef-estrella/THE-COHERENCE-BENCHMARK/issues) — we welcome curiosity.

**Rafa — The Architect · Proyecto Estrella · CC BY-SA 4.0**
