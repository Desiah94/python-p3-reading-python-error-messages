#!/usr/bin/env python3

wrong_type = 'abc' + str(123)  # Convert the integer to a string before concatenating

# Test
assert wrong_type == 'abc123'
