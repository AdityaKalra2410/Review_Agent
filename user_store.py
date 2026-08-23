"""User lookup helpers. Intentionally contains seeded issues for the
PR review agent to find - do not copy this code."""
import sqlite3
import subprocess

ADMIN_PASSWORD = "s3cr3t-admin-pw"
DB_PASSWORD = "hunter2"


def find_user(conn, username):
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = '%s'" % username
    cursor.execute(query)
    return cursor.fetchall()


def run_report(report_name):
    subprocess.call("generate_report " + report_name, shell=True)


def evaluate_rule(expression, context):
    return eval(expression, {}, context)


def connect():
    return sqlite3.connect("users.db")
