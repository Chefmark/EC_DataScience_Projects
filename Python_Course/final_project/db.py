import sqlite3
import os
from typing import Dict

class DB:
    db_url:str

    def __init__(self, db_url):
        self.db_url = db_url
        if not os.path.exists(self.db_url):
            self.__set_up_db()
            # self.__set_up_admin()
            # self.__set_up_seed()

    def __set_up_db(self):
        conn = sqlite3.connect(self.db_url)
        with open("store_setup.sql", "r") as file:
            script = file.read()
            conn.executescript(script)
            conn.commit()
        
        conn.close()

    def __set_up_admin(self):
        pass

    def __set_up_seed():
        pass

    def call_db(self, query, *args):
        conn = sqlite3.connect(self.db_url)
        cur = conn.cursor()
        res = cur.execute(query, args)
        data = res.fetchall()
        cur.close()
        conn.commit()
        conn.close()
        return data

    def insert_into(self, *, table:str, fields:Dict[str,str]):
        keys = ",".join(fields.keys())
        values = ",".join(fields.values())
        query = f"""
        INSERT INTO {table} (
            {keys}
        ) VALUES(
            '{values}'
        )
        """
        return self.call_db(query)
