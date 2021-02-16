---
title: Installing DeepLabCut - A three step guide
subtitle: Getting started with DeepLabCut for markerless tracking 

# Summary for listings and search engines
summary: Getting started with DeepLabCut for markerless tracking.

# Link this post with a project
projects: []

# Date published
date: "2021-02-15T00:00:00Z"

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


categories:

---

### Is DeepLabCut for me?
Probably yes. If you happen to work with videos and you want to extract information out of them, DeepLabCut is probably a good tool for you. If you need to track the position of a certain object on every single frame, you would benefit from using DLC. If, say, you want to track 5, 10 or 100 different points and their relative position (i.e., a pose), you should be using DeepLabCut. And if it turns out these points are repeated across multiple objects or individuals, you guessed it, DLC for multi-animal tracking! If you don’t happen to work with videos, you should probably start doing so.

A short remark first: This guide is about [DeepLabCut<sup>TM</sup>](http://www.mackenziemathislab.org/deeplabcut) and how to install it, this is no review about best tools available. There are several other promising open source projects for markerless tracking out there, like [OpenPose](https://cmu-perceptual-computing-lab.github.io/openpose/web/html/doc/), [EthoLoop](http://www.etholoop.org/index.html) and [OptiFlex](https://github.com/saptera/OptiFlex) just to name a few. I just happened to start using DeepLabCut when other software was not yet as easily available. For a review on different approaches see [Desmarais et al. (2020)](https://arxiv.org/abs/2010.06449) and [Mathis et al. (2020)](https://www.sciencedirect.com/science/article/abs/pii/S0896627320307170).

But now back to the topic. In case you haven’t heard of it, DeepLabCut is an open source package for markerless pose estimation based on transfer learning with deep neural networks ([Mathis et al., 2018](https://www.nature.com/articles/s41593-018-0209-y)). It uses algorithms from [DeeperCut](https://link.springer.com/chapter/10.1007/978-3-319-46466-4_3), and an extremely deep neural network pretrained on a dataset for object detection ([ImageNet](https://openaccess.thecvf.com/content_cvpr_2016/html/He_Deep_Residual_Learning_CVPR_2016_paper.html)). DeepLabCut was originally developed for animal pose estimation, which does not exclude humans, see [Namba et al. (2021)](https://www.nature.com/articles/s41598-021-83077-4), and can also be used to track inanimate objects, as we will see in our first DLC project.

{{< figure src="DLC_overview.png" title="DeepLabCut's overview. Check their online course [here](http://DLCcourse.deeplabcut.org). ">}}

## How to get started
First of all, you will need to use python and several python related libraries (i.e., a specific python environment). Or rather, DeepLabCut will need it, don’t panic! If you have no programming experience whatsoever and not the slightest interest in learning to code, this guide is still relevant for you. Nevertheless, I will assume either interest or minimal experience in any programming language, or at least with computers and not deleting the internet. This post series will provide you with code snippets, jupyter notebooks and plenty of useful references to work through the python code step by step. If you are still not interested, you will learn to use your mouse and a graphic user interface with pretty buttons.


### Installation
This is arguably the hardest part, but let’s start easy. 
First, you will have to install Anaconda, a free python distribution and package manager that will help you keep all your libraries up to date. The process varies slightly depending on your machine (Windows, macOS or Linux), but overall, you will have to click [here](https://docs.anaconda.com/anaconda/install/), choose your system, download the installer and click through all Next, Agree and Install buttons. Once finished, you can use Anaconda either through the Navigator (a graphic user interface) or the Terminal (the scary black pop-up window).

Next, you will install DeepLabCut, and for that you will have to choose between the full GPU and the simpler CPU version (see note below). On the [DeepLabCut](http://www.mackenziemathislab.org/deeplabcut) homepage, scroll to the bottom of the page to see the respective download files. For convenience you can find the same download links here for the [CPU](http://www.mackenziemathislab.org/s/DLC-CPU.yaml) and for the [GPU](http://www.mackenziemathislab.org/s/DLC-GPU.yaml) version. 

**Note**: Because training deep neural networks is quite computationally intensive, most machine learning approaches make use of additional hardware (graphic processing units or GPUs) originally used in gaming to perform the needed computations. That means that most standard computers and laptops won’t have the processing power required, without upgrading to a GPU first. But luckily, the CPU version of DeepLabCut will allow you to perform most of the pre- and post-processing on your own computer, while outsourcing the actual model training to a cloud computing environment like Google Colab (more on that in the next post).

In case you already have a GPU or the chance to upgrade your computer you will first have to install the Nvidia drivers from [here](https://www.nvidia.com/download/index.aspx) and CUDA 10 from [here](https://developer.nvidia.com/cuda-10.0-download-archive).

Once you downloaded the installation file from above and have anaconda installed open the {{< icon name="terminal" pack="fas" >}}  terminal, locate your DeepLabCut installation file (e.g., in Downloads directory), and create a new virtual environment for the specific file with the following command: 

```bash
ls Downloads
cd Downloads

conda env create -f DLC-CPU.yaml

conda env list
conda activate DLC-CPU
```

See as short video demo: 
{{< youtube yarI_m9F7VU >}}


### Upgrades and Downgreades
Next, we are going to upgrade DeepLabCut to the latest beta release, as of today 2.2b8 (check for newest release [here](https://github.com/DeepLabCut/DeepLabCut#versions)). We are also going to downgrade the library wxpython < 4.1, as some [issues](https://github.com/DeepLabCut/DeepLabCut/issues/682) have been reported. Again using the {{< icon name="terminal" pack="fas" >}}      terminal, upgrade deeplabcut == 2.2b8 and downgrade wxPython == 4.0.7 as follows:

```bash
conda activate DLC-CPU
pip install deeplabcut==2.2b8
pip install -U wxPython==4.0.7
```

See as short video demo: 
{{< youtube 8sfb0Qi2Hd0 >}}

### Starting DeepLabCut
Now that DeepLabCut is installed in its own virtual environment we can start having fun with it. And it actually is up to you how to [get started](https://github.com/DeepLabCut/DeepLabCut/blob/master/docs/UseOverviewGuide.md#the-options-for-using-deeplabcut)! DeepLabCut can be used from the GUI by mouse clicks, from terminal with python functions or from jupyter notebooks that can be easily moved to cloud computing servers like [google colab](https://colab.research.google.com/notebooks/intro.ipynb). 
Because we are working from a CPU environment and won’t be able to train our models locally, we will use a combination of jupyter notebooks to protocol our process and the DLC GUI for the easier overview. 

To get started, open the {{< icon name="terminal" pack="fas" >}}  terminal in macOS, activate your DLC-CPU conda environment and start the DeepLabCut GUI:

```bash
conda activate DLC-CPU
pythonw -m deeplabcut
```

In Windows open the {{< icon name="terminal" pack="fas" >}}  cmd command prompt, activate your environment and start DeepLabCut using *python* instead of *pythonw*:

```bash
conda activate DLC-CPU
python -m deeplabcut
```

Alternatively, you can also start a {{< icon name="python" pack="fab" >}} PythonW (macOS) or an IPython (Windows) shell and start DeepLabCut with the following python command:

```python
import deeplabcut

deeplabcut.launch_dlc()
```

Both methods above will start the DeepLabCut GUI. Find an arrangement on the screen that works for you to see the terminal output and the DeepLabCut window at the same time.

{{< figure src="featured.png" >}}

To start your first DeepLabCut project check out my next post on “Starting your first DLC Project”. If you feel comfortable trying by yourself, check out [these resources](https://github.com/DeepLabCut/DeepLabCut/blob/master/docs/UseOverviewGuide.md#create-a-new-project) from the DeepLabCut Github page, or these [youtube tutorials](https://www.youtube.com/channel/UC2HEbWpC_1v6i9RnDMy-dfA). 

You can also check my previous post for an example on how to apply DeepLabCut in [facial expression analysis using unsupervised machine learning](https://guillermohidalgogadea.com/openlabnotebook/upgrade-your-next-zoom-meeting/).



*Let me know on [Twitter](https://twitter.com/G_HidalgoGadea) if you found this guide useful or would like to have a more detailed discussion on any of the methods used above.*
