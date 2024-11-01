# Typical Performance Calculation for a Typical Meteorological Year (TMY) in Delhi
# Adjusting the production by reducing the clear-sky production by a typical cloud cover factor

import numpy as np
import matplotlib.pyplot as plt

# Data for solar irradiance for each month in Delhi (in kWh/m²/day)
months = [
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
]
irradiance = [3.5, 4.5, 5.8, 6.5, 7.0, 6.8, 5.5, 5.4, 5.8, 5.9, 4.5, 3.6]

# Monthly days in each month
monthly_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Solar PV System Design
pv_capacity_kw = 9  # PV system capacity in kW
pv_area_m2 = 2.5    # Area for thermal collector in m²
pv_efficiency = 20.8  # Typical PV efficiency
demand_pv_daily_kwh = 27.5  # Daily demand for PV in kWh

# Solar Thermal System Design
thermal_output_kw = 5  # Thermal system capacity in kW
thermal_efficiency = 0.70  # Efficiency of flat plate collector
demand_thermal_daily_kwh = 5 * 6  # Daily demand for thermal in kWh (5 kW for 6 hours)

# Clear-sky calculations for PV and Thermal performance
pv_energy_production = []
thermal_energy_production = []

for month_irradiance, days in zip(irradiance, monthly_days):
    # PV System production (assuming full clear sky conditions)
    monthly_pv_kwh = pv_capacity_kw * month_irradiance * days  # kWh per month
    pv_energy_production.append(monthly_pv_kwh)
    
    # Thermal System production (using irradiance and efficiency)
    monthly_thermal_kwh = pv_area_m2 * month_irradiance * days * thermal_efficiency  # kWh per month
    thermal_energy_production.append(monthly_thermal_kwh)

# Typical Meteorological Year (TMY) Adjustments
# Assuming typical cloud cover reduces production by 20% throughout the year
cloud_cover_reduction = 0.20  # 20% reduction due to typical meteorological conditions

# Simulate the impact of TMY on PV and Thermal production
pv_energy_production_tmy = []
thermal_energy_production_tmy = []

for month_index, days in enumerate(monthly_days):
    # PV Production for TMY
    monthly_pv_kwh_tmy = pv_energy_production[month_index] * (1 - cloud_cover_reduction)
    pv_energy_production_tmy.append(monthly_pv_kwh_tmy)
    
    # Thermal Production for TMY
    monthly_thermal_kwh_tmy = thermal_energy_production[month_index] * (1 - cloud_cover_reduction)
    thermal_energy_production_tmy.append(monthly_thermal_kwh_tmy)

# Convert lists to arrays for easier calculations
pv_energy_production_tmy = np.array(pv_energy_production_tmy)
thermal_energy_production_tmy = np.array(thermal_energy_production_tmy)

# Plot PV System - Monthly Production (Clear vs TMY)
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.bar(months, pv_energy_production, color='skyblue', edgecolor='black', alpha=0.7, label='Clear Sky Production')
plt.bar(months, pv_energy_production_tmy, color='blue', edgecolor='black', alpha=0.7, label='TMY Adjusted Production')
plt.xlabel('Month')
plt.ylabel('Energy (kWh)')
plt.title('PV System - Monthly Production (Clear vs TMY)')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Plot Thermal System - Monthly Production (Clear vs TMY)
plt.subplot(1, 2, 2)
plt.bar(months, thermal_energy_production, color='lightgreen', edgecolor='black', alpha=0.7, label='Clear Sky Production')
plt.bar(months, thermal_energy_production_tmy, color='darkgreen', edgecolor='black', alpha=0.7, label='TMY Adjusted Production')
plt.xlabel('Month')
plt.ylabel('Energy (kWh)')
plt.title('Thermal System - Monthly Production (Clear vs TMY)')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()
