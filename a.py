import pandas as pd

# Create a DataFrame from the provided data
data = {
    'Inventory ID': ['IN0001', 'IN0002', 'IN0003', 'IN0004', 'IN0005', 'IN0006', 'IN0007', 'IN0008', 'IN0009', 'IN0010', 'IN0011', 'IN0012', 'IN0013', 'IN0014', 'IN0015', 'IN0016', 'IN0017', 'IN0018', 'IN0019', 'IN0020', 'IN0021', 'IN0022', 'IN0023', 'IN0024', 'IN0025'],
    'Name': ['Item 1', 'Item 2', 'Item 3', 'Item 4', 'Item 5', 'Item 6', 'Item 7', 'Item 8', 'Item 9', 'Item 10', 'Item 11', 'Item 12', 'Item 13', 'Item 14', 'Item 15', 'Item 16', 'Item 17', 'Item 18', 'Item 19', 'Item 20', 'Item 21', 'Item 22', 'Item 23', 'Item 24', 'Item 25'],
    'Description': ['Desc 1', 'Desc 2', 'Desc 3', 'Desc 4', 'Desc 5', 'Desc 6', 'Desc 7', 'Desc 8', 'Desc 9', 'Desc 10', 'Desc 11', 'Desc 12', 'Desc 13', 'Desc 14', 'Desc 15', 'Desc 16', 'Desc 17', 'Desc 18', 'Desc 19', 'Desc 20', 'Desc 21', 'Desc 22', 'Desc 23', 'Desc 24', 'Desc 25'],
    'Unit Price': [51, 93, 57, 19, 75, 11, 56, 38, 59, 50, 59, 18, 26, 42, 32, 90, 97, 12, 82, 16, 19, 24, 29, 75, 14],
    'Quantity in Stock': [25, 132, 151, 186, 62, 5, 58, 101, 122, 175, 176, 22, 72, 62, 46, 96, 57, 6, 143, 124, 112, 182, 106, 173, 28],
    'Inventory Value': [1275, 12276, 8607, 3534, 4650, 55, 3248, 3838, 7198, 8750, 10384, 396, 1872, 2604, 1472, 8640, 5529, 72, 11726, 1984, 2128, 4368, 3074, 12975, 392],
    'Reorder Level': [29, 231, 114, 158, 39, 9, 109, 162, 82, 283, 229, 36, 102, 83, 23, 180, 98, 7, 164, 113, 75, 132, 142, 127, 21],
    'Reorder Time in Days': [13, 4, 11, 6, 12, 13, 7, 3, 3, 8, 1, 12, 9, 2, 15, 3, 12, 13, 12, 14, 11, 15, 1, 9, 8],
    'Quantity in Reorder': [50, 50, 150, 50, 50, 150, 100, 100, 150, 150, 100, 50, 100, 100, 50, 50, 50, 50, 150, 50, 50, 150, 150, 100, 50],
    'Discontinued?': ['no', 'no', 'no', 'no', 'no', 'no', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'Yes', 'no', 'no', 'no', 'no', 'Yes', 'no', 'no', 'no']
}

df = pd.DataFrame(data)

# Convert the DataFrame to a dictionary
inventory_dict = df.to_dict(orient='records')

# Print the resulting dictionary
print(inventory_dict)
