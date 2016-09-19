import os

def print_dir_contents(path):
    """
    function that will list all the directories/files/subdirectories 
    in a given directory
    """
    for i in os.listdir(path):
        childpath = os.path.join(path, i)
        if os.path.isdir(childpath):
            print_dir_contents(childpath)
        else:
            print(childpath)

print_dir_contents('/etc')
