import pandas as pd
import matplotlib.pyplot as plt

star_data = pd.read_csv("habitable_star_data.csv")

star_name = star_data["Star Name"]
distance = star_data["Distance (ly)"]
mass = star_data["Mass (M☉)"]
radius = star_data["Radius (R☉)"]
gravity = star_data["Surface Gravity (m/s²)"]

plt.figure()
plt.bar(star_name, mass)
plt.xlabel("Star Names")
plt.ylabel("Mass of Stars")
plt.title("Star Name vs Mass")
plt.xticks(rotation = 90)

plt.figure()
plt.bar(star_name, radius)
plt.xlabel("Star Names")
plt.ylabel("Radius of Stars")
plt.title("Star Name vs Radius")
plt.xticks(rotation = 90)

plt.figure()
plt.bar(star_name, distance)
plt.xlabel("Star Names")
plt.ylabel("Distance of Stars")
plt.title("Star Name vs Distance")
plt.xticks(rotation = 90)

plt.figure()
plt.bar(star_name, gravity)
plt.xlabel("Star Names")
plt.ylabel("Gravity of Stars")
plt.title("Star Name vs Gravity")
plt.xticks(rotation = 90)

plt.show()