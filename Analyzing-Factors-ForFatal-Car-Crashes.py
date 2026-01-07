import pandas as pd
import sys
import os

# Step 0: Change working directory
os.chdir(r"/Users/sahar/Desktop/Group Project cis 3920")
print(" Directory set to:", os.getcwd())

print("\n Starting crash data summary...")

# Step 1: Load datasets
try:
    crashes = pd.read_csv("Cleaned_Motor_Vehicle_Collisions.csv", low_memory=False)
    weather = pd.read_csv("Weather conditions.csv", low_memory=False)
    road = pd.read_csv("Road Conditions.csv", low_memory=False)
    print("Files loaded successfully.")
except Exception as e:
    print("Error loading files:", e)
    sys.exit()

# Step 2: Parse datetime columns
try:
    crashes['CRASH_DATETIME'] = pd.to_datetime(crashes['CRASH_DATETIME'], errors='coerce')
    weather['DateTime'] = pd.to_datetime(weather['DateTime'], errors='coerce')
    road['e_spec_date'] = pd.to_datetime(road['e_spec_date'], errors='coerce')
except Exception as e:
    print("Error parsing dates:", e)

# Step 3: Clean crash data
crashes.rename(columns={
    'VEHICLE TYPE CODE 1': 'VEHICLE_TYPE',
    'CONTRIBUTING FACTOR VEHICLE 1': 'CONTRIBUTING_FACTOR_1'
}, inplace=True)

crashes['NUMBER OF PERSONS KILLED'] = crashes['NUMBER OF PERSONS KILLED'].fillna(0).astype(float)

# Step 4: Crash summary
try:
    total_crashes = len(crashes)
    fatal_crashes = crashes['NUMBER OF PERSONS KILLED'].gt(0).sum()
    ford_crashes = crashes['VEHICLE_TYPE'].str.contains('FORD', na=False, case=False).sum()
    ford_fatal = crashes[crashes['VEHICLE_TYPE'].str.contains('FORD', na=False, case=False)]['NUMBER OF PERSONS KILLED'].gt(0).sum()

    ford_fatal_rate = (ford_fatal / ford_crashes * 100) if ford_crashes > 0 else 0
    non_ford_crashes = total_crashes - ford_crashes
    non_ford_fatal = fatal_crashes - ford_fatal
    non_ford_fatal_rate = (non_ford_fatal / non_ford_crashes * 100) if non_ford_crashes > 0 else 0
except Exception as e:
    print(" Error calculating summary stats:", e)
    sys.exit()

# Step 5: Create Summary Table
summary_df = pd.DataFrame({
    'Metric': [
        'Total number of crashes',
        'Number of crashes involving fatalities',
        'Number of crashes involving Ford vehicles',
        'Number of Ford-involved crashes that were fatal',
        'Fatal crash rate for Ford-involved crashes (%)',
        'Fatal crash rate for non-Ford crashes (%)'
    ],
    'Value': [
        total_crashes,
        fatal_crashes,
        ford_crashes,
        ford_fatal,
        round(ford_fatal_rate, 2),
        round(non_ford_fatal_rate, 2)
    ]
})

# Step 6: Output results
print("\nCrash Data Summary (No Merging):")
print(summary_df.to_string(index=False))
sys.stdout.flush()
