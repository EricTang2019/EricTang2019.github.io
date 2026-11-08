---
title: Revisiting My IMO Dream with an LLM Tutor
subtitle: Thoughts on the Future of Education and Human vs. Model Reasoning
description: "Having fun with GPT-6 Astra as my olympiad math tutor—and trying to outdo my high-school self!"
date: 2026-11-07 12:00:00 -0500
layout: post
page_class: post-page
lang: en
published: true
list_in_blog: true
permalink: /blog/imo-dream-with-gpt/
translation_url: /blog/imo-dream-with-gpt/zh/
translation_lang: zh-CN
translation_label: 中文
---

If you’re not familiar with the IMO, I’ve added a [quick introduction at the end](#imo-background).
{: #imo-introduction }

Earlier this week, I had a slightly odd idea: why not ask an LLM—GPT-6 Astra—to teach me olympiad combinatorics?

It’s been eight years since I last competed in a math olympiad. In high school, I dreamed of winning a gold medal at the International Mathematical Olympiad (IMO). That didn’t happen. I wasn’t a standout among the olympiad students around me. I’d had some training, though it was less systematic than what many of my Chinese peers had (you wouldn’t believe how much olympiad training goes on in China). My best result was a silver medal at the Chinese Mathematical Olympiad (CMO), and combinatorics was my weakest subject.

Even with some results to show for it, I often felt pretty defeated. I thought I simply wasn’t smart enough. Other people my age seemed to come up with beautiful, unexpected ideas that never occurred to me.

I haven’t had any further formal training in pure mathematics since high school, and until this week I hadn’t touched those school-level combinatorics problems again. During my undergraduate and PhD years, I’ve done research in learning theory, as well as some ongoing work on training LLMs to get better at mathematical problem solving.

So the thought was: models have gotten so good at math—why not let one teach me combinatorics? Just for fun. One problem a day. Maybe in a year or two, I could reach a level I’d never managed in high school.

I wasn’t prepared for how much fun this would be. The LLM turned out to be such a good teacher that I wanted to write about the experience.

## 1. Learning combinatorics with GPT-6 Astra

### 1.1 Getting started

<p class="post-note">I learned olympiad math in Chinese, so I’ve been prompting it in Chinese too. The English in the screenshots below comes from Google Translate.</p>


<figure class="post-screenshot">
  <a href="{{ '/images/blog/imo-dream/01-starting-redacted.png' | relative_url }}" aria-label="Open the full-size screenshot"><img src="{{ '/images/blog/imo-dream/01-starting-redacted.png' | relative_url }}" alt="My initial prompt and the model’s encouragement to get started." width="1473" height="1068" loading="lazy" decoding="async"></a>
  <figcaption>It first helped me put aside “Am I smart enough?” and focus on what I could improve with practice. It also pointed out that I could pick up this dream right now, <em>without waiting for AGI</em>.</figcaption>
</figure>

<figure class="post-screenshot">
  <a href="{{ '/images/blog/imo-dream/02-warm-up.png' | relative_url }}" aria-label="Open the full-size screenshot"><img src="{{ '/images/blog/imo-dream/02-warm-up.png' | relative_url }}" alt="The model selects 2011 IMO Shortlist C1 as a warm-up problem." width="1656" height="1346" loading="lazy" decoding="async"></a>
  <figcaption>It picked an easier problem, 2011 IMO Shortlist C1, to help me get back into the rhythm, and held back the solution so I could try it myself.</figcaption>
</figure>

### 1.2 Understanding how to teach olympiad combinatorics

<figure class="post-screenshot">
  <a href="{{ '/images/blog/imo-dream/03-learning-diagnosis.png' | relative_url }}" aria-label="Open the full-size screenshot"><img src="{{ '/images/blog/imo-dream/03-learning-diagnosis.png' | relative_url }}" alt="The model distinguishes missing tools from not recognizing when to use a familiar tool." width="1746" height="1626" loading="lazy" decoding="async"></a>
  <figcaption>It separated “I don’t know the tool” from “I know the tool, but don’t recognize when to use it.” That turned my old feeling of “I just lack inspiration” into something more concrete, with a clearer path for practice.</figcaption>
</figure>

<figure class="post-screenshot">
  <a href="{{ '/images/blog/imo-dream/04-training-landscape.png' | relative_url }}" aria-label="Open the full-size screenshot"><img src="{{ '/images/blog/imo-dream/04-training-landscape.png' | relative_url }}" alt="A discussion of combinatorics training through China’s national-team selection tests." width="1822" height="1578" loading="lazy" decoding="async"></a>
  <figcaption>I asked it for a bigger picture of combinatorics training, all the way up to China’s national-team selection tests.</figcaption>
</figure>

<figure class="post-screenshot">
  <a href="{{ '/images/blog/imo-dream/05-bedtime-problem.png' | relative_url }}" aria-label="Open the full-size screenshot"><img src="{{ '/images/blog/imo-dream/05-bedtime-problem.png' | relative_url }}" alt="A short combinatorics problem chosen for thinking about before sleep." width="1786" height="1442" loading="lazy" decoding="async"></a>
  <figcaption>It even picked me a bedtime problem: short enough to hold in my head, with very little calculation and no real need for pen and paper.</figcaption>
</figure>

### 1.3 Guiding me to a solution, step by step

It would ask what I was thinking and help me try it out. Here’s one exchange where I was experimenting with a weighted-sum approach.

<figure class="post-screenshot" id="example-guided-discovery">
  <a href="{{ '/images/blog/imo-dream/08-guided-attempt.png' | relative_url }}" aria-label="Open the full-size screenshot"><img src="{{ '/images/blog/imo-dream/08-guided-attempt.png' | relative_url }}" alt="I describe a weighted-sum idea, and the model helps identify the next step." width="1747" height="1408" loading="lazy" decoding="async"></a>
  <figcaption>I suggested choosing a point that maximized a weighted sum. It checked the gap I’d spotted in my first attempt, confirmed that the broader idea could work, and helped me focus on the next question: how should I choose the weights?</figcaption>
</figure>

<figure class="post-screenshot">
  <a href="{{ '/images/blog/imo-dream/09-testing-weights.png' | relative_url }}" aria-label="Open the full-size screenshot"><img src="{{ '/images/blog/imo-dream/09-testing-weights.png' | relative_url }}" alt="The model gives a small counterexample to my proposed choice of weights." width="1726" height="1252" loading="lazy" decoding="async"></a>
  <figcaption>My first choice of weights didn’t quite work. It gave me a small counterexample that showed exactly where the idea fell short.</figcaption>
</figure>

<figure class="post-screenshot">
  <a href="{{ '/images/blog/imo-dream/10-small-cases.png' | relative_url }}" aria-label="Open the full-size screenshot"><img src="{{ '/images/blog/imo-dream/10-small-cases.png' | relative_url }}" alt="At my request, the model lays out a small case so I can look for a pattern." width="1758" height="964" loading="lazy" decoding="async"></a>
  <figcaption>When I asked for a small case to explore, it chose <em>n</em> = 4 and <em>k</em> = 2 and laid out how the neighborhoods changed as the center moved. That gave me something concrete to inspect as I tried to spot what I should be adding up.</figcaption>
</figure>

### 1.4 Exploring proofs and connections

<figure class="post-screenshot" id="example-inversions">
  <a href="{{ '/images/blog/imo-dream/06-inversion-approach.png' | relative_url }}" aria-label="Open the full-size screenshot"><img src="{{ '/images/blog/imo-dream/06-inversion-approach.png' | relative_url }}" alt="The model develops an inversion-based idea I suggested into an argument." width="1790" height="1586" loading="lazy" decoding="async"></a>
  <figcaption>Once I’d solved a problem, I casually asked whether counting inversions could give another solution. It wasn’t the standard approach, but the model worked it out and showed me how to turn my idea into a complete proof.</figcaption>
</figure>

<figure class="post-screenshot" id="example-coloring">
  <a href="{{ '/images/blog/imo-dream/07-coloring-and-integrals.png' | relative_url }}" aria-label="Open the full-size screenshot"><img src="{{ '/images/blog/imo-dream/07-coloring-and-integrals.png' | relative_url }}" alt="A connection between coloring, rectangle tilings, and a complex-valued integral." width="1834" height="1506" loading="lazy" decoding="async"></a>
  <figcaption>After we’d solved a grid-coloring problem, I asked what else the idea could lead to. It explained how this kind of coloring argument is a special case of a more general way of assigning weights and adding—or integrating—them, and then used complex-valued weights to prove a neat result about tiling rectangles.</figcaption>
</figure>

It feels like having a fantastic one-on-one tutor helping me prepare for math olympiads. **Less than a week in, I already feel ready to take on C5-level problems from the IMO Shortlist. Back when I was competing eight years ago, it took me two years of training to get to that point.**

<!-- reflections-start -->

I’m planning to keep this up the way I’d keep going to the gym: an hour a day with the model, starting from one problem and following whatever interesting ideas it leads to.

This brief experiment has also left me with a few broader thoughts I’d like to write down.

<p class="post-caveat">(Given how fast models are improving, I’m skeptical that most analyses of their social impact based on today’s capabilities will stay useful for very long.)</p>

## 2. Thoughts on future education

### 2.1 LLMs are underrated as teachers

With the recent excitement around ChatGPT proving major mathematical results, I’ve seen a lot of discussion about what LLMs mean for mathematical research and education. I didn’t take the path of becoming a professional mathematician, so I don’t have much to say about the kind of training that research at the frontier requires.

But from my experience as someone who enjoys math, I think we’re seriously underestimating how good models can be as teachers in areas they already handle comfortably. In just a few days, an LLM helped me get back to my old level in olympiad combinatorics, close to a decade later, and gain insights I never had back then.

The examples above—[guiding me through my own attempts](#example-guided-discovery), [working through my inversion idea](#example-inversions), and [connecting a coloring argument to complex weights](#example-coloring)—are the kind of teaching I mean.

### 2.2 From olympiad training to school mathematics

For math olympiads, and by extension at least much of school mathematics, I think models already have a very good handle on the material. A frontier model can be a patient tutor who guides you through a problem without any specialized “skills” or additional post-training.

Within the small world of math olympiads, I suspect having a model as a coach will become a major part of how contestants train. It might even raise the competitive level of the whole community. Perhaps, as in Go, a large part of learning olympiad mathematics will eventually involve learning from AI.

For children who are eager to learn, I think this kind of one-on-one, exploratory teaching, adapted to the individual student, can be extremely effective—at least in mathematics. I’d expect something similar to be possible in many other subjects.

## 3. Human and model reasoning

Apparently, I have nothing better to do than work on IMO problems for fun. Meanwhile, since this summer, I’ve also been working on LLM post-training, training my own (small) language models to solve IMO problems.

Doing both has made me think about how human and model reasoning differ, what each is good at, and where the gap between the model and me actually lies.

### 3.1 Speed of CoT

There’s no way I can match the speed of a model’s chain-of-thought generation. I can only speak for myself, but for me the speed gap alone seems enough to rule out competing with the model at this kind of reasoning.

If I spend an hour on an IMO problem, the total amount of thinking I do—using a very rough token analogy—might not even add up to 100,000 tokens. I’d guess that’s far below what increasingly fast models, especially multi-agent systems, can work through in the same time.

Speed alone makes the competition look pretty hopeless for me. Not to mention that the model’s mathematical intuition now seems better than mine.

### 3.2 Sample complexity

A common claim is that humans have much lower sample complexity than models. Roughly speaking, we can reach the same level after seeing far fewer examples.

A math olympiad student might work through, at most, something on the order of 10,000 training problems. A model may see far more, especially once pre-training and mid-training are counted.

There’s another lesson I find interesting, though. The success of scaling might have something to teach human olympiad students like me: **perhaps we’ve also underestimated what more examples and more practice can do for us.**

When I was training, quite a few of us would get stuck on a problem and think, “I’m just not smart enough.” Maybe the effect of scaling was larger than we thought. Maybe we’ve also underestimated how far human reasoning can go in a short, timed competition.

### 3.3 Continual learning and forgetting

Continual learning and catastrophic forgetting are active problems in LLM training. In one narrow sense, the goal is to let a model keep learning new knowledge and skills from new data without forgetting what it already knew.

Doing these problems again has reminded me how much I forget. By the time I’m working on my 101st combinatorics problem, I’ll definitely be a little fuzzy on how I solved the first one. In that sense, I’m not sure I forget any less than the machine.

On the other hand, with GPT-6 Astra’s help, it took just ten targeted problems and some follow-up exploration to help me get my combinatorics skills back. I don’t think small models in the 4B/8B range have that kind of rapid recovery yet.

Mathematical reasoning seems like a particularly good setting for exploring this. Humans and models both train on problems. Their different strengths, weaknesses, and ways of continuing to learn might suggest better ways to train both.

## 4. Comparing ourselves a little less

One last thought: a possible upside of progress toward AGI is that it might make us compare ourselves with one another a little less.

In the environment I grew up in, we often found ourselves comparing intelligence, whether we wanted to or not. Someone else got better grades. Someone else got things done faster. There always seemed to be another comparison to make.

With LLMs now seemingly able to get through most undergraduate homework in one go, I wonder what it would feel like for my peers and me to go back to those school years. How much of that competitive atmosphere—the one we created ourselves and the one our surroundings encouraged—would we still see as useful? And how much would just seem pointless?

Maybe it would push us to rethink meritocracy and ask what it means to be intellectually ahead of our peers—or what it means to be intellectually exceptional in the first place.

All of this is a bit of thinking out loud. I’m really enjoying the parallel process of training a model to do IMO problems and training myself to do them. I think I’ll keep making math puzzles with GPT-6 Astra part of my routine.

<aside class="post-appendix" id="imo-background" aria-labelledby="imo-background-title" markdown="1">

## Appendix: A quick introduction to the IMO
{: #imo-background-title }

The [International Mathematical Olympiad (IMO)](https://www.imo-official.org/about/) is essentially the world championship of mathematics for high-school students. Think fiendishly difficult problems built from elementary mathematics: no calculus or other university-level tools required.

The [format](https://www.imo-official.org/regulations/) is two days, with three problems and four and a half hours each day—an average of 90 minutes per problem. But the problems generally get harder as you go. A strong contestant might finish the first problem in under half an hour, then spend most of the remaining time on the other two.

The four main areas are algebra, geometry, combinatorics, and number theory. Many contestants find combinatorics the hardest. The problems can feel like brainteasers: relatively little background knowledge to get started, but a lot depends on finding just the right idea. That elusive flash of insight was what I struggled with most.

For context, in high school I could reliably solve problems at the level of the first problem on each day (Problems 1 and 4). The second problem (Problems 2 and 5) was more hit-or-miss—and if it was combinatorics, I usually couldn’t get it during a timed exam.

[Back to the story](#imo-introduction)

</aside>
