#!/usr/bin/env python
# coding: utf-8

# # What does data look like

# ## What libraries should I import?

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# ## How to read data?
# Dummy data for the following exercises is provided [here](https://ruhr-uni-bochum.sciebo.de/s/Svwxncw01Ir9uxw).

# In[2]:


file = '/Users/guillermo/Downloads/pose-3d.csv'


# In[3]:


data = pd.read_csv(file, header=0)


# ## How is my data structured?

# In[4]:


data.info()


# In[5]:


np.shape(data)


# In[6]:


data


# ### Cleaning data

# In[7]:


coords = data.loc[:, ~data.columns.str.contains(
    'score|error|ncams|fnum|center|M_')]


# In[8]:


scores = data.loc[:, data.columns.str.contains('score')]


# ### Changing the data structure

# In[9]:


# Let us transform the data to be centered around a reference point
centered_coords = coords.copy()
for i in range(centered_coords.shape[1]):
    if '_x' in centered_coords.columns[i]:
        centered_coords.loc[:, centered_coords.columns[i]] = centered_coords.loc[:,
                                                                                 centered_coords.columns[i]].subtract(coords.loc[:, "nose1_x"].values)
    elif '_y' in centered_coords.columns[i]:
        centered_coords.loc[:, centered_coords.columns[i]] = centered_coords.loc[:,
                                                                                 centered_coords.columns[i]].subtract(coords.loc[:, "nose1_y"].values)
    elif '_z' in centered_coords.columns[i]:
        centered_coords.loc[:, centered_coords.columns[i]] = centered_coords.loc[:,
                                                                                 centered_coords.columns[i]].subtract(coords.loc[:, "nose1_z"].values)
    else:
        pass


# In[10]:


centered_coords


# In[11]:


# What is the difference between pandas Data Frame and numpy Array?
coords_egocentric = centered_coords.to_numpy()
coords_egocentric


# ## Reading DeepLabCut Data
# Note that DeepLabCut files contain multiple headers

# In[12]:


# .h5 vs csv with multiple headings
file = '/Users/guillermo/Downloads/DLC_data.csv'
data = pd.read_csv(file, header=0)
data


# You can specify multiple headers in `pd.read_csv(file, header=[0,1,2])`, but your data frame will be a little more difficult to subset, as columns will be a MultiIndex array.

# In[13]:


data = pd.read_csv(file, header=[0, 1, 2])
data


# In[14]:


data.columns


# In[15]:


data.columns.get_level_values(1)


# In[16]:


data.columns.get_level_values(2)


# Better rename the columns of your data frame to avoid MultiIndex

# In[17]:


data.columns.get_level_values(1) + '_' + data.columns.get_level_values(1)


# In[18]:


new_col_names = list(data.columns.get_level_values(
    1) + '_' + data.columns.get_level_values(2))
data.columns = new_col_names
data


# ## What does my data tell me?

# In[19]:


# Does this make sense?
coords.mean(axis='columns')


# In[20]:


# What about this?
coords.mean(axis='index')


# In[21]:


coords['lefteye1_x'].mean()


# In[22]:


coords.describe()


# ## How could my data look like

# In[23]:


scores.hist(figsize=(20, 20))


# In[24]:


scores.boxplot(column=['chin_score', 'lefteye1_score'], figsize=(10, 10))


# In[25]:


x_coords = coords.loc[:, coords.columns.str.contains('_x')]
y_coords = coords.loc[:, coords.columns.str.contains('_y')]
z_coords = coords.loc[:, coords.columns.str.contains('_z')]

t = 0

fig = plt.figure(figsize=(6, 4), dpi=100)
ax = fig.add_subplot(projection='3d')
x_points = x_coords[t:t+1]
y_points = y_coords[t:t+1]
z_points = z_coords[t:t+1]

ax.scatter3D(x_points, y_points, z_points)
ax.view_init(11, 280)
ax.set(xlabel='X axis', ylabel='Y axis', zlabel='Z axis')

plt.title("My First Plot")


# In the following section we will learn to calculate some easy kinematic features to better understand our data.

# ## Bonus

# In[26]:


