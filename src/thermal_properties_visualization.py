"""
Visualization of ZnO nanofluid thermal properties

This script provides visualizations for key thermal properties of ZnO nanofluids
based on research data from the project report.
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import os


plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("viridis")

results_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "results")
if not os.path.exists(results_dir):
    os.makedirs(results_dir)
    print(f"Created results directory at: {results_dir}")
else:
    print(f"Results directory exists at: {results_dir}")

def plot_thermal_conductivity_vs_temperature():
    """
    Plot the effect of temperature on thermal conductivity for different
    volume concentrations of ZnO nanofluids
    """
    temperatures = np.arange(30, 55, 5)  # Temperature in °C
    
    # Thermal conductivity ratios (k/k₀) for different volume percentages
    tc_ratio_02vol = [0.85, 0.95, 1.05, 1.2, 1.6]
    tc_ratio_03vol = [0.7, 0.8, 0.9, 1.05, 1.3]
    tc_ratio_04vol = [0.55, 0.65, 0.75, 0.9, 1.1]
    tc_ratio_05vol = [0.35, 0.5, 0.65, 0.75, 0.85]
    
    plt.figure(figsize=(10, 6))
    
    plt.plot(temperatures, tc_ratio_02vol, 'o-', linewidth=2, label='0.2 Vol%')
    plt.plot(temperatures, tc_ratio_03vol, 's-', linewidth=2, label='0.3 Vol%')
    plt.plot(temperatures, tc_ratio_04vol, '^-', linewidth=2, label='0.4 Vol%')
    plt.plot(temperatures, tc_ratio_05vol, 'd-', linewidth=2, label='0.5 Vol%')
    
    plt.xlabel('Temperature (°C)', fontsize=14)
    plt.ylabel('Thermal Conductivity Ratio (k/k₀)', fontsize=14)
    plt.title('Effect of Temperature on Thermal Conductivity Ratio\nfor Different ZnO Nanofluid Concentrations', fontsize=16)
    plt.legend(fontsize=12)
    plt.grid(True)
    plt.tight_layout()
    
    output_path = os.path.join(results_dir, 'thermal_conductivity_vs_temperature.png')
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"Saved figure to: {output_path}")
    plt.show()

def plot_heat_transfer_coefficient_axial():
    """
    Plot the heat transfer coefficient vs the axial position for
    different concentrations of ZnO nanofluid
    """
    
    axial_positions = [0, 200, 400, 600, 800]  # Axial position x/D
    
    # Heat transfer coefficients at Reynolds number = 1896
    htc_water = [575, 425, 375, 350, 325]
    htc_005vol = [625, 475, 425, 375, 350]
    htc_010vol = [650, 525, 450, 400, 375] 
    htc_015vol = [750, 575, 500, 450, 425]
    htc_020vol = [850, 650, 550, 500, 450]
    htc_025vol = [950, 775, 625, 550, 475]
    
    plt.figure(figsize=(10, 6))
    
    plt.plot(axial_positions, htc_water, 'o-', linewidth=2, label='Water')
    plt.plot(axial_positions, htc_005vol, 's-', linewidth=2, label='0.05 vol%')
    plt.plot(axial_positions, htc_010vol, '^-', linewidth=2, label='0.10 vol%')
    plt.plot(axial_positions, htc_015vol, 'd-', linewidth=2, label='0.15 vol%')
    plt.plot(axial_positions, htc_020vol, '*-', linewidth=2, label='0.20 vol%')
    plt.plot(axial_positions, htc_025vol, 'x-', linewidth=2, label='0.25 vol%')
    
    plt.xlabel('Axial Position (x/D)', fontsize=14)
    plt.ylabel('Heat Transfer Coefficient (W/m²°C)', fontsize=14)
    plt.title('Heat Transfer Coefficient vs. Axial Position\nfor Different ZnO Nanofluid Concentrations (Re = 1896)', fontsize=16)
    plt.legend(fontsize=12)
    plt.grid(True)
    plt.tight_layout()

    output_path = os.path.join(results_dir, 'heat_transfer_coefficient_axial.png')
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"Saved figure to: {output_path}")
    plt.show()

def plot_viscosity_vs_temperature():
    """
    Plot the effect of shape on viscosity for ZnO nanoparticles in R134a
    """
    temperatures = np.array([280, 285, 290, 295, 300, 305, 310])  # Temperature in K
    
    # Viscosity values for different particle shapes
    visc_r134a = [0.24, 0.22, 0.21, 0.19, 0.18, 0.17, 0.16]
    visc_spherical = [0.27, 0.26, 0.25, 0.24, 0.23, 0.23, 0.22]
    visc_cubic = [0.39, 0.38, 0.37, 0.35, 0.34, 0.33, 0.32]
    
    plt.figure(figsize=(10, 6))
    
    plt.plot(temperatures, visc_r134a, 'o-', linewidth=2, label='R-134a')
    plt.plot(temperatures, visc_spherical, 's-', linewidth=2, label='Spherical ZnO')
    plt.plot(temperatures, visc_cubic, '^-', linewidth=2, label='Cubic ZnO')
    
    plt.xlabel('Temperature (K)', fontsize=14)
    plt.ylabel('Viscosity (mPa·s)', fontsize=14)
    plt.title('Effect of ZnO Nanoparticle Shape on Viscosity\nof R-134a Refrigerant', fontsize=16)
    plt.legend(fontsize=12)
    plt.grid(True)
    plt.tight_layout()
    
    output_path = os.path.join(results_dir, 'viscosity_vs_temperature.png')
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"Saved figure to: {output_path}")
    plt.show()

def plot_comparative_base_fluids():
    """
    Plot comparison of thermal conductivity for ZnO in different base fluids
    """
    
    volume_fractions = [0, 0.5, 1.0, 1.5, 2.0]
    
    # Thermal conductivity for different base fluids
    tc_water = [0.6, 0.62, 0.65, 0.68, 0.71]
    tc_eg = [0.25, 0.37, 0.45, 0.5, 0.54]
    tc_mixture = [0.4, 0.5, 0.58, 0.62, 0.65]
    
    plt.figure(figsize=(10, 6))
    
    plt.plot(volume_fractions, tc_water, 'o-', linewidth=2, label='Water')
    plt.plot(volume_fractions, tc_eg, 's-', linewidth=2, label='Ethylene Glycol')
    plt.plot(volume_fractions, tc_mixture, '^-', linewidth=2, label='50% Water + 50% EG')
    
    plt.xlabel('ZnO Volume Fraction (%)', fontsize=14)
    plt.ylabel('Thermal Conductivity (W/m·K)', fontsize=14)
    plt.title('Thermal Conductivity of ZnO Nanofluids\nwith Different Base Fluids at 25°C', fontsize=16)
    plt.legend(fontsize=12)
    plt.grid(True)
    plt.tight_layout()
    
    output_path = os.path.join(results_dir, 'thermal_conductivity_base_fluids.png')
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"Saved figure to: {output_path}")
    plt.show()

def create_enhancement_summary():
    """
    Create a bar chart summarizing the enhancement in thermal properties
    """
    properties = ['Thermal Conductivity', 'Heat Transfer Coefficient', 
                 'Viscosity Increase', 'Stability']
    
    # Percentage enhancement at 0.25 vol% (approximate values from report)
    enhancement = [36, 65, 30, 75]
    
    plt.figure(figsize=(10, 6))
    
    bars = plt.bar(properties, enhancement, color=sns.color_palette("viridis", 4))
   
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height + 1,
                f'{height}%', ha='center', va='bottom', fontsize=12)
    
    plt.xlabel('Property', fontsize=14)
    plt.ylabel('Enhancement (%)', fontsize=14)
    plt.title('Enhancement in Properties with ZnO Nanofluid (0.25 vol%)\nCompared to Base Fluid', fontsize=16)
    plt.ylim(0, 100)
    plt.grid(True, axis='y')
    plt.tight_layout()
   
    output_path = os.path.join(results_dir, 'enhancement_summary.png')
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"Saved figure to: {output_path}")
    plt.show()


def plot_reynolds_effect_on_htc():
    """
    Plot the effect of Reynolds number on heat transfer coefficient
    at different ZnO nanofluid concentrations
    """
    reynolds_numbers = [1083, 1354, 1625, 1896, 2167]
    
    # Heat transfer coefficient at different Reynolds numbers for water and ZnO nanofluids
    htc_water = [525, 550, 575, 600, 625]
    htc_010vol = [600, 625, 650, 675, 700]
    htc_020vol = [700, 750, 800, 850, 900]
    htc_025vol = [750, 800, 875, 950, 1050]
    
    plt.figure(figsize=(10, 6))
    
    plt.plot(reynolds_numbers, htc_water, 'o-', linewidth=2, label='Water')
    plt.plot(reynolds_numbers, htc_010vol, 's-', linewidth=2, label='0.10 vol%')
    plt.plot(reynolds_numbers, htc_020vol, '^-', linewidth=2, label='0.20 vol%')
    plt.plot(reynolds_numbers, htc_025vol, 'd-', linewidth=2, label='0.25 vol%')
    
    plt.xlabel('Reynolds Number', fontsize=14)
    plt.ylabel('Heat Transfer Coefficient (W/m²°C)', fontsize=14)
    plt.title('Effect of Reynolds Number on Heat Transfer Coefficient\nfor Different ZnO Nanofluid Concentrations', fontsize=16)
    plt.legend(fontsize=12)
    plt.grid(True)
    plt.tight_layout()
    
    output_path = os.path.join(results_dir, 'reynolds_effect_on_htc.png')
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"Saved figure to: {output_path}")
    plt.show()


if __name__ == "__main__":
    print("Generating visualizations for ZnO nanofluid properties...")

    plot_thermal_conductivity_vs_temperature()
    plot_heat_transfer_coefficient_axial()
    plot_viscosity_vs_temperature()
    plot_comparative_base_fluids()
    create_enhancement_summary()
    plot_reynolds_effect_on_htc()
    
    print("All visualizations completed and saved!")