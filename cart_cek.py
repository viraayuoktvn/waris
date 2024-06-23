import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix

def gini_index(column):
    probabilities = column.value_counts(normalize=True)
    gini = 1 - sum(probabilities ** 2)
    return gini

def gini_gain(data, target_name, attribute_name):
    total_gini = gini_index(data[target_name])
    values, counts = np.unique(data[attribute_name], return_counts=True)
    weighted_gini = sum((counts[i] / sum(counts)) * gini_index(data.where(data[attribute_name] == values[i]).dropna()[target_name]) for i in range(len(values)))
    return total_gini - weighted_gini

# Fungsi untuk membuat dan mengevaluasi model decision tree tanpa pre-pruning dan pruning
def decision_tree_without_pruning(X_train, y_train, X_test, y_test):
    dt_classifiers = []
    accuracies = []
    precisions = []
    recalls = []
    gini_indices = {}
    gini_gains = {}
    
    for i in range(y_train.shape[1]):
        dt_classifier = DecisionTreeClassifier(criterion='gini', splitter="best", random_state=42)
        dt_classifier.fit(X_train, y_train.iloc[:, i])
        dt_classifiers.append(dt_classifier)
        y_pred = dt_classifier.predict(X_test)
        accuracy = accuracy_score(y_test.iloc[:, i], y_pred)
        precision = precision_score(y_test.iloc[:, i], y_pred, average="macro")
        recall = recall_score(y_test.iloc[:, i], y_pred, average="macro")
        accuracies.append(accuracy)
        precisions.append(precision)
        recalls.append(recall)

        # Menghitung Gini index untuk target ini
        target_name = y_train.columns[i]
        gini_indices[target_name] = gini_index(y_train.iloc[:, i])
        print(f"Gini index for {target_name}: {gini_indices[target_name]}")  # Debug print

        # Menghitung Gini gain untuk setiap fitur
        gini_gains[target_name] = {attr: gini_gain(pd.concat([X_train, y_train.iloc[:, i]], axis=1), target_name, attr) for attr in X_train.columns}

    model = {}
    for i in range(len(dt_classifiers)):
        model[y.columns[i]] = {'model': dt_classifiers[i], 'features': X.columns.tolist()}

    return dt_classifiers, accuracies, precisions, recalls, gini_indices, gini_gains

# Fungsi untuk membuat dan mengevaluasi model decision tree dengan pre-pruning
def decision_tree_with_prepruning(X_train, y_train, X_test, y_test, max_depth=None, min_samples_split=2):
    dt_classifiers = []
    accuracies = []
    precisions = []
    recalls = []
    gini_indices = {}
    gini_gains = {}

    for i in range(y_train.shape[1]):
        dt_classifier = DecisionTreeClassifier(criterion='gini', splitter="best", max_depth=max_depth,
                                               min_samples_split=min_samples_split, random_state=42)
        dt_classifier.fit(X_train, y_train.iloc[:, i])
        dt_classifiers.append(dt_classifier)
        y_pred = dt_classifier.predict(X_test)
        accuracy = accuracy_score(y_test.iloc[:, i], y_pred)
        precision = precision_score(y_test.iloc[:, i], y_pred, average="macro")
        recall = recall_score(y_test.iloc[:, i], y_pred, average="macro")
        accuracies.append(accuracy)
        precisions.append(precision)
        recalls.append(recall)

        # Menghitung Gini index untuk target ini
        target_name = y_train.columns[i]
        gini_indices[target_name] = gini_index(y_train.iloc[:, i])
        print(f"Gini index for {target_name}: {gini_indices[target_name]}")  # Debug print

        # Menghitung Gini gain untuk setiap fitur
        gini_gains[target_name] = {attr: gini_gain(pd.concat([X_train, y_train.iloc[:, i]], axis=1), target_name, attr) for attr in X_train.columns}

    model = {}
    for i in range(len(dt_classifiers)):
        model[y.columns[i]] = {'model': dt_classifiers[i], 'features': X.columns.tolist()}

    return dt_classifiers, accuracies, precisions, recalls, gini_indices, gini_gains

