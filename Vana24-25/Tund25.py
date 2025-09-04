import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

def create_database():
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS languages (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT UNIQUE NOT NULL
    );
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS countries (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT UNIQUE NOT NULL
    );
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS genres (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT UNIQUE NOT NULL
    );
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS directors (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT UNIQUE NOT NULL
    );
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS movies (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      title TEXT NOT NULL,
      director_id INTEGER,
      release_year INTEGER,
      genre_id INTEGER,
      duration INTEGER,
      rating REAL,
      language_id INTEGER,
      country_id INTEGER,
      description TEXT,
      FOREIGN KEY (director_id) REFERENCES directors(id),
      FOREIGN KEY (genre_id) REFERENCES genres(id),
      FOREIGN KEY (language_id) REFERENCES languages(id),
      FOREIGN KEY (country_id) REFERENCES countries(id)
    );
    """)

    cursor.executemany(
        "INSERT OR IGNORE INTO languages (name) VALUES (?)",
        [("RUS",), ("ENG",), ("EST",)]
    )
    cursor.executemany(
        "INSERT OR IGNORE INTO countries (name) VALUES (?)",
        [("Venemaa",), ("USA",), ("Eesti",)]
    )
    cursor.executemany(
        "INSERT OR IGNORE INTO genres (name) VALUES (?)",
        [("Drama",), ("Action",), ("Comedy",)]
    )
    cursor.executemany(
        "INSERT OR IGNORE INTO directors (name) VALUES (?)",
        [("Andrei Tarkovsky",), ("Christopher Nolan",), ("Aki Kaurismäki",)]
    )

    cursor.execute("SELECT COUNT(*) FROM movies;")
    count = cursor.fetchone()[0]
    if count == 0:
        sample_movies = [
            ("Solaris", "Andrei Tarkovsky", 1972, "Drama", 167, 8.1,
             "RUS", "Venemaa",
             "Psühholoogiline fiktsioon mälu ja reaalsuse kohta."),
            ("Inception", "Christopher Nolan", 2010, "Action", 148, 8.8,
             "ENG", "USA",
             "Varas, kes varastab unistuste saladusi."),
            ("November", "Aki Kaurismäki", 2017, "Comedy", 98, 7.5,
             "EST", "Eesti",
             "Melanhoolne romantiline komöödia, mille tegevus toimub Eesti talvel.")
        ]
        for title, director, year, genre, duration, rating, lang, country, desc in sample_movies:
            cursor.execute("""
    INSERT INTO movies
      (title, director_id, release_year, genre_id, duration,
       rating, language_id, country_id, description)
    VALUES
      (
        ?,
        (SELECT id FROM directors WHERE name=?),
        ?,
        (SELECT id FROM genres WHERE name=?),
        ?,
        ?,
        (SELECT id FROM languages WHERE name=?),
        (SELECT id FROM countries WHERE name=?),
        ?
      );
    """, (title, director, year, genre, duration, rating, lang, country, desc))

    conn.commit()
    conn.close()

def load_data_from_db(tree, search_query=""):
    for item in tree.get_children():
        tree.delete(item)
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    query = """
SELECT m.id, m.title, d.name, m.release_year, g.name,
  m.duration, m.rating, l.name, c.name, m.description