def face_skeleton(pose):
    """
    The face_skeleton function defines a mesh skeleton by connecting the facial landmarks as defined below.
    This function is directly passed to plot_3Dpose. 
    """
    skeletons = []
    for n in range(len(pose)):  # read out n_components from different poses

        lefteye = [pose[n]['lefteye1_x'], pose[n]['lefteye2_x']], [
            pose[n]['lefteye1_y'], pose[n]['lefteye2_y']], [pose[n]['lefteye1_z'], pose[n]['lefteye2_z']]
        righteye = [pose[n]['righteye1_x'], pose[n]['righteye2_x']], [
            pose[n]['righteye1_y'], pose[n]['righteye2_y']], [pose[n]['righteye1_z'], pose[n]['righteye2_z']]
        leyebrow = [pose[n]['leyebrow1_x'], pose[n]['leyebrow2_x'], pose[n]['leyebrow3_x']], [pose[n]['leyebrow1_y'], pose[n]
                                                                                              ['leyebrow2_y'], pose[n]['leyebrow3_y']], [pose[n]['leyebrow1_z'], pose[n]['leyebrow2_z'], pose[n]['leyebrow3_z']]
        reyebrow = [pose[n]['reyebrow1_x'], pose[n]['reyebrow2_x'], pose[n]['reyebrow3_x']], [pose[n]['reyebrow1_y'], pose[n]
                                                                                              ['reyebrow2_y'], pose[n]['reyebrow3_y']], [pose[n]['reyebrow1_z'], pose[n]['reyebrow2_z'], pose[n]['reyebrow3_z']]
        nose = [pose[n]['nose1_x'], pose[n]['nose3_x'], pose[n]['nose2_x'], pose[n]['nose4_x'], pose[n]['nose1_x']], [pose[n]['nose1_y'], pose[n]['nose3_y'], pose[n]
                                                                                                                      ['nose2_y'], pose[n]['nose4_y'], pose[n]['nose1_y']], [pose[n]['nose1_z'], pose[n]['nose3_z'], pose[n]['nose2_z'], pose[n]['nose4_z'], pose[n]['nose1_z']]
        lips = [pose[n]['uplip_x'], pose[n]['llip_x'], pose[n]['lowlip_x'], pose[n]['rlip_x'], pose[n]['uplip_x']], [pose[n]['uplip_y'], pose[n]['llip_y'], pose[n]
                                                                                                                     ['lowlip_y'], pose[n]['rlip_y'], pose[n]['uplip_y']], [pose[n]['uplip_z'], pose[n]['llip_z'], pose[n]['lowlip_z'], pose[n]['rlip_z'], pose[n]['uplip_z']]
        face = [pose[n]['rear_x'], pose[n]['chin_x'], pose[n]['lear_x']], [pose[n]['rear_y'], pose[n]
                                                                           ['chin_y'], pose[n]['lear_y']], [pose[n]['rear_z'], pose[n]['chin_z'], pose[n]['lear_z']]

        skeleton = lefteye, righteye, leyebrow, reyebrow, nose, lips, face
        skeletons.append(skeleton)

    return skeletons


def plot_3Dpose(pose, elevation, azimuth):
    """
    This plot function takes the average pose coordinates of facial landmarks, creates a skeleton and visualizes the facial expression
    in a 3D coordinate system with predefined elevantion and azimuth angles.
    """
    skeletons = face_skeleton(pose)

    ncols = 3
    nrows = math.ceil(len(pose)/ncols)
    width = ncols*6
    height = nrows * 5

    fig, axes = plt.subplots(nrows, ncols, figsize=(
        width, height), subplot_kw=dict(projection='3d'))

    for ax, n in zip(axes.flat, range(len(pose))):
        x_points = pose[n][['_x' in s for s in pose[n].index]]
        y_points = pose[n][['_y' in s for s in pose[n].index]]
        z_points = pose[n][['_z' in s for s in pose[n].index]]
        ax.scatter3D(x_points, y_points, z_points)
        ax.view_init(elevation, azimuth)
        ax.set(xlabel='X axis', ylabel='Y axis', zlabel='Z axis')
        ax.set_title('Predicted Pose: %d' % (n+1))
        for i in range(len(skeletons[0])):
            x = skeletons[n][i][0]
            y = skeletons[n][i][1]
            z = skeletons[n][i][2]
            ax.plot(x, y, z, color='g')

    plt.suptitle(
        'Hidden Markov Model predictions with N = %d Components' % len(pose))
    plt.show()
    return


def split_data(data, prediction):
    """
    The split_data function will be used to split time series data into smaller 
    chunks by the prediction variable.

    """
    n = max(prediction)+1  # read out the number of predicted components
    data['pred'] = prediction
    grouped = data.groupby(data.pred)
    predictions = [grouped.get_group(i) for i in range(n)]
    pose = [predictions[i].mean() for i in range(n)]

    return predictions, pose


# In[27]:


from hmmlearn import hmm
import math
# change the number of components you expect to find in your data
model1 = hmm.GaussianHMM(n_components=9, covariance_type="full")
model1.fit(coords)
pred1 = model1.predict(coords)


# In[28]:


_, pose1 = split_data(centered_coords, pred1)


# In[29]:


plot_3Dpose(pose1, 11, 280)


# In[ ]:




