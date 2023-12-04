# Analysis Results

## Analysis

## Regressor
For all experiemnts, we adopted the `LinearRegression()` from `scikit-learn`. As for the evaluation metric, we utilized the MSE (mean squared error) as our evaluation metric.

### Baseline
The baseline model is trained with the following features:

- `review/taste`
- `review/aroma`
- `review/appearance`
- `review/palate`


### Best feature
This model only considers the most correlated feature, i.e. `review/taste` when training.


### Reviews with BERT embeddings
We also added the `review/text` embeddings from BERT to train our regressor.