FROM movies m
LEFT JOIN directors d ON m.director_id = d.id
LEFT JOIN genres g ON m.genre_id = g.id
LEFT JOIN languages l ON m.language_id = l.id
LEFT JOIN countries c ON m.country_id = c.id
"""
    params = ()
    if search_query:
        query += " WHERE m.title LIKE ?"
        params = ('%' + search_query + '%',)
    cursor.execute(query, params)
    rows = cursor.fetchall()
    for row in rows:
        tree.insert("", "end", iid=row[0], values=row[1:])
    conn.close()

def open_reference_window():
    ref_win = tk.Toplevel(root)
    ref_win.title("Juhtimine")
    ref_win.geometry("300x250")
    ref_win.resizable(False, False)

    lbl_title = tk.Label(
        ref_win, text="LISA", font=("Helvetica", 14, "bold")
    )
    lbl_title.pack(pady=(10, 5))

    ref_type = tk.StringVar(value="languages")
    radio_frame = tk.Frame(ref_win)
    radio_frame.pack(pady=5)

    tk.Radiobutton(
        radio_frame, text="Keel", variable=ref_type,
        value="languages"
    ).grid(row=0, column=0, padx=10, pady=5, sticky="w")
    tk.Radiobutton(
        radio_frame, text="Žanr", variable=ref_type,
        value="genres"
    ).grid(row=0, column=1, padx=10, pady=5, sticky="w")
    tk.Radiobutton(
        radio_frame, text="Riik", variable=ref_type,
        value="countries"
    ).grid(row=1, column=0, padx=10, pady=5, sticky="w")
    tk.Radiobutton(
        radio_frame, text="Režissöör", variable=ref_type,
        value="directors"
    ).grid(row=1, column=1, padx=10, pady=5, sticky="w")

    entry = tk.Entry(ref_win, width=30)
    entry.pack(pady=(15, 10))

    btn_frame = tk.Frame(ref_win)
    btn_frame.pack(pady=10)

    def save_reference():
        table = ref_type.get()
        name = entry.get().strip()
        if not name:
            messagebox.showwarning("Viga", "Palun sisesta väärtus!")
            return
        try:
            conn = sqlite3.connect('movies.db')
            cur = conn.cursor()
            cur.execute(
                f"INSERT OR IGNORE INTO {table} (name) VALUES (?)",
                (name,)
            )
            conn.commit()
            conn.close()
            messagebox.showinfo("Edu", f"'{name}' lisatud tabelisse {table}.")
            entry.delete(0, tk.END)
        except sqlite3.Error as e:
            messagebox.showerror("Viga", f"Andmebaasi viga: {e}")

    tk.Button(
        btn_frame, text="Salvesta", width=15,
        command=save_reference
    ).grid(row=0, column=0, padx=5)

def open_update_window():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Valik puudub",
                               "Palun vali kõigepealt rida!")
        return
    record_id = selected[0]
    top = tk.Toplevel(root)
    top.title("Muuda filmi andmeid")
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    cursor.execute("""
SELECT m.title, d.name, m.release_year, g.name,
  m.duration, m.rating, l.name, c.name, m.description
FROM movies m
LEFT JOIN directors d ON m.director_id = d.id
LEFT JOIN genres g ON m.genre_id = g.id
LEFT JOIN languages l ON m.language_id = l.id
LEFT JOIN countries c ON m.country_id = c.id
WHERE m.id = ?
""", (record_id,))
    record = cursor.fetchone()
    director_list = [r[0] for r in cursor.execute(
        "SELECT name FROM directors")]
    genre_list = [r[0] for r in cursor.execute(
        "SELECT name FROM genres")]
    language_list = [r[0] for r in cursor.execute(
        "SELECT name FROM languages")]
    country_list = [r[0] for r in cursor.execute(
        "SELECT name FROM countries")]
    conn.close()

    labels = [
        ("Pealkiri", "entry"),
        ("Režissöör", "combobox", director_list),
        ("Aasta", "entry"),
        ("Žanr", "combobox", genre_list),
        ("Kestus", "entry"),
        ("Reiting", "entry"),
        ("Keel", "combobox", language_list),
        ("Riik", "combobox", country_list),
        ("Kirjeldus", "entry")
    ]
    entries = {}
    for i, item in enumerate(labels):
        text = item[0]
        tk.Label(top, text=text).grid(
            row=i, column=0, padx=10, pady=5, sticky=tk.W
        )
        if item[1] == "entry":
            widget = tk.Entry(top, width=50)
            widget.insert(0, record[i])
        else:
            widget = ttk.Combobox(
                top, width=48, values=item[2], state="readonly"
            )
            widget.set(record[i])
        widget.grid(row=i, column=1, padx=10, pady=5)
        entries[text] = widget

    def save_update():
        title = entries["Pealkiri"].get().strip()
        director = entries["Režissöör"].get()
        year = entries["Aasta"].get()
        genre = entries["Žanr"].get()
        duration = entries["Kestus"].get()
        rating = entries["Reiting"].get()
        language = entries["Keel"].get()
        country = entries["Riik"].get()
        description = entries["Kirjeldus"].get().strip()
        if not title or not year.isdigit():
            messagebox.showerror("Viga", "Kontrolli sisendandmeid!")
            return
        conn2 = sqlite3.connect('movies.db')
        cur2 = conn2.cursor()
        cur2.execute("SELECT id FROM directors WHERE name = ?",
                     (director,))
        director_id = cur2.fetchone()[0]
        cur2.execute("SELECT id FROM genres WHERE name = ?",
                     (genre,))
        genre_id = cur2.fetchone()[0]
        cur2.execute("SELECT id FROM languages WHERE name = ?",
                     (language,))
        language_id = cur2.fetchone()[0]
        cur2.execute("SELECT id FROM countries WHERE name = ?",
                     (country,))
        country_id = cur2.fetchone()[0]
        cur2.execute("""
