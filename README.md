# 🔄 Python Custom JSON Encoder & Decoder

This project demonstrates how to serialize and deserialize a custom Python class object using the built-in `json` module.

Since Python's default `json.dumps()` cannot directly serialize custom objects, this project shows how to:

- Create a custom JSON encoder using `JSONEncoder`
- Convert a class object to JSON
- Decode JSON back into a Python object
- Use `object_hook` for custom decoding

---

## 📌 Problem Statement

Python's `json` module cannot directly serialize custom class objects.

Example:
```python
json.dumps(User("Max", 27))
