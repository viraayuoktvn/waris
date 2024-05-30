import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# Function: Returns True, if a Value is Numeric
def is_number_value(value):
    if isinstance(value, str):  
        return False  # All string values are considered non-numeric
    return True  # Non-string values are considered numeric

# Function: Information Gain Ratio
def info_gain_ratio(target, feature):
    entropy = 0
    split_info = 0
    ig = 0
    for value in feature.iloc[:, 0].unique():
        probability = len(feature[feature.iloc[:, 0] == value]) / len(feature)
        entropy -= probability * np.log2(probability + np.finfo(float).eps)
        split_info -= probability * np.log2(probability + np.finfo(float).eps)
    ig = entropy
    probability = len(target[target == target.iloc[0]]) / len(target)
    ig *= probability
    split_info += np.finfo(float).eps
    ig /= split_info
    return ig

# Function: Decision Tree C4.5 Algorithm
def dt_c45(Xdata, ydata, target, cat_missing="none", num_missing="none", pre_pruning="none", chi_lim=0.1, min_lim=5):
    rule = []
    gain_ratio = np.zeros((1, Xdata.shape[1]))
    
    i = 0
    impurity = 0
    branch = [None] * 1
    branch[0] = Xdata
    root_index = 0
    stop = 2
    
    skip_update = False
    
    while (i < stop):
        impurity = np.amax(gain_ratio)
        gain_ratio.fill(0)
        for element in range(1, branch[i].shape[1]):
            if len(branch[i]) == 0:
                skip_update = True 
                break
            if branch[i].iloc[:, element].nunique() == 1:
                if ";" not in rule[i]:
                    rule[i] = rule[i] + " THEN " + target + " = " + branch[i].iloc[0, 0] + ";"
                    rule[i] = rule[i].replace(" AND  THEN ", " THEN ")
                skip_update = True
                break
            if i > 0 and is_number_value(Xdata.iloc[:, element-1]):
                gain_ratio[0, element] = 0.0
                value = np.sort(branch[i].iloc[:, element].unique())
                skip_update = False
                if (branch[i].iloc[:, element] == value[0]).sum() > 1:
                    start = 0
                    finish = len(branch[i].iloc[:, element].unique()) - 2
                else:
                    start = 1
                    finish = len(branch[i].iloc[:, element].unique()) - 2
                if len(branch[i]) == 2 or len(value) == 1 or len(value) == 2:
                    start = 0
                    finish = 1
                if len(value) == 3:
                    start = 0
                    finish = 2
                for bin_split in range(start, finish):
                    bin_sample = branch[i][branch[i].iloc[:, element] <= value[bin_split]]
                    if len(bin_sample) == 0:  # Handle empty branch
                        continue
                    # Check if branch index is valid
                    if len(ydata.iloc[bin_sample.index]) > 0:
                        igr = info_gain_ratio(target=ydata.iloc[bin_sample.index, 0], feature=Xdata.iloc[bin_sample.index, :])
                        if igr > float(gain_ratio[0, element]):
                            gain_ratio[0, element] = igr
            if i > 0 and not is_number_value(Xdata.iloc[:, element-1]):
                gain_ratio[0, element] = 0.0
                skip_update = False
                # Check if branch index is valid
                if len(ydata.iloc[branch[i].index]) > 0:
                    igr = info_gain_ratio(target=ydata.iloc[branch[i].index, 0], feature=pd.DataFrame(branch[i].iloc[:, element]))
                    gain_ratio[0, element] = igr

        if skip_update == False:
            root_index = np.argmax(gain_ratio)
            rule.append("IF " + branch[i].columns[root_index] + " <= " + str(np.sort(branch[i][branch[i].columns[root_index]].unique())[1]) + ";")
            newBranch = []
            for z in range(1, len(np.sort(branch[i][branch[i].columns[root_index]].unique()))):
                newBranch = branch[i][branch[i][branch[i].columns[root_index]] <= np.sort(branch[i][branch[i].columns[root_index]].unique())[z]]
                branch.append(newBranch)
            stop = len(branch)
        skip_update = False
        i = i + 1

    while ";" not in rule[-1]:
        rule.pop(-1)

    model = {"rule": rule, "target": target}
    return model

# Function: Predict with Decision Tree Model
def predict_with_model(X_test, model):
    predictions = []
    for _, instance in X_test.iterrows():
        rule = model['rule']
        target = model['target']
        for r in rule:
            condition = r.split(" IF ")[1].split(" ")[0]
            value = float(r.split(" <= ")[1].split(";")[0])
            if instance[condition] <= value:
                prediction = r.split(" THEN ")[1].split(" = ")[1].split(";")[0]
                predictions.append(prediction)
                break
    return predictions

