def grid_challenge(grid):
    n_rows = len(grid)
    n_cols = len(grid[0])
    
    def sort_rows():
        for row in range(n_rows):
            grid[row] = sorted(grid[row])
    
    def are_columns_sorted():
        for col in range(n_cols):
            for row in range(n_rows - 1):
                if grid[row][col] > grid[row + 1][col]:
                    return False
        return True
        
    sort_rows()
    return "YES" if are_columns_sorted() else "NO"