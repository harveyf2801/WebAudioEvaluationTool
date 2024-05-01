import csv

# Data string
data_string = """
Sine_Anchor_1_Loudness:
88
Sine_Anchor_1_Quality:
0
Sine_Phase_Difference_Analysis_Loudness:
50
Sine_Phase_Difference_Analysis_Quality:
50
Sine_Anchor_2_Loudness:
10
Sine_Anchor_2_Quality:
0
Sine_Cross_Spectrum_Loudness:
50
Sine_Cross_Spectrum_Quality:
43
Sine_Cross_Correlation_Loudness:
50
Sine_Cross_Correlation_Quality:
50
Sine_Hidden_Reference_Loudness:
50
Sine_Hidden_Reference_Quality:
50
Sine_Phase_Vocoder_Loudness:
36
Sine_Phase_Vocoder_Quality:
19
Snare_1_Hidden_Reference_Loudness:
50
Snare_1_Hidden_Reference_Quality:
50
Snare_1_Cross_Correlation_Loudness:
50
Snare_1_Cross_Correlation_Quality:
54
Snare_1_Cross_Spectrum_Loudness:
50
Snare_1_Cross_Spectrum_Quality:
13
Snare_1_Anchor_1_Loudness:
75
Snare_1_Anchor_1_Quality:
0
Snare_1_Phase_Difference_Analysis_Loudness:
47
Snare_1_Phase_Difference_Analysis_Quality:
13
Snare_1_Anchor_2_Loudness:
0
Snare_1_Anchor_2_Quality:
3
Snare_1_Phase_Vocoder_Loudness:
42
Snare_1_Phase_Vocoder_Quality:
30
Snare_1_Model_Loudness:
50
Snare_1_Model_Quality:
46
Snare_2_Phase_Difference_Analysis_Loudness:
56
Snare_2_Phase_Difference_Analysis_Quality:
14
Snare_2_Phase_Vocoder_Loudness:
50
Snare_2_Phase_Vocoder_Quality:
50
Snare_2_Model_Loudness:
45
Snare_2_Model_Quality:
38
Snare_2_Hidden_Reference_Loudness:
50
Snare_2_Hidden_Reference_Quality:
46
Snare_2_Anchor_1_Loudness:
83
Snare_2_Anchor_1_Quality:
20
Snare_2_Anchor_2_Loudness:
2
Snare_2_Anchor_2_Quality:
15
Snare_2_Cross_Spectrum_Loudness:
38
Snare_2_Cross_Spectrum_Quality:
27
Snare_2_Cross_Correlation_Loudness:
50
Snare_2_Cross_Correlation_Quality:
55
Snare_3_Anchor_2_Loudness:
2
Snare_3_Anchor_2_Quality:
6
Snare_3_Anchor_1_Loudness:
77
Snare_3_Anchor_1_Quality:
1
Snare_3_Phase_Vocoder_Loudness:
44
Snare_3_Phase_Vocoder_Quality:
44
Snare_3_Cross_Correlation_Loudness:
50
Snare_3_Cross_Correlation_Quality:
46
Snare_3_Hidden_Reference_Loudness:
50
Snare_3_Hidden_Reference_Quality:
55
Snare_3_Model_Loudness:
50
Snare_3_Model_Quality:
45
Snare_3_Phase_Difference_Analysis_Loudness:
50
Snare_3_Phase_Difference_Analysis_Quality:
21
Snare_3_Cross_Spectrum_Loudness:
50
Snare_3_Cross_Spectrum_Quality:
17
"""

if __name__ == '__main__':
    # Parse data string into dictionary
    data = data_string.strip().split('\n')
    data_dict = {}
    for i in range(0, len(data), 2):
        key = data[i].replace('_', '-').lower()
        if key.endswith(":"):
            key = key[:-1]
        value = data[i + 1]
        data_dict[key] = value

    # Write data to CSV file
    csv_file = 'online_test_data/online_data2.csv'
    with open(csv_file, 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data_dict.keys())
        # Check if file is empty to write header
        file.seek(0, 2)
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow(data_dict)

    print("Data appended to", csv_file)
