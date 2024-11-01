import matplotlib.pyplot as plt
thermal_categories = ["Winter Thermal Production", "Summer Thermal Production"]
thermal_values = [44.69, 63.44]
plt.figure(figsize=(10, 5))
plt.bar(thermal_categories, thermal_values, color=['lightgreen', 'salmon'])
plt.xlabel('Season')
plt.ylabel('Energy Production (kWh per day)')
plt.title('Theoretical Energy Production of Solar Thermal System')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()