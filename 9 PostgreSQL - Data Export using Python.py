#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import psycopg2
from sqlalchemy import create_engine

db_config = {'user': 'praktikum_student', 
            'pwd': 'Sdf4$2;d-d30pp', 
            'host': 'rc1b-wcoijxj3yxfsf3fs.mdb.yandexcloud.net',
            'port': 6432,
            'db': 'data-analyst-zen-project-db'} 

connection_string = 'postgresql://{}:{}@{}:{}/{}'.format(db_config['user'],
                                                db_config['pwd'],
                                                db_config['host'],
                                                db_config['port'],
                                                db_config['db'])

engine = create_engine(connection_string)


query = ''' SELECT *  FROM dash_visits'''
data_raw = pd.io.sql.read_sql(query, con=engine)

print(data_raw.head(5))


# In[ ]:




