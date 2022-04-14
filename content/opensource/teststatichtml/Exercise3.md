# DeepLabCut Tutorial

## How to get started

1. Installation of Anaconda and DeepLabCut environment
2. Start DeepLabCut either through the GUI or Jupyter Notebook
3. Take a minute to describe your dataset and research ideas
4. Manage your behavioral video data, e.g., split into trials
5. Create a new Project and load your behavioral video data
6. Define labeling markers and skeleton on your config.yaml file
7. Extract, label and check frames, before creating a training dataset
8. Train your model using a GPU
9. Analyze your data and create labeled videos

## Starting DeepLabCut with Jupyter

1. Open Anaconda Prompt
2. conda activate DEEPLABCUT (environment)
3. jupyter notebook / jupyter lab / ipython
4. import deeplabcut

## Downloading Jupyter Notebooks

On the next page you will find a [DeepLabCut Notebook](DLCjupyter.md), a jupyter notebook I prepared containing the most important steps needed to start your own project.

1. Download the notebook as .ipynb file
2. Rename the file and move it to your working directory
3. Open the notebook with jupyter lab or notebook
4. Start taking notes and make the notebook yours

## How does it work

```{figure} content/dlcworkflow.png
---
width: 800px
name: dlc_workflow
---
DeepLabCut workflow from Nath et al. 2019.
```

## Troubleshooting

```{admonition} Student contribution
:class: tip
The following tips and tricks were put together with the help of students during real troubleshooting in course exercises. Thank you for your contributions! 
```

:::{admonition} How do I get help?
:class: question, dropdown

