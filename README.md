# CSE258 Assignment2
[Link](https://cseweb.ucsd.edu/classes/fa23/cse258-a/slides/assignment2_fa23.pdf) to assignment slides.
## Setup
To download the beer data, run
```bash
sh setup.sh
```
To setup your python environment, run
```bash
pip install -r requirements.txt
```

> :warning: It is recommended to install your own PyTorch from this [link](https://pytorch.org/get-started/locally/)

To load the data into a pickle file, run
```bash
python helpers/load.py -c NUM
```
where `NUM` is the number of data you intended to load. Because this is a large dataset, choose the number wisely otherwise your computer might crash like mine :(.

## Run
To run Exploratory data analysis, run
```bash
python src/EDA.py
```

To run review text analysis, run:
```bash
python src/review_text_analysis.py
```

# TODOs
- [ ] Identify Dataset to study and describe its basic properties
- [ ] Identify a predictive task on this dataset and describe the features that will be relevant to it
- [ ] Describe what model/s you will use to solve this task
- [ ] Describe literature & research relevant to the dataset and task
- [ ] Describe and analyze results

# Dataset
## EDA
# Predictive Tasks
# Model

# Relavent leterature
[1] Li, Yang, et al. "Recent Developments in Recommender Systems: A Survey." arXiv preprint arXiv:2306.12680 (2023). [link](https://arxiv.org/pdf/2306.12680.pdf)
[2] Wu, Likang, et al. "A Survey on Large Language Models for Recommendation." arXiv preprint arXiv:2305.19860 (2023). [link](https://arxiv.org/pdf/2305.19860.pdf)

# Results
