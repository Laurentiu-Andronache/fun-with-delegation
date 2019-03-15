class ContractsWriter:
    def __init__(self, signee_1, signee_2, contract_type=''):
        self.signee_1 = signee_1
        self.signee_2 = signee_2
        self.contract_rules = []
        self.signee_1_signed = ''
        self.signee_2_signed = ''
        self._contract_type = 'Contract'
        if contract_type:
            self.header = contract_type

    def __add__(self, other):
        if isinstance(other, str):
            self.contract_rules.append(other)
            return self
        elif isinstance(other, list):
            self.contract_rules.extend(other)
            return self
        else:
            raise NotImplemented('Invalid rule.')

    def __repr__(self):
        return f'ContractsWriter({self.signee_1!r}, {self.signee_2!r})'

    def sign(self, signee):
        if signee == self.signee_1:
            self.signee_1_signed = 'signed!'
        elif signee == self.signee_2:
            self.signee_2_signed = 'signed!'
        else:
            raise ValueError('Signee not found.')

    @property
    def header(self):
        temp = f'\t{self._contract_type}\n'
        temp = temp + f'\tbetween Signee 1 {self.signee_1!r}, and Signee 2 {self.signee_2!r}:\n\n'
        return temp

    @header.setter
    def header(self, value):
        self._contract_type = self._contract_type + ' for ' + value

    @header.deleter
    def header(self):
        self._contract_type = 'Contract'

    def print_contract_type(self):
        print(self.header.split('\n')[0])

    def __str__(self):
        temp = self.header
        for rule in self.contract_rules:
            temp = temp + f'\t{rule}\n'
        temp = temp + f'\tSignee 1: {self.signee_1_signed}\n'
        temp = temp + f'\tSignee 2: {self.signee_2_signed}\n'
        return temp