UPDATE movies
SET title=?, director_id=?, release_year=?, genre_id=?,
    duration=?, rating=?, language_id=?, country_id=?,
    description=?
WHERE id=?
""", (
            title, director_id, int(year), genre_id, int(duration),
            float(rating) if rating else None, language_id,
            country_id, description, record_id
        ))
        conn2.commit()
        conn2.close()
        load_data_from_db(tree)
        top.destroy()
        messagebox.showinfo("Salvestamine",
                            "Andmed on edukalt uuendatud!")

    tk.Button(top, text="Salvesta", command=save_update).grid(
        row=len(labels), column=0, columnspan=2, pady=10
    )

def add_movie():
    top = tk.Toplevel(root)
    top.title("Lisa film")
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    director_list = [r[0] for r in cursor.execute(
        "SELECT name FROM directors")]
    genre_list = [r[0] for r in cursor.execute(
        "SELECT name FROM genres")]
    language_list = [r[0] for r in cursor.execute(
        "SELECT name FROM languages")]
    country_list = [r[0] for r in cursor.execute(
        "SELECT name FROM countries")]
    conn.close()

    labels = [
        "Pealkiri", "Režissöör", "Aasta", "Žanr", "Kestus",
        "Reiting", "Keel", "Riik", "Kirjeldus"
    ]
    entries = {}
    for i, label in enumerate(labels):
        tk.Label(top, text=label).grid(
            row=i, column=0, padx=10, pady=5, sticky=tk.W
        )
        if label in ("Režissöör", "Žanr", "Keel", "Riik"):
            values = {
                "Režissöör": director_list,
                "Žanr": genre_list,
                "Keel": language_list,
                "Riik": country_list
            }[label]
            widget = ttk.Combobox(
                top, values=values, state="readonly", width=48
            )
        else:
            widget = tk.Entry(top, width=50)
        widget.grid(row=i, column=1, padx=10, pady=5)
        entries[label] = widget

    def save():
        title = entries["Pealkiri"].get().strip()
        director = entries["Režissöör"].get()
        year = entries["Aasta"].get()
        genre = entries["Žanr"].get()
        duration = entries["Kestus"].get()
        rating = entries["Reiting"].get()
        language = entries["Keel"].get()
        country = entries["Riik"].get()
        description = entries["Kirjeldus"].get().strip()
        if not title or not year.isdigit():
            messagebox.showerror("Viga",
                "Palun täida pealkiri ja aasta korrektselt!")
            return
        conn2 = sqlite3.connect('movies.db')
        cur2 = conn2.cursor()
        cur2.execute("SELECT id FROM directors WHERE name = ?",
                     (director,))
        director_id = cur2.fetchone()[0]
        cur2.execute("SELECT id FROM genres WHERE name = ?",
                     (genre,))
        genre_id = cur2.fetchone()[0]
        cur2.execute("SELECT id FROM languages WHERE name = ?",
                     (language,))
        language_id = cur2.fetchone()[0]
        cur2.execute("SELECT id FROM countries WHERE name = ?",
                     (country,))
        country_id = cur2.fetchone()[0]
        cur2.execute("""
