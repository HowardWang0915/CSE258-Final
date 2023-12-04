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
- length of `reivew/text`

The _MSE_ on the test set is **0.00523**.


### Best feature
This model only considers the most correlated feature, i.e. `review/taste` when training.

The _MSE_ on the test set is **0.01004**.


### BERT embeddings
We turn the length of the `review/text` into embeddings from BERT to train our regressor only with the embeddings.

The _MSE_ on the test set is **0.013395**.

### Reviews with BERT embeddings
Fusing the four review ratings and the BERT embeddings of the `review/text` to train our regressor.

The _MSE_ on the test set is **0.004967**.
