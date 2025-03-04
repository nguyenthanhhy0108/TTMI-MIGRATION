# TTMI ERP Migration

## 🛠️ Installation

### 1. System Requirements
- **Python**
- **Conda**
- **ERP Next Docker**

### 2. Conda Installation
You should install **Miniconda**. Follow the official instructions [here](https://docs.conda.io/en/latest/miniconda.html).

### 3. ERP Next Docker Installation
You should install **ERP Next Docker**. Follow the official instructions [here](https://github.com/frappe/frappe_docker).

**`Waiting for CREATE-SITE container stop, everything will be done!`**

After these steps, make sure your ERP Next Docker is running on port **8080**.

### 4. Clone Repository
```bash
git clone https://github.com/nguyenthanhhy0108/TTMI-MIGRATION.git
cd TTMI-MIGRATION
```

### 5. Create Virtual Environment & Install Dependencies
```bash
conda create --name TTMI-MIGRATION python=3.13     # Create environment
conda activate TTMI-MIGRATION                      # Activate environment
pip install -r requirements.txt                    # Install dependencies
```

### 6. Run Migration

```bash
python main.py -v 0                                # Initialize you ERP-NEXT version
```

```bash
python main.py -v {your_expected_version}
```

## New Doctype:
- Order Source
- Item Price Table
- Province

## 📜 License
This project is licensed under the **MIT License**. See the full details in [`LICENSE`](LICENSE).

