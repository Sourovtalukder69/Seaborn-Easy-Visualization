# catplot() function use for create factor plot
# Factor plot : just can plot a point plot 
# specially a `kind`("bar", "boxplot", "scatterplot") parameter which is use to plot different different plot

# Now we will create a factor plot
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

x = sns.load_dataset("tips")
sns.factorplot(x="size", y="tip", data=x, hue="sex", kind="bar")
plt.show()