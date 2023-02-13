import pandas as pd
import psycopg2

conn = psycopg2.connect("""
    host=localhost
    port=5432
    dbname=postgres
    user=postgres
    password=password

""")

data = pd.read_csv("C:\\Users\\ruaabcn\\IdeaProjects\\Data\\deposit.csv")
df = pd.DataFrame(data)
print(df)

cursor = conn.cursor()

# Create Table
cursor.execute("""
		CREATE TABLE public.deposits (
			id int primary key,
			age varchar (50),
			job varchar (50),
		  marital varchar(50),
		  education varchar(50),
		  def varchar (50),
		  balance varchar(50),
		  housing varchar (50),
		  loan varchar (50),
		  contact varchar(50),
		  monthes varchar(50),
		  duration varchar (50),
			campaign varchar (50),
			pdays varchar (50),
			previous varchar (50),
		  poutcome varchar(50),
		  deposit  varchar(50))
  """)

conn.commit()

# Insert DataFrame to Table
for row in df.itertuples():
  cursor.execute(
      "INSERT INTO public.deposits (id,age, job,marital,education,def,"
      "balance,housing,loan,contact,monthes,duration,campaign,pdays,previous,"
      "poutcome,deposit) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"
      "%s,%s,%s)",
      (row.id, row.age, row.job, row.marital, row.education, row.default,
       row.balance, row.housing, row.loan, row.contact, row.month, row.duration,
       row.campaign, row.pdays, row.previous, row.poutcome, row.deposit))
conn.commit()
cursor.close()

query = "SELECT * from deposits"
data = pd.read_sql_query(query, conn)
data.info()
conn.close()
