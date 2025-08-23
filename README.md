# JSON Projects

This repository contains two projects that demonstrate JSON serialization and deserialization of custom Python objects using custom encoders and decoders.

---

## Project 1: JSON Serialization with Custom Encoder

This project demonstrates how to serialize custom Python objects into JSON format using a custom JSON encoder. The project includes two main classes, `Stock` and `Trade`, which represent stock market data and trade activities, respectively. These objects are serialized into JSON using the `CustomEncoder` class.

### Features

- **Custom Classes**:
  - `Stock`: Represents stock market data with attributes like symbol, date, open, high, low, close, and volume.
  - `Trade`: Represents trade activities with attributes like symbol, timestamp, order type, price, volume, and commission.

- **Custom JSON Encoder**:
  - The `CustomEncoder` class extends `JSONEncoder` to handle serialization of `Stock`, `Trade`, `datetime`, `date`, and `Decimal` objects.

- **Example Data**:
  - The `activity` dictionary contains sample stock quotes and trade activities, which are serialized into JSON format.

### How to Run

1. Ensure you have Python 3 installed.
2. Run the script `Project_1.py`:
   ```bash
   python Project_1.py
   ```
3. The serialized JSON output will be printed to the console.

---

## Project 2: JSON Deserialization with Custom Decoder

This project builds upon Project 1 by adding functionality to deserialize JSON data back into Python objects using a custom JSON decoder. The `CustomDecoder` class is used to parse JSON data and recreate `Stock` and `Trade` objects.

### Features

- **Custom JSON Decoder**:
  - The `CustomDecoder` class extends `JSONDecoder` to handle deserialization of `Stock` and `Trade` objects from JSON data.
  - Includes helper functions `decode_stock`, `decode_trade`, and `decode_financials` to reconstruct objects from their serialized representations.

- **Integration with Project 1**:
  - Reuses the `Stock`, `Trade`, and `CustomEncoder` classes from Project 1 for encoding and decoding.

### How to Run

1. Ensure you have Python 3 installed.
2. Run the script `Project_2.py`:
   ```bash
   python Project_2.py
   ```
3. The script demonstrates encoding data using `CustomEncoder` and decoding it back into Python objects using `CustomDecoder`.

---

## Dependencies

- Python Standard Library:
  - `datetime`
  - `decimal`
  - `json`

---

## License

This project is open-source and available under the MIT License.