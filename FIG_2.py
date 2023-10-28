import pandas as pandas
import matplotlib.pyplot as plt

weather_url = 'https://de.cyverse.org/anon-files//iplant/home/shared/commons_repo/curated/GenomesToFields_GenotypeByEnvironment_PredictionCompetition_2023/Testing_data/4_Testing_Weather_Data_2022.csv'

weather_data = pandas.read_csv(weather_url)

sample_data = weather_data.iloc[0]
fields = list(sample_data.keys())[2:]
values = sample_data.values[2:]

plt.bar(fields, values)
plt.xlabel('Fields')
plt.ylabel('Values')
plt.xticks(rotation=45, fontsize=7, ha='right')
plt.title('DEH1_2022 Sample Data Visual')
plt.subplots_adjust(bottom=0.3)
plt.show()