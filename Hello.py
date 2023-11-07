
# Required libraries and their exact versions:
# pip install matplotlib==3.4.3
# pip install streamlit==1.0.0

import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Set the Matplotlib style
plt.style.use('ggplot')

# Function to plot a sine wave
def plot_sine_wave():
    x = np.linspace(0, 4 * np.pi, 1000)
    y = np.sin(x)
    
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('sin(x)')
    plt.title('Sine Wave')
    plt.grid(True)
    
    # Display the plot within Streamlit
    st.pyplot()

# Function to plot a bar chart
def plot_bar_chart():
    labels = ['A', 'B', 'C', 'D', 'E']
    values = [10, 25, 5, 20, 15]
    
    plt.bar(labels, values)
    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.title('Bar Chart')
    plt.grid(True)
    
    # Display the plot within Streamlit
    st.pyplot()

# Main Streamlit app code
def main():
    st.title('Matplotlib Operations')
    st.write("Popular Matplotlib operations and plots explained")

    # Dropdown menu to select the operation
    operation = st.selectbox('Select an operation', ['Sine Wave', 'Bar Chart'])
    
    if operation == 'Sine Wave':
        plot_sine_wave()
    elif operation == 'Bar Chart':
        plot_bar_chart()

if __name__ == '__main__':
    main()
