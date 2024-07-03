# Machine learning functions
The machine learning plugin provides machine learning functionality as an aggregation function. It enables you to train Support Vector Machine (SVM) based classifiers and regressors for the supervised learning problems.
> **Note:** The machine learning functions are not optimized for distributed processing.The capability to train large data sets is limited by the execution of the final training on a single instance.

## Feature vector

### **`features()`**

| Function                   | Description                                                                                                                          | Return Type |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| `features(values...)`      | Constructs a feature vector from the given numerical values. Each value corresponds to a feature at the respective index in the map. | map<int, double> |

Example:
```sql
SELECT features(1.0, 2.0, 3.0) AS features;
    ---features
-----------------------
 {0=1.0, 1=2.0, 2=3.0}
```


## Classification
The function to train a classification model looks like as follows:
```sql
SELECT
  learn_classifier(
    species,
    features(sepal_length, sepal_width, petal_length, petal_width)
  ) AS model
FROM
  iris

#output:
                      model
-------------------------------------------------
 3c 43 6c 61 73 73 69 66 69 65 72 28 76 61 72 63
 68 61 72 29 3e
```
The trained model can not be saved natively, and needs to be passed in the format of a nested query:
```sql
SELECT
  classify(features(5.9, 3, 5.1, 1.8), model) AS predicted_label
FROM (
  SELECT
    learn_classifier(species, features(sepal_length, sepal_width, petal_length, petal_width)) AS model
  FROM
    iris
) t

#output:
 predicted_label
-----------------
 Iris-virginica
```

## Regression
The following code shows the creation of the model predicting sepal_length from the other 3 features:
```sql
SELECT
  learn_regressor(sepal_length, features(sepal_width, petal_length, petal_width)) AS model
FROM
  iris
  
#or

SELECT
  regress(features(3, 5.1, 1.8), model) AS predicted_target
FROM (
  SELECT
    learn_regressor(sepal_length, features(sepal_width, petal_length, petal_width)) AS model
  FROM iris
) t;
#output:
 predicted_target
-------------------
 6.407376822560477
``` 



## Machine learning functions
### **`features()`**
| Function                | Description                                          | Return Type            |
| ----------------------- | ---------------------------------------------------- | ---------------------- |
| `features(double, ...)`| Constructs a feature vector as a map of indices to values. | feature vector (map<bigint, double>) |

### **`learn_classifier()`**
| Function                        | Description                                                      | Return Type  |
| ------------------------------- | ---------------------------------------------------------------- | ------------ |
| `learn_classifier(label, features)` | Trains an SVM-based classifier model with the given label and feature datasets. | `Classifier` |


### **`learn_libsvm_classifier()`**

| Function                                    | Description                                                      | Return Type  |
| ------------------------------------------- | ---------------------------------------------------------------- | ------------ |
| `learn_libsvm_classifier(label, features, params)` | Trains an SVM-based classifier model with the given label and feature datasets, controlling the training process by libsvm parameters. | `Classifier` |

### **`classify()`**

| Function                    | Description                                                      | Return Type  |
| --------------------------- | ---------------------------------------------------------------- | ------------ |
| `classify(features, model)` | Predicts a label using the given classifier SVM model.          | `label`      |

### **`learn_regressor()`**

| Function                              | Description                                                      | Return Type  |
| ------------------------------------- | ---------------------------------------------------------------- | ------------ |
| `learn_regressor(target, features)`   | Trains an SVM-based regressor model with the given target and feature datasets. | `Regressor`  |

### **`leearn_libsvm_regressor()`**

| Function                                      | Description                                                      | Return Type  |
| --------------------------------------------- | ---------------------------------------------------------------- | ------------ |
| `learn_libsvm_regressor(target, features, params)` | Trains an SVM-based regressor model with the given target and feature datasets, controlling the training process by libsvm parameters. | `Regressor`  |

### **`regress()`**

| Function                    | Description                                                      | Return Type  |
| --------------------------- | ---------------------------------------------------------------- | ------------ |
| `regress(features, model)` | Predicts a target value using the given regressor SVM model.    | `target`     |



