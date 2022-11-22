"""
Converts a date to its ISO-8601 representation.
"""
from datetime import datetime

d = datetime.now()
iso_d = d.isoformat()
print(iso_d)

# -------------------- more --------------------
# datetime.isoformat() <--> datetime.fromisoformat()
