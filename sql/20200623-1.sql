CREATE TABLE Proxy (
    id INTEGER PRIMARY KEY,
    host TEXT NOT NULL,
    state TEXT,
    last_ping TEXT,
    last_delay INTEGER
);