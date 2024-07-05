import sqlite3

conn = sqlite3.connect("bravobeast.db")

c = sqlite3.Cursor(conn)

class Database:
    @staticmethod
    def add_captcha(captcha: str):
        c.execute("INSERT INTO captcha VALUES (?)", (captcha,))
        conn.commit()

    @staticmethod
    def update_market_channel(type: str, channelid: str, serverid: str):
        c.execute("SELECT COUNT(*) FROM channel_cats WHERE serverid = ?", (serverid,))
        exists = c.fetchone()[0]
        
        if exists:
            c.execute("UPDATE channel_cats SET type = ?, channelid = ? WHERE serverid = ?", (type, channelid, serverid))
        else:
            c.execute("INSERT INTO channel_cats (type, channelid, serverid) VALUES (?, ?, ?)", (type, channelid, serverid))
        
        conn.commit()