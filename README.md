# BearWave Paper 2 - Ionospheric foF2 Critical Frequency Analysis

## 📊 Overview
This repository contains the complete analysis code for **BearWave Paper 2** - a comprehensive ionospheric foF2 (critical frequency) analysis toolkit. The code analyzes data from Guam and Darwin monitoring stations and provides standardized 2x2 chart layouts for professional scientific reports.

## 🚀 Quick Start

### Prerequisites
```bash
pip install -r requirements.txt
```

### Basic Usage
```bash
# Generate all 6 standardized charts
python generators/generate_corrected_charts.py

# Run individual analysis
python analysis/guam_april15-28_fof2_7years.py

# Batch process all analyses
python automation/run_all_2x2_charts.py
```

## 📁 Repository Structure
- `core/` - Core layout and formatting modules
- `analysis/` - Main foF2 analysis scripts (6 scripts)
- `generators/` - Chart generation utilities
- `automation/` - Batch processing scripts
- `utilities/` - Display and viewing tools
- `docs/` - Documentation and guides
- `data/` - Place NVIS_data.xlsx here (not tracked by git)
- `output/` - Generated charts will be saved here

## 📋 Data Requirements
- NVIS_data.xlsx with Guam and Darwin sheets
- Place in the `data/` directory
- Update file paths in scripts if needed

## 📊 Generated Charts
- Standardized 2x2 layout with consistent positioning
- Hourly patterns, statistical distributions, temporal progression
- NVIS frequency band analysis
- Professional formatting for reports

## 🔧 Key Features
- **Standardized Layout Enforcer**: Ensures consistent chart positioning
- **Correct foF2 Calculations**: Uses proper ionospheric physics
- **Multi-Station Analysis**: Guam and Darwin comparative studies
- **Professional Formatting**: Ready for scientific reports

See `SCRIPT_DEPENDENCY_MAP.md` for detailed file relationships.

## 📞 Support
For issues or questions, refer to the documentation in the `docs/` directory.
