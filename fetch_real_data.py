import pandas as pd

def download_dataset():
    print("Fetching real-world IBM Customer Churn dataset...")
    # Public raw URL for the IBM Telco Churn Dataset
    url = "https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv"
    
    try:
        df = pd.read_csv(url)
        df.to_csv("customer_churn.csv", index=False)
        print(f"Success! Downloaded {len(df)} real customer records and saved to 'customer_churn.csv'.")
    except Exception as e:
        print(f"Failed to fetch data: {e}")

if __name__ == "__main__":
    download_dataset()
