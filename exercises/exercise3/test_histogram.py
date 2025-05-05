import plotly.express as px
import pandas as pd
import random
import numpy as np

# Initial sliders
slider_num_dice = 5
slider_num_throws = 101

# Simulate dice throws
df = pd.DataFrame(columns=[f"Die {i+1}" for i in range(slider_num_dice)])
for throw in range(slider_num_throws):
    df.loc[throw] = [random.randint(1, 6) for _ in range(slider_num_dice)]

# Calculate values
throw_means = df.mean(axis=1)
theoretical_mean = 3.5
calculated_mean = df.to_numpy().mean()
difference = np.abs(theoretical_mean - calculated_mean)
fig = px.histogram(throw_means, nbins=20, labels={'value': 'Mean per throw'}, title='Histogram of throw means')
fig.show()