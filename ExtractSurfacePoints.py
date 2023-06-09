import os
from stl import mesh
import trimesh
import datetime
import numpy as np
import h5py

now = datetime.datetime.now()

data_dir = './ModelNet40'
save_dir = './ModelNet40stl'
categories = {
    'airplane': 0,
    'bathtub': 1,
    'bed': 2,
    'bench': 3,
    'bookshelf': 4,
    'bottle': 5,
    'bowl': 6,
    'car': 7,
    'chair': 8,
    'cone': 9,
    'cup': 10,
    'curtain': 11,
    'desk': 12,
    'door': 13,
    'dresser': 14,
    'flower_pot': 15,
    'glass_box': 16,
    'guitar': 17,
    'keyboard': 18,
    'lamp': 19,
    'laptop': 20,
    'mantel': 21,
    'monitor': 22,
    'night_stand': 23,
    'person': 24,
    'piano': 25,
    'plant': 26,
    'radio': 27,
    'range_hood': 28,
    'sink': 29,
    'sofa': 30,
    'stairs': 31,
    'stool': 32,
    'table': 33,
    'tent': 34,
    'toilet': 35,
    'tv_stand': 36,
    'vase': 37,
    'wardrobe': 38,
    'xbox': 39
}

if not os.path.exists(save_dir):
    os.makedirs(save_dir)

for category in categories:
    cat_dir = os.path.join(data_dir, category, 'train')
    save_cat_dir = os.path.join(save_dir, category)
    if not os.path.exists(save_cat_dir):
        os.makedirs(save_cat_dir)
    files = os.listdir(cat_dir)
    for filename in files:
        file_path = os.path.join(cat_dir, filename)
        now = datetime.datetime.now()
        print(now.strftime('%y%m%d - %H:%M:%S'), ' ', filename)
        save_path = os.path.join(save_cat_dir, filename.split('.')[0] + '.stl')
        if os.path.exists(save_path):
            continue
        now = datetime.datetime.now()
        # print(now.strftime('%y%m%d - %H:%M:%S'), ' ', '진행')
        # stl 파일로 변환
        mesh = trimesh.load(file_path)
        mesh.export(save_path)
        now = datetime.datetime.now()
        # print(now.strftime('%y%m%d - %H:%M:%S'), ' ', filename, '저장 완료')

now = datetime.datetime.now()
print('off to stl (train) complate')

for category in categories:
    cat_dir = os.path.join(data_dir, category, 'test')
    save_cat_dir = os.path.join(save_dir, category)
    if not os.path.exists(save_cat_dir):
        os.makedirs(save_cat_dir)
    files = os.listdir(cat_dir)
    for filename in files:
        file_path = os.path.join(cat_dir, filename)
        now = datetime.datetime.now()
        print(now.strftime('%y%m%d - %H:%M:%S'), ' ', filename)
        save_path = os.path.join(save_cat_dir, filename.split('.')[0] + '.stl')
        if os.path.exists(save_path):
            continue
        now = datetime.datetime.now()
        # print(now.strftime('%y%m%d - %H:%M:%S'), ' ', '진행')
        # stl 파일로 변환
        mesh = trimesh.load(file_path)
        mesh.export(save_path)
        now = datetime.datetime.now()
        # print(now.strftime('%y%m%d - %H:%M:%S'), ' ', filename, '저장 완료')

now = datetime.datetime.now()
print('off to stl (test) complate')

def make_Points(file_path, n_points):

    mesh = trimesh.load(file_path)
    points, _ = trimesh.sample.sample_surface(mesh, n_points)
    min_xyz = np.min(points, axis=0)
    max_xyz = np.max(points, axis=0)
    scale = 1.0 / np.max(max_xyz - min_xyz)
    points_scaled = scale * (points - min_xyz)
    # print(points_scaled)

    return points_scaled

# Define input and output directories
stl_dir = './ModelNet40stl'
np_dir = './ModelNet40pcd'

# Create np_dir if it does not exist
if not os.path.exists(np_dir):
    os.makedirs(np_dir)

# # Define categories to process
# categories = os.listdir(stl_dir)

# Loop over categories
for category in categories:
    print('Processing category:', category)

    # Create output directory for current category
    current_np_dir = os.path.join(np_dir, category)
    if not os.path.exists(current_np_dir):
        os.makedirs(current_np_dir)

    # Get file list for current category
    category_dir = os.path.join(stl_dir, category)
    files = os.listdir(category_dir)

    # Loop over files in category
    for file in files:
        # Read stl file
        file_path = os.path.join(category_dir, file)
        print(now.strftime('%y%m%d - %H:%M:%S'), ' ', file)
        points = make_Points(file_path, n_points=2048)

        # Save npy file
        npy_file_path = os.path.join(current_np_dir, file.split('.')[0] + '.npy')
        np.save(npy_file_path, {'points': points})