import copy 

def spread_fire(grid):
    """Update the forest grid based on fire spreading rules, including edges."""
    grid_size = len(grid)
    update_grid = copy.deepcopy(grid)

    for i in range(grid_size):
        for j in range(grid_size):
            if grid[i][j] == 1:  # אם התא מכיל עץ

                # בדיקת כל הכיוונים מבלי לצאת מהגבולות
                neighbors = []

                # בדיקת קיום שכן למעלה
                if i > 0:
                    neighbors.append(grid[i-1][j])
                # בדיקת קיום שכן למטה
                if i < grid_size - 1:
                    neighbors.append(grid[i+1][j])
                # בדיקת קיום שכן משמאל
                if j > 0:
                    neighbors.append(grid[i][j-1])
                # בדיקת קיום שכן מימין
                if j < grid_size - 1:
                    neighbors.append(grid[i][j+1])

                # בדיקה האם אחד מהשכנים בוער
                if 2 in neighbors:
                    update_grid[i][j] = 2

    return update_grid





    
