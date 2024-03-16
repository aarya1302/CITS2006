import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load the dataset with semicolon as the separator

data_path = 'water_data.csv'

data = pd.read_csv(data_path, sep=";") #if reading water_data.csv
#data = pd.read_csv(data_path)
print(data)

# Display the first few rows of the dataset
X = data.drop(columns=['user.key'])
y = data['user.key']
print("Columns of the CSV file:", data.columns)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(data.drop(columns=['user.key', 'datetime']), data['user.key'], test_size=0.2, random_state=42)


# Display the shapes of the training and testing sets
print("Training set shape:", X_train.shape, y_train.shape)
print("Testing set shape:", X_test.shape, y_test.shape)

# Train a machine learning model using the training set
model = RandomForestClassifier(n_estimators=100, random_state=42)

model.fit(X_train, y_train)

# Model Evaluation
# Predict the testing set and calculate the accuracy
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model accuracy: {accuracy}")

# Perform Re Identification Attack

# ------------TODO--------------
def re_identification_attack(model, target_record):


    # Step 1: Predict Target Record: Use the predict method of the model to predict the target record. Remember to reshape the target record using reshape(1, -1) before passing it to the predict method.
    #TODO
    target_record = target_record.reshape(1, -1) 
    target_pred = model.predict(target_record)    
    # Step 2: Generate Synthetic Data: Create synthetic data by copying the target record and modifying one spefic feature. Can be a specific data value to make a syntehtic data point.
    #TODO
    syn_data = target_record
    syn_data[0][0] = 19322

    print(syn_data)
    # Step 3: Predict Synthetic Data: Use the predict method again to predict the synthetic data point.
    #TODO
    syn_pred = model.predict(syn_data)    
    # Step 4: Return Result: Return True if the predictions are different (indicating re identification), and False otherwise.
    return  (syn_pred != target_pred) 

#------------END TODO--------------

# Choose a target record for the attack
target_index = 0
target_record = X_test.iloc[target_index]

# Perform the Re Identification Attack
is_member = re_identification_attack(model, target_record.values)
print(f"Is target record a member of the training set? {'Yes' if is_member else 'No'}")

