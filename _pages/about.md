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

Hi! I am  Xiaohuan Pei (Terry) 😊, a PhD student at the University of Sydney, supervised by Professor Chang Xu. I major in deep learning at the school of computer science.

**Specialized Field**: Vision Language Models, Vision Language Actions.

**Recent Work**: Future-aware Attention,  EfficientVMamba, Cross-Self Pruning.


<!-- I obtained a PhD degree from Peking University supervised by A/Prof [Tingting Jiang](http://www.vie.group/ttj) and Prof [Yizhou Wang](https://cfcs.pku.edu.cn/english/people/faculty/yizhouwang/index.htm), and a Bachelor of Engineering from Tongji University. 
 -->


<!-- My research interests lie in intelligent surgical skill assessment using computer vision and generative artificial intelligence.
 -->

<!-- My research seeks to answer two principal questions, i.e., “what” is performed and “how well” it is performed, by observing human activities from visual or multi-modal data and using generative learning frameworks. This is pivotal to human-centric machine intelligence to comprehend, collaborate with, and amplify human capabilities in daily and professional lives.  -->

<!-- This stems from the notion that human behavior is inherently a generative act, conditioned on driving goals, environmental contexts, and prior experiences. Such an “understanding-by-generating" paradigm enables unsupervised learning of human activities. I also feel excited about delving into human skill assessment by viewing skills as emergent attributes generated from repeated action operations. My goal is to understand skill acquisition through generative learning, by connecting the generative process of actions and the learning curve of skills from novice to expert.  -->

<!-- My research about generative surgical AI lies in intelligent analysis of surgeries to enhance patient care and surgical education. The short-term goal is to demystify the intricacies of surgical procedures, e.g., tool usage and event patterns, using videos from minimally invasive or robotic surgeries, and establish links with surgical skills and clinical outcomes. My previous works have shown promising results; AI-based skill assessment on in-vivo clinical gastrectomy surgeries demonstrated remarkable correlations with the expert consensus. The long-term vision is to bring intelligence into the multimodal data of surgeries in an enriched context beyond videos, including perioperative imaging, robotic kinematics, textual records, and environmental and physiological metrics, to offer holistic insights into surgical procedures. By utilizing specialized models, foundational models, and specialized-foundational models of machine learning, my research aims to advance surgical data science from concept to translation in the next generation of surgery.
 -->
<!-- My research is rooted in understanding human action and skills with computer vision and generative artificial intelligence, which also involves fundamental problems in generative diffusion models and applications in automatic surgical skill assessment.
 -->
<!-- My research interests lie in computer vision, artificial intelligence, and related topics in the medical domain, specifically including:
- Generative AI, Diffusion Models
- Surgical AI, Surgical Skill Assessment
- Video Understanding and Action Analysis -->

<!-- My research interest includes neural machine translation and computer vision. I have published more than 100 papers at the top international AI conferences with total <a href='https://scholar.google.com/citations?user=DhtAFkwAAAAJ'>google scholar citations <strong><span id='total_cit'>260000+</span></strong></a> (You can also use google scholar badge <a href='https://scholar.google.com/citations?user=DhtAFkwAAAAJ'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>).
 -->

<span class='anchor' id='news'></span>

# 🔥 Updates
- *2025.05*: Release Light Future-aware Attention. 
- *2024.12*: Release a VLM inference project: CSP.
- *2024.12*: One paper accepted to AAAI 2025.
- *2024.01*: One paper accepted to ICLR 2024.
<!-- *2024.02*: Two papers accepted to CVPR 2024. 
*2024.02*: I will serve as an Area Chair for MICCAI 2024.  -->

<span class='anchor' id='publications'></span>



<br>

# 📝  Research Projects 

<div class='paper-box'><div class='paper-box-image'><div><div class="badge"></div><img src='images/future.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Future-aware Attention for Vision-Language Inference](-) 
<!-- <strong><span class='show_paper_citations' data='ElujT6oAAAAJ:_kc_bZDykSQC'></span></strong>
 -->

**Xiaohuan Pei**, Tao Huang, Yanxiang Ma, Chang Xu

[[Paper]](https://arxiv.org/pdf/2505.18605) [[UnderReview]](-) 

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge"></div><img src='images/csp.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Cross-Self KV Cache Pruning for Efficient Vision-Language Inference](https://arxiv.org/abs/2412.04652) 
<!-- <strong><span class='show_paper_citations' data='ElujT6oAAAAJ:_kc_bZDykSQC'></span></strong>
 -->

**Xiaohuan Pei**, Tao Huang, Chang Xu

<!-- *International Conference on Machine Learning (ICML), 2024* -->

[[Paper]](https://arxiv.org/pdf/2412.04652) [[Code]](https://github.com/TerryPei/CSP) 

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">AAAI 2025</div><img src='images/scan.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[EfficientVMamba: Atrous Selective Scan for Light Weight Visual Mamba](https://arxiv.org/pdf/2403.09977) 
<!-- <strong><span class='show_paper_citations' data='ElujT6oAAAAJ:_kc_bZDykSQC'></span></strong>
 -->

**Xiaohuan Pei**, Tao Huang, Chang Xu

*Proceedings of the AAAI Conference on Artificial Intelligence (AAAI), 2025*

[[Paper]](https://arxiv.org/pdf/2403.09977.pdf) [[Code]](https://github.com/TerryPei/EfficientVMamba) 

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

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICLR 2024</div><img src='images/NNretrieval.gif' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Neural Architecture Retrieval](https://openreview.net/pdf?id=1JtTPYBKqt) 
<!-- <strong><span class='show_paper_citations' data='ElujT6oAAAAJ:_kc_bZDykSQC'></span></strong>
 -->

**Xiaohuan Pei**, Yanxi Li, Minjing Dong, Chang Xu


*The International Conference on Learning Representations (ICLR), 2024*

[[Paper]](https://openreview.net/pdf?id=1JtTPYBKqt) [[Code]](https://github.com/TerryPei/NNRetrieval) 

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge"></div><img src='images/Annotator.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[GPT Self-Supervision for an Efficient Data Annotator](https://arxiv.org/pdf/2306.04349.pdf) 
<!-- <strong><span class='show_paper_citations' data='ElujT6oAAAAJ:_kc_bZDykSQC'></span></strong>
 -->

**Xiaohuan Pei**, Yanxi Li, Minjing Dong, Chang Xu

[[Paper]](https://arxiv.org/pdf/2306.04349.pdf) 
[[Code]](https://github.com/TerryPei/Annotator) 

</div>
</div>





<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICDM 2022</div><img src='images/C3P.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Contrastive Code-Comment Pre-training](https://ieeexplore.ieee.org/abstract/document/10027715) 
<!-- <strong><span class='show_paper_citations' data='ElujT6oAAAAJ:_kc_bZDykSQC'></span></strong>
 -->

**Xiaohuan Pei**, Daochang Liu, Qian Luo, Chang Xu

*International Conference on Data Mining (ICDM), 2022*

[[Paper]](https://ieeexplore.ieee.org/abstract/document/10027715) 
[[Code]](https://github.com/TerryPei/C3P) 

</div>
</div>





<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICDM 2022</div><img src='images/AGCDM.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Self-Attention Gated Model for Faster Cognitive Diagnosis](https://ieeexplore.ieee.org/abstract/document/10027634) 
<!-- <strong><span class='show_paper_citations' data='ElujT6oAAAAJ:_kc_bZDykSQC'></span></strong>
 -->

**Xiaohuan Pei**, Shuo Yang, Jiajun Huang, Chang Xu

*International Conference on Data Mining (ICDM), 2022*

[[Paper]](https://ieeexplore.ieee.org/abstract/document/10027634) 
[[Code]](https://github.com/TerryPei/AGCDM) 

</div>
</div>





# 📖 Teaching
- *2024*, Guest Lecture, Artifical Intelligence, The University of Sydney

- *2023, 2025*, Tutor for COMP5329 Deep Learning, The University of Sydney

<span class='anchor' id='awards'></span>

# 🎖 Awards
- ICDM Best Student Paper Award
- Two Full Scholarship Awards
- Outstanding Graduate
- National Second Prize in Mathematics Competition in China
- Provincial Prize in C++ Programming Competition in China



# 🌟 Grants

- The National Computational Infrastructure (NCI) Adapter Scheme, Australia

<span class='anchor' id='services'></span>

# Services
- Reviewer of TPAMI, ICML, NeurIPS, ICLR, CVPR, ICCV, KDD, ICDM.


**Contact:** xiaohuan.pei at sydney.edu.au, terrypei123 at gmail.com
