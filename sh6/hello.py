print("hello world")
import os
import pandas as pd
import yaml

def excel_to_yaml(excel_folder, output_yaml):
    # Initialize YAML dictionary
    yaml_data = {'version': 2, 'sources': []}

    # Iterate through Excel files in the input folder
    for filename in os.listdir(excel_folder):
        if filename.endswith(".xlsx"):
            excel_file = os.path.join(excel_folder, filename)
            
            # Read Excel file
            df = pd.read_excel(excel_file)

            # Initialize source dictionary
            source_data = {'name': filename.split('.')[0], 'tables': []}

            # Iterate through rows and construct YAML data
            current_table = None
            for index, row in df.iterrows():
                # If new table is found
                if pd.notna(row['Table']):
                    # Add previous table data to source
                    if current_table:
                        source_data['tables'].append(current_table)

                    # Initialize new table dictionary
                    current_table = {'name': row['Table'], 'tests': [], 'columns': []}

                # If test is found
                if pd.notna(row['Test']):
                    test_data = {'test.' + row['Test']: {'column_list': row['Column List'].split(','),
                                                          'transform': row['Transform']}}
                    # Add test to current table
                    current_table['tests'].append(test_data)

                # If column is found
                if pd.notna(row['Column']):
                    # Initialize new column dictionary
                    column_data = {'name': row['Column'], 'tests': []}

                    # Add tests to current column
                    for test in row['Tests'].split(','):
                        if test.strip():
                            column_data['tests'].append(test.strip())

                    # Add column to current table
                    current_table['columns'].append(column_data)

            # Add last table data to source
            if current_table:
                source_data['tables'].append(current_table)

            # Add source data to YAML dictionary
            yaml_data['sources'].append(source_data)

    # Write YAML data to file with proper indentation
    with open(output_yaml, 'w') as yaml_file:
        yaml.dump(yaml_data, yaml_file, default_flow_style=False, indent=4)

# Example usage:
input_excel_folder = 'input_excel_folder'
output_yaml_file = 'output.yaml'

excel_to_yaml(input_excel_folder, output_yaml_file)
