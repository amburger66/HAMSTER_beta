import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Load the image
img_path = "examples/ocr_reasoning.jpg"  # Make sure the image is in the same directory
img = mpimg.imread(img_path)
height, width, _ = img.shape

# Keypoints from the solution (normalized 0-1)
keypoints = [
    (0.58, 0.28),  # Start
    (0.59, 0.62),  # Grasp 'S'
    (0.59, 0.45),  # Lift
    (0.65, 0.47),  # Place on Pink Plate
]

# Convert to pixel coordinates
pixel_points = [(x * width, y * height) for x, y in keypoints]
x_coords, y_coords = zip(*pixel_points)

# Plotting
plt.figure(figsize=(10, 6))
plt.imshow(img)

# Draw the trajectory line
plt.plot(x_coords, y_coords, "b-", linewidth=2, label="Trajectory")

# Mark the points
plt.scatter(x_coords, y_coords, c="red", s=50, zorder=5)

# Annotate specific actions
plt.annotate(
    "Start",
    (x_coords[0], y_coords[0]),
    xytext=(0, -10),
    textcoords="offset points",
    color="white",
    fontweight="bold",
)
plt.annotate(
    "Grasp (Close)",
    (x_coords[1], y_coords[1]),
    xytext=(10, 0),
    textcoords="offset points",
    color="yellow",
    fontweight="bold",
)
plt.annotate(
    "Lift",
    (x_coords[2], y_coords[2]),
    xytext=(-30, 0),
    textcoords="offset points",
    color="white",
    fontweight="bold",
)
plt.annotate(
    "Place (Open)",
    (x_coords[3], y_coords[3]),
    xytext=(10, 0),
    textcoords="offset points",
    color="yellow",
    fontweight="bold",
)

plt.title("Robot Gripper Trajectory")
plt.axis("off")
plt.show()
