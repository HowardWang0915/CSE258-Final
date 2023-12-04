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
python src/helpers/load.py -c NUM -p PATH
```
where `NUM` is the number of data you intended to load, and `PATH` is the path where the `json.gz` file is located. Put your data in your `data/` folder so that it will be commited to github.

## Run
To run Exploratory data analysis, run
```bash
python src/EDA.py
```

To run BERT embeddings:
```bash
python src/bert_embeds.py --path <data_path>
```

To run predictive task:
```bash
python src/predictive.py --data-path <data_path> --embed_path <embed_path> --embed_mode <bert|bow>
```

# TODOs
- [ ] Identify Dataset to study and describe its basic properties
- [ ] Identify a predictive task on this dataset and describe the features that will be relevant to it
- [ ] Describe what model/s you will use to solve this task
- [ ] Describe literature & research relevant to the dataset and task
- [ ] Describe and analyze results

### Data Anaylsis
- [ ] Insight report

### Regressor
- [x] ~Best feature (review/taste)~
- [x] ~5 Ratings (review/taste, review/aroma, review/apperence, review/palate, length of review/text)~
- [x] ~5 Ratings + BERT embeddings~
- [ ] 5 Ratings + BoW embeddings
- [x] ~BERT embeddings only~
- [ ] BoW embeddings only

### Literature
- [ ] 2 - 3 sentence per lietrature

# Dataset
## EDA
# Predictive Tasks
# Model

# Relavent literature
[1] Li, Yang, et al. "Recent Developments in Recommender Systems: A Survey." arXiv preprint arXiv:2306.12680 (2023). [link](https://arxiv.org/pdf/2306.12680.pdf)

[2] Wu, Likang, et al. "A Survey on Large Language Models for Recommendation." arXiv preprint arXiv:2305.19860 (2023). [link](https://arxiv.org/pdf/2305.19860.pdf)

[3] Fan, Wenqi, et al. "Recommender systems in the era of large language models (llms)." arXiv preprint arXiv:2307.02046 (2023). [link](https://arxiv.org/pdf/2307.02046.pdf)

[4] Dezfouli, Parisa Abolfath Beygi, Saeedeh Momtazi, and Mehdi Dehghan. "Deep neural review text interaction for recommendation systems." Applied Soft Computing 100 (2021): 106985. [link](https://pdf.sciencedirectassets.com/272229/1-s2.0-S1568494620X00147/1-s2.0-S1568494620309248/main.pdf?X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCID4Uh6habjBZ3X5OvOMTAhS1T8I73T%2FawcFYiD2iaMtEAiEA9oGKS7hWUViTBy7m8oHj2EPRriBb4AikIX2iSK7ATLUqsgUIPhAFGgwwNTkwMDM1NDY4NjUiDP7omEkFQjjLkjIhmyqPBXp8Y5GJDAi%2B%2BU2Vr0ZSVFiTxCTcnli2sP89rAjD8WYDt%2B2Xw4ZQgZTjX8O6o3ORQPMYRG073GwIjjC9Me6%2BFxKymyG3bwvAnOOj8XZX7dTrHdl9Rf%2BAbiYYLOcSrD72GuksBIOYWEx7NJxk13SmJOkhu8Vl5JXbPaEpZhR4nlYSOyD4ExuqUh1CVum1z4lswDZQQgzyPdWOOxDk%2BI1Oe1omhlkXsQlOANBTsfFoJb%2FI57KCvweaNhFYNLQ%2FGteYYVRUOpZZneQhkOzJYVsS5nr%2BqUK3gpqGID17iIPcfLPtUh29LolRHW9IUJ5zj0nwnZAOaDwAP%2BvEO2WfCgojtomoUQWUWD4V20SLu%2BEmjSIqC8jgEsFxz8PzoBNVtvR3MnQigw0Q7qaPqnxjxGAz9OEEiLBXBSpJHPc4SqhDTTh7meis%2BI5Xe6NxMOqdyzGu1BTAtYZDU3IxRwavMUDltildwYR9nOOmhsjQ8rRBROVrc5CqQCWtH8ViSVPPXJDs1UuX1ydneE%2Fzf2nWQYfy4E53j0q4rqbCtEKTaocOE4jI1zzfAxvgWmlqs9jLsVtxBgZm1jamk9W37sHmZ5NqK4bRs75GSOtsnx373CTKlNuy5oXjlQoHN1dKFqO3beezqQuMSdOSf9qDML2Uz%2FAYxDxTElAgd111xaeFieftJ3O1QVqpqRAe4WuxreV1oTBPxM4pp7yKTB6lgroFIZEr0ikcNrMDrYnAKNuInF%2Bdj13p3ObNnQQ%2FDDEb6V8XhIqZyUp5VknU%2BYLmAPqnDe66WiUPUc%2Fg6Ptc0MeejLQvaWHaX%2FNsTF%2FX2KKoOzWKYXtfubvdDlgzKI7WTgzkpTtHmkKiETw7WE0uKjaWOUibq1kwwpCwqwY6sQHpFzVOYqPrIvUhxQMbFwOzyo%2BHgyMsbaKFTdIq%2B3PRdckOXBcpzcK%2BXq1KXiLG1MpF2xvPYk4F05QHLCHcW527hlCTgIe4H%2B7adUBapEyRJBQQ4OSMad3XyzBG2RQESXf5U9FU7EHaTXelvoYU9XbHUmiXKCjXtljYSk9u3FBTlcVemolZofejjC6EovtQmRQC2bFSbY5rFNUFk%2Fdd1FSq6tF8%2BUkl%2FC5Dmr%2Bebmpj0PA%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231203T055514Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIAQ3PHCVTY6GCOWTM6%2F20231203%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=838f726336091b59ca29ef387c6a4b41527efb12d154fd931e861c72f93fdc93&hash=9b108a72c1b5239a525f656fa2dfae55617893328fc1a50363cb30a99490c5df&host=68042c943591013ac2b2430a89b270f6af2c76d8dfd086a07176afe7c76c2c61&pii=S1568494620309248&tid=spdf-ea04bd1d-5ae1-4bfd-b21d-82f7e5c1b5bd&sid=331f1ec74526f844c51b1c97d8ffef2cda5bgxrqa&type=client&tsoh=d3d3LnNjaWVuY2VkaXJlY3QuY29t&ua=0f135855065756045508&rr=82f98f3f4e152f67&cc=us)

# Results
