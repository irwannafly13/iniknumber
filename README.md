# iNIKnumber

`iNIKnumber` is a Python package designed to parse and validate Indonesian NIK (Nomor Induk Kependudukan) numbers. The NIK is a unique identification number used in Indonesia, containing information about the holder's place of birth, date of birth, and a unique identifier.

## Features

- Parse province, kabupaten (regency), kecamatan (district), and kelurahan (village) codes from the NIK.
- Extract and validate the date of birth.
- Retrieve location names based on the codes.
- Designed for easy integration into other Python projects.

## Installation

Install `iNIKnumber` via pip:

```bash
pip install iniknumber --index-url https://pypi.org/simple/
```

## Usage

Here’s how you can use the package to parse and validate a NIK number:

### Example

```python
import iniknumber

# Example NIK number
nik_number = "3202080504910003"

# Parse the NIK
result = iniknumber.check_code(nik_number)

# Print the result
print(result)
```

### Expected Output

The above code will output:

```json
{
    "province_code": "32",
    "province_name": "JAWA BARAT",
    "kabupaten_code": "32.02",
    "kabupaten_name": "KAB. BANDUNG",
    "kecamatan_code": "32.02.08",
    "kecamatan_name": "CILEUNYI",
    "birth_date": "05-04-1991",
    "unique_number": "0003"
}
```

## Functions

### `check_code(nik: str) -> dict`

Parses the given NIK and returns a dictionary containing the following:

- `province_code`: The province code extracted from the NIK.
- `province_name`: The name of the province.
- `kabupaten_code`: The kabupaten (regency) code.
- `kabupaten_name`: The name of the kabupaten.
- `kecamatan_code`: The kecamatan (district) code.
- `kecamatan_name`: The name of the kecamatan.
- `birth_date`: The date of birth in `DD-MM-YYYY` format.
- `unique_number`: A unique identifier for individuals born on the same day in the same kecamatan.

### `load_region_data(code: str) -> dict`

Loads additional details about a specific region based on its code.

## Data

The package includes a CSV file containing mapping data for:

- Provinces
- Regencies (Kabupaten)
- Districts (Kecamatan)
- Villages (Kelurahan)

This data is used to translate codes into human-readable names.

## Contributing

Contributions are welcome! If you’d like to improve the package or add features, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For questions or suggestions, feel free to reach out via the [GitHub repository](https://github.com/yourusername/iniknumber).
