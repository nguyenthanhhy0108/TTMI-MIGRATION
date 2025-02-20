# ERPNext Migration

## 📌 Your Current Version
[Version Here](URL)

## 🛠️ Installation

### 1. System Requirements
- **Python**
- **Conda**

### 2. Conda Installation
You should install Miniconda. Follow the official instructions [here](https://docs.conda.io/en/latest/miniconda.html).

### 3. Clone Repository
```bash
git clone https://github.com/your-org/erpnext-migration.git
cd erpnext-migration
```

### 4. Create Virtual Environment & Install Dependencies
```bash
conda create --name TTMI-MIGRATION python=3.13     # Create environment
conda activate TTMI-MIGRATION                      # Activate environment
pip install -r requirements.txt                    # Install dependencies
```

### 5. Run Migration
```bash
python main.py -v {your_expected_version}
```

## 📜 License
This project is licensed under the **MIT License**. See the full details in [`LICENSE`](LICENSE).
