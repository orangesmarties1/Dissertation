# Uses matplotlib to make charts.


import matplotlib.pyplot as plot


# x: x axis data, y: y axis data, l: label, gain: True plots gain, False plots absolute
def plot_graph(x, y, x_labels, l, gain):
    _, ax = plot.subplots()
    
    baseline = y[0]
    
    # add axis labels and add axis limit
    plot.xlabel("Feature expansion method")
    plot.ylabel("Overall accuracy (%)")
    plot.ylim([min(y)-1, max(y)+1])
    ax.set_xticks(x)
    ax.set_xticklabels(x_labels)
    ax.yaxis.grid()
    
    # plot line across from baseline
    ax.axhline(y=baseline, color="0.1", linestyle="--", linewidth=2)
    
    w = 0.55
    bars = ax.bar(x, y, width=w, align="center", color="#444444", label=l)
    
    # add labels to bars
    count = 0
    for bar in bars:
        h = bar.get_height()
        x_pos = x[count]
        
        # label with +/- gain
        if gain:
            # if first (baseline) then annotate with value
            if count == 0:
                ax.annotate(str(h), (x_pos, h), (x_pos, h+0.1), ha="center")
            else:
                gain = h-baseline
                gain = ("+"+str(gain)) if gain > 0 else gain
                ax.annotate(str(gain), (x_pos, h), (x_pos, h+0.1), ha="center")
        # label with value
        else:
            ax.annotate(str(h), (x_pos, h), (x_pos, h+0.1), ha="center")
        
        count += 1
    
    # add legend
    leg = ax.legend(loc="upper right")
    for label in leg.get_texts():
        label.set_fontsize('medium')


if __name__ == "__main__":
    # bar chart for test dataset split and for overall accuracy
    
    x_data = [0, 1, 2, 3, 4, 5]
    x_labels = ("Baseline", "B", "C", "D", "E", "F")
    
    x_data2 = [0, 1, 2, 3, 4, 5, 6, 7]
    x_labels2 = ("Baseline", "A", "B", "C", "D", "E", "F", "G")
    
    # overall accuracy
    #y_data = [76.31, 77.02, 77.13, 78.18, 77.63, 78.29, 77.58, 77.41]
    
    # split 1
    #y_data = [79.37, 80.93, 80.04, 80.04, 78.93, 79.82]
    
    # split 2
    #y_data = [78.77, 79.43, 79.43, 80.96, 80.3, 80.74]
    
    # split 3
    #y_data = [74.49, 76.28, 75.61, 77.62, 77.4, 75.61]
    
    # split 4
    y_data = [72.58, 76.09, 75.43, 74.56, 73.68, 74.34]
    
    # plot the data
    plot_graph(x_data, y_data, x_labels, "% accuracy gain", True)
    
    # show plot 
    #plot.grid(True)
    plot.show()
    