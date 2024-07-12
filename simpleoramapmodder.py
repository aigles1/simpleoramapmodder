import os
import zipfile
import shutil

# Get a list of all files in the current directory
current_directory = os.getcwd()
files = os.listdir(current_directory)

# Find the .oramap file
oramap_file = [f for f in files if f.endswith('.oramap')]

if oramap_file:
	# Define the directories and file paths  
	original_zip_path = oramap_file[0]
	output_dir = 'output_map'
	assets_dir = 'assets'
	append_file_path = os.path.join('append', 'append.txt')
	category_file_path = os.path.join('append', 'category.txt')

	# Ensure output directory exists
	os.makedirs(output_dir, exist_ok=True)

	# Create a copy of the original oramap file in the output directory
	copied_zip_path = os.path.join(output_dir, os.path.basename(original_zip_path))
	shutil.copyfile(original_zip_path, copied_zip_path)

	# Function to add contents of assets directory to the oramap file
	def add_assets_to_zip(zipf, assets_dir):
		for foldername, subfolders, filenames in os.walk(assets_dir):
			for filename in filenames:
				file_path = os.path.join(foldername, filename)
				arcname = os.path.relpath(file_path, assets_dir)
				zipf.write(file_path, arcname)

	# Function to append content to map.yaml inside the oramap file and modify Title and Categories lines
	def append_and_modify_map_yaml(zip_path, append_content, category_content):
		with zipfile.ZipFile(zip_path, 'a') as zipf:
			map_yaml_path = 'map.yaml'
			
			# Extract map.yaml content
			with zipf.open(map_yaml_path, 'r') as map_yaml_file:
				map_yaml_content = map_yaml_file.read().decode()
			
			# Append new content
			map_yaml_content += append_content
			
			# Modify Title and Categories lines
			modified_lines = []
			for line in map_yaml_content.splitlines():
				if line.startswith('Title:'):
					line += ' BI-3.6'
				elif line.startswith('Categories:'):
					line = f'Categories: {category_content}'
				modified_lines.append(line)
			modified_map_yaml_content = '\n'.join(modified_lines)
			
			# Remove the original map.yaml
			temp_zip_path = zip_path + '.tmp'
			with zipfile.ZipFile(temp_zip_path, 'w') as temp_zipf:
				for item in zipf.infolist():
					if item.filename != map_yaml_path:
						temp_zipf.writestr(item, zipf.read(item.filename))
			
			# Add the updated map.yaml
			with zipfile.ZipFile(temp_zip_path, 'a') as temp_zipf:
				temp_zipf.writestr(map_yaml_path, modified_map_yaml_content)
			
			# Replace the original oramap with the updated oramap
			shutil.move(temp_zip_path, zip_path)

	# Add assets to the copied oramap file
	with zipfile.ZipFile(copied_zip_path, 'a') as zipf:
		add_assets_to_zip(zipf, assets_dir)

	# Read content of append.txt and category.txt
	with open(append_file_path, 'r') as append_file:
		append_content = append_file.read()
	with open(category_file_path, 'r') as category_file:
		category_content = category_file.read().strip()

	# Append content of append.txt to map.yaml, modify Title and Categories lines, and remove original map.yaml
	append_and_modify_map_yaml(copied_zip_path, append_content, category_content)

	# Rename the oramap file by adding 'BI' to the end of the name
	base_name, ext = os.path.splitext(os.path.basename(original_zip_path))
	new_zip_name = f"{base_name}_BI-3.6{ext}"
	new_zip_path = os.path.join(output_dir, new_zip_name)
	os.rename(copied_zip_path, new_zip_path)

	print(f"New oramap file created: {new_zip_path}")
else:
    print("No .oramap file found in the current directory.")