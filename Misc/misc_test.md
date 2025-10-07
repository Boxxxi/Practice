## 1
```python
def create_equiwidth_bins(float_list: list[float], n_bins: int=10):
    float_list = sorted(float_list)

    min_num, max_num = float_list[0], float_list[-1]
    interval_size = (max_num - min_num) / n_bins

    bin_counts = {}
    for i in range(n_bins):
        min_interval = min_num + i * interval_size
        max_interval = min_num + (i + 1) * interval_size
        bin_counts[(min_interval, max_interval)] = len(x for x in float_list if min_interval <= x < max_interval)
        if i == n_bins - 1:
            bin_counts[(min_interval, max_interval)] += len(x for x in float_list if x == max_interval)

    return bin_counts
```

## 2
I don't know this

## 3
```python
import math

def calculate_pearson_correlation(X, Y):
    n = len(X)
    sum_X = sum(X)
    sum_Y = sum(Y)
    sum_X_squared = sum(x ** 2 for x in X)
    sum_Y_squared = sum(y ** 2 for y in Y)
    sum_XY = sum(X[i] * Y[i] for i in range(n))
    numerator = n * sum_XY - sum_X * sum_Y
    denominator = math.sqrt((n * sum_X_squared - sum_X ** 2) * (n * sum_Y_squared - sum_Y ** 2))
    correlation = numerator / denominator
    return correlation
```

## 4
### Definitions and given information
- Sensitivity = TP / (TP + FN) (Proportion of actual diseased that are tested positive)
- Specificity = TN / (TN + FP) (Proportion of actual non-diseased that are tested negative)
- TP - Predicted positives that are actually positive
- FN - Predicted negatives that are actually positive
- TN - Predicted negatives that are actually negative
- FP - Predicted positives that are actually negative
- $P(D) = 0.01$ (Probability of disease)
- $P(T)$ (Probability of a positive test results)
- $P(T|D)$ (Probability of a positive test result given that person actually has the disease)
#### Probabilitic definition of sensitivity and specificity:
- Sensitivity $= 0.90 = P(T|D) / P(D) \implies P(T|D) = 0.0090$
- Specificity $= 0.95 = P(\sim T|\sim D) / P(\sim D) \implies = P(\sim T|\sim D) = 0.9405$

### Solution
$$
\begin{align*}
P(T) &= P(T|D) * P(D) + P(T|\sim D) * P(\sim D) \\
&= P(T|D) * P(D) + (1 - P(\sim T|\sim D)) * (1 - P(D)) \\
&= 0.0090 * 0.01 + (1 - 0.9405) * (1 - 0.01) \\
&= 0.058995
\end{align*}
$$

By Bayes' theorem:
$$P(D|T) = P(T|D) * P(D) / P(T) = 0.0090 * 0.01 / 0.058995 = 0.0015 = 0.15 \%$$


## 5
```python
def create_linear_regression_model(X: list[list[int]], y: list[int], early_stopping: int=10, learning_rate: float=0.01):
    m, b = 0, y[0]
    num_data = len(X)
    early_stopping = 10

    def calculate_mse(m, b):
        return sum((y[i] - (m * X[i] + b)) ** 2 for i in range(num_data)) / num_data

    prev_mse = float("inf")
    while N < 100 or early_stopping > 0:
        mse = calculate_mse(m, b)
        m_gradient = -2 * sum(X[i] * (y[i] - (m * X[i] + b)) for i in range(num_data)) / num_data
        b_gradient = -2 * sum(y[i] - (m * X[i] + b) for i in range(num_data)) / num_data

        m -= learning_rate * m_gradient
        b -= learning_rate * b_gradient
        if N % 10 == 0:
            print(f"Iteration {N}: m = {m}, b = {b}, MSE = {mse}")

        if (prev_mse - mse) / prev_mse < 0.0001:
            early_stopping -= 1
            if early_stopping == 0:
                print(f"Early stopping at iteration {N}")
        else:
            early_stopping = 10
        prev_mse = mse
        N += 1
    return m, b
```

## 6
Definition of bias in a model is the difference between the predicted values and the actual values. For a low bias model, the predicted values are close to the actual values. For a high bias model, the predicted values are far from the actual values.

Definition of variance in a model is the variability of the predicted values. For a low variance model, the predicted values are close to each other. For a high variance model, the predicted values are far from each other.

