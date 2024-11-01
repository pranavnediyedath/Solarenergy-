import matplotlib.pyplot as plt

# Data for separate graphs
pv_categories = ["Winter PV Production", "Summer PV Production"]
pv_values = [42.27, 65.13]  # kWh/day

thermal_categories = ["Winter Thermal Production", "Summer Thermal Production"]
thermal_values = [44.69, 63.44]  # kWh/day

# Create separate line plots for PV and Thermal Production

# Line plot for PV Production
plt.figure(figsize=(10, 5))
plt.plot(pv_categories, pv_values, marker='o', color='blue', label='PV Production')
plt.xlabel('Season')
plt.ylabel('Energy Production (kWh per day)')
plt.title('Theoretical Energy Production of Solar PV System')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()

# Line plot for Thermal Production
plt.figure(figsize=(10, 5))
plt.plot(thermal_categories, thermal_values, marker='o', color='green', label='Thermal Production')
plt.xlabel('Season')
plt.ylabel('Energy Production (kWh per day)')
plt.title('Theoretical Energy Production of Solar Thermal System')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()
