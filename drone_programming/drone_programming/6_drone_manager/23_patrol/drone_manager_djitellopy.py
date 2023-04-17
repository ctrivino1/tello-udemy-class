from djitellopy import Tello
import time

DEFAULT_DISTANCE = 30  # in cm
DEFAULT_SPEED = 10
DEFAULT_DEGREE = 10


class DroneManager(object):
    def __init__(self, speed=DEFAULT_SPEED):
        self.tello = Tello()
        self.speed = speed
        self.tello.connect()
        self.tello.streamon()
        self.tello.set_speed(speed)

    def __del__(self):
        self.tello.end()

    def takeoff(self):
        self.tello.takeoff()

    def land(self):
        self.tello.land()

    def move(self, direction, distance):
        distance = int(distance)
        if direction == 'up':
            self.tello.move_up(distance)
        elif direction == 'down':
            self.tello.move_down(distance)
        elif direction == 'left':
            self.tello.move_left(distance)
        elif direction == 'right':
            self.tello.move_right(distance)
        elif direction == 'forward':
            self.tello.move_forward(distance)
        elif direction == 'back':
            self.tello.move_back(distance)
        else:
            raise ValueError(f'Invalid direction: {direction}')

    def up(self, distance=DEFAULT_DISTANCE):
        self.move('up', distance)

    def down(self, distance=DEFAULT_DISTANCE):
        self.move('down', distance)

    def left(self, distance=DEFAULT_DISTANCE):
        self.move('left', distance)

    def right(self, distance=DEFAULT_DISTANCE):
        self.move('right', distance)

    def forward(self, distance=DEFAULT_DISTANCE):
        self.move('forward', distance)

    def back(self, distance=DEFAULT_DISTANCE):
        self.move('back', distance)

    def set_speed(self, speed):
        self.tello.set_speed(speed)

    def clockwise(self, degree=DEFAULT_DEGREE):
        self.tello.rotate_clockwise(degree)

    def counter_clockwise(self, degree=DEFAULT_DEGREE):
        self.tello.rotate_counter_clockwise(degree)

    def flip_front(self):
        self.tello.flip_forward()

    def flip_back(self):
        self.tello.flip_back()

    def flip_left(self):
        self.tello.flip_left()

    def flip_right(self):
        self.tello.flip_right()

    def patrol(self):
        self.is_patrol = True
        while self.is_patrol:
            self.move('up', DEFAULT_DISTANCE)
            self.rotate_clockwise(90)
            self.move('down', DEFAULT_DISTANCE)
            self.rotate_clockwise(90)
            self.move('back', DEFAULT_DISTANCE)
            self.rotate_clockwise(90)
            self.move('forward', DEFAULT_DISTANCE)
            self.rotate_clockwise(90)

    def stop_patrol(self):
        self.is_patrol = False
