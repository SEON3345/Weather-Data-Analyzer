import argparse
import pandas as pd
import matplotlib.pyplot as plt

def analyze(df):
    df = df.copy()
    df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
    df['temperature'] = pd.to_numeric(df['temperature'], errors='coerce')
    df['humidity'] = pd.to_numeric(df['humidity'], errors='coerce')
    return df.dropna(subset=['timestamp']).set_index('timestamp').resample('D').agg({'temperature': ['mean', 'min', 'max'], 'humidity': 'mean'})

def main():
    p = argparse.ArgumentParser(); p.add_argument('csv'); args = p.parse_args()
    daily = analyze(pd.read_csv(args.csv))
    print(daily); daily.to_csv('daily_weather.csv')
    daily['temperature'].plot(); plt.ylabel('Temperature (C)'); plt.tight_layout(); plt.savefig('weather.png'); plt.close()

if __name__ == '__main__':
    main()
