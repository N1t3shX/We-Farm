import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Import the training dataset containing plant disease records
df = pd.read_csv("dataset/plant_disease_with_ndvi_1000.csv")

# Extract feature columns used as model inputs
X = df[["temperature", "humidity", "rainfall", "soil_pH"]]

# Extract target variable (binary classification: 0 indicates healthy, 1 indicates disease presence)
y = df["disease_present"]

# Partition dataset into training and testing subsets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Initialize and train the Random Forest classifier with 100 decision trees
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Persist the trained model to disk for later use
joblib.dump(model, "ml/model.pkl")

print("✅ Model trained successfully")
print("✅ model.pkl created inside ml/")
