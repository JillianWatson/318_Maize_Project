import numpy as np
import pandas as pandas
import matplotlib.pyplot as plt

weather_url = 'https://de.cyverse.org/anon-files//iplant/home/shared/commons_repo/curated/GenomesToFields_GenotypeByEnvironment_PredictionCompetition_2023/Testing_data/4_Testing_Weather_Data_2022.csv'

weather_data = pandas.read_csv(weather_url)

PAR_data = weather_data['ALLSKY_SFC_PAR_TOT']

downsample_size = 300
downsampled_PAR = PAR_data.sample(n=downsample_size, random_state=40)

predicted_yield = 2 * downsampled_PAR + 30 + np.random.normal(0, 10, downsample_size)

plt.scatter(downsampled_PAR, predicted_yield, label='Predicted Yield')
plt.xlabel('Weather Data')
plt.ylabel('Predicted Grain Yield')
plt.title('Proposed Results: Predicted Grain Yield v. Weather Data')
plt.legend()
plt.grid(True)
plt.show()