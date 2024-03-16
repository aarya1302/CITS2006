
import pandas as pd
import numpy as np

def add_noise(value, epsilon):
    scale = 1 / epsilon
    noise = np.random.laplace(scale=scale)
    return value + noise

def apply_differential_privacy(input_file, output_file, epsilon):
    # TODO
    data = pd.read_csv(input_file, sep=";")
    data["meter.reading"] = data["meter.reading"].apply(lambda x : add_noise(x, epsilon))
    data.to_csv(output_file)

def main():
    input_file = 'water_data.csv'
    output_file = 'output.csv'
    epsilon = 1.0  # Privacy budget
    apply_differential_privacy(input_file, output_file, epsilon)
    print("Differential privacy applied successfully to the CSV file.")

if __name__ == "__main__":
    main()
