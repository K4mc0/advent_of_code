class File(object):

    def __init__(self, size, name):
        self.name = name
        self.size  =  size

class Folder(object):

    def __init__(self, name):
        self.name = name
        self.folders = []
        self.files = []
        self.size_of_files = 0
        self.total_size = 0
        self.prev = None

    def goto(self, name):
        for i in range(0, len(self.folders)):
            if(self.folders[i].name == name):
                return self.folders[i]
    
    def previous(self):
        return self.prev

    def add_folder(self, name):
        folder = Folder(name)
        self.folders.append(folder)
        folder.prev = self

    def add_file(self, size, name):
        file = File(size, name)
        self.files.append(file)
        self.size_of_files += size

    def go_to_root(self):
        while self.prev != None:
            self = self.prev
        return self

    def calculate_sizes(self):
        if (not self.folders):
            self.total_size = self.size_of_files  
        else:
            for f in range(0, len(self.folders)):
                self = self.folders[f]
                self.calculate_sizes()
                self = self.prev
                self.total_size += self.folders[f].total_size
            self.total_size += self.size_of_files

    def sum_of_folders_under_value(self, value):
        sum = 0
        if (self.folders):
            for f in range(0, len(self.folders)):
                self = self.folders[f]
                sum += self.sum_of_folders_under_value(value)
                self = self.prev
        if (self.total_size < value):
            sum += self.total_size
        return sum
    
    def find_directory_to_delete(self, value, curent_candidate):
        if (self.total_size > value and self.total_size < curent_candidate):
            candidate = self.total_size
        else:
            candidate = curent_candidate
        if (self.folders):
            for f in range(0, len(self.folders)):
                self = self.folders[f]
                candidate = self.find_directory_to_delete(value, candidate)
                self = self.prev    
        return candidate

with open("input.txt", "r") as file:
    lines = file.read().splitlines()

for line in lines:
    tmp = line.split()
    if (line == "$ cd /"):
        tree = Folder('/')
    else:
        if(tmp[0] == '$'):
            if(tmp[1] == "cd"):
                if(tmp[2] == ".."):
                    tree = tree.previous()
                else:
                    tree = tree.goto(tmp[2])
        else:
            if (tmp[0] == "dir"):
                tree.add_folder(tmp[1])
            else:
                tree.add_file(int(tmp[0]), tmp[1])

tree = tree.go_to_root()
tree.calculate_sizes()
print("total size", tree.total_size)
print("result for task 1 is", tree.sum_of_folders_under_value(100000))

total_disk_space = 70000000
space_for_update = 30000000
currently_free = total_disk_space - tree.total_size
space_needed = space_for_update - currently_free
print ("result for task 2 is", tree.find_directory_to_delete(space_needed, space_for_update))