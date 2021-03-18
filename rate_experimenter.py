import argparse
import numpy as np
import numpy_financial as npf
import pandas as pd
pd.options.display.float_format = "{:,.2f}".format

PARSER = argparse.ArgumentParser(description='Returns an amortization schedule for 5Y for given rates.')
PARSER.add_argument('--amount', help='Mortgage amount.')
PARSER.add_argument('--rates', help='A list of 5 rates.')
PARSER.add_argument('--length', help='Length of mortgage in years.')

def main():
    args = vars(PARSER.parse_args())

    mortgage_amount = float(args['amount'])
    rates = [float(x) / 12 for x in args['rates'].split(',')]
    assert len(rates) == 5, 'Please provide 5 rates.'
    total_periods = int(args['length']) * 12

    data = []
    for i, rate in enumerate(rates):
        monthly = -npf.pmt(rate, total_periods, mortgage_amount)
        yearly_interest = 0
        yearly_principal = 0
        for j in np.arange(12):
            yearly_interest += npf.ipmt(rate, j + 1, total_periods, mortgage_amount)
            yearly_principal += npf.ppmt(rate, j + 1, total_periods, mortgage_amount)
        total_periods -= 12
        mortgage_amount += yearly_principal
        data.append({
            'Year': i + 1,
            'Rate': rate * 12 * 100,
            'Interest': -yearly_interest,
            'Principal': -yearly_principal,
            'Remaining': mortgage_amount,
            'Monthly': monthly
        })

    df = pd.DataFrame(data)

    print()
    print(df.to_string(index=False))
    print()
    print('Total paid: {0}, Total interest: {1}'.format(
        np.round(df['Interest'].sum() + df['Principal'].sum(), 2), np.round(df['Interest'].sum(), 2)))
    
        

if __name__ == '__main__':
    main()
