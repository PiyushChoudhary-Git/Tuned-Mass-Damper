import serial
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import collections
import time
import csv

SERIAL_PORT = "COM5"  
BAUD_RATE = 115200

NUM_OFFSET_SAMPLES = 100
Y_AXIS_MIN = -5
Y_AXIS_MAX = 5
DATA_WINDOW_SIZE = 200
CSV_FILE_NAME = "acceleration_data.csv"

def compute_offset(ser, num_samples):
    """Read initial serial lines and compute the average y-axis offset."""
    offset_samples = []
    print(f"Collecting {num_samples} samples for offset calculation...")
    while len(offset_samples) < num_samples:
        try:
            line = ser.readline().decode('utf-8').strip()
            if line:
                parts = line.split()
                if len(parts) >= 2:
                    y_val = float(parts[1])
                    offset_samples.append(y_val)
        except Exception as e:
            print("Parsing error:", e)
    
    offset = sum(offset_samples) / len(offset_samples)
    print(f"Computed y-axis offset: {offset:.4f}")
    return offset

def main():
    try:
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
        time.sleep(2)
    except Exception as e:
        print("Failed to open serial port:", e)
        return

    y_offset = compute_offset(ser, NUM_OFFSET_SAMPLES)

    
    y_data = collections.deque([0] * DATA_WINDOW_SIZE, maxlen=DATA_WINDOW_SIZE)
    x_time_data = collections.deque([0] * DATA_WINDOW_SIZE, maxlen=DATA_WINDOW_SIZE)
    
    
    start_time = time.time()

    csv_file = open(CSV_FILE_NAME, mode='w', newline='')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["Time (ms)", "Acceleration (m/s^2)"]) 

    fig, ax = plt.subplots()
    line_plot, = ax.plot([], [], lw=1.5)
    ax.set_ylim(Y_AXIS_MIN, Y_AXIS_MAX)
    ax.set_title("Acceleration vs Time")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Acceleration (m/s²)")

    def update(frame):
        current_time = time.time() - start_time
        try:
            while ser.in_waiting:
                line_in = ser.readline().decode('utf-8').strip()
                if line_in:
                    parts = line_in.split()
                    if len(parts) >= 2:
                        y_val = float(parts[1])
                        y_val_adj = y_val - y_offset

                        y_data.append(y_val_adj)
                        x_time_data.append(current_time)

                        current_time_ms = int(current_time * 1000)
                        csv_writer.writerow([current_time_ms, y_val_adj])


            line_plot.set_data(x_time_data, y_data)
            ax.set_xlim(max(0, current_time - (DATA_WINDOW_SIZE * 0.05)), current_time)
        except Exception as e:
            print("Error reading/updating data:", e)
        return line_plot,

    ani = FuncAnimation(fig, update, interval=10)
    plt.show()
    ser.close()

if __name__ == "__main__":
    main()
