---
title: Software - PigeonSuperModel
subtitle: Pre-trained pigeon models for markerless pose estimation using DeepLabCut and SLEAP.

# Summary for listings and search engines
summary: The Pigeon Super Model is an open source implementation of multiple pre-trained deep-learning models for markerless pose tracking in pigeons.

# Link this post with a project
projects: []

# Date published
date: "2022-04-14T00:00:00Z"

# Date updated
lastmod: ""

# Is this an unpublished draft?
draft: false

# Show this page in the Featured widget?
featured: false

diagram: true

# Featured image
# Place an image named `featured.jpg/png` in this page's folder and customize its options here.
image:
  caption: 
  focal_point: ""
  placement: 2
  preview_only: false

authors:
- admin

tags:
- tool
- data

categories:

---

# Welcome to the [PigeonSuperModel](https://gitlab.ruhr-uni-bochum.de/ikn/pigeonsupermodel)

This project is hosted in [GitLab](https://gitlab.ruhr-uni-bochum.de/ikn/pigeonsupermodel).

## Why a Pigeon Super Model?

Advances in computational neuroethology and markerless pose tracking are making it ever easier for researchers to quantify animal behavior from non-invasive video recordings. Yet, these models still rely on GPUs for heavier computations and model training taking up to several days. With this Pigeon Super Model we provide multiple pre-trained neural networks for out-of-the-box video analysis of pigeon behavior, no previous labeling and training required. A further downside is the missing standards for video recording and analysis, which makes reproducibility across labs somewhat tricky. Instead, with the Pigeon Super Model, we advocate for a standardized set of markers for pigeon tracking and generalizable models across experiments, animals, and camera setups.

Here we make available a dataset of 1151 manually labeled images of different animals in different settings and from different camera angles. We also provide multiple pre-trained models for popular markerless tracking software (i.e., [DeepLabCut](https://deeplabcut.github.io/DeepLabCut) and [SLEAP](https://sleap.ai/)) to be used out-of-the-box on your own data without any additional configurations. We originally trained these models to generalize well across different experimental setups, using different cameras and different animals, and we found that pre-trained models can be easily re-trained on outlier frames to specialize on any particular data set using pigeons as a model organism.

## Contributors

The Pigeon Super Model was initiated by Guillermo Hidalgo Gadea and Sarah C. Möser. Data for this project was collected by the [Biopsychology Team](https://www.ruhr-uni-bochum.de/biopsy/members.html).

This work was carried out at the Institute of Cognitive Neuroscience (IKN), Department of Biopsychology at the Ruhr-University Bochum and supported by the German Research Foundation DFG in the context of funding the Research Training Group “Situated Cognition” (GRK 2185/1). Original: Gefördert durch die Deutsche Forschungsgemeinschaft (DFG) - Projektnummer GRK 2185/1.

*Let me know on [Twitter](https://twitter.com/G_HidalgoGadea) if you found this useful or would like to have a more detailed discussion on any of the methods used above.*
