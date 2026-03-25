# Create a dummy vulnerability: Command Injection
import os

command = input("Enter command: ")
os.system(command)  # <-- This is a critical security issue (B605)
