import argparse
import numpy as np
import numpy_financial as npf
import pandas as pd
pd.options.display.float_format = "{:,.2f}".format

PARSER = argparse.ArgumentParser(description='Returns an amortization schedule.')
PARSER.add_argument('--amount', help='Mortgage amount.')
PARSER.add_argument('--rate', help='A single rate (fixed).')
PARSER.add_argument('--length', help='Length of mortgage in years.')
PARSER.add_argument('--display_length', help='Number of years to display.')

def main():
    args = vars(PARSER.parse_args())

    mortgage_amount = float(args['amount'])
    rate = float(args['rate']) / 12
    total_periods = int(args['length']) * 12
    display_length = int(args['display_length'])

    monthly = -npf.pmt(rate, total_periods, mortgage_amount)

    print()
    print('Mortgage amount: {0}, Rate: {1}, Monthly payment: {2}'.format(
        mortgage_amount, args['rate'], np.round(monthly, 2)))
    print()

    interest_paid = []
    for i in np.arange(1, total_periods + 1):
        interest_paid.append(-npf.ipmt(rate, i, total_periods, mortgage_amount))

    interest_paid_yearly = []
    for year in np.arange(total_periods / 12):
        interest = 0
        principal = 0
        for i in np.arange(12):
            monthly_interest = interest_paid[int(year * 12 + i)]
            interest += monthly_interest
            principal += monthly - monthly_interest
        interest_paid_yearly.append({
            'Year': int(year + 1),
            'Interest': interest,
            'Principal': principal,
        })

    df = pd.DataFrame(interest_paid_yearly).head(display_length)
    print(df.to_string(index=False))
    print()
    print('Total paid: {0}, Total interest: {1}'.format(
        np.round(df['Interest'].sum() + df['Principal'].sum(), 2),
        np.round(df['Interest'].sum())))


if __name__ == '__main__':
    main()
