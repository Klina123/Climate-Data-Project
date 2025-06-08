import os
import pandas as pd
import matplotlib.pyplot as plt

# === Ensure output directory exists ===
os.makedirs("images", exist_ok=True)

# === Define file paths ===
city_files = {
    "Madison": "data/Madison.csv",
    "Phoenix": "data/Phoenix.csv",
    "New York": "data/New York.csv",
    "Chicago": "data/Chicago.csv"
}

# === Annual Average Temperature ===
def get_cleaned_yearly_avg(file_path):
    df = pd.read_csv(file_path, low_memory=False)
    df['DATE'] = pd.to_datetime(df['DATE'], errors='coerce')
    df = df.dropna(subset=['DailyMaximumDryBulbTemperature', 'DailyMinimumDryBulbTemperature'])
    df['TAVG'] = (df['DailyMaximumDryBulbTemperature'] + df['DailyMinimumDryBulbTemperature']) / 2
    df['YEAR'] = df['DATE'].dt.year
    yearly_avg = df.groupby('YEAR')['TAVG'].mean().reset_index()
    return yearly_avg[(yearly_avg['YEAR'] >= 1997) & (yearly_avg['YEAR'] <= 2024)]

for city, path in city_files.items():
    df_yearly = get_cleaned_yearly_avg(path)
    plt.figure(figsize=(10, 5))
    plt.plot(df_yearly['YEAR'], df_yearly['TAVG'], marker='o', label=city)
    plt.title(f"{city}: Annual Average Temperature (1997–2024)")
    plt.xlabel("Year")
    plt.ylabel("Average Temperature (°F)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"images/avg_temp_{city.lower().replace(' ', '_')}.png")
    plt.show()

# === Combined Annual Average Temperature ===
plt.figure(figsize=(12, 6))
for city, file in city_files.items():
    df_yearly = get_cleaned_yearly_avg(file)
    plt.plot(df_yearly['YEAR'], df_yearly['TAVG'], marker='o', label=city)
plt.title("Annual Average Temperature Trends (1997–2024)")
plt.xlabel("Year")
plt.ylabel("Average Temperature (°F)")
plt.grid(True)
plt.legend(title="City")
plt.tight_layout()
plt.savefig("images/all_avg_temp.png")
plt.show()

# === Annual Maximum Temperature ===
def get_yearly_max_temperature(file_path):
    df = pd.read_csv(file_path, low_memory=False)
    df['DATE'] = pd.to_datetime(df['DATE'], errors='coerce')
    df = df.dropna(subset=['DailyMaximumDryBulbTemperature'])
    df['YEAR'] = df['DATE'].dt.year
    yearly_max = df.groupby('YEAR')['DailyMaximumDryBulbTemperature'].max().reset_index()
    return yearly_max[(yearly_max['YEAR'] >= 1997) & (yearly_max['YEAR'] <= 2024)]

plt.figure(figsize=(12, 6))
for city, file in city_files.items():
    data = get_yearly_max_temperature(file)
    plt.plot(data['YEAR'], data['DailyMaximumDryBulbTemperature'], marker='o', label=city)
plt.title("Annual Highest Daily Maximum Temperature by City (1997–2024)")
plt.xlabel("Year")
plt.ylabel("Highest Daily Temperature (°F)")
plt.legend(title="City")
plt.grid(True)
plt.tight_layout()
plt.savefig("images/annual_max_temperature.png")
plt.show()

# === Hot Days Over 90°F ===
def get_extreme_heat_days(file_path, threshold=90):
    df = pd.read_csv(file_path, low_memory=False)
    df['DATE'] = pd.to_datetime(df['DATE'], errors='coerce')
    df = df.dropna(subset=['DailyMaximumDryBulbTemperature'])
    df = df[df['DailyMaximumDryBulbTemperature'] > threshold]
    df['YEAR'] = df['DATE'].dt.year
    hot_days = df.groupby('YEAR').size().reset_index(name='hot_days')
    return hot_days[(hot_days['YEAR'] >= 1997) & (hot_days['YEAR'] <= 2024)]

all_data = pd.DataFrame({'YEAR': list(range(1997, 2025))})
for city, path in city_files.items():
    city_data = get_extreme_heat_days(path)
    all_data = all_data.merge(city_data, on='YEAR', how='left', suffixes=('', f'_{city}'))
    all_data.rename(columns={'hot_days': city}, inplace=True)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 8), sharex=True, gridspec_kw={'height_ratios': [1, 2]})
years = all_data['YEAR']
bar_width = 0.2
x = range(len(years))

# Phoenix subplot
ax1.bar([p + 1.5 * bar_width for p in x], all_data['Phoenix'], width=bar_width, color='darkorange', label='Phoenix')
ax1.set_ylabel("Hot Days (Phoenix)")
ax1.set_title("Annual Number of Hot Days (> 90°F) by City (1997–2024)")
ax1.legend()

# Other cities subplot
colors = {'Madison': 'royalblue', 'New York': 'seagreen', 'Chicago': 'crimson'}
for i, city in enumerate(['Madison', 'New York', 'Chicago']):
    ax2.bar([p + i * bar_width for p in x], all_data[city], width=bar_width, label=city, color=colors[city])
ax2.set_xlabel("Year")
ax2.set_ylabel("Hot Days")
ax2.set_xticks([p + 1.5 * bar_width for p in x])
ax2.set_xticklabels(years, rotation=45)
ax2.legend(title="City")
ax2.grid(True, axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig("images/hot_days_by_city.png")
plt.show()