INSERT INTO movies
(title, director_id, release_year, genre_id, duration,
 rating, language_id, country_id, description)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
""", (
            title, director_id, int(year), genre_id, int(duration),
            float(rating) if rating else None, language_id,
            country_id, description
        ))
        conn2.commit()
        conn2.close()
        load_data_from_db(tree)
        top.destroy()
        messagebox.showinfo("Edu", "Film lisatud edukalt!")

    tk.Button(top, text="Salvesta", command=save).grid(
        row=len(labels), column=0, columnspan=2, pady=10
    )

def on_search():
    load_data_from_db(tree, search_entry.get())

def on_delete():
    selected = tree.selection()
    if selected:
        record_id = selected[0]
        if messagebox.askyesno("Kinnita", "Kas soovid kustutada?"):
            conn = sqlite3.connect('movies.db')
            cur = conn.cursor()
            cur.execute("DELETE FROM movies WHERE id=?", (record_id,))
            conn.commit()
            conn.close()
            load_data_from_db(tree)
            messagebox.showinfo("Edukalt", "Rida on kustutatud!")
    else:
        messagebox.showwarning("Valik puudub",
                               "Palun vali kõigepealt rida!")

# Põhirakendus
root = tk.Tk()
create_database()
root.title("Filmid")
root.geometry("1000x600")

top_frame = tk.Frame(root)
top_frame.pack(fill=tk.X, pady=10, padx=10)

search_frame = tk.Frame(top_frame)
search_frame.pack(side=tk.LEFT, anchor="w")
tk.Label(search_frame, text="Otsi filmi:").pack(side=tk.LEFT)
search_entry = tk.Entry(search_frame)
search_entry.pack(side=tk.LEFT, padx=5)
tk.Button(search_frame, text="Otsi", command=on_search).pack(side=tk.LEFT)

buttons_frame = tk.Frame(top_frame)
buttons_frame.pack(side=tk.RIGHT, anchor="e")
tk.Button(
    buttons_frame,
    text="Juhtimine",
    command=open_reference_window
).pack(side=tk.LEFT, padx=5)
tk.Button(buttons_frame, text="Lisa film",
          command=add_movie).pack(side=tk.LEFT, padx=5)
tk.Button(buttons_frame, text="Uuenda",
          command=open_update_window).pack(side=tk.LEFT, padx=5)
tk.Button(buttons_frame, text="Kustuta",
          command=on_delete).pack(side=tk.LEFT, padx=5)

frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True, pady=20, padx=10)
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
tree = ttk.Treeview(
    frame,
    columns=(
        "title", "director", "year", "genre", "duration",
        "rating", "language", "country", "description"
    ),
    show="headings",
    yscrollcommand=scrollbar.set
)
tree.pack(fill=tk.BOTH, expand=True)
scrollbar.config(command=tree.yview)

tree.heading("title", text="Pealkiri")
tree.heading("director", text="Režissöör")
tree.heading("year", text="Aasta")
tree.heading("genre", text="Žanr")
tree.heading("duration", text="Kestus")
tree.heading("rating", text="Reiting")
tree.heading("language", text="Keel")
tree.heading("country", text="Riik")
tree.heading("description", text="Kirjeldus")

tree.column("title", width=150)
tree.column("director", width=100)
tree.column("year", width=60)
tree.column("genre", width=100)
tree.column("duration", width=60)
tree.column("rating", width=60)
tree.column("language", width=80)
tree.column("country", width=80)
tree.column("description", width=200)

load_data_from_db(tree)
root.mainloop()