1. Check out the known issues reported on [GitHub](https://github.com/DeepLabCut/DeepLabCut/issues) using keywords from your error messages.
2. Read the [GitHub Documentation](https://docs.github.com/en/issues/tracking-your-work-with-issues/about-issues) for best practices on how to open new issues.
3. Go through the tips and tricks sections in the [Documentation](https://deeplabcut.github.io/DeepLabCut/docs/intro.html) to find any errors in your procedure or code.
:::

### Problems related to Jupyter Notebook

:::{admonition} I am struggling to start DeepLabCut correctly, what to do?
:class: question, dropdown
DeepLabCut can be started as on a **jupyter notebook** by opening the anaconda prompt, activating your DeepLabCut environment and starting ```jupyter notebook``` or ```jupyter lab```. Then open the correct notebook and start executing your code cells. This method is recommended at the beginning to create a new project, extract frames, as well as for model training and analysis. The cell outputs can be saved in jupyter notebook and contain valuable information for later. When it comes to labeling frames though, jupyter notebook can be unresponsive when opening and closing the labeling GUI. Alternatively, DeepLabCut could be started as a **graphical user interface** by opening the anaconda prompt, activating your DeepLabCut environment and running ```python -m deeplabcut```. If you are already working from a jupyter notebook, run ```deeplabcut.launch_dlc()``` to start the GUI from the same notebook. Remember to keep track of output messages in the terminal window.  
:::

:::{admonition} How can I find specific sections in my Jupyter Notebook?
:class: question, dropdown
Your jupyter notebook might be a little difficult to navigate, especially at the beginning. Try making your life a little easier by using markdown cells to comment and describe your code, thus creating a reproducible workflow. Add ```# Title 1``` and ```##Title 1.1``` as well as informative text and notes on how to use the notebook and what each code cell is supposed to do. Remember to add your name to the notebook if you intend to share it with others and give credit when using open source materials.
:::

:::{admonition} Jupyter Notebook is not trusted
:class: question, dropdown
Some functions may not work properly if the juypter notebook is not trusted. Click the "not trusted" button to solve the problem. This may happen when you open a notebook from someone else. Make sure to rename the file, save it to your computer and log the changes you do by e.g., adding your name as contributor or author, as well as changing the date.
:::

:::{admonition} Jupyter Notebook is not responding
:class: question, dropdown
In general, jupyter notebook indicates to be running by the orange sand clock icon in the browser tab. Within the notebook, every code cell is denoted by ```In [ ]:```. While running the cell, the label turns to ```In [ * ]:``` to indicate work in progress. After the process is finished, the cell is numbered ```In [ 1 ]:``` to show the order in which the code cells were executed.  
Sometimes jupyter notebook looks non-responsive but is actually running code in the background. Try to use ```print()``` commands regularly to show some progress in long loops.  
If jupyter notebook is really not responding, you can try interrupting and restarting the kernel. If that does not work either, save the notebook, close the jupyter tabs and kill the process in the terminal with ```Ctr + c```. Then start jupyter notebook again.  
:::

### Problems related to Data Management

:::{admonition} Plan your video recording setting in advance!
:class: question, dropdown
Consider lighting, camera position and video quality before you start your experiment. Camera position and lighting are crucial, when it comes to tracking. Testing the setup to see if it produces a good video before starting the experiment will make your life a lot easier afterwards. Make sure you see everything you want to track (e.g. no body parts are out of frame) and that lighting doesn't produce too many shadows or interferes with identifying body parts. If possible, also make sure there is not to much happening in the background which could be confused in tracking. Playing around with the setup at the beginning might safe you a lot of time afterwards.
:::

:::{admonition} How much video data do I need?
:class: question, dropdown
It depends on what you want to analyze. The easiest and safest would be for you to train a model with all the videos you want to analyze. If that does not work, make sure to have enough videos representative for the entire dataset. For freely moving animals this becomes especially challenging, as you may need video clips from different perspectives. Many videos will only show one side of the animal (2D plane) so at every time point the opposite side stays occluded. By using videos filmed from many different perspectives it’s easier to label everything and capture many angles and body parts.
:::

:::{admonition} Some steps in DeepLabCut take very long!
:class: question, dropdown
Data analysis is a slow process, and should be done carefully. Especially when dealing with large videos or big datasets, simple tasks such as copying files from one folder to another may take hours!

Some steps such as extracting frames, training a model, and analyzing videos may take very long. Try to plan ahead and let your computer work for you over night or even over the weekend.
:::

:::{admonition} How can I compare two models trained on the same data?
:class: question, dropdown
The process of extracting frames, e.g., with ```Kmeans``` or creating a training set is stochastic, and will be different every time. What if I want to use the same frames and the same training set for two different projects?

Create a single project first, edit the config.yaml and extract frames. Then duplicate the entire project directory on your computer with a new project name (**note:** remember to update the project name in the config.yaml file, e.g., ```project_path```). To create the training set in the second project, pass the trainIndices and testIndices from the previous project to ```deeplabcut.create_training_dataset(config_path, trainIndices=[trainIndices],testIndices=[testIndices])```, see [here](https://github.com/DeepLabCut/DeepLabCut/blob/2d813d96277b84dae4256b1465e76e79fd9b0bb3/deeplabcut/generate_training_dataset/trainingsetmanipulation.py#L722).

On the other hand, if you want to train two different networks, e.g. ```resnet-50``` and ```resnet-101```, use the function ```deeplabcut.create_training_model_comparison()``` to create the same training set twice in one project for different model architectures.
:::

### Problems related to the Config.yaml

:::{admonition} System cannot find path specified
:class: question, dropdown
Check again the correctness of the path you provided. If the file exists and the path is pointing correctly to it, check the direction of slashes used. Windows naturally uses backslashes for file paths, but these are not allowed in python. Try manually changing the path to forward slashes, e.g. ```C:/Users/Directory/```, or double backslashes, e.g. ```C:\\Users\\Directory\\```. Alternatively, you can use ```Tkinter``` to format your directory paths correctly.
:::

:::{admonition} Choosing the right project name
:class: question, dropdown
As a general rule, don't use spaces in directory names! Please, really, this can only end in disaster. Try using short but clear names, and don't make your project directories too deeply nested, e.g. ```/Disk/Projects/Important/Seminars/Data_Analysis/DeepLabCut/current_Project```. Some problems may occur within DeepLabCut with too long project paths, for example when you try ```plotting = True``` in ```deeplabcut.evaluate_network()``` and your frames can not be saved because Windows does not recognize your long project path, see [here](https://github.com/DeepLabCut/DeepLabCut/issues/891).
:::

:::{admonition} "IndexError: list index out of range"
:class: question, dropdown
The skeleton in the ```config.yaml``` can only be defined by connections between two keypoints. Connecting more than two points may lead to an index error.
:::

### Problems related to Labeling

:::{admonition} Labeling frames with many occluded markers
:class: question, dropdown
As a general rule, use more keypoints than you think you may need, this will help you cover more information. Especially when dealing with occluded body parts, maybe one of your redundant markers will be visible, even when others are occluded. Also try using more than 106 frames to ensure you have enough views for every keypoint. Keeping a marker that is never seen may make little sense.
:::

:::{admonition} More is always better, but increase variability
:class: question, dropdown
The decision of how many frames to extract is closely linked to the number of videos you are working with. Although frame extraction methods such as ```kmeans``` try to diversify the frames extracted from the video, it will be generally better to extract only 10 frames from 10 different videos than 100 frames of a single video. This only applies when trying to train a model that generalizes well. In specific circumnstances you may prefer to overfit the model to your specific data.
:::

:::{admonition} Labeling from multiple views
:class: question, dropdown
Be very clear on how you define your keypoints, being overly specific won't hurt. The ```top of the head``` for example may not be the same thing from a top view, front view or sidewise perspective. Try to find a definition that holds for different views and different levels of occlusion. Otherwise the labeled point will vary a lot and cause problems during training. Working in groups may help to find keypoint definitions that work for everyone. Also a little orientation on anatomical structure of the animal will help.
:::

:::{admonition} Multi animal labeling
:class: question, dropdown
Take special care when labeling multiple animals that you assign the correct ID. It would be a pain to find out half way through the labeling prowess that you just finished labeling the wrong animal. Make sure to use distinctive names so you don't confuse them too much. If so, a coffee break may help re-focus. The same is true for left and right, please don't confuse them! Or at least consistently only once, but don't switch back and forth.
:::

:::{admonition} Disagreement in Annotations
:class: question, dropdown
**Problem**: Different group members may identify the agreed upon tracking points on slightly different locations. **Solution**: None. This will keep happening, see on Expert Annotation Differences by [Tjandrasuwita et al., 2021](https://arxiv.org/abs/2106.06114). When possible, try to reach a consensus and update your definition, or have only one group member do the labeling, so that keypoints are consistent. If you need/want to track as a group, practice beforehand by discussing how you would label some example-frames.
:::

:::{admonition} Left is where your thumb is on the right
:class: question, dropdown
It is surprisingly easy to get confused with the right and left markers when animals keep moving and rotating between frames. Try to avoid these mistakes by ordering your labels in a fixed sequence that is oriented on the body anatomy or goes from one side to the another, or from top to bottom or whatever. Take a short break when not even this is helping.
:::
