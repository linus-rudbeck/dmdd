# pip install pandas matplotlib
import pandas as pd

df = pd.read_csv('customer_data.csv')

total_customers = len(df)
invalid_emails = len(df[df['email'] == 'invalid_mail'])
valid_emails = total_customers - invalid_emails

print(f"Total customers: {total_customers}")
print(f"Invalid emails: {invalid_emails}")
print(f"Valid emails: {valid_emails}")

print(type(total_customers))
print(type(invalid_emails))
print(type(valid_emails))

data = [invalid_emails, valid_emails]

pie_df = pd.DataFrame({'email': data}, index=['invalid', 'valid'])
pie_plot = pie_df.plot.pie(y='email', figsize=(5, 5))

pie_plot.figure.savefig('pie_plot.png')