# Fungsi untuk membuat dan mengevaluasi model decision tree dengan pruning
def decision_tree_with_pruning(X_train, y_train, X_test, y_test, ccp_alpha=0.0):
    dt_classifiers = []
    accuracies = []
    precisions = []
    recalls = []
    gini_indices = {}
    gini_gains = {}

    for i in range(y_train.shape[1]):
        dt_classifier = DecisionTreeClassifier(criterion='gini', splitter="best", ccp_alpha=ccp_alpha, random_state=42)
        dt_classifier.fit(X_train, y_train.iloc[:, i])
        dt_classifiers.append(dt_classifier)
        y_pred = dt_classifier.predict(X_test)
        accuracy = accuracy_score(y_test.iloc[:, i], y_pred)
        precision = precision_score(y_test.iloc[:, i], y_pred, average="macro")
        recall = recall_score(y_test.iloc[:, i], y_pred, average="macro")
        accuracies.append(accuracy)
        precisions.append(precision)
        recalls.append(recall)

         # Menghitung Gini index untuk target ini
        target_name = y_train.columns[i]
        gini_indices[target_name] = gini_index(y_train.iloc[:, i])
        print(f"Gini index for {target_name}: {gini_indices[target_name]}")  # Debug print

        # Menghitung Gini gain untuk setiap fitur
        gini_gains[target_name] = {attr: gini_gain(pd.concat([X_train, y_train.iloc[:, i]], axis=1), target_name, attr) for attr in X_train.columns}

    model = {}
    for i in range(len(dt_classifiers)):
        model[y.columns[i]] = {'model': dt_classifiers[i], 'features': X.columns.tolist()}

    return dt_classifiers, accuracies, precisions, recalls, gini_indices, gini_gains

# Fungsi untuk membuat dan mengevaluasi model decision tree dengan pre-pruning dan pruning
def decision_tree_with_prepruning_pruning(X_train, y_train, X_test, y_test, max_depth=None, min_samples_split=2,
                                          ccp_alpha=0.0):
    dt_classifiers = []
    accuracies = []
    precisions = []
    recalls = []
    gini_indices = {}
    gini_gains = {}

    for i in range(y_train.shape[1]):
        dt_classifier = DecisionTreeClassifier(criterion='gini', splitter="best", max_depth=max_depth,
                                               min_samples_split=min_samples_split, ccp_alpha=ccp_alpha,
                                               random_state=42)
        dt_classifier.fit(X_train, y_train.iloc[:, i])
        dt_classifiers.append(dt_classifier)
        y_pred = dt_classifier.predict(X_test)
        accuracy = accuracy_score(y_test.iloc[:, i], y_pred)
        precision = precision_score(y_test.iloc[:, i], y_pred, average="macro")
        recall = recall_score(y_test.iloc[:, i], y_pred, average="macro")
        accuracies.append(accuracy)
        precisions.append(precision)
        recalls.append(recall)

        # Menghitung Gini index untuk target ini
        target_name = y_train.columns[i]
        gini_indices[target_name] = gini_index(y_train.iloc[:, i])
        print(f"Gini index for {target_name}: {gini_indices[target_name]}")  # Debug print

        # Menghitung Gini gain untuk setiap fitur
        gini_gains[target_name] = {attr: gini_gain(pd.concat([X_train, y_train.iloc[:, i]], axis=1), target_name, attr) for attr in X_train.columns}

    model = {}
    for i in range(len(dt_classifiers)):
        model[y.columns[i]] = {'model': dt_classifiers[i], 'features': X.columns.tolist()}

    return dt_classifiers, accuracies, precisions, recalls, gini_indices, gini_gains

def print_confusion_matrix(y_test, y_pred, column_name, positive_label, negative_label):
    cm = confusion_matrix(y_test, y_pred, labels=[positive_label, negative_label])
    print(f"Confusion Matrix for {column_name}:")
    print(cm)
    tn, fp, fn, tp = cm.ravel()
    print(f"True Positives (TP, {positive_label}): {tp}")
    print(f"True Negatives (TN, {negative_label}): {tn}")
    print(f"False Positives (FP, {negative_label} misclassified as {positive_label}): {fp}")
    print(f"False Negatives (FN, {positive_label} misclassified as {negative_label}): {fn}")

# Load dataset
dataset = pd.read_csv("all biner v3.csv", delimiter=";")

# Set fitur-fitur (X) dan variabel target (y)
X = dataset[['total_ap', 'total_al', 'total_cp', 'total_cl', 'total_suami', 'total_istri', 'total_ayah', 'total_ibu',
             'total_kakek', 'total_nenek', 'total_si', 'total_sdlk', 'total_sdpk']]
