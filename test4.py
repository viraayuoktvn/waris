# Required Libraries
import numpy  as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score
from copy import deepcopy
from random import randint
from sklearn.metrics import classification_report
from sklearn.model_selection import KFold
from scipy import stats
import pickle

# Function: Returns True, if a Column is Numeric
def is_number(string):
    for i in range(0, len(string)):
        if pd.isnull(string[i]) == False:
            try:
                float(string[i])
                return True
            except ValueError:
                return False

# Function: Returns True, if a Value is Numeric
def is_number_value(value):
    if pd.isnull(value) == False:
        try:
            float(value)
            return True
        except ValueError:
            return False

# Function: Performs a Chi_Squared Test or Fisher Exact Test
def chi_squared_test(label_df, feature_df):
    label_df.reset_index(drop=True, inplace=True)
    feature_df.reset_index(drop=True, inplace=True)
    data = pd.concat([pd.DataFrame(label_df.values.reshape((label_df.shape[0], 1))), feature_df], axis = 1)
    data.columns=["label", "feature"]
    contigency_table = pd.crosstab(data.iloc[:,0], data.iloc[:,1], margins = False)
    m = contigency_table.values.sum()
    if m <= 10000 and contigency_table.shape == (2,2):
        p_value = stats.fisher_exact(contigency_table)
    else:
        p_value = stats.chi2_contingency(contigency_table, correction = False) # (No Yates' Correction)
    return p_value[1]

# Function: Prediction
def prediction_dt_c45(model, Xdata):
    Xdata = Xdata.reset_index(drop=True)
    ydata = pd.DataFrame(index=range(0, Xdata.shape[0]), columns=[y.columns[0]])
    data  = pd.concat([ydata, Xdata], axis = 1)
    rule = []

    # Preprocessing - Boolean Values
    for j in range(0, data.shape[1]):
        if data.iloc[:,j].dtype == "bool":
            data.iloc[:,j] = data.iloc[:, j].astype(str)

    dt_model = deepcopy(model)

    for i in range(0, len(dt_model)):
        dt_model[i] = dt_model[i].replace("{", "")
        dt_model[i] = dt_model[i].replace("}", "")
        dt_model[i] = dt_model[i].replace(";", "")
        dt_model[i] = dt_model[i].replace("IF ", "")
        dt_model[i] = dt_model[i].replace("AND", "")
        dt_model[i] = dt_model[i].replace("THEN", "")
        dt_model[i] = dt_model[i].replace("=", "")
        dt_model[i] = dt_model[i].replace("<", "<=")

    for i in range(0, len(dt_model) -2):
        splited_rule = [x for x in dt_model[i].split(" ") if x]
        rule.append(splited_rule)

    for i in range(0, Xdata.shape[0]):
        for j in range(0, len(rule)):
            rule_confirmation = len(rule[j])/2 - 1
            rule_count = 0
            for k in range(0, len(rule[j]) - 2, 2):
                if is_number_value(data[rule[j][k]][i]) == False:
                    if (data[rule[j][k]][i] in rule[j][k+1]):
                        rule_count = rule_count + 1
                        if (rule_count == rule_confirmation):
                            data.iloc[i,0] = rule[j][len(rule[j]) - 1]
                    else:
                        k = len(rule[j])
                elif is_number_value(data[rule[j][k]][i]) == True:
                     if rule[j][k+1].find("<=") == 0:
                         if data[rule[j][k]][i] <= float(rule[j][k+1].replace("<=", "")):
                             rule_count = rule_count + 1
                             if (rule_count == rule_confirmation):
                                 data.iloc[i,0] = rule[j][len(rule[j]) - 1]
                         else:
                             k = len(rule[j])
                     elif rule[j][k+1].find(">") == 0:
                         if data[rule[j][k]][i] > float(rule[j][k+1].replace(">", "")):
                             rule_count = rule_count + 1
                             if (rule_count == rule_confirmation):
                                 data.iloc[i,0] = rule[j][len(rule[j]) - 1]
                         else:
                             k = len(rule[j])

    for i in range(0, Xdata.shape[0]):
        if pd.isnull(data.iloc[i,0]):
            data.iloc[i,0] = dt_model[len(dt_model)-1]

    return data

# Function: Calculates the Information Gain Ratio
def info_gain_ratio(target, feature = [], uniques = []):
    entropy = 0
    denominator_1 = feature.count()
    data = pd.concat([pd.DataFrame(target.values.reshape((target.shape[0], 1))), feature], axis = 1)
    for entp in range(0, len(np.unique(target))):
        numerator_1 = data.iloc[:,0][(data.iloc[:,0] == np.unique(target)[entp])].count()
        if numerator_1 > 0:
            entropy = entropy - (numerator_1/denominator_1)* np.log2((numerator_1/denominator_1))
    info_gain = float(entropy)
    info_gain_r = 0
    intrinsic_v = 0
    for word in range(0, len(uniques)):
        denominator_2 = feature[(feature == uniques[word])].count()
        if denominator_2[0] > 0:
            intrinsic_v = intrinsic_v - (denominator_2/denominator_1)* np.log2((denominator_2/denominator_1))
        for lbl in range(0, len(np.unique(target))):
            numerator_2 = data.iloc[:,0][(data.iloc[:,0] == np.unique(target)[lbl]) & (data.iloc[:,1]  == uniques[word])].count()
            if numerator_2 > 0:
                info_gain = info_gain + (denominator_2/denominator_1)*(numerator_2/denominator_2)* np.log2((numerator_2/denominator_2))
    if intrinsic_v[0] > 0:
        info_gain_r = info_gain/intrinsic_v
    return float(info_gain_r)

