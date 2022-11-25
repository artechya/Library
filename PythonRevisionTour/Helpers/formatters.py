class Table:
    '''
    Used to diaplay tabular information  

    Keyword Arguments:  

    rows -- List of lists, each list is a row  

    header -- Single list, has column names  

    spacing -- Int, minimum space between columns
    '''

    def __init__(self, rows, header=[], spacing=2):
        self.rows = rows
        self.header = header
        self.spacing = spacing

    def display(self):        
        if self.header:
            tab_length = max([max([len(str(i)) for i in row]) for row in self.rows] + [max(len(str(i)) for i in self.header)]) + self.spacing
            for element in self.header:
                print(element, end=' ' * (tab_length - len(str(element))))
            print('\n' + '-' * tab_length * len(self.header))
        else:
            tab_length = max([max([len(str(i)) for i in row]) for row in self.rows]) + self.spacing
        
        for row in self.rows:
            for element in row:
                print(element, end=' ' * (tab_length - len(str(element))))
            print()
