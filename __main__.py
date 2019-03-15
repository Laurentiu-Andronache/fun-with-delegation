from writers import ContractsWriter


class LoanContract(ContractsWriter):

    def __init__(self, signee_1, signee_2):
        contract_type = 'loan'
        super().__init__(signee_1, signee_2, contract_type)


class DelegatedLoanContract:
    def __init__(self, *args, **kwargs):
        self.__dict__['_contract'] = ContractsWriter(*args, **kwargs)
        self._contract.header = 'loan'

    def __getattr__(self, item):
        return getattr(self._contract, item)

    def __setattr__(self, key, value):
        setattr(self._contract, key, value)

    def __iadd__(self, other):
        self._contract += other
        return self

    def __str__(self):
        return str(self._contract)

    def __repr__(self):
        return repr(self._contract)



if __name__ == '__main__':
    loan_contract = DelegatedLoanContract('Alan', 'John')
    loan_contract += 'Signee_1 will load 2,000 EUR to Signee_2.'
    loan_contract += 'Signee_2 will repay eventually.'
    loan_contract.sign('Alan')
    print(repr(loan_contract))
    print(loan_contract)
    print('DONE!')
