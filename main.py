import argparse
from model import KMeans
from utils import get_image, show_image, save_image, error


def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='K-Means Clustering on Image')
    parser.add_argument('--num_clusters', type=int, default=50, help='Number of clusters for K-Means')
    parser.add_argument('--image', type=str, default='image/input_image.jpg')
    args = parser.parse_args()

    # get image
    original_image = get_image(args.image)
    img_shape = original_image.shape

    # reshape image
    image = original_image.reshape(original_image.shape[0] * original_image.shape[1], original_image.shape[2])

    # create model
    kmeans = KMeans(args.num_clusters)

    # fit model
    kmeans.fit(image)

    # replace each pixel with its closest cluster center
    image = kmeans.replace_with_cluster_centers(image)

    # reshape image
    image_clustered = image.reshape(img_shape)

    # Print the error
    print('MSE:', error(original_image, image_clustered))

    # show/save image
    # show_image(image)
    save_image(image_clustered, f'image/image_clustered_{args.num_clusters}.jpg')

if __name__ == '__main__':
    main()
