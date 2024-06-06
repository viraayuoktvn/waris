import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.metrics import accuracy_score, precision_score, recall_score

# Fungsi untuk membuat dan mengevaluasi model decision tree tanpa pre-pruning dan pruning
def decision_tree_without_pruning(X_train, y_train, X_test, y_test):
    dt_classifiers = []
    accuracies = []
    precisions = []
    recalls = []
    
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
    
    model = {}
    for i in range(len(dt_classifiers)):
        model[y.columns[i]] = {'model': dt_classifiers[i], 'features': X.columns.tolist()}

    return dt_classifiers, accuracies, precisions, recalls

# Fungsi untuk membuat dan mengevaluasi model decision tree dengan pre-pruning
def decision_tree_with_prepruning(X_train, y_train, X_test, y_test, max_depth=None, min_samples_split=2):
    dt_classifiers = []
    accuracies = []
    precisions = []
    recalls = []
    
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

    model = {}
    for i in range(len(dt_classifiers)):
        model[y.columns[i]] = {'model': dt_classifiers[i], 'features': X.columns.tolist()}

    return dt_classifiers, accuracies, precisions, recalls

# Fungsi untuk membuat dan mengevaluasi model decision tree dengan pruning
def decision_tree_with_pruning(X_train, y_train, X_test, y_test, ccp_alpha=0.0):
    dt_classifiers = []
    accuracies = []
    precisions = []
    recalls = []
    
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
    
    model = {}
    for i in range(len(dt_classifiers)):
        model[y.columns[i]] = {'model': dt_classifiers[i], 'features': X.columns.tolist()}

    return dt_classifiers, accuracies, precisions, recalls

# Fungsi untuk membuat dan mengevaluasi model decision tree dengan pre-pruning dan pruning
def decision_tree_with_prepruning_pruning(X_train, y_train, X_test, y_test, max_depth=None, min_samples_split=2,
                                          ccp_alpha=0.0):
    dt_classifiers = []
    accuracies = []
    precisions = []
    recalls = []
    
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

    model = {}
    for i in range(len(dt_classifiers)):
        model[y.columns[i]] = {'model': dt_classifiers[i], 'features': X.columns.tolist()}

    return dt_classifiers, accuracies, precisions, recalls

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
dt_classifiers, accuracies, precisions, recalls = decision_tree_without_pruning(X_train, y_train, X_test, y_test)
for i, dt_classifier in enumerate(dt_classifiers):
    tree_rules = export_text(dt_classifier, feature_names=list(X.columns))
    print(f"Decision Tree Rules for {y.columns[i]} without Pre-pruning and Pruning (Gini impurity):\n", tree_rules)
    print(f"Accuracy for {y.columns[i]} without Pre-pruning and Pruning (Gini impurity):", accuracies[i])
    print(f"Precision for {y.columns[i]} without Pre-pruning and Pruning (Gini impurity):", precisions[i])
    print(f"Recall for {y.columns[i]} without Pre-pruning and Pruning (Gini impurity):", recalls[i])
    print("\n")

# Decision tree dengan pre-pruning menggunakan Gini impurity
dt_classifiers, accuracies, precisions, recalls = decision_tree_with_prepruning(X_train, y_train, X_test, y_test, max_depth=10, min_samples_split=10)
for i, dt_classifier in enumerate(dt_classifiers):
    tree_rules = export_text(dt_classifier, feature_names=list(X.columns))
    print(f"Decision Tree Rules for {y.columns[i]} with Pre-pruning (Gini impurity):\n", tree_rules)
    print(f"Accuracy for {y.columns[i]} with Pre-pruning (Gini impurity):", accuracies[i])
    print(f"Precision for {y.columns[i]} with Pre-pruning (Gini impurity):", precisions[i])
    print(f"Recall for {y.columns[i]} with Pre-pruning (Gini impurity):", recalls[i])
    print("\n")

# Decision tree dengan pruning menggunakan Gini impurity
dt_classifiers, accuracies, precisions, recalls = decision_tree_with_pruning(X_train, y_train, X_test, y_test, ccp_alpha=0.01)
for i, dt_classifier in enumerate(dt_classifiers):
    tree_rules = export_text(dt_classifier, feature_names=list(X.columns))
    print(f"Decision Tree Rules for {y.columns[i]} with Pruning (Gini impurity):\n", tree_rules)
    print(f"Accuracy for {y.columns[i]} with Pruning (Gini impurity):", accuracies[i])
    print(f"Precision for {y.columns[i]} with Pruning (Gini impurity):", precisions[i])
    print(f"Recall for {y.columns[i]} with Pruning (Gini impurity):", recalls[i])
    print("\n")

# Decision tree dengan pre-pruning dan pruning menggunakan Gini impurity
dt_classifiers, accuracies, precisions, recalls = decision_tree_with_prepruning_pruning(X_train, y_train, X_test, y_test, max_depth=10, min_samples_split=10, ccp_alpha=0.01)
for i, dt_classifier in enumerate(dt_classifiers):
    tree_rules = export_text(dt_classifier, feature_names=list(X.columns))
    print(f"Decision Tree Rules for {y.columns[i]} with Pre-pruning and Pruning (Gini impurity):\n", tree_rules)
    print(f"Accuracy for {y.columns[i]} with Pre-pruning and Pruning (Gini impurity):", accuracies[i])
    print(f"Precision for {y.columns[i]} with Pre-pruning and Pruning (Gini impurity):", precisions[i])
    print(f"Recall for {y.columns[i]} with Pre-pruning and Pruning (Gini impurity):", recalls[i])
    print("\n")
