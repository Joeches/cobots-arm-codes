import urlib
import time

def pick_and_place(joint_names, object_name, destination_joint_name):
    # Connect to the cobot arm
    ur = urlib.UrSDK()
    arm = ur.get_arm(joint_names[0])

    # Move the arm to the pickup position
    arm.move_to_position(joint_names[1], joint_names[2], joint_names[3])

    # Pick up the object
    arm.pick_up_object(object_name)

    # Move the arm to the drop-off position
    arm.move_to_position(joint_names[4], joint_names[5], joint_names[6])

    # Drop off the object
    arm.drop_off_object(destination_joint_name)

    # Disconnect from the cobot arm
    arm.disconnect()
    ur.disconnect()

# Example usage:
pick_and_place(['joint1', 'joint2', 'joint3', 'joint4', 'joint5', 'joint6'], 'object1', 'joint7')
