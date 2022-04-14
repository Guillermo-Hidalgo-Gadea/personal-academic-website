# Getting started with DeepLabCut

DeepLabCut is a toolbox for markerless pose estimation of animals performing various tasks.

**Documentation:** https://deeplabcut.github.io/DeepLabCut/docs/intro.html  
**Sourcecode:** https://github.com/DeepLabCut/DeepLabCut

DeepLabCut is an open source package for markerless pose estimation based on transfer learning with deep neural networks ([Mathis et al., 2018](https://www.nature.com/articles/s41593-018-0209-y)). It uses algorithms from [DeeperCut](https://link.springer.com/chapter/10.1007/978-3-319-46466-4_3), and an extremely deep neural network pre-trained on a dataset for object detection ([ImageNet](https://openaccess.thecvf.com/content_cvpr_2016/html/He_Deep_Residual_Learning_CVPR_2016_paper.html)). DeepLabCut was originally developed for animal pose estimation, which does not exclude humans, see [Namba et al. (2021)](https://www.nature.com/articles/s41598-021-83077-4), and can also be used to track inanimate objects.

## Installation

DeepLabCut will need to use python and several python related libraries (i.e, a specific python environment), so the first step should be installing [Anaconda](https://docs.anaconda.com/anaconda/install/).  
You can then create a designated environment and install DeepLabCut:  

1. Download the installation file from here: <http://www.mackenziemathislab.org/s/DEEPLABCUT.yaml>
2. Open Terminal and execute:

```
cd Downloads
conda env create -f DEEPLABCUT.yaml
conda activate DEEPLABCUT
pip install --upgrade deeplabcut
```

## Starting the DeepLabCut GUI

Open Anaconda Prompt and execute:
```
conda activate DEEPLABCUT #or your environment name
python -m deeplabcut
```

## Downloading Jupyter Notebooks

On the next page you will find a [DeepLabCut Notebook](DLCjupyter.md), a jupyter notebook I prepared containing the most important steps needed to start your own project.

1. Download the notebook as .ipynb file
2. Rename the file and move it to your working directory
3. Open the notebook with jupyter lab or notebook
4. Start taking notes and make the notebook yours

## Documentation

Check the DeepLabCut documentation for more background and tips on how to get started.  

<iframe src="https://deeplabcut.github.io/DeepLabCut/docs/intro.html" frameborder="1" width="800" height="600"></iframe>
