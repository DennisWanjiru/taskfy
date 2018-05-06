class Task(object):
    id = 1

    def __init__(self, title, desc):
        self.id = Task.id
        self.title = title
        self.desc = desc
        self.completed = False
        Task.id += 1