y = dataset[['hw_ap', 'hw_al', 'hw_cp', 'hw_cl', 'hw_suami', 'hw_istri', 'hw_ayah', 'hw_ibu', 'hw_kakek', 'hw_nenek',
             'hw_si', 'hw_sdlk', 'hw_sdpk']]

# Membagi dataset menjadi data latih dan data uji
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Decision tree tanpa pre-pruning dan pruning menggunakan Gini impurity
dt_classifiers, accuracies, precisions, recalls, gini_indices, gini_gains = decision_tree_without_pruning(X_train, y_train, X_test, y_test)
for i, dt_classifier in enumerate(dt_classifiers):
    tree_rules = export_text(dt_classifier, feature_names=list(X.columns))
    y_pred = dt_classifier.predict(X_test)
    print(f"Decision Tree Rules for {y.columns[i]} without Pre-pruning and Pruning (Gini impurity):\n", tree_rules)
    print(f"Accuracy for {y.columns[i]} without Pre-pruning and Pruning (Gini impurity):", accuracies[i])
    print(f"Precision for {y.columns[i]} without Pre-pruning and Pruning (Gini impurity):", precisions[i])
    print(f"Recall for {y.columns[i]} without Pre-pruning and Pruning (Gini impurity):", recalls[i])
    print(f"Gini index for {y.columns[i]}: {gini_indices[y.columns[i]]}")

    # Inspecting unique values to determine labels
    unique_values_test = y_test.iloc[:, i].unique()
    unique_values_pred = np.unique(y_pred)
    print(f"Unique values in y_test for {y.columns[i]}: {unique_values_test}")
    print(f"Unique values in y_pred for {y.columns[i]}: {unique_values_pred}")

    # Assuming binary classification, use the first two unique values as labels
    positive_label = unique_values_test[0]
    negative_label = unique_values_test[1]

    print_confusion_matrix(y_test.iloc[:, i], y_pred, y.columns[i], positive_label=positive_label, negative_label=negative_label)

    # Menampilkan Gini gain untuk setiap atribut
    gains = gini_gains[y.columns[i]]
    sorted_gains = sorted(gains.items(), key=lambda item: item[1], reverse=True)
    print(f"Gini gains for {y.columns[i]}:")
    for attr, gain in sorted_gains:
        print(f"{attr}: {gain:.4f}")
    print("\n")

# # Decision tree dengan pre-pruning menggunakan Gini impurity
# dt_classifiers, accuracies, precisions, recalls, gini_indices, gini_gains = decision_tree_with_prepruning(X_train, y_train, X_test, y_test, max_depth=10, min_samples_split=10)
# for i, dt_classifier in enumerate(dt_classifiers):
#     tree_rules = export_text(dt_classifier, feature_names=list(X.columns))
#     y_pred = dt_classifier.predict(X_test)
#     print(f"Decision Tree Rules for {y.columns[i]} with Pre-pruning (Gini impurity):\n", tree_rules)
#     print(f"Accuracy for {y.columns[i]} with Pre-pruning (Gini impurity):", accuracies[i])
#     print(f"Precision for {y.columns[i]} with Pre-pruning (Gini impurity):", precisions[i])
#     print(f"Recall for {y.columns[i]} with Pre-pruning (Gini impurity):", recalls[i])
#     print(f"Gini index for {y.columns[i]}: {gini_indices[y.columns[i]]}")

#     # Inspecting unique values to determine labels
#     unique_values_test = y_test.iloc[:, i].unique()
#     unique_values_pred = np.unique(y_pred)
#     print(f"Unique values in y_test for {y.columns[i]}: {unique_values_test}")
#     print(f"Unique values in y_pred for {y.columns[i]}: {unique_values_pred}")

#     # Assuming binary classification, use the first two unique values as labels
#     positive_label = unique_values_test[0]
#     negative_label = unique_values_test[1]

#     print_confusion_matrix(y_test.iloc[:, i], y_pred, y.columns[i], positive_label=positive_label, negative_label=negative_label)

