import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# Function to plot pie charts.
def plot_pie_chart(input_data, input_labels, input_colors, input_title, input_explode):

    if input_colors != []:
        plt.pie(input_data,
                autopct="%1.2f%%",
                colors=input_colors,
                explode=input_explode,
                shadow=True)
    else:
        plt.pie(input_data,
                autopct="%1.2f%%",
                explode=input_explode,
                shadow=True)
    #     circ = plt.Circle((0,0),.9,color="white")
    #     plt.gca().add_artist(circ)

    plt.title(input_title)
    plt.legend(input_labels, loc="upper right")

    # plt.show()


# Function to plot horizontal bar charts.
def plot_barh_chart(input_data_1, input_data_2, input_color, input_xlabel, input_title):
    # fig = plt.figure(figsize=(10, 7))
    plt.barh(input_data_1, input_data_2, color=input_color)

    plt.xlabel(input_xlabel)
    plt.title(input_title, pad=20)

    # plt.show()


def plot_two_barh_charts(y_data1, x_data1, color1, xlabel1, title1, y_data2, x_data2, color2, xlabel2, title2):
    fig, ax1 = plt.subplots(1, 2, figsize=(15, 10))

    plt.subplot(121)
    plot_barh_chart(y_data1, x_data1, color1, xlabel1, title1)

    plt.subplot(122)
    plot_barh_chart(y_data2, x_data2, color2, xlabel2, title2)

    plt.show()


# Function to plot pie subplots
def plot_two_pie_subplots(data_1, labels_1, colors_1, title_1, data_2, labels_2, colors_2, title_2, explode):
    fig, ax1 = plt.subplots(1, 2, figsize=(15, 10))

    plt.subplot(121)
    plot_pie_chart(data_1,
                   labels_1,
                   colors_1,
                   title_1,
                   explode
                   )

    plt.subplot(122)
    plot_pie_chart(data_2,
                   labels_2,
                   colors_2,
                   title_2,
                   explode
                   )

    plt.show()