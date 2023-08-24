import os

class Finder : 

    files : list[str] = []
    spotted_lines : list[int] = []

    def __init__(self, str_list : list[str], path : str) -> any : 

        self._str_list : list[str] = str_list
        self._path : str = path

        if not os.path.isdir(self._path) :
            raise Exception('Path does not exist!') 

        print('\nFinder inited.')
        
    def start(self) :
        print('Finder started.')
        self.registerAllDirectoryFiles()
        self.readAllFiles()

        if not self.files :
            return print(f'\nThe path ({self._path}) don\'t contain any files.\n')
        if not self.spotted_lines :
            return print(f'\nThe research don\'t found any of your words in ({self._path}).\n')

    def readAllFiles (self) : 
        print('\nStarting reading all found files ... \n')
        for entry in self.files : 

            try : 
                opened_file = open(entry.path,mode='r')
                
                file_lines = opened_file.readlines()

                for index, line in enumerate(file_lines, start=1) :
                    for str in self._str_list :
                        if str.lower() in line.lower() : 
                            if not index in self.spotted_lines :
                                self.spotted_lines.append(index)
                                print(f'Word "{str}" found in "{entry.path}" at line {index}.')
                            
                opened_file.close()
            except :
                 print(f'failed to open "{entry.path}".')

    def registerAllDirectoryFiles (self, path = None) : 
       print('\nstarting registering all files in the target folder ...\n')
       if path is None : 
           path = self._path

       with os.scandir(path) as entries:
           for entry in entries:
                if entry.is_file():
                    print(f'File found : {entry.name} ({entry.path}).')
                    self.files.append(entry)
                else : 
                    self.registerAllDirectoryFiles(entry)
