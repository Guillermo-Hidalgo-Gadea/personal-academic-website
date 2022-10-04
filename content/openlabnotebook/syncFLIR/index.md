---
title: Software - syncFLIR
subtitle: A synchronized multiview video recording setup in C++ using FLIR cameras and Spinnaker SDK on Windows machines.

# Summary for listings and search engines
summary: SyncFLIR is a repository with code and instructions to build a synchronized multi-view video recording setup using computer vision cameras from FLIR on Windows.

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

categories:

---

# Welcome to [syncFLIR](https://gitlab.ruhr-uni-bochum.de/ikn/syncflir)

The project is hosted in [GitLab](https://gitlab.ruhr-uni-bochum.de/ikn/syncflir).

## What is this for?

Instead of using independent action cameras to record behavioral experiments and painfully trying to synchronize the different video tracks by e.g. hand-clapping cues or blinking LEDs, make your life easier using triggered cameras. Such an array of wired cameras is scalable without considerable extra effort, allowing for synchronized multi-view video recording and 3D triangulation. This project will help you solve half the problem, you only need to set it up.

SyncFLIR was tested with up to 8 BlackFlyS cameras from FLIR with wired GPIO connectors. One of the cameras is used as pacemaker to trigger all the rest. Alternatively, you can use an external TTL signal generator to trigger all cameras externally. **NEW:** The sourcecode is now compatible with Chameleon3 cameras, too!

## How does it work?

Video recording is performed in separate parallel threads for each camera to reach higher framerate up to 170Hz, but the high data stream with increasing number of cameras may require special hardware specifications. For example, each camera should be connected to independent USB ports, requiring a USB 3.1 host controller card with as many independent channels. Additionally, SSD cards with high writing speeds of 800MB/s and capacity of 2TB will be necessary for longer recordings at higher framerate. If further upgrading is not an option, the different cameras can be distributed over separate machines while being still synchronized with all the others.

To further optimize processing speed, video frames are saved in a binary file as intermediate storage (RECord to BINary: `RECtoBIN.cpp`). The recording process is logged in a .csv file with exact time stamps and frame IDs. In a subsequent process, the binary files can be read out and converted to AVI video files with different video compressions (BINary to AVI: `BINtoAVI.cpp`). To keep track of recording consistancy (i.e., skipped frames, inter-frame-intervals, average fps, etc.) use the diagnostics tool provided ( `Diagnostics.py`) to analyze the .csv recording log.

# Installation

Install the Spinnaker [SDK](http://softwareservices.flir.com/Spinnaker/latest/index.html) and test your camera connections with SpinView. **Note:** Some parts of the code seem to be compatible with Spinnaker library version 2.3.0.77 only (see [issue #3](https://gitlab.ruhr-uni-bochum.de/ikn/syncflir/-/issues/3)). The sourcecode is in C++, but if you don't feel like compiling, download the executables provided `RECtoBIN.exe` and `BINtoAVI.exe` together with the corresponding `myconfig.txt` file. Configure your recording parameters such as camera serial number and framerate in the `myconfig.txt` file before running RECtoBIN.exe. To work on the sourcecode directly, replace the .cpp file in any existing  `/Spinnaker/src` project and compile the file with the corresponding .h files.

# Recording

1. Set your parameters in the myconfig.txt file
2. Record multiple synchronized videos using RECtoBIN.exe
3. Update the generated metadata.txt file to configure video compression
4. Convert the recorded binary files to raw or compressed video with BINtoAVI.exe
5. Play your videos using the [VideoPyToolbox](https://github.com/Guillermo-Hidalgo-Gadea/VideoPyToolbox)
6. Process your recording logfile running Diagnostics.py and look out for any skipped frames!

# Wiki 

In the documentation you will find a list of the equipment needed to build your setup, instructions on how to wire everything up, as well as detailed installation and usage instructions to get yourself started. Brows the [Wiki](https://gitlab.ruhr-uni-bochum.de/ikn/syncflir/-/wikis/Wiki) for more information and step by step guides. If there is something missing feel free to open a new issue.

# Credits

SyncFLIR uses code examples and entire helper functions provided by FLIR Integrated Imaging Solutions, Inc. (FLIR) and the copyright for Spinnaker SDK applies, accordingly.

# License

SyncFLIR is distributed under the MIT License. See [`LICENSE`](https://gitlab.ruhr-uni-bochum.de/ikn/syncflir/-/blob/master/LICENSE) for more information.

# Funding

The development of syncFLIR was carried out at the Institute of Cognitive Neuroscience (IKN), Department of Biopsychology at the Ruhr-University Bochum and supported by the German Research Foundation DFG in the context of funding the Research Training Group “Situated Cognition” (GRK 2185/1). *Original: Gefördert durch die Deutsche Forschungsgemeinschaft (DFG) - Projektnummer GRK 2185/1*.

*Let me know on [Twitter](https://twitter.com/G_HidalgoGadea) if you found this useful or would like to have a more detailed discussion on any of the methods used above.*
