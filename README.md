# ClusterCompress

ClusterCompress is a simple image compression tool using K-Means clustering. It reduces the number of unique colors in an image, compressing it while preserving visual quality.

## Features
- Implements K-Means from scratch using NumPy
- Compresses images by reducing color space
- Supports command-line input for number of clusters
- Dockerized for portability and easy setup

## Example
Original image → ClusterCompress with k=16 → Output image with reduced colors.

## Project Structure
ClusterCompress/
├── Dockerfile
├── requirements.txt
├── .dockerignore
├── .gitignore
├── main.py
├── model.py
├── utils.py
├── image/
│   └── input_image.jpg
└── README.md

## Installation

### Run with Docker

You can build and run the project entirely in Docker without needing to install dependencies manually.

### Build the Docker Image
From the root directory of the project, run:
```bash
    docker build -t clustercompress .
```

### Run the Container
Mount the image directory (to access input/output) and pass the desired number of clusters:
```bash
    docker run -it --rm -v $(pwd):/app clustercompress /bin/bash
```

### Run the python script
Once you are in the container's shell, execute the following command.
```bash
    python main.py 
```

## Input/Output
- Input image should be at: image/input_image.jpg
- Output will be saved as: image_clustered_32.jpg

## Arguments
--num_clusters (int): Number of color clusters (e.g., 16, 32, 64)  
--image (file path): Image file path (e.g., 'image/input_image.jpg')

## How It Works
1. Loads and normalizes the image
2. Reshapes the image into a list of RGB pixels
3. Applies K-Means to group colors into clusters
4. Reconstructs the image using cluster centers
5. Saves the compressed image

## Example Results
| k   | Description                          |
|-----|--------------------------------------|
| 8   | High compression, lower quality      |
| 32  | Good balance                        |
| 64  | Near-original quality               |

## Testing & Debugging
To visualize results:
```python
    from utils import show_image
    show_image(image_clustered)
```
