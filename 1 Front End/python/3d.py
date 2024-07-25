import cv2
import numpy as np
import open3d as o3d

def load_image(image_path):
    # Carregar a imagem
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise ValueError(f"Imagem não encontrada no caminho: {image_path}")
    return img

def create_point_cloud(image):
    # Gerar uma nuvem de pontos a partir da imagem
    h, w = image.shape
    points = []
    for y in range(h):
        for x in range(w):
            z = image[y, x] / 255.0  # Normalizar o valor da profundidade
            points.append([x, y, z])
    points = np.array(points)

    # Criar a nuvem de pontos usando Open3D
    point_cloud = o3d.geometry.PointCloud()
    point_cloud.points = o3d.utility.Vector3dVector(points)
    return point_cloud

def main(image_path):
    # Carregar a imagem
    image = load_image(image_path)

    # Criar a nuvem de pontos
    point_cloud = create_point_cloud(image)

    # Visualizar a nuvem de pontos
    o3d.visualization.draw_geometries([point_cloud])

if __name__ == "__main__":
    image_path = "C:/Users/gusta/Downloads/logo-removebg-preview.png"
    main(image_path)