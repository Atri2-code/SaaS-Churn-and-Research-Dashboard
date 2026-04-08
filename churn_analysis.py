import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_real_churn(data_file):
    print("Loading customer data...")
    try:
        df = pd.read_csv(data_file)
    except FileNotFoundError:
        print("Data not found. Run fetch_real_data.py first.")
        return

    # 1. Data Cleaning & Preprocessing
    # Convert 'Churn' from Yes/No strings to 1/0 for mathematical analysis
    df['Churn_Numeric'] = df['Churn'].apply(lambda x: 1 if x == 'Yes' else 0)
    
    sns.set_theme(style="whitegrid")
    
    print(f"Overall Platform Churn Rate: {(df['Churn_Numeric'].mean() * 100):.2f}%")

    # 2. Operational Insight: Does engaging with Tech Support reduce churn?
    plt.figure(figsize=(8, 5))
    sns.barplot(x='TechSupport', y='Churn_Numeric', data=df, errorbar=None, palette="magma")
    plt.title('Operational Impact: Churn Rate vs. Tech Support Engagement')
    plt.ylabel('Probability of Churn')
    plt.xlabel('Has Tech Support?')
    plt.tight_layout()
    plt.savefig('tech_support_impact.png')
    print("Saved 'tech_support_impact.png'")

    # 3. Retention Insight: When do users drop off? (Tenure Analysis)
    plt.figure(figsize=(10, 5))
    sns.histplot(data=df, x='tenure', hue='Churn', multiple="stack", palette="Set2", bins=36)
    plt.title('Retention Drop-off: Churn vs. Customer Tenure (Months)')
    plt.ylabel('Number of Customers')
    plt.xlabel('Months Subscribed')
    plt.tight_layout()
    plt.savefig('tenure_churn_distribution.png')
    print("Saved 'tenure_churn_distribution.png'")

    # 4. Business Insight: Contract Type vs Churn
    plt.figure(figsize=(8, 5))
    sns.barplot(x='Contract', y='Churn_Numeric', data=df, errorbar=None, palette="coolwarm")
    plt.title('Business Strategy: Churn Rate by Contract Type')
    plt.ylabel('Probability of Churn')
    plt.xlabel('Contract Type')
    plt.tight_layout()
    plt.savefig('contract_churn.png')
    print("Saved 'contract_churn.png'")

if __name__ == "__main__":
    analyze_real_churn("customer_churn.csv")