# Function: Calculate Accuracy
def calculate_accuracy(y_true, y_pred):
    correct = 0
    for i in range(len(y_true)):
        if y_true[i] == y_pred[i]:
            correct += 1
    return correct / float(len(y_true))

# Function: Calculate Precision
def calculate_precision(y_true, y_pred):
    true_positive = sum(1 for true, pred in zip(y_true, y_pred) if true == pred == 1)
    predicted_positive = sum(1 for pred in y_pred if pred == 1)
    return true_positive / predicted_positive if predicted_positive > 0 else 0

# Function: Calculate Recall
def calculate_recall(y_true, y_pred):
    true_positive = sum(1 for true, pred in zip(y_true, y_pred) if true == pred == 1)
    actual_positive = sum(1 for true in y_true if true == 1)
    return true_positive / actual_positive if actual_positive > 0 else 0

# Function: Train and Evaluate Decision Tree Models
def train_and_evaluate_models(X_train, y_train, X_test, y_test, target_column, pruning="none", pre_pruning="none"):
    if not isinstance(y_train, pd.Series):
        raise ValueError("y_train should be a Series.")

    if pruning == "after":
        model = dt_c45(X_train, y_train, target_column)  # Perbaikan disini
    elif pruning == "before":
        model = dt_c45(X_train, y_train, target_column, pre_pruning=pre_pruning)  # Perbaikan disini
    else:
        raise ValueError("Invalid pruning method specified.")

    # Evaluate the model using test data
    y_pred = predict_with_model(X_test, model)  # Update function call
    accuracy = calculate_accuracy(y_test, y_pred)
    precision = calculate_precision(y_test, y_pred)
    recall = calculate_recall(y_test, y_pred)

    return model, accuracy, precision, recall

# Load data
data = pd.read_csv("all biner fix.csv", delimiter=";")

# Set features (X) and target variables (y)
X = data[['total_ap', 'total_al', 'total_cp', 'total_cl', 'total_suami', 'total_istri', 'total_ayah', 'total_ibu',
             'total_kakek', 'total_nenek', 'total_si', 'total_sdlk', 'total_sdpk']]
y = data[['hw_ap', 'hw_al', 'hw_cp', 'hw_cl', 'hw_suami', 'hw_istri', 'hw_ayah', 'hw_ibu', 'hw_kakek', 'hw_nenek',
             'hw_si', 'hw_sdlk', 'hw_sdpk']]

# Bagi data menjadi set pelatihan dan pengujian
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train and Evaluate Decision Tree Models with Pruning
models_with_pruning = {}
for target_column in y.columns:
    model, accuracy, precision, recall = train_and_evaluate_models(X_train, y_train[target_column], X_test, y_test[target_column], target_column, pruning="after")
    models_with_pruning[target_column] = {"model": model, "accuracy": accuracy, "precision": precision, "recall": recall}

# Train and Evaluate Decision Tree Models with Pre-Pruning
models_with_pre_pruning = {}
for target_column in y.columns:
    model, accuracy, precision, recall = train_and_evaluate_models(X_train, y_train[target_column], X_test, y_test[target_column], target_column, pre_pruning="before")
    models_with_pre_pruning[target_column] = {"model": model, "accuracy": accuracy, "precision": precision, "recall": recall}

# Train and Evaluate Decision Tree Models with Pruning and Pre-Pruning
models_with_both = {}
for target_column in y.columns:
    model, accuracy, precision, recall = train_and_evaluate_models(X_train, y_train[target_column], X_test, y_test[target_column], target_column, pruning="after", pre_pruning="before")
    models_with_both[target_column] = {"model": model, "accuracy": accuracy, "precision": precision, "recall": recall}

# Print Results
def print_model_and_metrics(models, pruning_info):
    for target_column, model_info in models.items():
        print(f"Decision Tree Rules for {target_column} {pruning_info}:")
        for r in model_info['model']['rule']:
            print(r)
        print(f"Accuracy for {target_column} {pruning_info}: {model_info['accuracy']:.2f}")
        print(f"Precision for {target_column} {pruning_info}: {model_info['precision']:.2f}")
        print(f"Recall for {target_column} {pruning_info}: {model_info['recall']:.2f}")
        print()

print("Decision Tree Models with Pruning:")
print_model_and_metrics(models_with_pruning, "with Pruning (Information Gain)")

print("Decision Tree Models with Pre-Pruning:")
print_model_and_metrics(models_with_pre_pruning, "with Pre-Pruning (Information Gain)")

print("Decision Tree Models with Pruning and Pre-Pruning:")
print_model_and_metrics(models_with_both, "with Pruning and Pre-Pruning (Information Gain)")
