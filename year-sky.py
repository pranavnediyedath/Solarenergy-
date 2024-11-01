import matplotlib.pyplot as plt
import numpy as np

# Sample data: average monthly solar irradiance in kWh/m² for a typical year in Delhi
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

# Typical solar irradiance data in kWh/m² (replace this with actual TMY data if available)
solar_irradiance = [
    120, 140, 180, 220, 240, 210,
    180, 170, 200, 210, 150, 130
]

# Create a bar graph
plt.figure(figsize=(10, 6))
plt.bar(months, solar_irradiance, color='orange')

# Add titles and labels
plt.title('Annual Typical Solar Resource for a Typical Meteorological Year (TMY) in Delhi')
plt.xlabel('Months')
plt.ylabel('Solar Irradiance (kWh/m²)')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the plot
plt.tight_layout()
plt.show()
