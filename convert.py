import subprocess

# Define the Git repository URL
repository_url = "https://github.com/mystic123/tensorflow-yolo-v3"

# Define the target directory where you want to clone the repository
target_directory = "/path/to/your/target/directory"

# Construct the Git clone command
git_clone_command = ["git", "clone", repository_url, target_directory]

try:
    # Run the Git clone command
    subprocess.run(git_clone_command, check=True, shell=False)
    print("Git repository cloned successfully.")
except subprocess.CalledProcessError as e:
    print(f"Error cloning the Git repository: {e}")


import subprocess

# Define the paths and arguments for the conversion script
conversion_script = "convert_weights_pb.py"
class_names_arg = "--class_names"
class_names_value = "classes.names"
weights_file_arg = "--weights_file"
weights_file_value = "yolov3_training_last.weights"
data_format_arg = "--data_format"
data_format_value = "NHWC"

# Construct the command to run the conversion script
conversion_command = [
    "python", conversion_script,
    class_names_arg, class_names_value,
    weights_file_arg, weights_file_value,
    data_format_arg, data_format_value
]

try:
    # Run the conversion script
    subprocess.run(conversion_command, check=True, shell=False)
    print("Conversion script executed successfully.")
except subprocess.CalledProcessError as e:
    print(f"Error executing the conversion script: {e}")
