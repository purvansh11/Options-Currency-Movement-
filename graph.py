import matplotlib.pyplot as plt
import matplotlib
def trading_plot(buffer_plot,dates,hash_value_dates,region_of,cost,date,currency,timespan,election_year):
    buffer_plot = 120
    plot_start_index = hash_value_dates[date]-buffer_plot
    # plot_start_date = dates[plot_start_index]
    plot_end_index = hash_value_dates[date]+buffer_plot
    # plot_end_date = dates[plot_end_index]
    traded_at = []
    x_values = []
    x_val = -buffer_plot

    for i in range(plot_start_index,plot_end_index+1):
        try:
            # traded_at.append(round((float(cost[dates[i]][region_of[currency]])),10))
            traded_at.append(round(float(cost[dates[i]][region_of[currency]]) - float(cost[date][region_of[currency]]),10))
            x_values.append(x_val)
            x_val += 1
        except:
            continue
    plt.plot(x_values,traded_at)
    plt.gca()
    # aus_plot.axes.get_yaxis().set_visible(False)
    plt.title("Plot of {} for a range of {} days in the year {}".format(currency,buffer_plot,election_year))
    plt.axvline(x=-timespan*30, color='black', linestyle='--')
    plt.axvline(x=timespan*30, color='black', linestyle='--')
    plt.axhline(y=min(traded_at), color='red', linestyle='--')
    plt.axhline(y=max(traded_at), color='green', linestyle='--')
    plt.grid()
    plt.show()
    return [x_values,traded_at]

def options_plot(traded_at,hash_value_dates,dates,buffer_plot,date,timespan,strike):
    buffer_options_plot = timespan * 30
    euro_plot = []
    american_plot = []
    days_after_election = []
    x_index = -buffer_options_plot
    # strike = 0.0
    fig , (ax1,ax2) = plt.subplots(1,2)
    fig.suptitle("Digital Options Trading")
    # print(traded_at[80], traded_at[110] , traded_at[110] * ( 1 + strike/100))
    cnt_ones_euro = 0
    cnt_ones_american = 0
    for i in range(buffer_plot - buffer_options_plot, buffer_plot + buffer_options_plot+1):
        if traded_at[i+30] >= traded_at[i] * ( 1 + strike/100):
            euro_plot.append(1)
            cnt_ones_euro += 1
        else:
            euro_plot.append(0)
        days_after_election.append(x_index)
        x_index += 1

    ax1.axes.get_yaxis().set_visible(False)
    ax1.set_title("European")
    ax1.plot(days_after_election,euro_plot)

    for i in range(buffer_plot - buffer_options_plot, buffer_plot + buffer_options_plot+1):
        flag = False
        for j in range(i+1,i+31):
            if traded_at[j] >= (traded_at[i] * ( 1 + (strike/100))):
                flag = True
                break
        if flag == True:
            american_plot.append(1)
            cnt_ones_american += 1
        else:
            american_plot.append(0)
            
    ones_perc_european = round((cnt_ones_euro/len(days_after_election))*100,5)
    ones_perc_american = round((cnt_ones_american/len(days_after_election))*100,5)
    print("ones_perc_european",ones_perc_european)
    print("ones_perc_american",ones_perc_american)
    print("strike",strike)

    ax2.axes.get_yaxis().set_visible(False)
    ax2.set_title("American")
    ax2.plot(days_after_election,american_plot)
    plt.show()

    # fig = matplotlib.pyplot.gcf()
    # fig.set_size_inches(70.5, 10.5,forward = True)
    # fig.savefig('test2png.png', dpi=100)
    
    return [euro_plot,american_plot,days_after_election]