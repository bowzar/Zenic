from data_postgresql.postgresql_connection_string_builder import *
from data_postgresql.provider_postgresql import *

cntString = "Host=192.168.20.10;Port=5432;Database=data_burg;Username=sde;Password=123456;"
b = PostgreSQLConnectionStringBuilder(cntString)
print(b.connection_string)

provider = ProviderPostgreSQL(b.connection_string)
provider.open_connection()
e0 = provider.execute("SELECT bm FROM tb_dat_xzdy LIMIT 100", None,
                      lambda cursor: cursor.fetchall())

print(e0)
