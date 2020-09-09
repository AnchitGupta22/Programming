# importing libraries
import seaborn as sns
import matplotlib.pyplot as plt

# function to visualize the step by step state of the array
def draw_graph(x, y, data, title):
    sns.set(style="darkgrid", rc={'figure.figsize':(5, 3)})
    
    ax = sns.barplot(x=x, y=y, data=data)
    ax.set_title(title, fontsize=20)
    
    plt.show()
