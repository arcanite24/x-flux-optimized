import os
import json
import argparse


def txt_to_json(input_folder):
    # Ensure the input folder exists
    if not os.path.exists(input_folder):
        raise ValueError(f"The specified folder '{input_folder}' does not exist.")

    # Iterate over all files in the input folder
    for file_name in os.listdir(input_folder):
        if file_name.endswith(".txt"):
            # Construct full file path
            txt_file_path = os.path.join(input_folder, file_name)

            # Read the contents of the txt file
            with open(txt_file_path, "r") as txt_file:
                txt_contents = txt_file.read()

            # Prepare JSON data
            json_data = {"caption": txt_contents}

            # Construct JSON file path
            json_file_name = os.path.splitext(file_name)[0] + ".json"
            json_file_path = os.path.join(input_folder, json_file_name)

            # Write JSON data to the file
            with open(json_file_path, "w") as json_file:
                json.dump(json_data, json_file, indent=4)


def main():
    parser = argparse.ArgumentParser(
        description="Convert .txt files to .json files with specified format."
    )
    parser.add_argument(
        "input_folder", type=str, help="The input folder containing .txt files."
    )

    args = parser.parse_args()
    txt_to_json(args.input_folder)


if __name__ == "__main__":
    main()
