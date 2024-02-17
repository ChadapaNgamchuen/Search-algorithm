import pyglet
import random

# Create a window
window = pyglet.window.Window(width=1000, height=350, caption='Binary Search Visualization')
batch = pyglet.graphics.Batch()

# Generate a sorted list with random numbers ensuring 88 is included
numbers = sorted(random.sample(range(1, 200), 19) + [88])

# Variables to control the animation and search
left, right = 0, len(numbers) - 1
mid = (left + right) // 2
found = False
search_complete = False

def binary_search():
    global left, right, mid, found, search_complete
    if left <= right and not found:
        mid = (left + right) // 2
        if numbers[mid] == 88:
            found = True
        elif numbers[mid] < 88:
            left = mid + 1
        else:
            right = mid - 1
    else:
        search_complete = True

# Schedule the binary search to run every 0.5 seconds
pyglet.clock.schedule_interval(lambda dt: binary_search(), 0.5)

@window.event
def on_draw():
    window.clear()
    for i, number in enumerate(numbers):
        # Define the position and size of each 'box'
        x = i * 70 + 10  # Increase the spacing between rectangles
        y = window.height // 2
        width = 50
        height = 50

        # Draw the box
        if left <= i <= right and not search_complete:
            color = (100, 100, 255)  # Blue for the current search interval
        elif i == mid and not search_complete:
            color = (255, 0, 0)  # Red for the middle element
        elif found and i == mid:
            color = (0, 255, 0)  # Green if 88 is found
        else:
            color = (200, 200, 200)  

        pyglet.shapes.Rectangle(x, y, width, height, color=color, batch=batch).draw()
        # Draw the number inside the box
        label = pyglet.text.Label(str(number), x=x+width//2, y=y+height//2, anchor_x='center', anchor_y='center', batch=batch)
        label.draw()

    # Draw the popup circle if 88 is found
    if found:
        x = mid * 70 + 10  # Calculate x position for the circle
        y = window.height // 2  # Y position remains the same as rectangles
        radius = 25  # Radius of the circle
        pyglet.shapes.Circle(x + width // 2, y + height // 2, radius, color=(255, 255, 0), batch=batch).draw()
        # Draw the number inside the circle
        label = pyglet.text.Label(str(numbers[mid]), x=x+width//2, y=y+height//2, anchor_x='center', anchor_y='center', batch=batch)
        label.draw()

pyglet.app.run()
