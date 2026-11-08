---
title: 跟着 LLM 老师重拾我的 IMO 梦
subtitle: 关于未来教育、人类推理与模型推理的一些思考
description: "让 GPT-6 Astra 当竞赛老师，开开心心做题，争取超过高中的自己！"
date: 2026-11-07 12:00:00 -0500
layout: post
page_class: post-page
lang: zh-CN
translation_notice: "中文版是机翻的。"
published: true
list_in_blog: false
permalink: /blog/imo-dream-with-gpt/zh/
translation_url: /blog/imo-dream-with-gpt/
translation_lang: en
translation_label: English
---

如果你不太熟悉 IMO，我在[文末放了一段简单介绍](#imo-background)。
{: #imo-introduction }

这周周中，我冒出一个奇思妙想：让一个 LLM——GPT-6 Astra——来教我 IMO 的组合数学问题。

距离我最后一次参加数学奥林匹克竞赛，已经过去八年了。高中时，我有一个 IMO 金牌梦，但没能实现。我在数学竞赛中并不是特别出色，接受过一定的训练，但相较于身边许多同龄的中国选手，并不是很系统（你可能想象不到中国的竞赛训练量有多大）。我最好的成绩是 CMO 银牌，其中最薄弱的部分就是组合数学。

虽然取得了一些成绩，但当时我内心其实经常很受打击。我觉得自己不够聪明，总是想不到那些出色的同龄人能想到的奇思妙想。

高中之后，我没有再接受过纯粹数学的训练，也再没碰过中学的组合趣题。本科和博士期间，我做过一些 learning theory 相关的科研，也在继续做一些通过 LLM training 提高数学题能力的研究。

几天前，我突然想：现在模型数学这么厉害，为什么不让它教我怎么做组合题呢？就当作一个乐趣，每天做一道。说不定一两年后，我能达到一个连高中时都不具备的水平。

这个体验真是太快乐了。我感觉 LLM 真的是一个太好的老师，于是决定把它记录下来。

## 1. 跟着 GPT-6 Astra 学组合数学

### 1.1 重新开始

<p class="post-note">因为我是用中文学的数学竞赛，所以也用中文来 prompt 它。下面截图中的英文来自 Google 翻译。</p>


<figure class="post-screenshot">
  <a href="{{ '/images/blog/imo-dream/01-starting-redacted.png' | relative_url }}" aria-label="查看完整截图"><img src="{{ '/images/blog/imo-dream/01-starting-redacted.png' | relative_url }}" alt="最初的提问，以及模型鼓励我开始学习的回答。" width="1473" height="1068" loading="lazy" decoding="async"></a>
  <figcaption>它先鼓励我暂时放下“我够不够聪明”的疑问，看看哪些地方可以通过练习提高。它还特别指出：现在就可以重拾这个梦，<em>不必等到 AGI 实现</em>。</figcaption>
</figure>

<figure class="post-screenshot">
  <a href="{{ '/images/blog/imo-dream/02-warm-up.png' | relative_url }}" aria-label="查看完整截图"><img src="{{ '/images/blog/imo-dream/02-warm-up.png' | relative_url }}" alt="模型选择 2011 年 IMO Shortlist C1 作为热身题。" width="1656" height="1346" loading="lazy" decoding="async"></a>
  <figcaption>它先选了一道相对简单的 2011 年 IMO Shortlist C1，帮我恢复手感，也没有急着给解答，留出空间让我自己想。</figcaption>
</figure>

### 1.2 对整个组合竞赛教学的理解

<figure class="post-screenshot">
  <a href="{{ '/images/blog/imo-dream/03-learning-diagnosis.png' | relative_url }}" aria-label="查看完整截图"><img src="{{ '/images/blog/imo-dream/03-learning-diagnosis.png' | relative_url }}" alt="模型区分不会某种工具，与知道工具但想不到在这里使用的不同瓶颈。" width="1746" height="1626" loading="lazy" decoding="async"></a>
  <figcaption>它把“我不知道这个工具”和“我知道这个工具，但想不到在这里用”区分开来。原先那种笼统的“我就是缺灵感”，变成了更具体的问题，也有了更清晰的练习路径。</figcaption>
</figure>

<figure class="post-screenshot">
  <a href="{{ '/images/blog/imo-dream/04-training-landscape.png' | relative_url }}" aria-label="查看完整截图"><img src="{{ '/images/blog/imo-dream/04-training-landscape.png' | relative_url }}" alt="讨论组合数学训练，以及中国国家队选拔考试中的题目特点。" width="1822" height="1578" loading="lazy" decoding="async"></a>
  <figcaption>我还让它从宏观上介绍组合题的训练，一直讲到中国国家队选拔考试的题目特点。</figcaption>
</figure>

<figure class="post-screenshot">
  <a href="{{ '/images/blog/imo-dream/05-bedtime-problem.png' | relative_url }}" aria-label="查看完整截图"><img src="{{ '/images/blog/imo-dream/05-bedtime-problem.png' | relative_url }}" alt="模型挑选了一道适合睡前在脑中思考的组合题。" width="1786" height="1442" loading="lazy" decoding="async"></a>
  <figcaption>它甚至贴心地给我选了一道睡前题：题目短，计算少，不太需要动笔，可以放在脑子里慢慢想。</figcaption>
</figure>

### 1.3 一步一步引导我做出题

它会先问我有什么想法，再引导我自己试下去。比如下面这次，我在尝试一个加权求和的思路。

<figure class="post-screenshot" id="example-guided-discovery">
  <a href="{{ '/images/blog/imo-dream/08-guided-attempt.png' | relative_url }}" aria-label="查看完整截图"><img src="{{ '/images/blog/imo-dream/08-guided-attempt.png' | relative_url }}" alt="我提出加权求和的思路，模型帮我找到下一步该考虑的问题。" width="1747" height="1408" loading="lazy" decoding="async"></a>
  <figcaption>我提出，可以选择一个让加权和最大的点。它检查了我在最初尝试中发现的漏洞，确认这个大方向可行，再引导我思考下一步：权重到底该怎么选？</figcaption>
</figure>

<figure class="post-screenshot">
  <a href="{{ '/images/blog/imo-dream/09-testing-weights.png' | relative_url }}" aria-label="查看完整截图"><img src="{{ '/images/blog/imo-dream/09-testing-weights.png' | relative_url }}" alt="模型用一个小反例说明我提出的权重选法为什么不够。" width="1726" height="1252" loading="lazy" decoding="async"></a>
  <figcaption>我最先想到的权重选法并不完全奏效。它给了一个小反例，让我看清这个想法到底差在哪里。</figcaption>
</figure>

<figure class="post-screenshot">
  <a href="{{ '/images/blog/imo-dream/10-small-cases.png' | relative_url }}" aria-label="查看完整截图"><img src="{{ '/images/blog/imo-dream/10-small-cases.png' | relative_url }}" alt="按照我的要求，模型列出一个小规模情形，让我自己观察规律。" width="1758" height="964" loading="lazy" decoding="async"></a>
  <figcaption>当我想要一个小规模情形来观察时，它取了 <em>n</em> = 4、<em>k</em> = 2，列出中心移动时邻域怎样变化。这让我有了一个具体的例子，可以自己试着看出究竟该累加什么。</figcaption>
</figure>

### 1.4 探索证明与联系

<figure class="post-screenshot" id="example-inversions">
  <a href="{{ '/images/blog/imo-dream/06-inversion-approach.png' | relative_url }}" aria-label="查看完整截图"><img src="{{ '/images/blog/imo-dream/06-inversion-approach.png' | relative_url }}" alt="模型沿着我随口提出的逆序对思路，讲解怎样完成论证。" width="1790" height="1586" loading="lazy" decoding="async"></a>
  <figcaption>做完一道题之后，我随口问了一句，也许统计逆序数也能得到另一种解法。虽然这不是标准思路，但模型沿着我的想法走了下去，把它做出来，再教我怎样补成一个完整的证明。</figcaption>
</figure>

<figure class="post-screenshot" id="example-coloring">
  <a href="{{ '/images/blog/imo-dream/07-coloring-and-integrals.png' | relative_url }}" aria-label="查看完整截图"><img src="{{ '/images/blog/imo-dream/07-coloring-and-integrals.png' | relative_url }}" alt="从染色、矩形铺砌到复值积分的联系。" width="1834" height="1506" loading="lazy" decoding="async"></a>
  <figcaption>我们一起做完一道方格染色题后，我问这种想法还能引出什么有意思的东西。它告诉我，可以把这种染色论证看作更一般的赋权、相加或积分方法的一个特例，随后又用复数权重给我讲了一个很巧妙的矩形铺砌结论。</figcaption>
</figure>

这种体验，好像是有了一位非常好的一对一老师，来帮助我准备数学竞赛。**短短不到一周，我已经有信心挑战 IMO Shortlist C5 难度的题目了。八年前参加竞赛时，达到这一步，我用了两年的训练。**

<!-- reflections-start -->

我已经打算把这个过程像去健身房一样持续下去，每天花一个小时和它一起，从一道题出发，进行一些有趣的思考。

除此之外，这短短一周的体验也让我有了一些更宏观的思考，想记在这里。

<p class="post-caveat">（考虑到模型进步如此飞速，我其实觉得，大多数基于现有模型能力来分析社会效应的讨论，恐怕不会有太长的实效性。）</p>

## 2. 关于未来教育的一些思考

### 2.1 LLM 当老师的能力被严重低估了

最近 ChatGPT 证明出数学大成果之后，我看到了很多关于 LLM 对数学研究和教育影响的讨论。我没有走上职业数学这条路，所以并不太知道前沿数学需要什么样的教育。

不过，从我作为一个数学爱好者的体验来看，模型在它能够完全 handle 的任务上，当老师的能力其实被大家远远低估了。我用短短几天时间，借助 LLM 的帮助，恢复了快十年前数学竞赛组合题的水平，而且获得了很多当年并没有的理解。

上面这些例子——[引导我沿着自己的想法尝试](#example-guided-discovery)、[沿着我的逆序数思路走通证明](#example-inversions)，以及[从染色讲到复数权重](#example-coloring)——就是我说的这种教学体验。

### 2.2 从数学竞赛到基础教育

对于数学竞赛和 IMO 本身，延伸到至少基础教育，我觉得这部分内容模型已经能够很好地 handle。现有的 frontier model，甚至不需要特殊的 skills 和额外的 post-training，就可以成为一个很好的、循循善诱的老师。

具体到数学竞赛这个小群体，我觉得未来让模型担任导师，会成为参赛者训练的一种重要方式，甚至可能提高整个群体的竞技水平。有点像围棋，或许有一天，数学竞赛的学习也会在很大程度上从 AI 发起。

对于基础教育，对好学的孩子而言，模型一对一、探索式、因材施教的教育，至少在数学上可以有非常好的效果。我想很多其他学科也会如此。

## 3. 人类推理与模型推理

看起来，我已经闲到开始做 IMO 题找乐子了。与此同时，从今年暑假以来，我也一直在做 LLM post-training，训练我自己的（小）语言模型做 IMO 题。

这两种体验让我开始思考：人和模型的思考到底有什么不同，各自的优势是什么，以及我作为一个个体，与模型数学能力的差距到底在哪里。

### 3.1 CoT 的速度

我不可能跟上模型生成 CoT 的速度。我只能代表自己，但对我而言，思考速度的差距本身，就足以让我觉得自己不可能在这种推理上和模型竞争。

如果非常粗略地用 token 来类比，我做一道 IMO 题，一个小时里的思考总量，可能还不到 10 万个 token。我猜，这远小于还在持续加速的模型，尤其是多智能体系统，在同样时间里能够完成的思考量。

光是速度这一点，就让我觉得很难竞争了。更不用说，模型现在的数学直觉看起来也已经超过了我。

### 3.2 Sample complexity

一个常见的说法是，人类学习的 sample complexity 比模型低很多。通俗地说，就是人可以通过更少的例子，达到相同的水平。

比如，一个数学竞赛学生在竞赛期间训练过的题目，可能至多也就是 10k 这个量级，而模型训练中见过的题目可能远超这些；如果把 pre-training 和 mid-training 也算进去，就更多了。

不过，模型的发展和 scaling，也可能给像我这样的数学竞赛选手一些启发：**也许更多 sample 和更多练习，对于人类提高的作用，同样被低估了。**

当时训练的时候，我和不少竞赛选手一旦遇到做不出来的题，就容易觉得是自己不够聪明。但也许 scaling 的影响比我们想象中更大。人类在这种短时竞赛里的思考能力上限，或许也被低估了。

### 3.3 Continual learning 与 forgetting

Continual learning 和 catastrophic forgetting 是目前 LLM training 中大家在尝试解决的问题。一种狭义的理解，是让模型在持续从新数据里学习知识和技能的同时，不要忘记之前学过的东西。

我最近才很明显地意识到，遗忘对人也广泛存在。比如，当我做到第 101 道组合题时，肯定已经不太记得第 1 道的做法了。从这个角度看，我的遗忘可能也不比机器少。

另一方面，在 GPT-6 Astra 的帮助下，通过有针对性的十道题和延伸思考，我就找回了做组合题的整体能力。我不觉得 4B/8B 这个级别的小模型，目前已经具备这种快速恢复的能力。

我想，数学推理是一个很适合探索这些问题的场景。人和模型都在做训练，各自在持续学习中的强项、劣势，以及进行学习的方式，或许都能为如何训练彼此提供一些启发。

## 4. 少一点人与人的比较

最后还想说的一点是，我觉得 AGI 发展的一个可能的好作用，是让人与人之间少一些比较。

在我成长的环境里，我们经常主动或被动地陷入关于智力的比较。不如别人成绩好，不如别人做事快，好像总有下一个可以比较的地方。

在今天的 LLM 已经几乎可以一次完成绝大多数本科作业的时候，我想，如果我和同龄人回到上学的那个时代，可能会重新思考：我们自己和周围环境共同营造的竞争氛围，到底有多少是积极的，又有多少其实没有意义？

也许人们会重新反思优绩主义，认真想一想，在智力上超过同龄人意味着什么，甚至单单是智力上的出色，又意味着什么。

上面这些都是一些随想。不过，我真的很享受一边训练模型做 IMO、一边训练自己做 IMO 的并行过程。我大概会把和 GPT-6 Astra 一起做数学趣题，当成一个习惯持续下去。

<aside class="post-appendix" id="imo-background" aria-labelledby="imo-background-title" markdown="1">

## 附录：IMO 简介
{: #imo-background-title }

[国际数学奥林匹克竞赛（IMO）](https://www.imo-official.org/about/)基本上可以理解为高中生数学的世界锦标赛。通俗地说，就是用初等数学知识来解决非常难的题，不需要微积分之类的大学数学工具。

[比赛分两天](https://www.imo-official.org/regulations/)，每天三道题，四个半小时，平均每道题有一个半小时。不过，每天的题目通常是越来越难的。高手可能不到半小时就做完第一题，然后把剩下的大部分时间花在后两题上。

四个主要的知识模块是代数、几何、组合和数论。很多选手觉得组合最难。这类题有点像智力题：入手所需的背景知识不多，但往往特别依赖那个恰到好处的想法。而这种灵机一动，正是我当年最头疼的地方。

交代一下我当时的水平：高中时，我大概能稳定做出每天第一题这个难度的题（也就是第 1、4 题）。第二题（第 2、5 题）就比较看运气了——如果碰上组合题，多半在考场上做不出来。

[回到正文开头](#imo-introduction)

</aside>
