import torch
import pandas as pd
import numpy as np

n = 10000
m = 1000
# Specify the dimensions of the sample
par = torch.distributions.pareto.Pareto(torch.tensor([1.0]), torch.tensor([1.0]))
norm = torch.distributions.normal.Normal(torch.tensor([0.0]), torch.tensor([1.0]))
bern = torch.distributions.bernoulli.Bernoulli(torch.tensor([0.4]))
data_points = norm.sample((n,1)).squeeze(-1).numpy()
data_points = np.hstack((data_points, data_points * 0.1 + par.sample((n,1)).squeeze(-1).numpy()))
data_points = np.hstack((data_points, bern.sample((n,1)).squeeze(-1).numpy()))
data_points = np.hstack((data_points, np.zeros((n,m))))

# Create a DataFrame from the (m, n) sample without specifying column names
data_frame = pd.DataFrame(data_points)


# Write to CSV without index or header
data_frame.to_csv("big_stupid_file.csv", index=False, header=False, mode="a")
