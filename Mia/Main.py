import matplotlib.pyplot as plt


# Aqui tengo mis funciones de visualización
def create_scatter():
    plt.scatter([1,2,3,4],[4,5,6,7])
    filename = "fig.png"
    plt.savefig(filename)
    print(f"Saved files as {filename}")

    plt.close()
    #plt.show()

def create_barplot():
    plt.bar(['A', 'B', 'C', 'D'], [4,3,4,5])
    filename = "fig2.png"
    plt.savefig(filename)
    print(f"Saved files as {filename}")

    plt.close()
    
