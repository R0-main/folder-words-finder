import os

class Finder : 

    files : list[str] = []
    spotted_lines : list[int] = []

    def __init__(self, str_list : list[str], path : str) -> any : 

        self._str_list : list[str] = str_list
        self._path : str = path

        print('Finder Innited')
        
    def start(self) :
        print('Finder Started')
        self.registerAllDirectoryFiles()
        self.readAllFiles()

        if not self.files :
            return print(f'The Path ({self._path}) Don\'t Contain Any File')
        if not self.spotted_lines :
            return print(f'The Research Don\'t Found Any Of Your Words In ({self._path})')

    def readAllFiles (self) : 
        print('\nStarting Reading All Registered Files ... \n')
        for entry in self.files : 
            # Open a file: file
            opened_file = open(entry.path,mode='r')
            
            file_lines = opened_file.readlines()

            for index, line in enumerate(file_lines, start=1) :
                for str in self._str_list :
                    if str in line : 
                        if not index in self.spotted_lines :
                            self.spotted_lines.append(index)
                            print(f'Word "{str}" found in "{entry.path}" at line {index}.')
                        
            opened_file.close()

    def registerAllDirectoryFiles (self, path = None) : 
       print('Starting Registering All Files In The Target Folder ...\n')
       if path is None : 
           path = self._path

       with os.scandir(path) as entries:
           for entry in entries:
                if entry.is_file():
                    print(f'File found : {entry.name} ({entry.path})')
                    self.files.append(entry)
                else : 
                    self.registerAllDirectoryFiles(entry)



if __name__ == '__main__' : 

    words : list[str] = input('Words : ').split(',')
    path : str = input('Path :')

    finder : Finder = Finder(words, path)
    finder.start()
