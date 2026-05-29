**Pytest**
```python
import pytest
from csv_reader import read_csv

def test_read_csv():
    csv_data = read_csv('example.csv')
    assert len(csv_data) > 0
    assert isinstance(csv_data, list)
    assert isinstance(csv_data[0], dict)

def test_read_csv_empty_file():
    csv_data = read_csv('empty.csv')
    assert len(csv_data) == 0

def test_read_csv_invalid_file():
    with pytest.raises(FileNotFoundError):
        read_csv('invalid_file.csv')
```

**Jest**
```javascript
import { readCsv } from './csv-reader';

describe('readCsv', () => {
  it('should return data from a valid CSV file', async () => {
    const csvData = await readCsv('example.csv');
    expect(csvData).not.toBeNull();
    expect(csvData).toBeInstanceOf(Array);
    expect(csvData[0]).toBeInstanceOf(Object);
  });

  it('should return an empty array from an empty CSV file', async () => {
    const csvData = await readCsv('empty.csv');
    expect(csvData).toEqual([]);
  });

  it('should throw an error for an invalid CSV file', async () => {
    await expect(readCsv('invalid_file.csv')).rejects.toThrowError('ENOENT');
  });
});
```
