import pandas as pd

def perform_eda(data, labels):
    merged_data = pd.merge(data, labels, how='left', on=['timestamp'])
    summary_stats = merged_data.describe()
    correlation_matrix = merged_data.corr()
    anomaly_regions = merged_data[merged_data['label'].notnull()]
    non_anomaly_regions = merged_data[merged_data['label'].isnull()]
    significant_variables = {}
    for column in data.columns:
        if column != 'timestamp':
            anomaly_mean = anomaly_regions[column].mean()
            non_anomaly_mean = non_anomaly_regions[column].mean()
            if abs(anomaly_mean - non_anomaly_mean) > 2 * (anomaly_regions[column].std() + non_anomaly_regions[column].std()):
                significant_variables[column] = (anomaly_mean, non_anomaly_mean)
    return summary_stats, correlation_matrix, significant_variables

def perform_overall_eda(data_files, label_files):
    overall_summary_stats = None
    overall_correlation_matrix = None
    overall_significant_variables = {}
    for data_file, label_file in zip(data_files, label_files):
        data = pd.read_csv(data_file)
        labels = pd.read_csv(label_file)
        summary_stats, correlation_matrix, significant_variables = perform_eda(data, labels)
        if overall_summary_stats is None:
            overall_summary_stats = summary_stats
        else:
            overall_summary_stats = pd.concat([overall_summary_stats, summary_stats], axis=1)
        if overall_correlation_matrix is None:
            overall_correlation_matrix = correlation_matrix
        else:
            overall_correlation_matrix += correlation_matrix
        overall_significant_variables[data_file] = significant_variables
    num_datasets = len(data_files)
    overall_correlation_matrix /= num_datasets
    return overall_summary_stats, overall_correlation_matrix, overall_significant_variables

if __name__ == "__main__":
    data_files = ['test.csv', 'smap_test.csv', 'msl_test.csv', 'psm_test.csv']
    label_files = ['test_label.csv', 'smap_test_labels.csv', 'msl_test_labels.csv', 'psm_test_labels.csv']
    overall_summary_stats, overall_correlation_matrix, overall_significant_variables = perform_overall_eda(data_files, label_files)
    print("Overall Summary Statistics:")
    print(overall_summary_stats)
    print("\nOverall Correlation Matrix:")
    print(overall_correlation_matrix)
    for data_file in data_files:
        print(f"\nAnalysis for '{data_file}':")
        if overall_significant_variables[data_file]:
            print("Significant Variables:")
            for var, (anomaly_mean, non_anomaly_mean) in overall_significant_variables[data_file].items():
                print(f"{var}: Anomaly Mean - {anomaly_mean}, Non-Anomaly Mean - {non_anomaly_mean}")
        else:
            print("No significant variables found.")
