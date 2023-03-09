import os
path = "C:\\Users\\Lenovo\\Desktop\\MyGitProj\\"
print("Directories in path:")
print([d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))])
print("Files in path:")
print([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
print("All contents in path:")
print(os.listdir(path))