# Plant Trees 🌲🌲🌲 with Python

---

### Install
```bash
pip install git+https://github.com/mdn522/ecologi-python.git
```

### Import
```python
from ecologi import Ecologi

eco = Ecologi()
# eco = Ecologi(auth_token='YOUR-AUTH-TOKEN')
# auth_token is required for Impact API
```

---

## Reporting API

```python
username = ''

# Get Total Number of Trees
eco.get_total_number_of_trees(username)

# Get Total Tonnes of CO2e Offset
eco.get_user_carbon_offset(username)

# Get Total Impact
eco.get_user_impact(username)
```

---

## Impact API

### Purchase Trees
```python
eco.purchase_trees()  # Provide necessary arguments mentioned in the API docs
```

### Purchase Carbon Offsets
```python
eco.purchase_trees()  # Provide necessary arguments mentioned in the API docs
```
