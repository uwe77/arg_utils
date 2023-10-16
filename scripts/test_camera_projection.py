import os
import pytest
import numpy as np
import add_path
import matplotlib.pyplot as plt
from arg_utils.camera_projection import camera_projection as cam_proj

@pytest.fixture

def test_read_camera_info():
    test_cam_proj = cam_proj()
    test_cam_proj.read_camera_info('datas/ViperX_apriltags/camera_info.yaml')
    assert np.array_equal(test_cam_proj.camera_matrix, np.array([[615.73449707, 0., 317.83758545], [0., 616.25183105, 241.18086243], [0., 0., 1.]]))
    assert np.array_equal(test_cam_proj.dist_coeffs, np.array([[0, 0, 0, 0, 0]]))
    assert test_cam_proj.cameraParams_Intrinsic == [615.7344970703125, 616.2518310546875, 317.8375854492188, 241.1808624267578]

# def test_read_images():
#     test_cam_proj = cam_proj()
#     test_cam_proj.read_images(idx=300, img_path='ViperX_apriltags/rgb/', depth_path='ViperX_apriltags/depth/')
#     assert test_cam_proj.img is not None
#     assert test_cam_proj.gray is not None
#     assert test_cam_proj.depth is not None
#     assert test_cam_proj.img_dst is not None

if __name__ == '__main__':
    test_cam_proj = cam_proj()
    test_cam_proj.read_camera_info('datas/ViperX_apriltags/camera_info.yaml')
    test_cam_proj.read_images(idx=300, img_path='datas/ViperX_apriltags/rgb/', depth_path='datas/ViperX_apriltags/depth/')
    test_cam_proj.apriltag_detection('tag36h11')
    test_cam_proj.solvePnP(0.0415)
    draw_image = test_cam_proj.draw_point()
    figsize = 15 # param larger is bigger, adjust as needed
    plt.rcParams['figure.figsize'] = (figsize, figsize)
    plt.imshow(draw_image, cmap = 'brg')
    plt.show()
    joints = ['Joint_1_pose', 'Joint_2_pose', 
          'Joint_3_pose', 'Joint_4_pose', 
          'Joint_5_pose', 'Joint_6_pose']

    for joint in joints:
        joint_data = np.array(data[joint][0]['transformation_matrix'][0])
        joint_data = joint_data.reshape(4, 4)
        if joints.index(joint) > 0:
        joint_data = np.matmul(previous_data, joint_data)
        draw_image = cam_project.draw_point(tag_2_inv, joint_data)
        previous_data = joint_data
        
    plt.imshow(draw_image, cmap = 'brg')
    plt.show()
