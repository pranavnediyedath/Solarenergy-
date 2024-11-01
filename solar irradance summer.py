import numpy as np
import matplotlib.pyplot as plt

# Constants for Summer's Day
latitude = 28.7  # Latitude of Delhi in degrees
declination = 20.34  # Declination around May 21st (Summer Solstice) in degrees
tilt_angle = latitude  # Tilt angle equal to latitude
azimuth_angle = -15  # Azimuth angle for tilted panel (15° to the East)

# Sunrise, Sunset, and Length of Day for Summer Day (e.g., June 21st)
sunrise = "05:20 AM"
sunset = "07:25 PM"
length_of_day = "14 hours and 05 minutes"

# Time range from sunrise to sunset (5:28 AM to 7:21 PM)
hours = np.linspace(5 + 20/60, 19 + 25/60, 100)  # Hours from 5:28 AM to 7:21 PM

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
# Using a simplified model for GHI, peaking at 1000 W/m² around solar noon
ghi_max = 1000  # Max GHI at noon
ghi_horizontal = ghi_max * np.maximum(0, np.sin(np.radians(solar_altitudes)))

# Incidence angle on tilted plate calculation
def incidence_tilted(latitude, declination, hour_angle, tilt_angle, azimuth_angle):
    cos_theta = (np.sin(np.radians(declination)) * np.sin(np.radians(latitude)) * np.cos(np.radians(tilt_angle)) +
                 np.cos(np.radians(declination)) * np.cos(np.radians(latitude)) * np.cos(np.radians(hour_angle)) * np.cos(np.radians(tilt_angle)) +
                 np.cos(np.radians(declination)) * np.sin(np.radians(tilt_angle)) * np.sin(np.radians(hour_angle - azimuth_angle)))
    cos_theta = np.clip(cos_theta, -1.0, 1.0)
    return np.degrees(np.arccos(cos_theta))

# Incidence angle on tilted plate
incidence_tilted_values = incidence_tilted(latitude, declination, hour_angles, tilt_angle, azimuth_angle)

# Solar irradiance on tilted plate (assuming clear sky model)
# Using a simplified model, scaling by cosine of incidence angle
ghi_tilted = ghi_max * np.maximum(0, np.cos(np.radians(incidence_tilted_values)))

# Printing the values
print("Summer's Day Solar Resource (June 21st):")
print("Sunrise:", sunrise)
print("Sunset:", sunset)
print("Length of Day:", length_of_day)
print("\nTime (Hours):")
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
plt.title('Incidence Angles for Horizontal and Tilted Plates (Clear Sky Summer Day in Delhi)')
plt.legend()
plt.grid(True)

# Plotting Irradiance
plt.subplot(2, 1, 2)
plt.plot(hours, ghi_horizontal, label='Solar Irradiance (Horizontal Plate)', color='b', linestyle='-', linewidth=2)
plt.plot(hours, ghi_tilted, label='Solar Irradiance (Tilted Plate)', color='r', linestyle='--', linewidth=2)
plt.xlabel('Time of Day (Hours)')
plt.ylabel('Solar Irradiance (W/m²)')
plt.title('Solar Irradiance for Horizontal and Tilted Plates (Clear Sky Summer Day in Delhi)')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()