import pandas as pd

def perform_eda(data, labels):
    merged_data = pd.merge(data, labels, how='left', on=['timestamp'])
    anomaly_regions = merged_data[merged_data['label'].notnull()]
    non_anomaly_regions = merged_data[merged_data['label'].isnull()]
    significant_variables = {}
    for column in data.columns:
        if column != 'timestamp':
            anomaly_mean = anomaly_regions[column].mean()
            non_anomaly_mean = non_anomaly_regions[column].mean()
            if abs(anomaly_mean - non_anomaly_mean) > 2 * (anomaly_regions[column].std() + non_anomaly_regions[column].std()):
                significant_variables[column] = (anomaly_mean, non_anomaly_mean)
    return significant_variables

def find_root_cause(data_files, label_files):
    root_cause_variables = {}
    for data_file, label_file in zip(data_files, label_files):
        data = pd.read_csv(data_file)
        labels = pd.read_csv(label_file)
        significant_variables = perform_eda(data, labels)
        root_cause_variables[data_file] = significant_variables
    return root_cause_variables

if __name__ == "__main__":
    data_files = ['test.csv', 'smap_test.csv', 'msl_test.csv', 'psm_test.csv']
    label_files = ['test_label.csv', 'smap_test_labels.csv', 'msl_test_labels.csv', 'psm_test_labels.csv']
    root_cause_variables = find_root_cause(data_files, label_files)
    for data_file in data_files:
        print(f"\nRoot cause analysis for '{data_file}':")
        if root_cause_variables[data_file]:
            print("Significant Variables:")
            for var, (anomaly_mean, non_anomaly_mean) in root_cause_variables[data_file].items():
                print(f"{var}: Anomaly Mean - {anomaly_mean}, Non-Anomaly Mean - {non_anomaly_mean}")
        else:
            print("No significant variables found.")
