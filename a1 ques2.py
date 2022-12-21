gross_income=float(input("GROSS INCOME:"))
no_of_dependents=int(input("NO. OF DEPENDENTS:"))
taxable_income= gross_income-10000-(3000*no_of_dependents)
tax=taxable_income*0.02
print('YOUR TAX',tax)
