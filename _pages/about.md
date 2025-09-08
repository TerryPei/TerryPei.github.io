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

<span class='anchor' id='about-me'></span>

Hi! I am  Xiaohuan Pei (Terry) 😊, a PhD student at the University of Sydney, honorably supervised by Professor Chang Xu. I major in deep learning at the school of computer science.

**Specialized Field**: Efficiency, Vision Language Models, Vision Language Actions.
<!-- <a href="https://scholar.google.com/citations?user=ElujT6oAAAAJ" target="_blank" style="margin-left: 10px;">
  <img alt="Google Scholar" src="https://img.shields.io/badge/455-Citations-4A90E2?logo=google-scholar&logoColor=white">
</a> -->


**Recent Projects**: 

Future-aware Masking for Vision Language Inference, 

Cross-Self Pruning with \$nSoftmax\$ (equivalent to GPT-OSS sink implementation from an inference perspective).



<!-- <span class='anchor' id='news'></span>
# 🎉 Updates
- *2025.05*: Light Future-aware Attention. 
- *2024.12*: VLM inference with KV cache.
- *2024.12*: One paper accepted to AAAI 2025.
- *2024.01*: One paper accepted to ICLR 2024.
<span class='anchor' id='publications'></span> -->



<br>

# 📝  Recent Work

<div class='paper-box'><div class='paper-box-image'><div><div class="badge"></div><img src='images/future.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Light Future-aware Masking for Vision-Language Inference](-) 
<!-- <strong><span class='show_paper_citations' data='ElujT6oAAAAJ:_kc_bZDykSQC'></span></strong>
 -->

**Xiaohuan Pei**, Tao Huang, Yanxiang Ma, Chang Xu

[[Paper]](https://arxiv.org/pdf/2505.18605) 
<!-- [[UnderReview]](-)  -->

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


<div class='paper-box'><div class='paper-box-image'><div><div class="badge"></div><img src='images/Annotator.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[GPT Self-Supervision for an Efficient Data Annotator](https://github.com/TerryPei/TerryPei.github.io/blob/main/papers/Annotator.pdf) 
<!-- <strong><span class='show_paper_citations' data='ElujT6oAAAAJ:_kc_bZDykSQC'></span></strong>
 -->

**Xiaohuan Pei**, Yanxi Li, Minjing Dong, Chang Xu

[[Paper]](https://github.com/TerryPei/TerryPei.github.io/blob/main/papers/Annotator.pdf) 
[[Code]](https://github.com/TerryPei/Annotator) 
[[News]](https://mp.weixin.qq.com/s/8661PcsHCprNdRKhucstIw) 


</div>
</div>

# Preprints

**Xiaohuan Pei**, Tao Huang, Chang Xu.  
   *Rethinking Causal Mask Attention for Vision-Language Inference.*  
   Under review (2025).

Yuxing Chen*, **Xiaohuan Pei***, Minjing Dong, Chang Xu.  
   *Dynamic Anticipatory Pruning for Efficient Vision-Language-Actions Manipulations.*  
   Under review (2025).

**Xiaohuan Pei**, Tao Huang, Chang Xu.  
   *Cross-Self KV Cache Pruning for Efficient Vision-Language Inference.*  
   arXiv preprint [arXiv:2412.04652](https://arxiv.org/abs/2412.04652) (2024).  

**Xiaohuan Pei**, Yanxi Li, Chang Xu.  
   *GPT self-supervision for a better data annotator.*  
   arXiv preprint [arXiv:2306.04349](https://arxiv.org/abs/2306.04349) (2023).

 Yuheng Shi, **Xiaohuan Pei**, Minjing Dong, Chang Xu.  
   *Catching the details: self-distilled ROI predictors for fine-grained Vision-Language-Model perception.*  
   Under review (2025).

 **Xiaohuan Pei**, Yanxi Li, Minjing Dong, Chang Xu.  
   *Text-driven Neural Architecture Embeddings and Retrieval.*  
   Under review (2024).



# Aademic Publications

   **Xiaohuan Pei**, Tao Huang, and Chang Xu.  
   *Efficientvmamba: Atrous selective scan for light weight visual mamba.*  
   Proceedings of the AAAI Conference on Artificial Intelligence (AAAI 2024). *(Core Rank A\*)*

   Tao Huang, **Xiaohuan Pei**, Chang Xu.  
   *Localmamba: Visual state space model with windowed selective scan.*  
   European Conference on Computer Vision (ECCV 2024), Workshop. *(Core Rank A\*)*

  **Xiaohuan Pei**, Yanxi Li, Minjing Dong, Chang Xu.  
   *Neural Architecture Retrieval.*  
   The Twelfth International Conference on Learning Representations (ICLR 2024). *(Core Rank A\*)*

  **Xiaohuan Pei**, Daochang Liu, Qian Luo, Chang Xu.  
   *Contrastive code-comment pre-training.*  
   IEEE International Conference on Data Mining (ICDM 2022). *(Core Rank A\*)*

  **Xiaohuan Pei**, Shuo Yang, Jiajun Huang.  
   *Self-attention gated cognitive diagnosis for faster adaptive educational assessments.*  
   IEEE International Conference on Data Mining (ICDM 2022). *(Core Rank A\*)*

  Hongyan Xu*, **Xiaohuan Pei***, Xiu Su, You Shan, Chang Xu.  
   *TCNAS: Transformer Architecture Evolving in Clone Detection.*  
   IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP 2024).


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



# 🌟 Grants

- The National Computational Infrastructure (NCI) Adapter Scheme, Australia

<span class='anchor' id='services'></span>

# Services
- Reviewer of TPAMI, ICML, NeurIPS, ICLR, CVPR, ICCV, KDD, ICDM.


**Contact:** xiaohuan.pei at sydney.edu.au, terrypei123 at gmail.com
