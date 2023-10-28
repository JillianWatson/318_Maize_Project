import pandas as pandas
import matplotlib.pyplot as plt

weather_url = 'https://de.cyverse.org/anon-files//iplant/home/shared/commons_repo/curated/GenomesToFields_GenotypeByEnvironment_PredictionCompetition_2023/Testing_data/4_Testing_Weather_Data_2022.csv'

weather_data = pandas.read_csv(weather_url)

PAR_data = weather_data['ALLSKY_SFC_PAR_TOT']

plt.hist(PAR_data, bins=20, color='orange', alpha=0.7, edgecolor='black')
plt.xlabel('All Sky Surface PAR Total (W/m^2)')
plt.ylabel('Frequency')
plt.title('Histogram of All Sky Surface Par Total for Maize Crop')
plt.show()
