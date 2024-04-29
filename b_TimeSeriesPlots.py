import pandas as pd
import matplotlib.pyplot as plt

def plot_time_series_with_anomaly(data_file, label_file):
    data = pd.read_csv(data_file)
    labels = pd.read_csv(label_file)
    plt.figure(figsize=(10, 6))
    plt.plot(data.index, data.values, label='Time Series Data')
    plt.title(f'Time Series Data with Anomaly Regions ({data_file})')
    for i, row in labels.iterrows():
        plt.axvspan(row['start_time'], row['end_time'], color='red', alpha=0.3, label='Anomaly Region')
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    data_files = ['test.csv', 'smap_test.csv', 'msl_test.csv', 'psm_test.csv']
    label_files = ['test_label.csv', 'smap_test_labels.csv', 'msl_test_labels.csv', 'psm_test_labels.csv']

    for data_file, label_file in zip(data_files, label_files):
        plot_time_series_with_anomaly(data_file, label_file)
