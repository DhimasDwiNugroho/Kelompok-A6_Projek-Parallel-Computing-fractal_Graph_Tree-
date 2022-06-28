import turtle
import queue
import threading
from multiprocessing import Process
import multiprocessing
import time

MINIMUM_BRANCH_LENGTH = 5
def build_tree(t, branch_length, shorten_by, angle):
  if branch_length > MINIMUM_BRANCH_LENGTH:
    t.forward(branch_length)
    new_length = branch_length - shorten_by
    t.left(angle)
    build_tree(t, new_length, shorten_by, angle)
    t.right(angle * 2)
    build_tree(t, new_length, shorten_by, angle)
    t.left(angle)
    t.backward(branch_length)

def process_queue():
    while not graphics.empty():
        (graphics.get())(1)

    if threading.active_count() >= 1:
        turtle.ontimer(process_queue, 100)

def process_queue2():
    while not graphics.empty():
        (graphics.get())(1)

    if threading.active_count() >= 1:
        turtle.ontimer(process_queue2, 100)

start_time = time.time()
graphics = queue.Queue(2)  # size = number of hardware threads you have - 1

tree = turtle.Turtle()
tree.hideturtle()
tree.setheading(90)
tree.color('green')
tree.speed(0)
thread1 = threading.Thread(target=build_tree, args=(tree, 50, 5, 30))
thread1.daemon = True  # thread dies when main thread (only non-daemon thread) exits.
thread1.start()


process_queue()

if __name__ == "main":
    Multi1 = multiprocessing.Process(target=process_queue())
    Multi1.start()
    Multi2 = multiprocessing.Process(target=process_queue())
    Multi2.start()
 
    Multi1.join()
    Multi2.join()

turtle.mainloop() 

finish_time = time.time()
print(f"Program finished in {finish_time-start_time} seconds")