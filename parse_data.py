import csv

def count_clothing_types(csv_file):
    clothing_type_counts = {}
    
    with open(csv_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            clothing_type = row['clothing_type']
            if clothing_type in clothing_type_counts:
                clothing_type_counts[clothing_type] += 1
            else:
                clothing_type_counts[clothing_type] = 1
    
    return clothing_type_counts

clothing_type_counts = count_clothing_types('shop_data.csv')

# Print the counts for each product type
for clothing_type, count in clothing_type_counts.items():
    print(clothing_type, "-", count)


def count_clothing_type_and_color(csv_file):
    same_clothing_type_and_color_count = 0
    
    with open(csv_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            clothing_type = row['clothing_type']
            color = row['color']
            if clothing_type == color:
                same_clothing_type_and_color_count += 1
    
    return same_clothing_type_and_color_count

# Replace 'your_csv_file.csv' with the path to your CSV file
count = count_clothing_type_and_color('shop_data.csv')
print("Number of rows with the same product type and color:", count)
