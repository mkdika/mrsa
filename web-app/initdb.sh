#!/bin/sh

cat schema.sql | sqlite3 sentiment.db