#     # Menampilkan Gini gain untuk setiap atribut
#     gains = gini_gains[y.columns[i]]
#     sorted_gains = sorted(gains.items(), key=lambda item: item[1], reverse=True)
#     print(f"Gini gains for {y.columns[i]}:")
#     for attr, gain in sorted_gains:
#         print(f"{attr}: {gain:.4f}")
#     print("\n")

# # Decision tree dengan pruning menggunakan Gini impurity
# dt_classifiers, accuracies, precisions, recalls, gini_indices, gini_gains = decision_tree_with_pruning(X_train, y_train, X_test, y_test, ccp_alpha=0.01)
# for i, dt_classifier in enumerate(dt_classifiers):
#     tree_rules = export_text(dt_classifier, feature_names=list(X.columns))
#     y_pred = dt_classifier.predict(X_test)
#     print(f"Decision Tree Rules for {y.columns[i]} with Pruning (Gini impurity):\n", tree_rules)
#     print(f"Accuracy for {y.columns[i]} with Pruning (Gini impurity):", accuracies[i])
#     print(f"Precision for {y.columns[i]} with Pruning (Gini impurity):", precisions[i])
#     print(f"Recall for {y.columns[i]} with Pruning (Gini impurity):", recalls[i])
#     print(f"Gini index for {y.columns[i]}: {gini_indices[y.columns[i]]}")

#     # Inspecting unique values to determine labels
#     unique_values_test = y_test.iloc[:, i].unique()
#     unique_values_pred = np.unique(y_pred)
#     print(f"Unique values in y_test for {y.columns[i]}: {unique_values_test}")
#     print(f"Unique values in y_pred for {y.columns[i]}: {unique_values_pred}")

#     # Assuming binary classification, use the first two unique values as labels
#     positive_label = unique_values_test[0]
#     negative_label = unique_values_test[1]

#     print_confusion_matrix(y_test.iloc[:, i], y_pred, y.columns[i], positive_label=positive_label, negative_label=negative_label)

#     # Menampilkan Gini gain untuk setiap atribut
#     gains = gini_gains[y.columns[i]]
#     sorted_gains = sorted(gains.items(), key=lambda item: item[1], reverse=True)
#     print(f"Gini gains for {y.columns[i]}:")
#     for attr, gain in sorted_gains:
#         print(f"{attr}: {gain:.4f}")
#     print("\n")

# # Decision tree dengan pre-pruning dan pruning menggunakan Gini impurity
# dt_classifiers, accuracies, precisions, recalls, gini_indices, gini_gains = decision_tree_with_prepruning_pruning(X_train, y_train, X_test, y_test, max_depth=10, min_samples_split=10, ccp_alpha=0.01)
# for i, dt_classifier in enumerate(dt_classifiers):
#     tree_rules = export_text(dt_classifier, feature_names=list(X.columns))
#     y_pred = dt_classifier.predict(X_test)
#     print(f"Decision Tree Rules for {y.columns[i]} with Pre-pruning and Pruning (Gini impurity):\n", tree_rules)
#     print(f"Accuracy for {y.columns[i]} with Pre-pruning and Pruning (Gini impurity):", accuracies[i])
#     print(f"Precision for {y.columns[i]} with Pre-pruning and Pruning (Gini impurity):", precisions[i])
#     print(f"Recall for {y.columns[i]} with Pre-pruning and Pruning (Gini impurity):", recalls[i])
#     print(f"Gini index for {y.columns[i]}: {gini_indices[y.columns[i]]}")

#     # Inspecting unique values to determine labels
#     unique_values_test = y_test.iloc[:, i].unique()
#     unique_values_pred = np.unique(y_pred)
#     print(f"Unique values in y_test for {y.columns[i]}: {unique_values_test}")
#     print(f"Unique values in y_pred for {y.columns[i]}: {unique_values_pred}")

#     # Assuming binary classification, use the first two unique values as labels
#     positive_label = unique_values_test[0]
#     negative_label = unique_values_test[1]

#     print_confusion_matrix(y_test.iloc[:, i], y_pred, y.columns[i], positive_label=positive_label, negative_label=negative_label)

#     # Menampilkan Gini gain untuk setiap atribut
#     gains = gini_gains[y.columns[i]]
#     sorted_gains = sorted(gains.items(), key=lambda item: item[1], reverse=True)
#     print(f"Gini gains for {y.columns[i]}:")
#     for attr, gain in sorted_gains:
#         print(f"{attr}: {gain:.4f}")
#     print("\n")
