# Climate-Data-Project

This project investigates whether climate warming is real by analyzing long-term temperature data from four U.S. cities between 1997 and 2024. It focuses on trends in average annual temperature, yearly maximum temperature, and the number of hot days per year.

---

## 🔍 Cities Analyzed

* Madison, WI
* Phoenix, AZ
* New York, NY
* Chicago, IL

---

## 📁 Repository Structure

```
Climate-Data-Project/
│
├── .gitignore
├── README.md
├── report.md                 # Final markdown report
├── report.pdf                # Exported PDF version of the report
├── project3.py               # Python script used for analysis and plotting
├── data/                     # Raw CSV data (external links due to size)
│   └── placeholder.txt
├── images/                   # All generated figures
│   ├── avg_temp_chicago.png
│   ├── avg_temp_madison.png
│   ├── avg_temp_new_york.png
│   ├── avg_temp_phoenix.png
│   ├── all_avg_temp.png
│   ├── annual_max_temperature.png
│   └── hot_days_by_city.png
```

---

## ▶️ How to Run the Code

1. Clone this repository:

   ```bash
   git clone https://github.com/Klina123/Climate-Data-Project.git
   cd Climate-Data-Project
   ```

2. Install dependencies:

   ```bash
   pip install pandas matplotlib
   ```

3. Download the data files and place them inside the `data/` folder.

---

## 🔗 Data Access

Due to GitHub's file size limitations, the CSV files are hosted externally:

* [Madison.csv](https://drive.google.com/file/d/1aoSTqCPlN9f2_6Vn-HmHETCkYTPVKwQf/view?usp=sharing)
* [Phoenix.csv](https://drive.google.com/file/d/1S0ZdmUMZZh3P-BaO6ljrZAFCwqs7N0a6/view?usp=sharing)
* [New York.csv](https://drive.google.com/file/d/1OX2Nz7zvAbkefH9MHn_MQVD2-1DrGCqa/view?usp=sharing)
* [Chicago.csv](https://drive.google.com/file/d/1L2MNsNhjueT-JrdjHH3JvP-IFVrso9HF/view?usp=sharing)

Make sure to download these files and place them in the `data/` directory to re-run the analysis.

---

## 📊 Outputs

The analysis generates the following charts (in the `images/` folder):

* `avg_temp_*.png`: Annual average temperature line plots for each city
* `all_avg_temp.png`: Combined average temperature trends
* `annual_max_temperature.png`: Yearly highest daily temperature
* `hot_days_by_city.png`: Number of days above 90°F

---

## 📄 Report

See the full results, visualizations, and interpretation in:

* `report.md` – The markdown version of the final report
* `report.pdf` – Printable version of the same report

---

## 🧑‍💻 Author

**Klina123**
[https://github.com/Klina123](https://github.com/Klina123)
