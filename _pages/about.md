---
layout: folio
permalink: /
title: Jingwu Tang
description: "Jingwu Tang — PhD student at Carnegie Mellon University. Reinforcement learning, imitation learning, multi-calibration, and LLM post-training, particularly self-distillation."
author_profile: false
redirect_from:
  - /about/
  - /about.html
---

<section class="intro" aria-labelledby="intro-title">
  <div class="intro-heading">
    <h1 id="intro-title">Jingwu Tang<span class="chinese-name" lang="zh-Hans">唐静吾</span></h1>
  </div>
  <figure class="portrait">
    <img src="{{ '/images/portrait.png' | relative_url }}" alt="Jingwu Tang" width="1280" height="1280" fetchpriority="high">
  </figure>
  <div class="intro-text">
    <p class="intro-lede">I am a PhD student in the <a href="https://www.cs.cmu.edu/">School of Computer Science</a> at <a href="https://www.cmu.edu/">Carnegie Mellon University</a>, where I am fortunate to be advised by <a href="https://zstevenwu.com/">Steven Wu</a> and <a href="https://feifang.info/">Fei Fang</a>. Before that, I obtained my bachelor’s degree at the Turing Class, <a href="https://www.pku.edu.cn/">Peking University</a>, where I was fortunate to be advised by <a href="https://cfcs.pku.edu.cn/english/people/faculty/xiaotiedeng/index.htm">Xiaotie Deng</a>.</p>
    <p class="research-interests">My research interests lie in reinforcement learning, imitation learning, and multi-calibration. In 2026, I spent a wonderful summer at Amazon working on self-distillation of large language models for hard reasoning tasks.</p>
    <div class="contact-links" aria-label="Contact and profiles">
      <a href="mailto:jingwutang@cmu.edu">Email</a>
      <a href="{{ site.author.googlescholar }}">Google Scholar</a>
      <a href="https://github.com/{{ site.author.github }}">GitHub</a>
      <a href="{{ '/files/Jingwu_Tang_CV.pdf' | relative_url }}">CV</a>
    </div>
  </div>
</section>

<section class="section-grid" id="research" aria-labelledby="research-title">
  <div class="section-content">
    <div class="section-heading">
      <h2 id="research-title">Selected publications</h2>
    </div>
    <ol class="publication-list">
      {% assign selected_publications = site.data.publications | where: 'selected', true %}
      {% for paper in selected_publications %}
      <li class="publication">
        <div class="publication-heading">
          <h3>{% if paper.url %}<a href="{{ paper.url }}">{{ paper.title | escape }}</a>{% else %}{{ paper.title | escape }}{% endif %}</h3>
          <p class="publication-venue">{{ paper.venue }} <span>{{ paper.year }}</span></p>
        </div>
        <p class="publication-authors">{{ paper.authors | escape | replace: 'Jingwu Tang', '<strong>Jingwu Tang</strong>' }}.</p>
        {% if paper.note %}<p class="publication-note">{{ paper.note }}.</p>{% endif %}
      </li>
      {% endfor %}
    </ol>
    <p class="section-note">* Equal contribution.</p>
  </div>
</section>

<section class="section-grid" id="background" aria-labelledby="background-title">
  <div class="section-content">
    <h2 id="background-title">Service</h2>
    <dl class="service-list">
      <dt>Workflow Co-Chair</dt>
      <dd>AAMAS 2026</dd>
      <dt>Program Committee</dt>
      <dd>NeurIPS 2024, 2025; ICML 2025, 2026; ICLR 2025, 2026; AAAI 2024</dd>
      <dt>Workshop Program Committee</dt>
      <dd>ICML 2024: MHFAIA, ARLET, RLControlTheory<br>AAAI 2023: PPAI</dd>
    </dl>
  </div>
</section>

<section class="section-grid aside-section" id="aside" aria-labelledby="aside-title">
  <div class="section-content">
    <h2 id="aside-title">Others</h2>
    <p>I highly recommend exploring the special collections in university archives. At Princeton, I had the opportunity to see and even handle the transcript and photograph John Nash submitted with his application.</p>
    <div class="archive-gallery">
      <figure>
        <a href="{{ '/images/Nash_front.jpg' | relative_url }}"><img src="{{ '/images/Nash_front.jpg' | relative_url }}" alt="John Nash’s transcript and photograph from his Princeton application" width="3024" height="4032" loading="lazy" decoding="async"></a>
        <figcaption>John Nash’s transcript and photograph from his Princeton application.</figcaption>
      </figure>
      <figure>
        <a href="{{ '/images/Nash_back.jpeg' | relative_url }}"><img src="{{ '/images/Nash_back.jpeg' | relative_url }}" alt="A handwritten note on the back of John Nash’s photograph" width="4032" height="3024" loading="lazy" decoding="async"></a>
        <figcaption>An interesting note on the back of Nash’s photograph.</figcaption>
      </figure>
    </div>
    <p class="erdos-note">My <a href="https://en.wikipedia.org/wiki/Erd%C5%91s_number">Erdős number</a> is 3.</p>
  </div>
</section>
