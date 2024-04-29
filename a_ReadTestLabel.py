import pandas as pd

def read_data_and_labels(data_files, label_files):
    data_dict = {}
    label_dict = {}
    for data_file, label_file in zip(data_files, label_files):
        data_key = data_file.split('.')[0]
        label_key = label_file.split('.')[0]
        data_dict[data_key] = pd.read_csv(data_file)
        label_dict[label_key] = pd.read_csv(label_file)
    return data_dict, label_dict

if __name__ == "__main__":
    data_files = ['test.csv', 'smap_test.csv', 'msl_test.csv', 'psm_test.csv']
    label_files = ['test_label.csv', 'smap_test_labels.csv', 'msl_test_labels.csv', 'psm_test_labels.csv']

    test_data, test_labels = read_data_and_labels(data_files, label_files)

    for key in test_data:
        print(f"Test Data '{key}':")
        print(test_data[key].head())
        print(f"\nTest Labels '{key}_labels':")
        print(test_labels[f"{key}_labels"].head())
