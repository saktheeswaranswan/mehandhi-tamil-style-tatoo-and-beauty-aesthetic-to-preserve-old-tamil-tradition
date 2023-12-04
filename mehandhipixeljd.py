import cv2
import csv
import numpy as np

def get_dark_pixels(image_path, max_points=1000, threshold=100):
    # Read the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Find dark pixels based on the threshold
    dark_pixels = (gray_image < threshold)

    # Get the coordinates of dark pixels
    dark_pixel_coords = np.column_stack(np.where(dark_pixels))

    # If there are more than max_points, randomly select max_points
    if len(dark_pixel_coords) > max_points:
        indices = np.random.choice(len(dark_pixel_coords), max_points, replace=False)
        dark_pixel_coords = dark_pixel_coords[indices]

    return dark_pixel_coords.tolist()

def save_dark_pixels_to_csv(dark_pixel_coords, csv_filename):
    with open(csv_filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['X', 'Y'])

        for coord in dark_pixel_coords:
            csv_writer.writerow(coord)

if __name__ == "__main__":
    image_path = "/home/josva/Music/mehandhi/fggf.jpg"
    csv_filename = "dark_pixelfs.csv"
    max_points = 100000
    threshold_value = 100

    dark_pixel_coords = get_dark_pixels(image_path, max_points, threshold_value)
    save_dark_pixels_to_csv(dark_pixel_coords, csv_filename)

    print(f"Dark pixel coordinates saved to {csv_filename}")

