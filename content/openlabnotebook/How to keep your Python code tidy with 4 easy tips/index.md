---
title: How to keep your Python code tidy with these 4 easy tips
subtitle: Defining functions, classes, modules and config files to standardize your workflow in python. 

# Summary for listings and search engines
summary: Define functions, classes, modules and config files to upgrade your workflow in python. 

# Link this post with a project
projects: []

# Date published
date: "2021-03-05T00:00:00Z"

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


Those of us using python for data science without a solid programming background may agree that working code is good-enough code. But good enough may depend on how many times you are going to use it, and how much effort you will have to put into deciphering it in the future. Your perfectly working code can get very long very quickly, and loosing track of what part of your code was doing what is only natural. I will share 4 easy tips that will help keep your code clean.

### Do I really need functions, classes, modules and config files in python?
When parts of your code are repeated several times, it is useful to wrap these sections up as **functions**. These functions have to be defined once at the beginning of your script and can be called repeatedly in your code in a single, very informative line.
If these functions get too big, when they need several arguments or are even nested within each other, it may be useful to define a **class** instead, with specific attributes and methods.

A further problem with an unclear script structure appears when you need to input hardcoded parameters directly into the source code (e.g., adapting file paths). A very handy trick to make your life easier in the future, and also help out colleagues that may want to use your code, is to bundle and outsource hardcoded parameters to a separate **config file** (e.g., yaml). This file will contain all parameters that need to be adapted beforehand and most of all, is 'human readable' for those not used to read code. Last but not least, you can keep on outsourcing classes and functions to separate python files and import them as **modules** in your now tidy and manageable script.

