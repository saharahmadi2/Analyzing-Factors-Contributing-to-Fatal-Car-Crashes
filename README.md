# Analyzing-Factors-Contributing-to-Fatal-Car-Crashes
This project focuses on analyzing a real-world dataset to better understand the relationships between key variables and the outcomes they influence.
Analyzing Factors Contributing to Fatal Car Crashes: A Case Study of Ford Vehicles
Overview

A recent industry report claims that Ford vehicles are involved in the highest number of fatal car crashes. This project investigates whether Ford’s higher involvement in fatal crashes is causal or simply correlational, driven by factors such as market share, traffic exposure, weather conditions, and road conditions.

The objective is to determine whether Ford vehicles are inherently more dangerous or whether external factors explain the observed fatality rates.

Research Question

Does the involvement of Ford vehicles increase the likelihood of fatal crashes, or is Ford’s higher fatal crash count primarily explained by non-causal factors such as exposure, weather, and road conditions?

Data Sources

Motor_Vehicle_Collisions_-_Crashes.csv
NYC crash data containing vehicle make, injury and fatality counts, contributing factors, vehicle damage, and crash details.

Weather Data (National Weather Service)
Historical weather conditions at the time of each crash (rain, snow, fog, etc.).

Road Conditions & Maintenance Data (NYC DOT)
Information on road quality, construction zones, and maintenance activity.

Methodology
1. Data Cleaning & Preprocessing

Handle missing and extreme values

Standardize vehicle make categories

Merge weather and road condition datasets with crash data

2. Exploratory Data Analysis (EDA)

Compare fatal crash rates between Ford and other vehicle makes

Analyze the impact of weather and road conditions on crash severity

Visualize trends and distributions

3. Modeling

Regression models are used to predict the likelihood of a fatal crash while controlling for external factors.

Dependent Variable

Fatal crash indicator

Independent Variables

VEHICLE_MAKE

NUMBER_OF_PERSONS_INJURED

NUMBER_OF_PERSONS_KILLED

CONTRIBUTING_FACTOR_1

VEHICLE_DAMAGE

VEHICLE_TYPE

POINT_OF_IMPACT

Weather conditions

Road conditions 

Hypothesis

Ford’s higher involvement in fatal crashes is primarily due to market share and exposure, along with environmental factors such as weather and road conditions. After controlling for these variables, we expect no significant difference in fatal crash risk between Ford vehicles and other popular makes.



Conclusion

This project provides an empirical evaluation of fatal crash risk by vehicle make. By incorporating external factors such as weather and road conditions, the analysis helps distinguish correlation from causation in assessing vehicle safety.
