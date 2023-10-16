EE_pose:
    transformation from base_link to ee_arm_link

Tag_pose:
    transformation from base_link to tag_link

Joint_X_pose:
    transformation from XXX_link to XXX_link
        6-Dof joints [waist, shoulder, elbow, forearm_roll, wrist_angle, wrist_rotate]
        1. waist	: from base_link to shoulder_link
        2. shoulder	: from shoulder_link to upper_arm_link
        3. elbow	: from upper_arm_link to upper_forearm_link
        4. forearm_roll: from upper_forearm_link to lower_forearm_link
        5. wrist_angle	: from lower_forearm_link to wrist_link
        6. wrist_rotate: from wrist_link to gripper_link

Bag file link:
    https://drive.google.com/file/d/17FuqYJxAqzs8viGosXYHOcTsuHzu6Ib9/view?usp=sharing

Tag description:
    Family is "tag36h11", ID is "0.1.2", size is "0.0415"(m)
