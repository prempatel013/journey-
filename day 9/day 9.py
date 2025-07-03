"""
🧠 PYTHON DAY 9: MACHINE LEARNING FUNDAMENTALS 🧠
Covers:
1. Machine Learning Basics
2. Scikit-Learn Pipeline
3. Model Evaluation
4. Real-World ML Project
"""

# ================ 1. MACHINE LEARNING BASICS ================
print("\n" + "="*60 + "\n🔍 1. MACHINE LEARNING CONCEPTS\n" + "="*60)

"""
🔍 Key ML Types:
1. Supervised Learning (Labeled data)
   - Classification: Predict categories
   - Regression: Predict continuous values

2. Unsupervised Learning (Unlabeled data)
   - Clustering: Group similar data
   - Dimensionality Reduction: Simplify data

3. Reinforcement Learning (Reward-based)
"""

# ================ 2. SCIKIT-LEARN PIPELINE ================
print("\n" + "="*60 + "\n⚙️ 2. SCIKIT-LEARN WORKFLOW\n" + "="*60)

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.pipeline import make_pipeline

# 🛠️ Example 1: Classification with Iris Dataset
def iris_classification():
    # Load dataset
    iris = load_iris()
    X, y = iris.data, iris.target
    feature_names = iris.feature_names
    target_names = iris.target_names
    
    print(f"\nFeatures: {feature_names}")
    print(f"Target classes: {target_names}")
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # Create pipeline
    model = make_pipeline(
        StandardScaler(),
        RandomForestClassifier(n_estimators=100, random_state=42)
    )
    
    # Train model
    model.fit(X_train, y_train)
    
    # Evaluate
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred, target_names=target_names)
    
    print(f"\nModel Accuracy: {accuracy:.2f}")
    print("\nClassification Report:")
    print(report)
    
    return model

print("Running Iris classification...")
iris_model = iris_classification()

# ================ 3. DATA VISUALIZATION ================
print("\n" + "="*60 + "\n📊 3. DATA VISUALIZATION\n" + "="*60)

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# 🛠️ Example 2: Visualizing the Iris Dataset
def visualize_iris():
    iris = sns.load_dataset('iris')
    
    # Pairplot
    print("\nGenerating pairplot...")
    sns.pairplot(iris, hue='species', palette='husl')
    plt.suptitle("Iris Dataset Pairplot", y=1.02)
    plt.savefig('iris_pairplot.png')
    plt.close()
    
    # Feature distributions
    plt.figure(figsize=(12, 6))
    for i, feature in enumerate(iris.columns[:-1]):
        plt.subplot(2, 2, i+1)
        sns.boxplot(x='species', y=feature, data=iris)
        plt.title(f"{feature} by Species")
    plt.tight_layout()
    plt.savefig('iris_boxplots.png')
    plt.close()
    
    print("Visualizations saved as iris_pairplot.png and iris_boxplots.png")

visualize_iris()

# ================ 4. REAL-WORLD ML PROJECT ================
print("\n" + "="*60 + "\n🏆 4. HOUSE PRICE PREDICTION\n" + "="*60)

from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import cross_val_score

def housing_prediction():
    # Load dataset
    housing = fetch_california_housing()
    X, y = housing.data, housing.target
    feature_names = housing.feature_names
    
    print("\nCalifornia Housing Features:")
    print(feature_names)
    
    # Create pipeline
    model = make_pipeline(
        StandardScaler(),
        LinearRegression()
    )
    
    # Cross-validation
    cv_scores = cross_val_score(model, X, y, cv=5, scoring='r2')
    print(f"\nCross-validated R² scores: {cv_scores}")
    print(f"Mean R²: {cv_scores.mean():.2f} (±{cv_scores.std():.2f})")
    
    # Final evaluation
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    print(f"\nTest MSE: {mse:.2f}")
    print(f"Test R²: {r2:.2f}")
    
    # Feature importance
    if hasattr(model.named_steps['linearregression'], 'coef_'):
        coef = model.named_steps['linearregression'].coef_
        importance = pd.DataFrame({
            'Feature': feature_names,
            'Coefficient': coef
        }).sort_values('Coefficient', key=abs, ascending=False)
        
        print("\nFeature Importance:")
        print(importance)
    
    return model

print("\nRunning House Price Prediction...")
housing_model = housing_prediction()

# ================ 5. MODEL PERSISTENCE ================
print("\n" + "="*60 + "\n💾 5. SAVING & LOADING MODELS\n" + "="*60)

import joblib

def save_model(model, filename):
    joblib.dump(model, filename)
    print(f"Model saved as {filename}")

def load_model(filename):
    return joblib.load(filename)

# Save our models
save_model(iris_model, 'iris_classifier.joblib')
save_model(housing_model, 'housing_predictor.joblib')

# ================ 6. NEXT STEPS ================
print("\n" + "="*60 + "\n🚀 6. CONTINUING YOUR ML JOURNEY\n" + "="*60)
print("""
1. Deep Learning:
   - TensorFlow/Keras
   - PyTorch
   - Computer Vision (OpenCV)

2. Advanced Topics:
   - Hyperparameter tuning
   - Feature engineering
   - Time series forecasting

3. Deployment:
   - Flask/FastAPI for model serving
   - ONNX for cross-platform models
   - TensorFlow Lite for mobile

4. Specialized Domains:
   - NLP with spaCy/transformers
   - Recommendation systems
   - Anomaly detection
""")

print("\n" + "="*60 + "\n🎉 CONGRATS ON COMPLETING DAY 9! 🎉\n" + "="*60)