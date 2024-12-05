## Data oulives code

2022-07-28

Insight (not very original): Data outlives code. Why is that?

Example: You write some code to train a multitask classification deep learning network. You train some models and save the results: .hdf5 files, .csv files, log.txt, plots in .png. Two years later the code doesn't run anymore (pip install fails for some reason, you can't reproduce the code environment), but the data artifacts are very easy to open and peruse.

Docker images are supposed to help in creating reproducible code environments. It helps, but it's still much harder to re-run code than it is to re-use data.

Corollary: if you focus on generating useful data, they will remain generating value longer than any code you create.

### Update 2022-10-29

One of the reasons code is much harder to re-run is because it has many dependencies: the right compiler, the right libraries in the right version, installed in the right places. Data, however, usually have fewer dependencies in order to be read.