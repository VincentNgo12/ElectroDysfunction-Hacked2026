from ethan_face_tracking import update_servo
from ethan_servo_gesture import go_home

print("=== Vision Tracking Test ===")
print("Enter a point as two numbers: x y")
print("Type 'home' to return servos to home position")
print("Type 'q' to quit")

go_home()

while True:

    user_input = input("\nEnter point (x y): ").strip().lower()

    if user_input == 'q':
        print("Exiting tracking test.")
        break

    elif user_input == 'home':
        go_home()

    else:
        try:
            x, y = map(float, user_input.split())
            print(f"Calling update_servo(({x}, {y}))")
            update_servo((x, y))

        except ValueError:
            print("Invalid input. Enter two numbers separated by a space, e.g. 1000 20")