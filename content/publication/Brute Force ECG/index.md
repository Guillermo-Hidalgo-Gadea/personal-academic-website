---
title: "Brute Force ECG Feature Extraction Applied on Discomfort Detection"

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here 
# and it will be replaced with their full name and linked to their profile.
authors:
- admin
- Annika Kreuder
- Carsten Stahlschmidt
- Sebastian Schnieder
- Jarek Krajewski

# Author notes (optional)
#author_notes:
#- "Equal contribution"
#- "Equal contribution"

date: "2019-01-01"
doi: "https://doi.org/10.1007/978-3-319-91211-0_33"

# Schedule page publish date (NOT publication's date).
publishDate: ""

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["1"]

# Publication name and optional abbreviated publication name.
publication: Information Technology in Biomedicine
publication_short: 

abstract: This paper presents the idea of brute force feature extraction for Electrocardiography (ECG) signals applied to discomfort detection. To build an ECG Discomfort Corpus an experimental discomfort induction was conducted. 50 subjects underwent a 2 h (dis-)comfort condition in separate sessions in randomized order. ECG and subjective discomfort was recorded. 5 min ECG segments were labeled with corresponding subjective discomfort ratings, and 6365 brute force features (65 low-level descriptors, first and second order derivatives, and 47 functionals) and 11 traditional heart rate variability (HRV) parameters were extracted. Random Forest machine learning algorithm outperformed SVM and kNN approaches and achieved the best subject-dependent, 10-fold cross-validation results (\r=.51\). With this experiment, we are able to show that (a) brute force ECG feature sets achieved better discomfort detection than traditional HRV based ECG feature set; (b) cepstral and spectral flux based features appear to be the most promising to capture HRV phenomena.


tags: []

# Display this page in the Featured widget?
featured: true

# Custom links (uncomment lines below)
# links:
# - name: Custom Link
#   url: http://example.org

url_pdf: 'https://www.researchgate.net/publication/325605196_Brute_Force_ECG_Feature_Extraction_Applied_on_Discomfort_Detection#fullTextFileContent'
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
image:
  caption: 
  focal_point: ""
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
#projects:

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
#slides: 
---