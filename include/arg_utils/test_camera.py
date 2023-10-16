import os
import pytest
import numpy as np
from camera_projection import camera_projection

# a = camera_projection()
# a.read_camera_info()

@pytest.fixture
def camera_info_path():
    return os.path.join(os.path.dirname(__file__), 'ViperX_apriltags/test_camera_info.yaml')

def test_read_camera_info(camera_info_path, monkeypatch):
    expected_camera_matrix = np.array([[615.73449707, 0., 317.83758545], 
                                       [0., 616.25183105, 241.18086243], 
                                       [0., 0., 1.]])
    expected_dist_coeffs = np.array([[0, 0, 0, 0, 0]])
    my_class = camera_projection()
    my_class.read_camera_info()
    assert np.array_equal(my_class.camera_matrix, expected_camera_matrix)
    assert np.array_equal(my_class.dist_coeffs, expected_dist_coeffs)
    assert my_class.cameraParams_Intrinsic == [615.7344970703125, 616.2518310546875, 317.8375854492188, 241.1808624267578]
    # mock_open.assert_called_once_with(camera_info_path, 'r')