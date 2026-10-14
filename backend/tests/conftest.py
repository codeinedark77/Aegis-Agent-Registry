import os
import pytest

# Ensure testing environment variables are always set before app imports
os.environ["DATABASE_URL"] = "sqlite+aiosqlite:///:memory:"
os.environ["SECRET_KEY"] = "supersecretkey1234567890testingkey!"
os.environ["DEBUG"] = "False"
