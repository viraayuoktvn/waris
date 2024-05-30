import pandas as pd
import numpy as np

# Function: Returns True, if a Value is Numeric
def is_number_value(value):
    return isinstance(value, (int, float, np.int64, np.float64))

# Function: Information Gain Ratio
def info_gain_ratio(target, feature, uniques):
    entropy = 0
    split_info = 0
    ig = 0
    for element in range(0, len(uniques)):
        if is_number_value(uniques[element]):
            probability = len(feature[feature <= uniques[element]]) / len(feature)
        else:
            probability = len(feature[feature == uniques[element]]) / len(feature)
        entropy -= probability * np.log2(probability + np.finfo(float).eps)
        split_info -= probability * np.log2(probability + np.finfo(float).eps)
    ig = entropy
    probability = len(target[target == target.iloc[0]]) / len(target)
    ig *= probability
    split_info += np.finfo(float).eps
    ig /= split_info
    return ig

# Function: C4.5 Algorithm
def dt_c45(Xdata, ydata, target):
    rule = []
    dataset = pd.concat([ydata, Xdata], axis=1)
    uniqueWords = [dataset.iloc[:, j].unique() for j in range(dataset.shape[1])]
    i = 0
    impurity = 0
    branch = [None]*1
    branch[0] = dataset
    gain_ratio = np.empty([1, branch[i].shape[1]])
    root_index = 0
    skip_update = False
    stop = False

    while (i >= 0) and (not stop):
        if (branch[i].shape[0] <= 5) or (len(branch[i][target].unique()) == 1):
            stop = True
            continue

        for j in range(0, branch[i].shape[1] - 1):
            gain_ratio[0, j] = info_gain_ratio(branch[i][target], branch[i].iloc[:, j], uniqueWords[j])

        max_gain_ratio_index = np.argmax(gain_ratio)

        if (skip_update == False):
            i = i + 1
            branch.append(None)
            for value in uniqueWords[max_gain_ratio_index]:
                temp = branch[i - 1][branch[i - 1].iloc[:, max_gain_ratio_index] == value]
                branch[i] = pd.concat([branch[i] if branch[i] is not None else pd.DataFrame(), temp])
                if len(temp) > 0:
                    rule.append("IF " + str(branch[i - 1].columns[max_gain_ratio_index]) + " <= " + str(value) + " THEN ")
                else:
                    mode = temp[target].mode()[0]
                    rule.append("IF " + str(branch[i - 1].columns[max_gain_ratio_index]) + " <= " + str(value) + " THEN " + str(mode) + ";")
            skip_update = False

    for i in range(0, len(branch)):
        if (branch[i] is not None) and (len(branch[i]) > 0):
            mode = branch[i][target].mode()[0]
            if len(rule) > i:
                rule[i] = rule[i] + str(mode) + ";"
            else:
                rule.append(str(branch[i].columns[0]) + " = " + str(branch[i].iloc[0, 0]) + " THEN " + str(mode) + ";")

    return {'rule': rule, 'target': target}

# Function: Train Decision Tree Models
def train_decision_tree_models(X, y):
    models = {}
    for target_column in y.columns:
        model = dt_c45(X, y, target_column)
        models[target_column] = model
    return models

# Load data
data = pd.read_csv("all biner fix.csv", delimiter=";")

# Set features (X) and target variables (y)
X = data[['total_ap', 'total_al', 'total_cp', 'total_cl', 'total_suami', 'total_istri', 'total_ayah', 'total_ibu',
             'total_kakek', 'total_nenek', 'total_si', 'total_sdlk', 'total_sdpk']]
y = data[['hw_ap', 'hw_al', 'hw_cp', 'hw_cl', 'hw_suami', 'hw_istri', 'hw_ayah', 'hw_ibu', 'hw_kakek', 'hw_nenek',
             'hw_si', 'hw_sdlk', 'hw_sdpk']]

# Train Decision Tree Models
models = train_decision_tree_models(X, y)

# Print Results
for target_column, model_info in models.items():
    print(f"Target: {target_column}")
    print("Rule:")
    for r in model_info['rule']:
        print(r)
    print()
