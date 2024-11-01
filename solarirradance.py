import numpy as np
import matplotlib.pyplot as plt

# Constants
latitude = 28.7  # Latitude of Delhi in degrees
declination = -19.93  # Declination on December 21st in degrees
tilt_angle = latitude  # Tilt angle equal to latitude
azimuth_angle = -15  # Azimuth angle for tilted panel (15° to the East)

# Time range from sunrise to sunset (7:10 AM to 5:30 PM)
hours = np.linspace(7 + 10/60, 17 + 30/60, 100)  # Hours from 7:10 AM to 5:29 PM

# Solar hour angle (h) calculation
solar_noon = 12.0
hour_angles = 15 * (hours - solar_noon)  # Solar hour angle in degrees

# Function to calculate solar altitude angle (alpha)
def solar_altitude(latitude, declination, hour_angle):
    return np.degrees(np.arcsin(np.sin(np.radians(latitude)) * np.sin(np.radians(declination)) +
                                np.cos(np.radians(latitude)) * np.cos(np.radians(declination)) * np.cos(np.radians(hour_angle))))

# Solar altitude angle for the given hours
solar_altitudes = solar_altitude(latitude, declination, hour_angles)

# Incidence angle on a horizontal plate (complement of solar altitude angle)
incidence_horizontal = 90 - solar_altitudes

# Solar irradiance on horizontal plate (assuming a clear sky model)
# Using a simplified model for GHI, peaking at 600 W/m² around solar noon
ghi_max = 600  # Max GHI at noon
ghi_horizontal = ghi_max * np.maximum(0, np.sin(np.radians(solar_altitudes)))

# Incidence angle on tilted plate calculation
def incidence_tilted(latitude, declination, hour_angle, tilt_angle, azimuth_angle):
    return np.degrees(np.arccos(np.sin(np.radians(declination)) * np.sin(np.radians(latitude)) * np.cos(np.radians(tilt_angle)) +
                                np.cos(np.radians(declination)) * np.cos(np.radians(latitude)) * np.cos(np.radians(hour_angle)) * np.cos(np.radians(tilt_angle)) +
                                np.cos(np.radians(declination)) * np.sin(np.radians(tilt_angle)) * np.sin(np.radians(hour_angle - azimuth_angle))))

# Incidence angle on tilted plate
incidence_tilted_values = incidence_tilted(latitude, declination, hour_angles, tilt_angle, azimuth_angle)

# Solar irradiance on tilted plate (assuming clear sky model)
# Using a simplified model, scaling by cosine of incidence angle
ghi_tilted = ghi_max * np.maximum(0, np.cos(np.radians(incidence_tilted_values)))
print("Time (Hours):")
print(hours)
print("\nIncidence Angle (Horizontal Plate):")
print(incidence_horizontal)
print("\nSolar Irradiance (Horizontal Plate) [W/m²]:")
print(ghi_horizontal)
print("\nIncidence Angle (Tilted Plate):")
print(incidence_tilted_values)
print("\nSolar Irradiance (Tilted Plate) [W/m²]:")
print(ghi_tilted)

# Plotting the incidence angles and irradiance for both panels
plt.figure(figsize=(14, 10))

# Plotting Incidence Angles
plt.subplot(2, 1, 1)
plt.plot(hours, incidence_horizontal, label='Incidence Angle (Horizontal Plate)', color='b', linestyle='-', linewidth=2)
plt.plot(hours, incidence_tilted_values, label='Incidence Angle (Tilted Plate)', color='r', linestyle='--', linewidth=2)
plt.xlabel('Time of Day (Hours)')
plt.ylabel('Incidence Angle (Degrees)')
plt.title('Incidence Angles for Horizontal and Tilted Plates (Winter  Day in Delhi)')
plt.legend()
plt.grid(True)

# Plotting Irradiance
plt.subplot(2, 1, 2)
plt.plot(hours, ghi_horizontal, label='Solar Irradiance (Horizontal Plate)', color='b', linestyle='-', linewidth=2)
plt.plot(hours, ghi_tilted, label='Solar Irradiance (Tilted Plate)', color='r', linestyle='--', linewidth=2)
plt.xlabel('Time of Day (Hours)')
plt.ylabel('Solar Irradiance (W/m²)')
plt.title('Solar Irradiance for Horizontal and Tilted Plates (Clear Sky Day in Delhi)')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
