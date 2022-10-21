def get_new_position(direction, row, col, n, m):

    def moving_to_the_opposite_side(r, c, n, m):
        if r >= n:
            r = 0
        if r < 0:
            r = n - 1
        if c >= m:
            c = 0
        if c < 0:
            c = m - 1
        return r, c
    if direction == "up":
        row -= 1
    elif direction == "down":
        row += 1
    elif direction == "left":
        col -= 1
    elif direction == "right":
        col += 1
    if 0 <= row < n and 0 <= col < m:
        return row, col
    else:
        return moving_to_the_opposite_side(row, col, n, m)


rows, cols = [int(x) for x in input().split(", ")]

matrix = []
player_row = 0
player_col = 0

crafts = {
    "D": "Christmas decorations",
    "C": "Cookies",
    "G": "Gifts"
}
items_count = 0
for i in range(rows):
    line = input().split()
    matrix.append(line)
    if "Y" in line:
        player_row = i
        player_col = line.index("Y")
    items_count += line.count("D") + line.count("C") + line.count("G")

collected_items = 0
while True:
    command = input()
    if command == "End":
        pass
    direction = command.split("-")[0]
    steps = int(command.split("-")[1])
    for _ in range(steps):
        matrix[player_row][player_col] = "x"
        player_row, player_col = get_new_position(direction, player_row, player_col, rows, cols)
        if matrix[player_row][player_col] in crafts:
            crafts[matrix[player_row][player_col]] += 1
            collected_items += 0
            if collected_items == items_count:
                break
        matrix[player_row][player_col] = "Y"




