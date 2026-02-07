---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}


<style>
/* Lightweight preview: 不改 main.scss，只新增 .proj 系列 */
.proj{position:relative;display:block;overflow:hidden;}
.proj-still{display:block;width:100%;height:auto;transition:opacity 120ms ease;}
.proj-video{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:0;pointer-events:none;transition:opacity 180ms ease;}
.proj.is-playing .proj-video,.proj:hover .proj-video{opacity:1;}
.proj.is-playing .proj-still,.proj:hover .proj-still{opacity:0;}
@media (prefers-reduced-motion: reduce){.proj-still,.proj-video{transition:none !important;}}
</style>


<span class='anchor' id='about-me'></span>

**Xiaohuan Pei (Terry)** is a PhD student in Computer Science at the University of Sydney (USYD), supervised by Prof. [Chang Xu](http://changxu.xyz/).  He collaborate with A/Prof. [Tao Huang](https://taohuang.info/) at SJTU, RA/Prof. [Yanxi Li](https://liyxi.github.io/) at NTU, A/Prof. [Minjing Dong](https://www.cs.cityu.edu.hk/~minjdong/) at CityU, [Yuheng Shi]() at USYD and researcher [Pichao Wang](https://wangpichao.github.io/) at NVIDIA. 
He is a visiting graduate researcher at the University of California, Los Angeles (UCLA), hosted by Prof. [Cho-Jui Hsieh](https://samueli.ucla.edu/people/cho-jui-hsieh/). 

Recently, his research centers on large-scale pretraining of foundation models from scratch at the billion-parameter level, with a particular focus on principled training recipes spanning **Stage-1 (Alignment)**, **Stage-2 (SFT)**, and a newly designed **Stage-3** paradigm. In parallel, he investigates foundation models for autonomous driving, emphasizing scalable pretraining pipelines and efficiency-oriented inference to support real-world deployment. 

<!-- He is currently on the short list of "make it work". -->

<!-- Currently, he is working on fundation models pretraining from scratch at the billion-parameter scale, with a primary focus on kinds of recipes of **Stage-1 (Alignment)**, **Stage-2 (SFT)** and their own designed **Stage-3**. In parallel, He is also exploring foundation models for autonomous driving, with an emphasis on scalable pretraining and efficient inference. -->

  <!-- He will join the University of California, Los Angeles (UCLA) hosted by Prof. [Cho-Jui Hsieh](https://samueli.ucla.edu/people/cho-jui-hsieh/) as a visiting PhD researcher.  -->


 <!-- Hi! I am Xiaohuan Pei (Terry)😊 , a PhD student at the University of Sydney, honorably supervised by Prof. [Chang Xu](http://changxu.xyz/). I also received my MPhil degree at the USYD. Before that, I obtained a BSc degree from CCNU, supervised by Prof. [Zhifeng Wang](https://www.cs.cmu.edu/~novawzf/). 
 I major in deep learning at the School of Computer Science, with a research focus on the efficiency of vision–language models and foundation models.   -->


<!-- **Specialized Field**: Efficiency, Vision Language Models, Vision Language Actions. -->

<!-- <a href="https://scholar.google.com/citations?user=ElujT6oAAAAJ" target="_blank" style="margin-left: 10px;">
  <img alt="Google Scholar" src="https://img.shields.io/badge/455-Citations-4A90E2?logo=google-scholar&logoColor=white">
</a> -->

<!-- **Recent Highlights**:  -->
<!-- Action-aware Dynamic Pruning for Efficient Vision-Language-Action, -->

<!-- Future-aware Masking for Vision Language Model, 

Cross-Self Pruning with \$nSoftmax\$ (OSS sink implementation released one year earlier than OpenAI). -->

<span style="color:red"> Openning to one research intern position working on efficiency for World Model.</span>







<!-- <span class='anchor' id='news'></span>
# 🎉 Updates
- *2025.05*: Light Future-aware Attention. 
- *2024.12*: VLM inference with KV cache.
- *2024.12*: One paper accepted to AAAI 2025.
- *2024.01*: One paper accepted to ICLR 2024.
<span class='anchor' id='publications'></span> -->

<!-- Self-Distilled RoI Predictors for Fine-Grained MLLM Perception -->

<br>





# 📝  Selected Work 

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICLR 2026</div><img src='images/ADP2.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Action-aware Dynamic Pruning for Efficient Vision-Language-Action
Manipulation](https://arxiv.org/pdf/2509.22093) 
<!-- <strong><span class='show_paper_citations' data='ElujT6oAAAAJ:_kc_bZDykSQC'></span></strong>
 -->

**Xiaohuan Pei**<sup>*</sup>, Yuxing Chen<sup>*</sup>, Siyu Xu, Yunke Wang, Yuheng Shi, Chang Xu

[[Paper]](https://arxiv.org/pdf/2509.22093)
[[Code]](https://github.com/chen7086/VLA-ADP)


</div>
</div>








<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICLR 2026</div><img src='images/SD-RPN.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Self-Distilled RoI Predictors for Fine-Grained MLLM Perception](https://arxiv.org/pdf/2509.16944) 
<!-- <strong><span class='show_paper_citations' data='ElujT6oAAAAJ:_kc_bZDykSQC'></span></strong>
 -->

Yuheng Shi, **Xiaohuan Pei**, Minjing Dong, Chang Xu

[[Paper]](https://arxiv.org/pdf/2509.16944)
[[Code]](https://github.com/YuHengsss/SD-RPN)
<!-- [[UnderReview]](-)  -->

</div>
</div>





<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICLR 2026</div><img src='images/future.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Light Future-aware Masking for Vision-Language Inference](https://arxiv.org/pdf/2505.18605)
<!-- <strong><span class='show_paper_citations' data='ElujT6oAAAAJ:_kc_bZDykSQC'></span></strong>
 -->

**Xiaohuan Pei**, Tao Huang, Yanxiang Ma, Chang Xu

[[Paper]](https://arxiv.org/pdf/2505.18605) 
[[Code]](-) 

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge"></div><img src='images/csp.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Cross-Self KV Cache Pruning for Efficient Vision-Language Inference](https://github.com/TerryPei/TerryPei.github.io/blob/main/papers/CSP.pdf) 
<!-- <strong><span class='show_paper_citations' data='ElujT6oAAAAJ:_kc_bZDykSQC'></span></strong>
 -->

**Xiaohuan Pei**, Tao Huang, Chang Xu 

<!-- *International Conference on Machine Learning (ICML), 2024* -->

[[Paper]](https://github.com/TerryPei/TerryPei.github.io/blob/main/papers/CSP.pdf) [[Code]](https://github.com/TerryPei/CSP) <a href="https://github.com/TerryPei/CSP" target="_blank">
  <img alt="GitHub stars" src="https://img.shields.io/github/stars/TerryPei/CSP?style=social">
</a>

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">AAAI 2025</div><img src='images/scan.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[EfficientVMamba: Atrous Selective Scan for Light Weight Visual Mamba](https://arxiv.org/pdf/2403.09977) 
<!-- <strong><span class='show_paper_citations' data='ElujT6oAAAAJ:_kc_bZDykSQC'></span></strong>
 -->

**Xiaohuan Pei**, Tao Huang, Chang Xu

*Proceedings of the AAAI Conference on Artificial Intelligence (AAAI), 2025*

[[Paper]](https://arxiv.org/pdf/2403.09977.pdf) [[Code]](https://github.com/TerryPei/EfficientVMamba) [[Tutorial]](https://mp.weixin.qq.com/s/zCwQRcOiNOx06Hnkr3EYvw)
<a href="https://github.com/TerryPei/EfficientVMamba" target="_blank">
  <img alt="GitHub stars" src="https://img.shields.io/github/stars/TerryPei/EfficientVMamba?style=social">
</a>

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICLR 2024</div><img src='images/NAR.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Neural Architecture Retrieval](https://openreview.net/pdf?id=1JtTPYBKqt) 
<!-- <strong><span class='show_paper_citations' data='ElujT6oAAAAJ:_kc_bZDykSQC'></span></strong>
 -->

**Xiaohuan Pei**, Yanxi Li, Minjing Dong, Chang Xu
<!-- <a href="https://github.com/TerryPei/NNRetreival" target="_blank">
  <img alt="GitHub stars" src="https://img.shields.io/github/stars/TerryPei/EfficientVMamba?style=social">
</a> -->


*The International Conference on Learning Representations (ICLR), 2024*

[[Paper]](https://openreview.net/pdf?id=1JtTPYBKqt) [[Code]](https://github.com/TerryPei/NNRetrieval) 

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ECCV W 2024</div><img src='images/local.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[LocalMamba: Visual State Space Model with Windowed Selective Scan](https://dl.acm.org/doi/abs/10.1007/978-3-031-91979-4_2) 
<!-- <strong><span class='show_paper_citations' data='ElujT6oAAAAJ:_kc_bZDykSQC'></span></strong>
 -->

Tao Huang, **Xiaohuan Pei**, Chang Xu

*The European Conference on Computer Vision (ECCV), Workshop, 2024*

[[Paper]](https://dl.acm.org/doi/abs/10.1007/978-3-031-91979-4_2) [[Code]](https://github.com/hunto/LocalMamba) 
<a href="https://github.com/hunto/LocalMamba" target="_blank">
  <img alt="GitHub stars" src="https://img.shields.io/github/stars/hunto/LocalMamba?style=social">
</a>

</div>
</div>




# 🧑🏻‍💻 Preprints

  *Cross-Self KV Cache Pruning for Efficient Vision-Language Inference.*  
  **Xiaohuan Pei**, Tao Huang, Chang Xu.   
  arXiv preprint [arXiv:2412.04652].


   *GPT self-supervision for a better data annotator.*  
   **Xiaohuan Pei**, Yanxi Li, Chang Xu.   
   arXiv preprint [arXiv:2306.04349]  (2023).
   

   *Text-driven Neural Architecture Embeddings and Retrieval.*  
  **Xiaohuan Pei**, Yanxi Li, Minjing Dong, Chang Xu.  



# 🧑🏻‍💻 Academic Publications

*Action-aware Dynamic Pruning for Efficient Vision-Language-Action
Manipulation.*  
**Xiaohuan Pei**, Yuxing Chen, Siyu Xu, Yunke Wang, Yuheng Shi, Chang Xu   
The Fourteenth International Conference on Learning Representations (ICLR 2026). *(Core Rank A\*)*

*Catching the details: self-distilled ROI predictors for fine-grained Vision-Language-Model perception.*    
Yuheng Shi, **Xiaohuan Pei**, Minjing Dong, Chang Xu.  
The Fourteenth International Conference on Learning Representations (ICLR 2026). *(Core Rank A\*)*

*Rethinking Causal Mask Attention for Vision-Language Inference.*  
**Xiaohuan Pei**, Tao Huang, Yanxiang Ma, Chang Xu.    
The Fourteenth International Conference on Learning Representations (ICLR 2026). *(Core Rank A\*)*

*Efficientvmamba: Atrous selective scan for light weight visual mamba.*  
**Xiaohuan Pei**, Tao Huang, and Chang Xu.  
Proceedings of the AAAI Conference on Artificial Intelligence (AAAI 2025). *(Core Rank A\*)*  


*Localmamba: Visual state space model with windowed selective scan.*  
Tao Huang, **Xiaohuan Pei**, Chang Xu.  
European Conference on Computer Vision (ECCV 2024), Workshop. *(Core Rank A\*)*  


*Neural Architecture Retrieval.*  
**Xiaohuan Pei**, Yanxi Li, Minjing Dong, Chang Xu.  
The Twelfth International Conference on Learning Representations (ICLR 2024). *(Core Rank A\*)*  


*Contrastive code-comment pre-training.*  
**Xiaohuan Pei**, Daochang Liu, Qian Luo, Chang Xu.  
IEEE International Conference on Data Mining (ICDM 2022). *(Core Rank A\*)*  


*Self-attention gated cognitive diagnosis for faster adaptive educational assessments.*  
**Xiaohuan Pei**, Shuo Yang, Jiajun Huang, Chang Xu.  
IEEE International Conference on Data Mining (ICDM 2022). *(Core Rank A\*)*  


*TCNAS: Transformer Architecture Evolving in Clone Detection.*    
Hongyan Xu*, **Xiaohuan Pei***, Shan You, Chang Xu.    
IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP 2024). *(Core Rank A*)


# 📖 Teaching
- *2024*, Guest Lecture, Artifical Intelligence, The University of Sydney

- *2023, 2025*, Tutor for COMP5329 Deep Learning, The University of Sydney

<span class='anchor' id='awards'></span>

# 🎖 Awards
- ICDM Best Student Paper Award
- Two Full Scholarship Awards
- Outstanding Graduate
- National Second Prize in Mathematics Competition
- Provincial Prize in C++ Programming Competition



# 🌟 Funding Grants

- The National Computational Infrastructure (NCI) Adapter Scheme, Australia

<span class='anchor' id='services'></span>

# Services
- Reviewer of TPAMI, ICML, NeurIPS, ICLR, CVPR, ICCV, KDD, ICDM.


**Contact:** xiaohuan.pei at sydney.edu.au, terrypei123 at gmail.com
