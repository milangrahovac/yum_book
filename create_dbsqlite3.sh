#!/bin/bash

DB_FILE="db.sqlite3"

if [ ! -f "$DB_FILE" ]; then
  touch "$DB_FILE"
  echo "Created: $DB_FILE"
else
  echo "Already exists: $DB_FILE"
fi
