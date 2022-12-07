from collections import namedtuple

Command = namedtuple('Command', 'name args output')
File = namedtuple('File', 'size')

class Directory:
    def __init__(self, parent=None):
        self.parent = parent
        self.children = {}
        self._size = None

    @property
    def size(self):
        if self._size is None:
            self._size = sum(c.size for c in self.children.values())
        return self._size


class FileSystem:
    def __init__(self):
        self.root = Directory('')
        self.current = self.root

    def mkdir(self, name):
        if name not in self.current.children:
            self.current.children[name] = Directory(self.current)

    def cd(self, path):
        if path == '/': 
            self.current = self.root
        elif path == '..':
            self.current = self.current.parent
        else:
            self.current = self.current.children[path]


def iterdirs(root, recursive=False):
    yield root
    for child in root.children.values():
        if isinstance(child, Directory):
            yield from iterdirs(child, recursive)
    


def parse(data):
    data = data.strip('$ ')
    for entry in data.split('\n$ '):
        command, *output = entry.split('\n')
        name, *args = command.split()
        yield Command(name, args, output)


def run(commands):
    fs = FileSystem()

    for command in commands:

        if command.name == 'cd':
            path = command.args[0]
            fs.cd(path)

        elif command.name == 'ls':
            for line in command.output:
                if line.startswith('dir'):
                    _, name = line.split()
                    fs.mkdir(name)
                else:
                    size, name = line.split()
                    fs.current.children[name] = File(int(size)) 

    return fs


if __name__ == '__main__':
    from aocd import data

    commands = parse(data)
    fs = run(commands)
    dirs = list(iterdirs(fs.root, recursive=True))

    print('part 1', sum(d.size for d in dirs if d.size <= 100000))

    total_size = fs.root.size
    unused = 70e6 - total_size
    required = 30e6 - unused
    print('part 2', min(d.size for d in dirs if d.size > required))
