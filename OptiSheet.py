import matplotlib.pyplot as plt
from rectpack import newPacker

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

def get_user_input():
    # Get main rectangle size
    main_width = int(input("Enter the width of the Main Piece: "))
    main_height = int(input("Enter the height of the Main Piece: "))
    main_rect = Rectangle(main_width, main_height)

    # Get the number of sub-rectangles
    num_rectangles = int(input("Enter the number of Small Pieces: "))

    # Get size for each sub-rectangle
    sub_rectangles = []
    for i in range(num_rectangles):
        width = int(input(f"Enter the width of Small Piece {i + 1}: "))
        height = int(input(f"Enter the height of Small Piece {i + 1}: "))
        sub_rectangles.append(Rectangle(width, height))

    return main_rect, sub_rectangles

def pack_rectangles(main_rect, sub_rectangles, gap):
    # Create a new packer
    packer = newPacker()

    # Add rectangles to the packer
    for i, rect in enumerate(sub_rectangles):
        packer.add_rect(rect.width + gap, rect.height + gap, i)

    # Pack the rectangles into the main rectangle
    packer.add_bin(main_rect.width, main_rect.height)
    packer.pack()

    # Get the placement information
    placements = packer[0]

    return placements

def visualize_rectangles(main_rect, placements, gap):
    fig, ax = plt.subplots()
    ax.set_xlim(0, main_rect.width)
    ax.set_ylim(0, main_rect.height)
    ax.set_aspect('equal', 'box')

    # Plot sub-rectangles with gap
    for rect in placements:
        rect_patch = plt.Rectangle((rect.x + gap/2, rect.y + gap/2), rect.width - gap, rect.height - gap, linewidth=1, edgecolor='r', facecolor='none')
        ax.add_patch(rect_patch)

        # Display dimensions inside each box
        plt.text(rect.x + gap, rect.y + gap, f'{rect.width - gap}x{rect.height - gap}', fontsize=8, va='center', ha='center')

    # Plot main rectangle
    main_rect_patch = plt.Rectangle((0, 0), main_rect.width, main_rect.height, linewidth=1, edgecolor='b', facecolor='none')
    ax.add_patch(main_rect_patch)

    plt.show()

if __name__ == "__main__":
    main_rect, sub_rectangles = get_user_input()
    gap = 10

    placements = pack_rectangles(main_rect, sub_rectangles, gap)

    for i, rect in enumerate(placements):
        print(f"Small Piece {i + 1}: x={rect.x + gap/2}, y={rect.y + gap/2}, width={rect.width - gap}, height={rect.height - gap}")

    visualize_rectangles(main_rect, placements, gap)
