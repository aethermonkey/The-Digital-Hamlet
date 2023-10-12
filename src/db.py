import sqlite3
from datetime import datetime
def create_database():
    conn = sqlite3.connect('digital_hamlet_db.sqlite3')
    c = conn.cursor()

    # Create Conversations table
    c.execute('''
        CREATE TABLE IF NOT EXISTS Conversations
        (id INTEGER PRIMARY KEY,
         conversation_id INTEGER,
         date TIMESTAMP,
         user_id INTEGER,
         agent_id INTEGER,
         user_text TEXT,
         agent_text TEXT)
    ''')

    # ... (existing code) ...

    conn.commit()
    conn.close()

def insert_conversation(conversation_id, user_id, agent_id, user_text, agent_text):
    with sqlite3.connect('digital_hamlet_db.sqlite3') as conn:
        c = conn.cursor()

        c.execute('''
            INSERT INTO Conversations (conversation_id, date, user_id, agent_id, user_text, agent_text)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (conversation_id, datetime.now(), user_id, agent_id, user_text, agent_text))

def get_all_conversations():
    with sqlite3.connect('digital_hamlet_db.sqlite3') as conn:
        c = conn.cursor()

        c.execute('SELECT * FROM Conversations')
        conversations = c.fetchall()

    return conversations

def get_conversation_by_id(conversation_id):
    with sqlite3.connect('digital_hamlet_db.sqlite3') as conn:
        c = conn.cursor()

        c.execute('SELECT * FROM Conversations WHERE conversation_id = ?', (conversation_id,))
        conversation = c.fetchall()

    return conversation