The concept of Bias-Variance trade-off arises from the fact that a model that always outputs a constant value has zero variance (the perfect low variance model), but that would have a very high bias. Addition of parameters to the model would introduce variability in the predictions, and lead to increase in variance. But increasing the parameters, would give us closer predictions to the actual values on the training dataset, therefore reducing the bias of the model. Finally if we introduce as many parameters as the number of data points itself, we can easily create a polynomial model that perfectly fits the training data (the perfect low bias model), but would have very high variance. Hence, when we try to reduce the bias of a model in training, we invariably increase the variance of the model and vice-versa.


## 7
Accuracy can be misleading when the data is imbalanced. For example, assuming a dataset where only 1% od the data is positive; and consider an ML model that predicts everything as negative. In this case the model has an accuracy of 99%, but given the objective of actually identifying the positives, it is a very poor model.

## 8
AUPRC is the area under the precision-recall curve; while AUROC is the area under the ROC curve. The difference between the 2 curves are that the y-axis of the ROC curve is the true positive rate (TPR) while the y-axis of the precision-recall curve is the precision. The X-axis in both cases is false positive rate (FPR - also called recall).

Consider the case where the data has 50 positive samples and 50 negative samples. Assume the model outputs probabilities of 0.7 for all samples except 10 negative sample for which it predicts 0.3. Then, we can calculate AUROC and AUPRC as:

- At probability threshold 0.3
  - TPR = True Positives / Actual Positives = 
  - FPR = False Positives / Actual Negatives = 5 / 5 = 1
  - Precision = True Positives / Predicted Positives = 95 / 100 = 0.95
- At probability threshold 0.7
  - TPR = True Positives / Actual Positives = 95 / 95 = 1
  - FPR = False Positives / Actual Negatives = 4 / 5 = 0.8
  - Precision = True Positives / Predicted Positives = 95 / 99 = ~0.95

Therefore, AUROC = 1, AUPRC = 0.97.


## 9
The geometric meaning of a dot product between 2 unit vectors is the cosine of the angle between the 2 vectors. In case of non-unit vectors, we simply multiply the magnitude of the length of the vectors to the cosine value. In a way it is a number representing the angular distance between the 2 vectors. If the vectors point approximately towards the same direction, the dot product will be large while if they point in opposite directions, the dot product will be small.

The dot product is zero when the vectors are perpendicular or orthogonal to each other ($\cos90\degree = 0$). In machine learning, this helps us tremendously in dimensionality reduction algorithms, where we can use the dot product to figure out which basis variables (in a lower dimension) captures the highest variance in the data, and use them further in our analysis. Similarly, dot products are the core of gradient descent algorithms.

## 10
To do PCA, we take the covariance matrix of the high-dimensional data, and then we perform eigenvalue decomposition on it to get eigenvectors and eigenvalues. The eigenvectors are the principal components of the data (or the basis vectors corresponding to the eigenvalues) and the eigenvalues are the variances of the data along those principal components. Now to select the top k principal components, we sort eigenvalues in decreasing order and select the top k corresponding eigenvectors as the basis vectors (as these are the principal components explaining the most variance in the data).

## 11
Preprocessing steps:
- Convert timezones to UTC, then to timeinmillis
- For duplicate transaction IDs, compare information presence in each duplicate transaction, and create one single clean row combining all the information (take the most frequent value of the column in case of inconsistency), then drop duplicate transaction ID, keeping only the clean row.
- In case of missing values still being present, there can be different ways of handling them based on the definition of the column, or its nature (categorical/ordinal/continuous). For categorical columns, creating dummy variables is a good idea. For ordinal and continuous columns, KNN-based imputation can be used.
- Additional: Since it seems the data is transactional, if the rows have a transaction amount and a balance column, these 2 could be used along with timeinmillis to create more accurate null value imputation in either column.

## 12
High training accuracy but low test accuracy could be because of the model over-fitting on the training data. Over-fitting can happen for the following reasons - 
- High number of parameters (This can be tested by dropping parameters from the model and fitting the model again, and then comparing the effects on training and testing accuracy, or an l1-regularized model can be fitted and the performances compared to the original model)
- High variance in the data (This can be tested by fitting the model on multiple subsets of the data, and then comparing the effects on training and testing accuracy. K-fold cross validation approach can also be used to create the model and performances can be compared)
- High number of outliers in the data (This can be tested by fitting the model on the data without the outliers, and then comparing the effects on training and testing accuracy)