### Let’s start with an example: 
In a previous example on [facial expression analysis using unsupervised machine learning](https://guillermohidalgogadea.com/openlabnotebook/upgrade-your-next-zoom-meeting/) I extracted 3D coordinates from synchronized face videos using [DeepLabCut](http://www.mackenziemathislab.org/deeplabcut) and [Anipose](https://anipose.readthedocs.io/en/latest/).


{{< youtube id="JaR1tO0EBnU" autoplay="true" >}}

# 

Now, the following python script (1) reads the csv dataset (2) filters some variables, (3) builds a skeleton for each time frame by connecting some body parts of interest, (4) creates 3D plots at every timeframe, and (5) creates a video of the skeleton over time, as shown above. Although 67 lines of code may still be manageable, it is easy to lose track of each block when upscaling to the entire analysis pipeline, or even when repeating the code with a second, third and n<sup>th</sup> dataset.

{{< icon name="python" pack="fab" >}} PoseAnalysis.py :
<div style="overflow: auto; height:300pt; width:100%;">

```python
import pandas as pd
import matplotlib.pyplot as plt
import cv2

# 1) Open data from csv filepath
filepath = "/GitHub/UQOAB/Pose Analysis/pose-3d.csv"
data = pd.read_csv(filepath, header=0)

# 2) Filter body part coordinates and ignore other variables
coordinates = data.loc[:,~data.columns.str.contains("score|error|ncams|fnum|center|M_")]

# 3) Create skeletons from body parts for each timeframe
skeletons = []
for t in range(len(coordinates)):

    lefteye = [coordinates['lefteye1_x'][t], coordinates['lefteye2_x'][t]], [coordinates['lefteye1_y'][t], coordinates['lefteye2_y'][t]], [coordinates['lefteye1_z'][t], coordinates['lefteye2_z'][t]]
    righteye = [coordinates['righteye1_x'][t], coordinates['righteye2_x'][t]], [coordinates['righteye1_y'][t], coordinates['righteye2_y'][t]], [coordinates['righteye1_z'][t], coordinates['righteye2_z'][t]]
    leyebrow = [coordinates['leyebrow1_x'][t], coordinates['leyebrow2_x'][t],coordinates['leyebrow3_x'][t]],[coordinates['leyebrow1_y'][t], coordinates['leyebrow2_y'][t],coordinates['leyebrow3_y'][t]],[coordinates['leyebrow1_z'][t], coordinates['leyebrow2_z'][t],coordinates['leyebrow3_z'][t]]
    reyebrow = [coordinates['reyebrow1_x'][t], coordinates['reyebrow2_x'][t],coordinates['reyebrow3_x'][t]],[coordinates['reyebrow1_y'][t], coordinates['reyebrow2_y'][t],coordinates['reyebrow3_y'][t]],[coordinates['reyebrow1_z'][t], coordinates['reyebrow2_z'][t],coordinates['reyebrow3_z'][t]]
    nose = [coordinates['nose1_x'][t],coordinates['nose3_x'][t],coordinates['nose2_x'][t],coordinates['nose4_x'][t],coordinates['nose1_x'][t]],[coordinates['nose1_y'][t],coordinates['nose3_y'][t],coordinates['nose2_y'][t],coordinates['nose4_y'][t],coordinates['nose1_y'][t]],[coordinates['nose1_z'][t],coordinates['nose3_z'][t],coordinates['nose2_z'][t],coordinates['nose4_z'][t],coordinates['nose1_z'][t]]
    lips = [coordinates['uplip_x'][t],coordinates['llip_x'][t],coordinates['lowlip_x'][t],coordinates['rlip_x'][t],coordinates['uplip_x'][t]],[coordinates['uplip_y'][t],coordinates['llip_y'][t],coordinates['lowlip_y'][t],coordinates['rlip_y'][t],coordinates['uplip_y'][t]],[coordinates['uplip_z'][t],coordinates['llip_z'][t],coordinates['lowlip_z'][t],coordinates['rlip_z'][t],coordinates['uplip_z'][t]]
    face = [coordinates['rear_x'][t],coordinates['chin_x'][t],coordinates['lear_x'][t]],[coordinates['rear_y'][t],coordinates['chin_y'][t],coordinates['lear_y'][t]],[coordinates['rear_z'][t],coordinates['chin_z'][t],coordinates['lear_z'][t]]

    # Create skeleton from bodyparts for given timeframe
    skeleton = lefteye, righteye, leyebrow, reyebrow, nose, lips, face

    # Summarize skeletons over all timeframes
    skeletons.append(skeleton)

# 4) Plot skeleton in 3D coordinates for each successive timeframe
img_array = [] # Initialize image array to save images from all timeframes

for timeframe in range(len(coordinates)):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.view_init(11, -80) #(elevation, azimuth)
    ax.set_title("3D frame from %s data" %filepath.split("/")[-1])

    for bodypart in range(len(skeletons[0])):
        x = skeletons[timeframe][bodypart][0]
        y = skeletons[timeframe][bodypart][1]
        z = skeletons[timeframe][bodypart][2]
        ax.plot(x,y,z, color='k')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.savefig("figure.png");
    plt.close()

    # save figue and append to img_array
    img = cv2.imread("figure.png")
    height, width, layers = img.shape
    img_array.append(img)

# 5) create video from moving skeleton
out = cv2.VideoWriter('3Dframe.avi',cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 25, (width,height))

for i in range(len(img_array)):
    out.write(img_array[i])
out.release()
```
</div>

### Tip 1: Define your own functions
The first tip is probably the easiest: find functional blocks in your code, wrap them up as a function and move them to the top of your script. In your pipeline you will only need to call the function with the arguments you specified before. See an exmaple below, specifically the condensed part at the bottom of the script:

{{< icon name="python" pack="fab" >}} PoseAnalysisTip1.py :
<div style="overflow: auto; height:300pt; width:100%;">

```python
import pandas as pd
import matplotlib.pyplot as plt
import cv2

# 1) Define functions
def create_skeleton(data):
    """
    This function creates skeletons from defined bodyparts for each timeframe.
    """
    skeletons = []
    for t in range(len(data)): # read out n_components from different poses

        lefteye = [data['lefteye1_x'][t], data['lefteye2_x'][t]], [data['lefteye1_y'][t], data['lefteye2_y'][t]], [data['lefteye1_z'][t], data['lefteye2_z'][t]]
        righteye = [data['righteye1_x'][t], data['righteye2_x'][t]], [data['righteye1_y'][t], data['righteye2_y'][t]], [data['righteye1_z'][t], data['righteye2_z'][t]]
        leyebrow = [data['leyebrow1_x'][t], data['leyebrow2_x'][t],data['leyebrow3_x'][t]],[data['leyebrow1_y'][t], data['leyebrow2_y'][t],data['leyebrow3_y'][t]],[data['leyebrow1_z'][t], data['leyebrow2_z'][t],data['leyebrow3_z'][t]]
        reyebrow = [data['reyebrow1_x'][t], data['reyebrow2_x'][t],data['reyebrow3_x'][t]],[data['reyebrow1_y'][t], data['reyebrow2_y'][t],data['reyebrow3_y'][t]],[data['reyebrow1_z'][t], data['reyebrow2_z'][t],data['reyebrow3_z'][t]]
        nose = [data['nose1_x'][t],data['nose3_x'][t],data['nose2_x'][t],data['nose4_x'][t],data['nose1_x'][t]],[data['nose1_y'][t],data['nose3_y'][t],data['nose2_y'][t],data['nose4_y'][t],data['nose1_y'][t]],[data['nose1_z'][t],data['nose3_z'][t],data['nose2_z'][t],data['nose4_z'][t],data['nose1_z'][t]]
        lips = [data['uplip_x'][t],data['llip_x'][t],data['lowlip_x'][t],data['rlip_x'][t],data['uplip_x'][t]],[data['uplip_y'][t],data['llip_y'][t],data['lowlip_y'][t],data['rlip_y'][t],data['uplip_y'][t]],[data['uplip_z'][t],data['llip_z'][t],data['lowlip_z'][t],data['rlip_z'][t],data['uplip_z'][t]]
        face = [data['rear_x'][t],data['chin_x'][t],data['lear_x'][t]],[data['rear_y'][t],data['chin_y'][t],data['lear_y'][t]],[data['rear_z'][t],data['chin_z'][t],data['lear_z'][t]]

        # Create skeleton from bodyparts for given timeframe
        skeleton = lefteye, righteye, leyebrow, reyebrow, nose, lips, face

        # Summarize skeletons over all timeframes
        skeletons.append(skeleton)

    return skeletons

def create_video_from_skeleton(data, elevation, azimuth):
    """
    This function takes the list of skeletons previously created, generates 3D plots and creates a video file.
    """
    img_array = [] # Initialize image array to save images from all timeframes

    for timeframe in range(len(data)):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        ax.view_init(elevation, azimuth)
        ax.set_title("3D frame from %s data" %filepath.split("/")[-1])
        for bodypart in range(len(data[0])):
            x = data[timeframe][bodypart][0]
            y = data[timeframe][bodypart][1]
            z = data[timeframe][bodypart][2]
            ax.plot(x,y,z, color='k')

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        plt.savefig("figure.png");
        plt.close()

        # Save figue in img_array
        img = cv2.imread("figure.png")
        height, width, layers = img.shape
        img_array.append(img)

    # Create video from moving skeleton
    out = cv2.VideoWriter('3Dframe.avi',cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 25, (width,height))

    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()

# 2) Open data from csv filepath
filepath = "/GitHub/UQOAB/Pose Analysis/pose-3d.csv"
data = pd.read_csv(filepath, header=0)

# 3) Filter body part coordinates and ignore other variables
coordinates = data.loc[:,~data.columns.str.contains("score|error|ncams|fnum|center|M_")]

# 4) Create skeletons wtih function...
skeletons = create_skeleton(data = coordinates)

# 5) Create video file with function...
create_video_from_skeleton(data = skeletons, elevation = 10, azimuth = -90)
```
</div>

### Tip 2: Define your own classes with attributes and methods
When you have functions that build upon each other like in this example, you can run them sequentially like above, or nested within each other with the output of the first function being the input of the second (e.g., ```create_video_from_skeleton(data = create_skeleton(data = coordinates), elevation = 10, azimuth = -90)```). But this nesting gets complex quickly.

An alternative would be to treat both functions as methods of the same superprdinate class. For this, we define a class Pose_3D with some attributes like the filepath it comes from, and even its filtered coordinates, and assign the functions defined before as methods for the Pose_3D class. In the pipeline below, you will only need to create an object of this class, and then apply the methods you need to the object you created.

{{< icon name="python" pack="fab" >}} PoseAnalysisTip2.py :
<div style="overflow: auto; height:300pt; width:100%;">

```python
import pandas as pd
import matplotlib.pyplot as plt
import cv2

# 1) Define class with attributes and methods
class Pose_3D:
    """
    This class initializes a Pose_3D object with attributes such as filepath, data etc. and methods such as create_skeleton and create_video_from_skeleton.
    """
    def __init__(self, filepath):
        self.filepath = filepath
        self.data = pd.read_csv(filepath, header=0)
        self.coordinates = self.data.loc[:,~self.data.columns.str.contains("score|error|ncams|fnum|center|M_")]
        self.skeletons = []
        self.img_array = []

    def create_skeleton(self):
        """
        This function creates skeletons from defined bodyparts for each timeframe.
        """
        for t in range(len(self.coordinates)): # read out n_components from different poses

            lefteye = [self.coordinates['lefteye1_x'][t], self.coordinates['lefteye2_x'][t]], [self.coordinates['lefteye1_y'][t], self.coordinates['lefteye2_y'][t]], [self.coordinates['lefteye1_z'][t], self.coordinates['lefteye2_z'][t]]
            righteye = [self.coordinates['righteye1_x'][t], self.coordinates['righteye2_x'][t]], [self.coordinates['righteye1_y'][t], self.coordinates['righteye2_y'][t]], [self.coordinates['righteye1_z'][t], self.coordinates['righteye2_z'][t]]
            leyebrow = [self.coordinates['leyebrow1_x'][t], self.coordinates['leyebrow2_x'][t],self.coordinates['leyebrow3_x'][t]],[self.coordinates['leyebrow1_y'][t], self.coordinates['leyebrow2_y'][t],self.coordinates['leyebrow3_y'][t]],[self.coordinates['leyebrow1_z'][t], self.coordinates['leyebrow2_z'][t],self.coordinates['leyebrow3_z'][t]]
            reyebrow = [self.coordinates['reyebrow1_x'][t], self.coordinates['reyebrow2_x'][t],self.coordinates['reyebrow3_x'][t]],[self.coordinates['reyebrow1_y'][t], self.coordinates['reyebrow2_y'][t],self.coordinates['reyebrow3_y'][t]],[self.coordinates['reyebrow1_z'][t], self.coordinates['reyebrow2_z'][t],self.coordinates['reyebrow3_z'][t]]
            nose = [self.coordinates['nose1_x'][t],self.coordinates['nose3_x'][t],self.coordinates['nose2_x'][t],self.coordinates['nose4_x'][t],self.coordinates['nose1_x'][t]],[self.coordinates['nose1_y'][t],self.coordinates['nose3_y'][t],self.coordinates['nose2_y'][t],self.coordinates['nose4_y'][t],self.coordinates['nose1_y'][t]],[self.coordinates['nose1_z'][t],self.coordinates['nose3_z'][t],self.coordinates['nose2_z'][t],self.coordinates['nose4_z'][t],self.coordinates['nose1_z'][t]]
            lips = [self.coordinates['uplip_x'][t],self.coordinates['llip_x'][t],self.coordinates['lowlip_x'][t],self.coordinates['rlip_x'][t],self.coordinates['uplip_x'][t]],[self.coordinates['uplip_y'][t],self.coordinates['llip_y'][t],self.coordinates['lowlip_y'][t],self.coordinates['rlip_y'][t],self.coordinates['uplip_y'][t]],[self.coordinates['uplip_z'][t],self.coordinates['llip_z'][t],self.coordinates['lowlip_z'][t],self.coordinates['rlip_z'][t],self.coordinates['uplip_z'][t]]
            face = [self.coordinates['rear_x'][t],self.coordinates['chin_x'][t],self.coordinates['lear_x'][t]],[self.coordinates['rear_y'][t],self.coordinates['chin_y'][t],self.coordinates['lear_y'][t]],[self.coordinates['rear_z'][t],self.coordinates['chin_z'][t],self.coordinates['lear_z'][t]]

            # Create skeleton from bodyparts for given timeframe
            skeleton = lefteye, righteye, leyebrow, reyebrow, nose, lips, face

            # Summarize skeletons over all timeframes
            self.skeletons.append(skeleton)

        return self.skeletons

    def create_video_from_skeleton(self, elevation, azimuth):
        """
        This function takes the list of skeletons previously created, generates 3D plots and creates a video file.
        """
        for timeframe in range(len(self.coordinates)):
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')

            ax.view_init(elevation, azimuth)
            ax.set_title("3D frame from %s data" %self.filepath.split("/")[-1])
            for bodypart in range(len(self.skeletons[0])):
                x = self.skeletons[timeframe][bodypart][0]
                y = self.skeletons[timeframe][bodypart][1]
                z = self.skeletons[timeframe][bodypart][2]
                ax.plot(x,y,z, color='k')

            ax.set_xlabel('X')
            ax.set_ylabel('Y')
            ax.set_zlabel('Z')

            plt.savefig("figure.png");
            plt.close()

            # Save figue in img_array
            img = cv2.imread("figure.png")
            height, width, layers = img.shape
            self.img_array.append(img)

        # Create video from moving skeleton
        out = cv2.VideoWriter('3Dframe.avi',cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 25, (width,height))

        for i in range(len(self.img_array)):
            out.write(self.img_array[i])
        out.release()

# 2) Define csv filepath to open data
filepath = "/GitHub/UQOAB/Pose Analysis/pose-3d.csv"

# 3) Create pose object from class...
pose = Pose_3D(filepath)

# 4) Create skeletons as class method...
pose.create_skeleton()

# 5) Create video file as class method...
pose.create_video_from_skeleton(elevation = 10, azimuth = -80)
```
</div>

### Tip 3: Outsource parameters to a separate config files
Although the code is already quite compact and nested, you will have noticed that parameters like *fielpath* and the *elevation* and *azimuth* for the 3D plot are still hardcoded and may need to be changed for future analysis. This is only a brief example and you probably remember what you need to change in which line, but colleagues using your code may not be aware of where to find these variables quickly (try to imagine a script with hundreds of lines and several parameters to change in different parts of the code). 

A trick that comes in handy is to outsource these parameters to a separate config file, and let the classes initialize by reading their attributes from the config file themselves. This way, you only need to set your parameters in the config file and then run the code, without even looking at it and certainly not trying to find parameters to be changed.

{{< icon name="file" pack="fas" >}} config.yaml :
```yaml
# Change the Parameters needed for PoseAnalysis.py here:
filepath: "/GitHub/UQOAB/Pose Analysis/pose-3d.csv"
elevation: 10
azimuth: -80
```

{{< icon name="python" pack="fab" >}} PoseAnalysisTip3.py :
<div style="overflow: auto; height:300pt; width:100%;">

```python
import pandas as pd
import matplotlib.pyplot as plt
import cv2
import yaml

# 1) Define class with attributes and methods. Note that hardcoded attributes are taken from config.yaml file
class Pose_3D:
    """
    This class initializes a Pose_3D object with attributes such as filepath, data etc. and methods such as create_skeleton and create_video_from_skeleton.
    """
    def __init__(self):
        with open("config.yaml", "r") as file:
            config = yaml.safe_load(file) # read from config.yaml

        self.filepath = config['filepath'] # name of the parameter in config.yaml
        self.elevation = config['elevation']
        self.azimuth = config['azimuth']
        self.data = pd.read_csv(self.filepath, header=0)
        self.coordinates = self.data.loc[:,~self.data.columns.str.contains("score|error|ncams|fnum|center|M_")]
        self.skeletons = []
        self.img_array = []

    def create_skeleton(self):
        """
        This function creates skeletons from defined bodyparts for each timeframe.
        """
        for t in range(len(self.coordinates)): # read out n_components from different poses

            lefteye = [self.coordinates['lefteye1_x'][t], self.coordinates['lefteye2_x'][t]], [self.coordinates['lefteye1_y'][t], self.coordinates['lefteye2_y'][t]], [self.coordinates['lefteye1_z'][t], self.coordinates['lefteye2_z'][t]]
            righteye = [self.coordinates['righteye1_x'][t], self.coordinates['righteye2_x'][t]], [self.coordinates['righteye1_y'][t], self.coordinates['righteye2_y'][t]], [self.coordinates['righteye1_z'][t], self.coordinates['righteye2_z'][t]]
            leyebrow = [self.coordinates['leyebrow1_x'][t], self.coordinates['leyebrow2_x'][t],self.coordinates['leyebrow3_x'][t]],[self.coordinates['leyebrow1_y'][t], self.coordinates['leyebrow2_y'][t],self.coordinates['leyebrow3_y'][t]],[self.coordinates['leyebrow1_z'][t], self.coordinates['leyebrow2_z'][t],self.coordinates['leyebrow3_z'][t]]
            reyebrow = [self.coordinates['reyebrow1_x'][t], self.coordinates['reyebrow2_x'][t],self.coordinates['reyebrow3_x'][t]],[self.coordinates['reyebrow1_y'][t], self.coordinates['reyebrow2_y'][t],self.coordinates['reyebrow3_y'][t]],[self.coordinates['reyebrow1_z'][t], self.coordinates['reyebrow2_z'][t],self.coordinates['reyebrow3_z'][t]]
            nose = [self.coordinates['nose1_x'][t],self.coordinates['nose3_x'][t],self.coordinates['nose2_x'][t],self.coordinates['nose4_x'][t],self.coordinates['nose1_x'][t]],[self.coordinates['nose1_y'][t],self.coordinates['nose3_y'][t],self.coordinates['nose2_y'][t],self.coordinates['nose4_y'][t],self.coordinates['nose1_y'][t]],[self.coordinates['nose1_z'][t],self.coordinates['nose3_z'][t],self.coordinates['nose2_z'][t],self.coordinates['nose4_z'][t],self.coordinates['nose1_z'][t]]
            lips = [self.coordinates['uplip_x'][t],self.coordinates['llip_x'][t],self.coordinates['lowlip_x'][t],self.coordinates['rlip_x'][t],self.coordinates['uplip_x'][t]],[self.coordinates['uplip_y'][t],self.coordinates['llip_y'][t],self.coordinates['lowlip_y'][t],self.coordinates['rlip_y'][t],self.coordinates['uplip_y'][t]],[self.coordinates['uplip_z'][t],self.coordinates['llip_z'][t],self.coordinates['lowlip_z'][t],self.coordinates['rlip_z'][t],self.coordinates['uplip_z'][t]]
            face = [self.coordinates['rear_x'][t],self.coordinates['chin_x'][t],self.coordinates['lear_x'][t]],[self.coordinates['rear_y'][t],self.coordinates['chin_y'][t],self.coordinates['lear_y'][t]],[self.coordinates['rear_z'][t],self.coordinates['chin_z'][t],self.coordinates['lear_z'][t]]

            # Create skeleton from bodyparts for given timeframe
            skeleton = lefteye, righteye, leyebrow, reyebrow, nose, lips, face

            # Summarize skeletons over all timeframes
            self.skeletons.append(skeleton)

        return self.skeletons

    def create_video_from_skeleton(self):
        """
        This function takes the list of skeletons previously created, generates 3D plots and creates a video file.
        """
        for timeframe in range(len(self.coordinates)):
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')

            ax.view_init(self.elevation, self.azimuth)
            ax.set_title("3D frame from %s data" %self.filepath.split("/")[-1])
            for bodypart in range(len(self.skeletons[0])):
                x = self.skeletons[timeframe][bodypart][0]
                y = self.skeletons[timeframe][bodypart][1]
                z = self.skeletons[timeframe][bodypart][2]
                ax.plot(x,y,z, color='k')

            ax.set_xlabel('X')
            ax.set_ylabel('Y')
            ax.set_zlabel('Z')

            plt.savefig("figure.png");
            plt.close()

            # Save figue in img_array
            img = cv2.imread("figure.png")
            height, width, layers = img.shape
            self.img_array.append(img)

        # Create video from moving skeleton
        out = cv2.VideoWriter('3Dframe.avi',cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 25, (width,height))

        for i in range(len(self.img_array)):
            out.write(self.img_array[i])
        out.release()

# 2) Create pose object from class...
pose = Pose_3D()

# 3) Create skeletons as class method...
pose.create_skeleton()

# 4) Create video file as class method...
pose.create_video_from_skeleton()
```
</div>

### Tip 4: Outsource functions and classes to separate modules 
After outsourcing hardcoded parameters, the last tip is to keep going and outsource functions and classes, too. You can move these bulky blocks of code to a separate script and then load them as modules from your new sleek script, or even from the command line. Make sure to name these files properly and have them in your working directory to avoid import errors (see [documentation](https://docs.python.org/3/reference/import.html)). 

{{< icon name="python" pack="fab" >}} PoseAnalysisTip4.py :
```python
# 1) Load class from module...
from PoseModule import Pose_3D

# 2) Create pose object from class...
pose = Pose_3D()

# 3) Create skeletons as class method...
pose.create_skeleton()

# 4) Create video file as class method...
pose.create_video_from_skeleton()
```

{{< icon name="file" pack="fas" >}} config.yaml :
```yaml
# Change the Parameters needed for PoseAnalysis.py here:
filepath: "/GitHub/UQOAB/Pose Analysis/pose-3d.csv"
elevation: 10
azimuth: -80
```

{{< icon name="python" pack="fab" >}} PoseModule.py :
<div style="overflow: auto; height:300pt; width:100%;">

```python
import pandas as pd
import matplotlib.pyplot as plt
import cv2
import yaml

class Pose_3D:
    """
    This class initializes a Pose_3D object with attributes such as filepath, data etc. and methods such as create_skeleton and create_video_from_skeleton.
    """
    def __init__(self):
        with open("config.yaml", "r") as file:
            config = yaml.safe_load(file) # read from config.yaml

        self.filepath = config['filepath']
        self.elevation = config['elevation']
        self.azimuth = config['azimuth']
        self.data = pd.read_csv(self.filepath, header=0)
        self.coordinates = self.data.loc[:,~self.data.columns.str.contains("score|error|ncams|fnum|center|M_")]
        self.skeletons = []
        self.img_array = []

    def create_skeleton(self):
        """
        This function creates skeletons from defined bodyparts for each timeframe.
        """
        for t in range(len(self.coordinates)): # read out n_components from different poses

            lefteye = [self.coordinates['lefteye1_x'][t], self.coordinates['lefteye2_x'][t]], [self.coordinates['lefteye1_y'][t], self.coordinates['lefteye2_y'][t]], [self.coordinates['lefteye1_z'][t], self.coordinates['lefteye2_z'][t]]
            righteye = [self.coordinates['righteye1_x'][t], self.coordinates['righteye2_x'][t]], [self.coordinates['righteye1_y'][t], self.coordinates['righteye2_y'][t]], [self.coordinates['righteye1_z'][t], self.coordinates['righteye2_z'][t]]
            leyebrow = [self.coordinates['leyebrow1_x'][t], self.coordinates['leyebrow2_x'][t],self.coordinates['leyebrow3_x'][t]],[self.coordinates['leyebrow1_y'][t], self.coordinates['leyebrow2_y'][t],self.coordinates['leyebrow3_y'][t]],[self.coordinates['leyebrow1_z'][t], self.coordinates['leyebrow2_z'][t],self.coordinates['leyebrow3_z'][t]]
            reyebrow = [self.coordinates['reyebrow1_x'][t], self.coordinates['reyebrow2_x'][t],self.coordinates['reyebrow3_x'][t]],[self.coordinates['reyebrow1_y'][t], self.coordinates['reyebrow2_y'][t],self.coordinates['reyebrow3_y'][t]],[self.coordinates['reyebrow1_z'][t], self.coordinates['reyebrow2_z'][t],self.coordinates['reyebrow3_z'][t]]
            nose = [self.coordinates['nose1_x'][t],self.coordinates['nose3_x'][t],self.coordinates['nose2_x'][t],self.coordinates['nose4_x'][t],self.coordinates['nose1_x'][t]],[self.coordinates['nose1_y'][t],self.coordinates['nose3_y'][t],self.coordinates['nose2_y'][t],self.coordinates['nose4_y'][t],self.coordinates['nose1_y'][t]],[self.coordinates['nose1_z'][t],self.coordinates['nose3_z'][t],self.coordinates['nose2_z'][t],self.coordinates['nose4_z'][t],self.coordinates['nose1_z'][t]]
            lips = [self.coordinates['uplip_x'][t],self.coordinates['llip_x'][t],self.coordinates['lowlip_x'][t],self.coordinates['rlip_x'][t],self.coordinates['uplip_x'][t]],[self.coordinates['uplip_y'][t],self.coordinates['llip_y'][t],self.coordinates['lowlip_y'][t],self.coordinates['rlip_y'][t],self.coordinates['uplip_y'][t]],[self.coordinates['uplip_z'][t],self.coordinates['llip_z'][t],self.coordinates['lowlip_z'][t],self.coordinates['rlip_z'][t],self.coordinates['uplip_z'][t]]
            face = [self.coordinates['rear_x'][t],self.coordinates['chin_x'][t],self.coordinates['lear_x'][t]],[self.coordinates['rear_y'][t],self.coordinates['chin_y'][t],self.coordinates['lear_y'][t]],[self.coordinates['rear_z'][t],self.coordinates['chin_z'][t],self.coordinates['lear_z'][t]]

            # Create skeleton from bodyparts for given timeframe
            skeleton = lefteye, righteye, leyebrow, reyebrow, nose, lips, face

            # Summarize skeletons over all timeframes
            self.skeletons.append(skeleton)

        return self.skeletons

    def create_video_from_skeleton(self):
        """
        This function takes the list of skeletons previously created, generates 3D plots and creates a video file.
        """
        for timeframe in range(len(self.coordinates)):
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')

            ax.view_init(self.elevation, self.azimuth)
            ax.set_title("3D frame from %s data" %self.filepath.split("/")[-1])
            for bodypart in range(len(self.skeletons[0])):
                x = self.skeletons[timeframe][bodypart][0]
                y = self.skeletons[timeframe][bodypart][1]
                z = self.skeletons[timeframe][bodypart][2]
                ax.plot(x,y,z, color='k')

            ax.set_xlabel('X')
            ax.set_ylabel('Y')
            ax.set_zlabel('Z')

            plt.savefig("figure.png");
            plt.close()

            # Save figue in img_array
            img = cv2.imread("figure.png")
            height, width, layers = img.shape
            self.img_array.append(img)

        # Create video from moving skeleton
        out = cv2.VideoWriter('3Dframe.avi',cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 25, (width,height))

        for i in range(len(self.img_array)):
            out.write(self.img_array[i])
        out.release()
```
</div>


I hope these tips help you keep your code clean and readable. Not only to optimize your workflow but also to save you some serious debugging effort in the future. Check out my [Github repository]( https://github.com/Guillermo-Hidalgo-Gadea/UQOAB/tree/main/Pose%20Analysis) for all files described above, sample dataset and output video.

*Let me know on [Twitter](https://twitter.com/G_HidalgoGadea) if you found this guide useful or would like to have a more detailed discussion on any of the methods used above.*

<script data-name="BMC-Widget" data-cfasync="false" src="https://cdnjs.buymeacoffee.com/1.0.0/widget.prod.min.js" data-id="g.hidalgogadea" data-description="Support me on Buy me a coffee!" data-message="Thanks for visiting! If you like the website, consider buying me a coffee. Add a note and we could have it together via video call." data-color="#FFDD00" data-position="Right" data-x_margin="18" data-y_margin="18"></script>