# Function: Binary Split on Continuous Variables
def split_me(feature, split):
    result = pd.DataFrame(feature.values.reshape((feature.shape[0], 1)))
    for fill in range(0, len(feature)):
        result.iloc[fill,0] = feature.iloc[fill]
    lower = "<=" + str(split)
    upper = ">" + str(split)
    for convert in range(0, len(feature)):
        if float(feature.iloc[convert]) <= float(split):
            result.iloc[convert,0] = lower
        else:
            result.iloc[convert,0] = upper
    binary_split = []
    binary_split = [lower, upper]
    return result, binary_split

# Ensure there are no AND 0 = {1} or AND 0 = {Tidak Dapat} in the rules
def clean_rule(rule):
    cleaned_rule = []
    for r in rule:
        # Only append rules that don't contain 'AND 0 ='
        if 'AND 0 =' not in r:
            cleaned_rule.append(r)
    return cleaned_rule

# Function: C4.5 Algorithm
def dt_c45(Xdata, ydata, cat_missing = "none", num_missing = "none", pre_pruning = "none", chi_lim = 0.1, min_lim = 5):

    ################     Part 1 - Preprocessing    #############################
    # Preprocessing - Creating Dataframe
    name = ydata.columns[0]  # Mengambil nama kolom pertama dari DataFrame ydata
    ydata = pd.DataFrame(ydata.values.reshape((ydata.shape[0], 1)))
    for j in range(0, ydata.shape[1]):
        if ydata.iloc[:,j].dropna().value_counts().index.isin([0,1]).all():
            for i in range(0, ydata.shape[0]):
               if ydata.iloc[i,j] == 'Dapat':
                   ydata.iloc[i,j] = 'Dapat'
               else:
                   ydata.iloc[i,j] = 'Tidak Dapat'
    dataset = pd.concat([ydata, Xdata], axis = 1)

     # Preprocessing - Boolean Values
    for j in range(0, dataset.shape[1]):
        if dataset.iloc[:,j].dtype == "bool":
            dataset.iloc[:,j] = dataset.iloc[:, j].astype(str)

    # Preprocessing - Unique Words List
    unique = []
    uniqueWords = []
    for j in range(0, dataset.shape[1]):
        for i in range(0, dataset.shape[0]):
            token = dataset.iloc[i, j]
            if not token in unique:
                unique.append(token)
        uniqueWords.append(unique)
        unique = []

    # Preprocessing - Label Matrix
    label = np.array(uniqueWords[0])
    label = label.reshape(1, len(uniqueWords[0]))

    ################    Part 2 - Initialization    #############################
    # C4.5 - Initializing Variables
    i = 0
    impurity = 0
    branch = [None]*1
    branch[0] = dataset
    gain_ratio = np.empty([1, branch[i].shape[1]])
    lower = "0"
    root_index = 0
    rule = [None]*1
    rule[0] = "IF "
    skip_update = False
    stop = 2
    upper = "3"

    ################     Part 3 - C4.5 Algorithm    #############################
    # C4.5 - Algorithm
    while (i < stop):
        impurity = np.amax(gain_ratio)
        gain_ratio.fill(0)
        for element in range(1, branch[i].shape[1]):
            if len(branch[i]) == 0:
                skip_update = True
                break
            if len(np.unique(branch[i][0])) == 1 or len(branch[i]) == 1:
                if ";" not in rule[i]:
                    rule[i] = rule[i] + " THEN " + name + " = " + branch[i].iloc[0, 0] + ";"
                    rule[i] = rule[i].replace(" AND  THEN ", " THEN ")
                skip_update = True
                break
            if branch[i].columns[element] == '0':  # Skip if column name is '0'
                continue
            if i > 0 and is_number(dataset.iloc[:, element]) == False and pre_pruning == "chi_2" and chi_squared_test(branch[i].iloc[:, 0], branch[i].iloc[:, element]) > chi_lim:
                if ";" not in rule[i]:
                    rule[i] = rule[i] + " THEN " + name + " = " + branch[i].agg(lambda x:x.value_counts().index[0])[0] + ";"
                    rule[i] = rule[i].replace(" AND  THEN ", " THEN ")
                skip_update = True
                continue
            if is_number(dataset.iloc[:, element]) == True:
                gain_ratio[0, element] = 0.0
                value = np.sort(branch[i].iloc[:, element].unique())
                skip_update = False
                if branch[i][(branch[i].iloc[:, element] == value[0])].count()[0] > 1:
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
                    bin_sample = split_me(feature = branch[i].iloc[:, element], split = value[bin_split])
                    if i > 0 and pre_pruning == "chi_2" and chi_squared_test(branch[i].iloc[:, 0], bin_sample[0]) > chi_lim:
                        if ";" not in rule[i]:
                            rule[i] = rule[i] + " THEN " + name + " = " + branch[i].agg(lambda x:x.value_counts().index[0])[0] + ";"
                            rule[i] = rule[i].replace(" AND  THEN ", " THEN ")
                        skip_update = True
                        continue
                    igr = info_gain_ratio(target = branch[i].iloc[:, 0], feature = bin_sample[0], uniques = bin_sample[1])
                    if igr > float(gain_ratio[0, element]):
                        gain_ratio[0, element] = igr
                        uniqueWords[element] = bin_sample[1]
            if is_number(dataset.iloc[:, element]) == False:
                gain_ratio[0, element] = 0.0
                skip_update = False
                igr = info_gain_ratio(target = branch[i].iloc[:, 0], feature =  pd.DataFrame(branch[i].iloc[:, element].values.reshape((branch[i].iloc[:, element].shape[0], 1))), uniques = uniqueWords[element])
                gain_ratio[0, element] = igr
            if i > 0 and pre_pruning == "min" and len(branch[i]) <= min_lim:
                if ";" not in rule[i]:
                    rule[i] = rule[i] + " THEN " + name + " = " + branch[i].agg(lambda x:x.value_counts().index[0])[0] + ";"
                    rule[i] = rule[i].replace(" AND  THEN ", " THEN ")
                skip_update = True
                continue

        if i > 0 and pre_pruning == "impur" and np.amax(gain_ratio) < impurity and np.amax(gain_ratio) > 0:
            if ";" not in rule[i]:
                rule[i] = rule[i] + " THEN " + name + " = " + branch[i].agg(lambda x:x.value_counts().index[0])[0] + ";"
                rule[i] = rule[i].replace(" AND  THEN ", " THEN ")
            skip_update = True
            continue

        if skip_update == False:
            root_index = np.argmax(gain_ratio)
            rule[i] = rule[i] + str(list(branch[i])[root_index])

            for word in range(0, len(uniqueWords[root_index])):
                uw = uniqueWords[root_index][word].replace("<=", "")
                uw = uw.replace(">", "")
                lower = "<=" + uw
                upper = ">" + uw
                if uniqueWords[root_index][word] == lower:
                    branch.append(branch[i][branch[i].iloc[:, root_index] <= float(uw)])
                elif uniqueWords[root_index][word] == upper:
                    branch.append(branch[i][branch[i].iloc[:, root_index]  > float(uw)])
                else:
                    branch.append(branch[i][branch[i].iloc[:, root_index] == uniqueWords[root_index][word]])

                rule.append(rule[i] + " = " + "{" + uniqueWords[root_index][word] + "}")

            for logic_connection in range(1, len(rule)):
                if len(np.unique(branch[i][0])) != 1 and rule[logic_connection].endswith(" AND ") == False and rule[logic_connection].endswith("}") == True and 'AND 0 =' not in rule[logic_connection]:
                    rule[logic_connection] = rule[logic_connection] + " AND "
        skip_update = False
        i = i + 1
        print("iteration: ", i)
        stop = len(rule)

    for i in range(len(rule) - 1, -1, -1):
        if rule[i].endswith(";") == False:
            del rule[i]

    rule.append("Total Number of Rules: " + str(len(rule)))
    rule.append(dataset.agg(lambda x:x.value_counts().index[0])[0])
    print("End of Iterations")

    return rule

# Loading Dataset
data = pd.read_csv('all biner fix.csv', sep=';')

df = pd.DataFrame(data)

# Memisahkan fitur dan target
X = df[['total_kakek', 'total_ayah']]  # Fitur, tetap sebagai integer
y = df[['hw_kakek']]  # Target, tetap sebagai string

# Run C4.5
dt_model = dt_c45(Xdata = X, ydata = y)

print(dt_model)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Print the rules of the decision tree model
print("Decision Tree Rules:")
for rule in dt_model:
    print(rule)

# Make predictions on the test data
predictions = prediction_dt_c45(dt_model, X_test)

# Convert the predicted labels to a format compatible with sklearn metrics
y_pred = predictions[y.columns[0]]

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

# Calculate precision
precision = precision_score(y_test, y_pred, pos_label='Dapat')  # Assuming binary classification

# Calculate recall
recall = recall_score(y_test, y_pred, pos_label='Dapat')  # Assuming binary classification

# Print the evaluation metrics
print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)

# Save the model
# with open('decision_tree_model.pkl', 'wb') as file:
#     pickle.dump(dt_model, file)

# Visualize Decision Tree
# dot = visualize_decision_tree(dt_model)
# dot.render('decision_tree', format='png', view=True)