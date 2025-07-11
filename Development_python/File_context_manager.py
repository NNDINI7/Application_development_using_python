#custom Conetxt manager using class

class ManagedFile:
    def __init__(self,filename,mode):
        self.filename = filename 
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
        if exc_type is not None:
            print(f"An exception occurred: {exc_value}")
        return True
    
with ManagedFile('test.txt', 'w') as f:
    f.write('Hello, World!')