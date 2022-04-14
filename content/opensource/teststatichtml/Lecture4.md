# Recent advances in computational ethology

New advances in computer vision and machine learning have led to a great **boom of new techniques** to track animals from video data and analyze their behavior. For a quick overview of the number of different techniques developed in computational ethology I recommend a [paper compilation](https://github.com/anl13/animal_papers) on Github by An Liang.

## New Techniques

Some of the most popular methods are:

```{panels}
[DeepLabCut](https://github.com/DeepLabCut/DeepLabCut)
---
[Anipose](https://github.com/lambdaloop/anipose)
---
[DANNCE](https://github.com/spoonsso/dannce)
---
[Etholoop](http://etholoop.org/) 
---
[DeepPoseKit](https://github.com/jgraving/deepposekit)
---
[DeepEthogram](https://github.com/jbohnslav/deepethogram)
---
[SLEAP](https://github.com/murthylab/sleap)
---
[MARS](https://neuroethology.github.io/MARS/)
---
[VAME](https://github.com/LINCellularNeuroscience/VAME) 
---
[B-SOiD](https://github.com/YttriLab/B-SOID)
---
[SMAL](https://smal.is.tue.mpg.de/index.html) 
---
... [and many more!](https://github.com/anl13/animal_papers)
```

These methods all differ in their **user-friendliness** for non-software developers, but also in the techniques used for marker-based or pixel-based **pose estimation**, overall **model architecture**, individual or social **scene complexity**, behavior **clustering method**, use of supervised or unsupervised **machine learning**, and the degree of **self-sufficiency**.

## Fields of research

These methods have been used so far to analyze behavior (ethology) and the link between behavior and neural activity (neuroethology) in animals such as humans, chimpanzees, macaques, cats, mice, rats, bats, octopus, lizards, ants, and many many more.
See for yourself:

<table>
<tbody> <tr> 
<td width=500>
<blockquote class="twitter-tweet" tw-align-center><p lang="en" dir="ltr">First video to come out of my full body chimp <a href="https://twitter.com/hashtag/deeplabcut?src=hash&amp;ref_src=twsrc%5Etfw">#deeplabcut</a> model! Lots of work to do still, but a good start! <a href="https://t.co/74VtQrhHMY">pic.twitter.com/74VtQrhHMY</a></p>&mdash; Charlotte Wiltshire (@Charlotte9080) <a href="https://twitter.com/Charlotte9080/status/1373677768483995648?ref_src=twsrc%5Etfw">March 21, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</td>
<td width=500>
<blockquote class="twitter-tweet" tw-align-center><p lang="en" dir="ltr">Far from perfect, but I labelled only 40 frames, trained the network for 1,5h (5000 iterations) et voilà 🦇🌺amazing tool <a href="https://twitter.com/DeepLabCut?ref_src=twsrc%5Etfw">@DeepLabCut</a> <a href="https://twitter.com/hashtag/deeplabcut?src=hash&amp;ref_src=twsrc%5Etfw">#deeplabcut</a> <a href="https://twitter.com/hashtag/bats?src=hash&amp;ref_src=twsrc%5Etfw">#bats</a> <a href="https://twitter.com/hashtag/batpollination?src=hash&amp;ref_src=twsrc%5Etfw">#batpollination</a> <a href="https://twitter.com/hashtag/markerlessposeestimation?src=hash&amp;ref_src=twsrc%5Etfw">#markerlessposeestimation</a> <a href="https://t.co/NOqK2DKd7d">pic.twitter.com/NOqK2DKd7d</a></p>&mdash; Dr. Ralph Simon (@RalSimon) <a href="https://twitter.com/RalSimon/status/1306234887096143872?ref_src=twsrc%5Etfw">September 16, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</td>
</tr></tbody>
<tbody> <tr> 
<td width=500>
<blockquote class="twitter-tweet" tw-align-center><p lang="en" dir="ltr">Delighted to announce that our 55 point facial landmark model for primates is available on <a href="https://twitter.com/hashtag/deeplabcut?src=hash&amp;ref_src=twsrc%5Etfw">#deeplabcut</a> Model Zoo. <a href="https://t.co/EP6OSR3Z3j">https://t.co/EP6OSR3Z3j</a> <a href="https://t.co/L6RTbWC68J">pic.twitter.com/L6RTbWC68J</a></p>&mdash; Claire Witham (@witham_claire) <a href="https://twitter.com/witham_claire/status/1260526921777020929?ref_src=twsrc%5Etfw">May 13, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</td>
<td width=500>
<blockquote class="twitter-tweet" tw-align-center><p lang="en" dir="ltr">Almost ready for uploading my talk on <a href="https://twitter.com/hashtag/tail?src=hash&amp;ref_src=twsrc%5Etfw">#tail</a> <a href="https://twitter.com/hashtag/biomechanics?src=hash&amp;ref_src=twsrc%5Etfw">#biomechanics</a> in 38 <a href="https://twitter.com/hashtag/lizard?src=hash&amp;ref_src=twsrc%5Etfw">#lizard</a> species for the <a href="https://twitter.com/hashtag/sicb2021?src=hash&amp;ref_src=twsrc%5Etfw">#sicb2021</a>.<br>We use modern markerless tracking techniques <a href="https://twitter.com/hashtag/deeplabcut?src=hash&amp;ref_src=twsrc%5Etfw">#deeplabcut</a> to get the input for our kinematic analyses.<br>⁦<a href="https://twitter.com/Wasatchquatch?ref_src=twsrc%5Etfw">@Wasatchquatch</a>⁩ ⁦<a href="https://twitter.com/cclemente4?ref_src=twsrc%5Etfw">@cclemente4</a>⁩ <a href="https://twitter.com/hashtag/usceduau?src=hash&amp;ref_src=twsrc%5Etfw">#usceduau</a> <a href="https://t.co/IZQQElAdz2">pic.twitter.com/IZQQElAdz2</a></p>&mdash; JojoSchultz (@JojoMimic) <a href="https://twitter.com/JojoMimic/status/1341206398177177600?ref_src=twsrc%5Etfw">December 22, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</td>
</tr></tbody>
<tbody> <tr> 
<td width=500>
<blockquote class="twitter-tweet" tw-align-center><p lang="en" dir="ltr">The <a href="https://twitter.com/hashtag/DeepLabCut?src=hash&amp;ref_src=twsrc%5Etfw">#DeepLabCut</a> workshop is paying off! Thanks <a href="https://twitter.com/TrackingPlumes?ref_src=twsrc%5Etfw">@TrackingPlumes</a> and <a href="https://twitter.com/TrackingActions?ref_src=twsrc%5Etfw">@TrackingActions</a> for your support! Moving behavioral phenotyping in <a href="https://twitter.com/hashtag/stress?src=hash&amp;ref_src=twsrc%5Etfw">#stress</a> <a href="https://twitter.com/hashtag/resilience?src=hash&amp;ref_src=twsrc%5Etfw">#resilience</a> research to a new level! <a href="https://t.co/MLMwSmcFxS">pic.twitter.com/MLMwSmcFxS</a></p>&mdash; Mathias Schmidt (@MathiasVSchmidt) <a href="https://twitter.com/MathiasVSchmidt/status/1082573729568305152?ref_src=twsrc%5Etfw">January 8, 2019</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</td>
<td width=500>
<blockquote class="twitter-tweet" tw-align-center><p lang="en" dir="ltr">1st vids using <a href="https://twitter.com/DeepLabCut?ref_src=twsrc%5Etfw">@DeepLabCut</a> for zombie ant <a href="https://twitter.com/hashtag/biomechanics?src=hash&amp;ref_src=twsrc%5Etfw">#biomechanics</a>! Wasn’t going to pass up a chance to collaborate with <a href="https://twitter.com/CharissaB?ref_src=twsrc%5Etfw">@CharissaB</a> and learn to use <a href="https://twitter.com/hashtag/DeepLabCut?src=hash&amp;ref_src=twsrc%5Etfw">#DeepLabCut</a> ! Thanks <a href="https://twitter.com/shirazi_en?ref_src=twsrc%5Etfw">@shirazi_en</a> for these 1st tries. Hope to get some $ to devote more effort into this!🤞🏼😉 <a href="https://twitter.com/hashtag/UCF?src=hash&amp;ref_src=twsrc%5Etfw">#UCF</a> <a href="https://twitter.com/UCFCECS?ref_src=twsrc%5Etfw">@UCFCECS</a> <a href="https://twitter.com/UCFSciences?ref_src=twsrc%5Etfw">@UCFSciences</a> <a href="https://t.co/59Qk9fLJHU">pic.twitter.com/59Qk9fLJHU</a></p>&mdash; Helen J. Huang (@HelenJHuang) <a href="https://twitter.com/HelenJHuang/status/1184117052409294849?ref_src=twsrc%5Etfw">October 15, 2019</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</td>
</tr></tbody>
<tbody> <tr> 
<td width=500>
<blockquote class="twitter-tweet" tw-align-center><p lang="en" dir="ltr">Procrastinating from writing my PhD thesis by training <a href="https://twitter.com/hashtag/DeepLabCut?src=hash&amp;ref_src=twsrc%5Etfw">#DeepLabCut</a> to follow my friends cats nose around. Tempted to start a cat behavioural lab from home. <a href="https://twitter.com/hashtag/neuroscience?src=hash&amp;ref_src=twsrc%5Etfw">#neuroscience</a> <a href="https://twitter.com/hashtag/CatsOfTwitter?src=hash&amp;ref_src=twsrc%5Etfw">#CatsOfTwitter</a> <a href="https://t.co/aqXvq7eZej">pic.twitter.com/aqXvq7eZej</a></p>&mdash; tom sainsbury (@sainsbury_tom) <a href="https://twitter.com/sainsbury_tom/status/1144236110996004865?ref_src=twsrc%5Etfw">June 27, 2019</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</td>
<td width=500>
<blockquote class="twitter-tweet" tw-align-center><p lang="en" dir="ltr"><a href="https://twitter.com/DeepLabCut?ref_src=twsrc%5Etfw">@DeepLabCut</a> tracking fine motor control on a new level! <a href="https://twitter.com/hashtag/machinelearning?src=hash&amp;ref_src=twsrc%5Etfw">#machinelearning</a> <a href="https://twitter.com/DouglasGWallace?ref_src=twsrc%5Etfw">@DouglasGWallace</a> <a href="https://twitter.com/erickaschaef?ref_src=twsrc%5Etfw">@erickaschaef</a> <a href="https://twitter.com/NABBlackwell?ref_src=twsrc%5Etfw">@NABBlackwell</a> <a href="https://t.co/tJoPPr4NnH">pic.twitter.com/tJoPPr4NnH</a></p>&mdash; Jenna Osterlund Oltmanns (@JennaDoubleO) <a href="https://twitter.com/JennaDoubleO/status/1458689910462980096?ref_src=twsrc%5Etfw">November 11, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</td>
</tr></tbody>
<tbody> <tr> 
<td width=500>
<blockquote class="twitter-tweet" tw-align-center><p lang="en" dir="ltr">Thank you <a href="https://twitter.com/hashtag/DeepLabCut?src=hash&amp;ref_src=twsrc%5Etfw">#DeepLabCut</a> ! (Only 18 frames for annotation)<a href="https://t.co/Kqv9FF6wnG">https://t.co/Kqv9FF6wnG</a> <a href="https://t.co/3omDeI6hvV">pic.twitter.com/3omDeI6hvV</a></p>&mdash; RyoT🐀🐵🔬🖥 (@takeuchi_fr) <a href="https://twitter.com/takeuchi_fr/status/1067726318320545792?ref_src=twsrc%5Etfw">November 28, 2018</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</td>
<td width=500>
<blockquote class="twitter-tweet" tw-align-center><p lang="en" dir="ltr">Oh, you evolved for 600M years to disrupt visual detection? <br>No problem! Thanks to the hard work of <a href="https://twitter.com/TrackingActions?ref_src=twsrc%5Etfw">@TrackingActions</a> and <a href="https://twitter.com/TrackingPlumes?ref_src=twsrc%5Etfw">@TrackingPlumes</a> on <a href="https://twitter.com/DeepLabCut?ref_src=twsrc%5Etfw">@DeepLabCut</a>, we can track octopus!<br><br>PS: Notice the siphon switching sides at the end, insane details! <a href="https://twitter.com/hashtag/deeplabcut?src=hash&amp;ref_src=twsrc%5Etfw">#deeplabcut</a> <a href="https://twitter.com/hashtag/cephalopod?src=hash&amp;ref_src=twsrc%5Etfw">#cephalopod</a> <a href="https://twitter.com/SimonGingins?ref_src=twsrc%5Etfw">@SimonGingins</a> <a href="https://t.co/6vRRMQ4hp3">pic.twitter.com/6vRRMQ4hp3</a></p>&mdash; Eduardo Sampaio (@OctoEduardo) <a href="https://twitter.com/OctoEduardo/status/1156601744228528128?ref_src=twsrc%5Etfw">July 31, 2019</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</td>
</tr></tbody>
<tbody> <tr> 
<td width=500>
<blockquote class="twitter-tweet" tw-align-center><p lang="en" dir="ltr"><a href="https://twitter.com/hashtag/deeplabcut?src=hash&amp;ref_src=twsrc%5Etfw">#deeplabcut</a> is a game changing tool that can automatically track and label the body parts of moving animals. The software works across species and can be applied to any video.<a href="https://t.co/Df1moOPReK">https://t.co/Df1moOPReK</a> <a href="https://t.co/SQmkzWH5YB">pic.twitter.com/SQmkzWH5YB</a></p>&mdash; CLAST (@ColAnimalTech) <a href="https://twitter.com/ColAnimalTech/status/1016655776797089792?ref_src=twsrc%5Etfw">July 10, 2018</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</td>
<td width=500>
<blockquote class="twitter-tweet" tw-align-center><p lang="en" dir="ltr"><a href="https://twitter.com/DeepLabCut?ref_src=twsrc%5Etfw">@DeepLabCut</a> pretty good for 2 hours of training on colab on 19 images, and without any refinement or filtering. THANK YOU <a href="https://twitter.com/TrackingActions?ref_src=twsrc%5Etfw">@TrackingActions</a> <a href="https://twitter.com/TrackingPlumes?ref_src=twsrc%5Etfw">@TrackingPlumes</a> <a href="https://twitter.com/jessy_lauer?ref_src=twsrc%5Etfw">@jessy_lauer</a>! This speed is HUGE for undergraduate research. <a href="https://twitter.com/hashtag/DeepLabCut?src=hash&amp;ref_src=twsrc%5Etfw">#DeepLabCut</a> <a href="https://twitter.com/hashtag/multianimal?src=hash&amp;ref_src=twsrc%5Etfw">#multianimal</a> <a href="https://t.co/ce8V7owFz8">pic.twitter.com/ce8V7owFz8</a></p>&mdash; brandon jackson (@backyardbiomech) <a href="https://twitter.com/backyardbiomech/status/1264588334413877248?ref_src=twsrc%5Etfw">May 24, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</td>
</tr></tbody>
<tbody> <tr> 
<td width=500>
<blockquote class="twitter-tweet" tw-align-center><p lang="en" dir="ltr">DeepLabCut Model Zoo is live!<br><br>Working from home? try out <a href="https://twitter.com/hashtag/deeplabcut?src=hash&amp;ref_src=twsrc%5Etfw">#deeplabcut</a> on your favorite pets, no need to install anything.<br><br>Use custom DeepLabCut Model Zoo <a href="https://twitter.com/GoogleColab?ref_src=twsrc%5Etfw">@GoogleColab</a>  Notebook:<a href="https://t.co/IfUX0ahw6t">https://t.co/IfUX0ahw6t</a> <a href="https://t.co/JsSCAgsl8I">pic.twitter.com/JsSCAgsl8I</a></p>&mdash; Sebastien Hausmann (@SebHausmann) <a href="https://twitter.com/SebHausmann/status/1260637579189288963?ref_src=twsrc%5Etfw">May 13, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</td>
<td width=500>
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">The next post in the series on how to use <a href="https://twitter.com/hashtag/DeepLabCut?src=hash&amp;ref_src=twsrc%5Etfw">#DeepLabCut</a> is out! 🎉 This time on outlier correction.<br><br>3⃣ Refining your DLC model - correct outliers and help your model generalize to new data: <a href="https://t.co/tmPKrxSULv">https://t.co/tmPKrxSULv</a> <br><br>As before, with cool examples and <a href="https://twitter.com/hashtag/jupyternotebooks?src=hash&amp;ref_src=twsrc%5Etfw">#jupyternotebooks</a> provided! <a href="https://t.co/oVCHxcIOKf">https://t.co/oVCHxcIOKf</a> <a href="https://t.co/xJhwGVkIWB">pic.twitter.com/xJhwGVkIWB</a></p>&mdash; Guillermo Hidalgo Gadea (@G_HidalgoGadea) <a href="https://twitter.com/G_HidalgoGadea/status/1394244837411536896?ref_src=twsrc%5Etfw">May 17, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</td>
</tr></tbody>
</table>

:::{admonition} Exercise
:class: warning
Choose one of the Tweets above and try to find out its background. Who posted it? Where does she work? What is her role? Can you find her research online? How has she used DeepLabCut, and what for?

**Skim the web for 10 minutes and present your chosen tweet to the group.**
:::
