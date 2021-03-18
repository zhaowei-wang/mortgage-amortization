# mortgage-amortization
Utilities to compute the amortization schedule for fixed/variable rate mortgages.

Examples:

python3 rate_experimenter.py --amount=700000 --rates=0.014,0.014,0.0165,0.019,0.024 --length=25

 Year  Rate  Interest  Principal  Remaining  Monthly
 1  1.40  9,649.26  23,552.16 676,447.84 2,766.78
 2  1.40  9,317.40  23,884.01 652,563.82 2,766.78
 3  1.65 10,589.92  23,525.04 629,038.79 2,842.91
 4  1.90 11,749.91  23,256.05 605,782.74 2,917.16
 5  2.40 14,292.80  22,459.69 583,323.06 3,062.71

Total paid: 172276.23, Total interest: 55599.29

python3 schedule.py --amount=700000 --rate=0.0174 --length=25 --display_length=5

Mortgage amount: 700000.0, Rate: 0.0174, Monthly payment: 2879.18

 Year  Interest  Principal
 1 12,000.73  22,549.38
 2 11,605.23  22,944.89
 3 11,202.79  23,347.33
 4 10,793.29  23,756.83
 5 10,376.61  24,173.51

Total paid: 172750.59, Total interest: 55979.0
