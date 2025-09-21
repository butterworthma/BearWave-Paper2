#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Apply Standardized Format to All foF2 Analysis Scripts
======================================================

This script applies the standardized report format to all foF2 analysis scripts
to ensure consistent appearance for professional reports.

Author: Research Team
License: MIT
"""

import os
import subprocess
from datetime import datetime

# List of foF2 analysis scripts to standardize
FOF2_SCRIPTS = [
    "guam_april15-28_fof2_7years.py",
    "guam_april15_fof2_7years.py", 
    "guam_fof2_april.py",
    "darwin_april15-28_fof2_7years.py",
    "darwin_april15_fof2_7years.py",
    "darwin_fof2_april.py"
]

def run_script_with_standardized_format(script_name):
    """Run a foF2 analysis script with standardized formatting"""
    
    script_path = f"Mark_paper_2/{script_name}"
    
    if not os.path.exists(script_path):
        print(f"❌ Script not found: {script_name}")
        return False
    
    print(f"\n📊 Running {script_name} with standardized format...")
    print("="*60)
    
    try:
        # Run the script using the virtual environment
        result = subprocess.run([
            "python",
            script_path
        ], 
        cwd="/Users/samanthabutterworth/PycharmProjects/pythonProject3",
        capture_output=True, 
        text=True, 
        timeout=300)  # 5 minute timeout
        
        if result.returncode == 0:
            print(f"✅ Successfully completed: {script_name}")
            if result.stdout:
                # Print last few lines of output to show completion
                lines = result.stdout.strip().split('\n')
                for line in lines[-5:]:
                    if line.strip():
                        print(f"   {line}")
            return True
        else:
            print(f"❌ Error in {script_name}:")
            if result.stderr:
                print(f"   {result.stderr}")
            return False
            
    except subprocess.TimeoutExpired:
        print(f"⏰ Timeout: {script_name} took too long to complete")
        return False
    except Exception as e:
        print(f"❌ Exception running {script_name}: {e}")
        return False

def generate_all_standardized_charts():
    """Generate all foF2 charts with standardized formatting"""
    
    print("🎯 GENERATING ALL STANDARDIZED foF2 ANALYSIS CHARTS")
    print("="*65)
    print("This will create consistent, report-ready charts for all stations and periods")
    print()
    
    # Check if standardized format module exists
    if not os.path.exists("Mark_paper_2/standardized_report_format.py"):
        print("❌ Standardized format module not found!")
        print("   Please ensure standardized_report_format.py exists in Mark_paper_2/")
        return
    
    successful_runs = []
    failed_runs = []
    
    # Run each script
    for script in FOF2_SCRIPTS:
        success = run_script_with_standardized_format(script)
        if success:
            successful_runs.append(script)
        else:
            failed_runs.append(script)
    
    # Summary
    print(f"\n🎉 STANDARDIZED CHART GENERATION COMPLETE!")
    print("="*55)
    
    print(f"\n✅ SUCCESSFUL ({len(successful_runs)}/{len(FOF2_SCRIPTS)}):")
    for script in successful_runs:
        print(f"  • {script}")
    
    if failed_runs:
        print(f"\n❌ FAILED ({len(failed_runs)}/{len(FOF2_SCRIPTS)}):")
        for script in failed_runs:
            print(f"  • {script}")
    
    print(f"\n📁 All charts saved to: /Users/samanthabutterworth/PycharmProjects/pythonProject3/")
    
    # List expected output files
    print(f"\n📊 EXPECTED STANDARDIZED CHART FILES:")
    timestamp = datetime.now().strftime('%Y%m%d')
    expected_files = [
        f"foF2_Analysis_Guam_April_15_28_Combined_Overview_{timestamp}_*.png",
        f"foF2_Analysis_Guam_April_15th_Combined_Overview_{timestamp}_*.png",
        f"foF2_Analysis_Guam_April_Combined_Overview_{timestamp}_*.png",
        f"foF2_Analysis_Darwin_April_15_28_Combined_Overview_{timestamp}_*.png",
        f"foF2_Analysis_Darwin_April_15th_Combined_Overview_{timestamp}_*.png",
        f"foF2_Analysis_Darwin_April_Combined_Overview_{timestamp}_*.png"
    ]
    
    for file_pattern in expected_files:
        print(f"  • {file_pattern}")
    
    print(f"\n💡 STANDARDIZED FORMAT FEATURES:")
    print("  • Consistent 16×12 inch size for all charts")
    print("  • Uniform color scheme across all analyses")
    print("  • Standardized titles and labels")
    print("  • Professional layout with proper spacing")
    print("  • NVIS frequency band integration")
    print("  • Day/night shading on hourly patterns")
    print("  • High resolution (160 DPI) for reports")
    
    print(f"\n🎯 READY FOR REPORT INTEGRATION:")
    print("  All charts now have consistent formatting and can be")
    print("  directly inserted into research reports or presentations.")

def check_chart_files():
    """Check which standardized chart files exist"""
    
    print("\n📋 CHECKING EXISTING STANDARDIZED CHART FILES:")
    print("="*50)
    
    chart_dir = "/Users/samanthabutterworth/PycharmProjects/pythonProject3/"
    
    # Look for standardized chart files
    standardized_files = []
    all_files = os.listdir(chart_dir)
    
    for file in all_files:
        if file.startswith("foF2_Analysis_") and file.endswith(".png"):
            standardized_files.append(file)
    
    if standardized_files:
        print(f"✅ Found {len(standardized_files)} standardized chart files:")
        for file in sorted(standardized_files):
            file_path = os.path.join(chart_dir, file)
            file_size = os.path.getsize(file_path) / (1024 * 1024)  # MB
            mod_time = datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%Y-%m-%d %H:%M')
            print(f"  • {file} ({file_size:.1f} MB, {mod_time})")
    else:
        print("❌ No standardized chart files found")
        print("   Run generate_all_standardized_charts() to create them")

def main():
    """Main function"""
    
    print("🎨 STANDARDIZED foF2 CHART GENERATOR")
    print("="*40)
    print("Options:")
    print("1. Generate all standardized charts")
    print("2. Check existing chart files")
    print("3. Run specific script")
    print()
    
    choice = input("Select option (1-3, default 1): ").strip()
    
    if choice == "2":
        check_chart_files()
    elif choice == "3":
        print("\nAvailable scripts:")
        for i, script in enumerate(FOF2_SCRIPTS, 1):
            print(f"  {i}. {script}")
        
        try:
            script_choice = int(input(f"\nSelect script (1-{len(FOF2_SCRIPTS)}): ")) - 1
            if 0 <= script_choice < len(FOF2_SCRIPTS):
                run_script_with_standardized_format(FOF2_SCRIPTS[script_choice])
            else:
                print("❌ Invalid selection")
        except ValueError:
            print("❌ Invalid input")
    else:
        # Default: generate all charts
        generate_all_standardized_charts()

if __name__ == "__main__":
    main()
