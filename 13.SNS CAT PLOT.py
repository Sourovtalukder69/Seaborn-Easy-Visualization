# Catplot : Specially here  `kind=` parameter use for plot different different plot
# categorical scatter plot
#   stripplot()-with kind="strip"
#   swarmplot()-with kind = "swarm"

# Categorical distribution plots with catplot
#   boxplot()-with kind = "box"
#   violinplot()-with kind = "violin"
#   boxenplot()-with kind = "boxen"   # without whisker

# Categorical estimate plots with catplot
# pointplot()-with kind="point"
# barplot() - with kind = "bar"
# countplot() - with kind = "count"


import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

var = sns.load_dataset("tips").head(20)
sns.catplot(x="tip", y="size", data=var, hue="sex", height=2)
plt.show()


# now we will use `kind` parameter for plot different plot

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

var = sns.load_dataset("tips")
sns.catplot(x="day", y="size", data=var, hue="sex", kind="point")
plt.show()
