# VortexBlade: A Mid-Fidelity Free-Wake Solver for Propeller Aerodynamics

<p align="center">
<img width="512" height="512" alt="VortexBlade Logo" src="https://github.com/user-attachments/assets/77bc0471-584e-447a-8ddc-cbee6d75a04d" />
</p>

**VortexBlade is an advanced aerodynamic analysis tool that combines a three-dimensional, unsteady free-wake vortex method with a Blade Element Momentum (BEM) approach to deliver mid-fidelity performance predictions for propellers and rotors. By simulating the full wake development, it overcomes the inherent limitations of standalone BEMT-based approaches, especially in complex flow conditions.**

---

## Core Aerodynamic Theory

VortexBlade is built on a first-principles approach to fluid dynamics. Unlike simplified models that rely on momentum balance, this solver directly simulates the behavior of the wake as it is shed from the propeller blades.

* **Free-Wake Method:** The core of the solver is its "free-wake" methodology. At each time step, vortex filaments representing the vorticity shed from the trailing edge of the blades are introduced into the flow field. These filaments are then convected downstream with the local velocity, which is a sum of the freestream velocity and the velocity induced by all other vortex elements in the wake. This allows the wake to develop its shape freely and realistically, capturing complex phenomena like wake contraction and interaction.

* **Biot-Savart Law:** The velocity induced by each straight-line vortex segment on every other point in the flow field (both on the blades and in the wake) is calculated using the Biot-Savart law. This fundamental law relates the strength ($\Gamma$) and geometry of a vortex element ($d\vec{l}$) to the velocity it induces ($\vec{V}$) at a point defined by the position vector $\vec{r}$.

    $$\vec{V} = \frac{\Gamma}{4\pi} \int \frac{d\vec{l} \times \vec{r}}{|\vec{r}|^3}$$

* **Vortex Core Growth Model:** To avoid the physical and mathematical singularity at the center of a vortex filament, a viscous core model is implemented. The core radius of each filament evolves at every time step according to a turbulent viscosity model. The turbulent viscosity ($\nu_t$) is first calculated based on the local vortex strength ($\Gamma$) and kinematic viscosity ($\nu$):

    $$\nu_t = \nu \left(1 + C_1 \left(\frac{|\Gamma|}{\nu}\right)^n\right)$$

    The core radius ($r_c$) then grows with time ($t$) from its initial radius ($r_{c,0}$), driven by this turbulent viscosity:

    $$r_c(t) = \sqrt{r_{c,0}^2 + 4a \nu_t t}$$

    This allows the core to grow dynamically in response to physical vortex stretching, realistically diffusing the vorticity over time and ensuring a stable, physical solution.

---

## Key Features

* **Mid-Fidelity Free-Wake Model:** Accurately simulates the convection and interaction of shed vortex filaments for a precise calculation of the non-uniform induced velocity field.
* **Selectable Aero Solvers:** Choose between the classic **XFOIL** for iterative polar generation or the AI-based **NeuralFoil** for rapid, on-the-fly aerodynamic predictions.
* **Interactive GUI:** A comprehensive and user-friendly interface allows for easy setup of simulation parameters, flight conditions, and analysis methods without touching a line of code.
* **Parallelized Solution:** Leverages MATLAB's `parfor` to significantly accelerate demanding calculations like wake convection and induced velocity updates.
* **Advanced Live Visualization:** The GUI provides an interactive 3D plot of the developing wake, a 2D contour plot of the axial inflow, and real-time performance graphs.
* **Post-Processing & Animation:** Save complete simulation states and use the built-in animation tool to create high-quality videos (`.mp4`) or GIFs (`.gif`).
* **Modular Propeller Library:** Easily add, manage, and visualize different propeller geometries through a simple folder structure.

---

## Version Changelog

### **Version 2.0**

* **NeuralFoil Integration:**
    * VortexBlade now integrates **NeuralFoil** as an AI-based alternative to XFOIL. It is a deep neural network trained on XFOIL data that provides near-instantaneous aerodynamic predictions.
    * When selected, NeuralFoil calculates coefficients in real-time for the exact AoA and Reynolds number of each blade element at every time step, eliminating the need for pre-generated polar tables. More information can be found at [github.com/peterdsharpe/NeuralFoil](https://github.com/peterdsharpe/NeuralFoil).
* **GUI & Workflow Enhancements:**
    * Added a dropdown menu to seamlessly switch between **'XFOIL'** and **'NeuralFoil'** analysis methods.
    * Included a script to automate the installation of required Python dependencies for NeuralFoil.

### **Version 1.2**

* **Dynamic Stall Model:** Implemented a Beddoes-Leishmann type dynamic stall model to accurately capture unsteady aerodynamic effects (e.g., lift overshoot) during rapid changes in angle of attack.
* **Performance & Visualization:**
    * Fully vectorized the core induced velocity routine for significantly faster simulation times.
    * Switched to the 'coolwarm' colormap for higher-quality, more intuitive contour plots.
* **GUI & User Experience:** Added a button to display the fully extended and blended aerodynamic polars directly in the GUI.

---

## Showcase

### Main Application Interface

The intuitive GUI gives you full control over every aspect of the simulation, from propeller selection and flight conditions (velocity, angle of incidence) to the numerical details of the wake discretization and vortex core model.

V1.2 Axial Flow
<img width="1780" height="1324" alt="image" src="https://github.com/user-attachments/assets/e6db4046-dfad-4c0f-b475-432378ad5225" />

<img width="2996" height="1874" alt="CleanShot 2025-07-27 at 02 02 13@2x" src="https://github.com/user-attachments/assets/ea51b1a1-17a9-4bca-893b-969c69f5213a" />

### Live Wake Visualization

https://github.com/user-attachments/assets/63215b23-d7e6-47ff-94d0-5ae12465593d

https://github.com/user-attachments/assets/9059d387-2025-40d8-8dd0-6631dacbcbb5

Gain a deep understanding of the propeller's aerodynamic environment by observing the wake structure evolve in real-time. The interface displays the 3D vortex filaments trailing from the blades, the solid propeller geometry, and a 2D slice of the induced velocity field simultaneously.

---

## Getting Started

### Prerequisites

* A computer capable of running the provided VortexBlade executable.
* **For NeuralFoil:** A compatible Python environment configured with MATLAB. The solver will attempt to install the required dependencies automatically. The `run_neuralfoil.py` script must be in the same folder as the executable.
* **For XFOIL:** There is no prerequsites for XFOIL. XFOIL wil lbe downloaded to the root folder automatically during analysis.

### Installation & Running

At this time, VortexBlade is being distributed as a standalone executable.

1.  **Download:** Obtain the application package.
2.  **Unzip:** Extract the contents to a folder on your computer.
3.  **Run:** Execute the `VortexBlade.exe` file.

---

## How to Use

1.  **Load a Propeller:** Click the **"Load Propeller..."** button to select a propeller package folder. Use the "Visualize Propeller" button to inspect its 3D geometry.
2.  **Select Analysis Method:** Choose between 'XFOIL' or 'NeuralFoil'. If using pre-loaded XFOIL polars, check the "Use Pre-Loaded Polars" box.
3.  **Set Flight Conditions:** Input the velocity, angle of incidence, altitude, and RPM.
4.  **Configure Wake Model:** Adjust parameters like the number of wake revolutions and the azimuthal step size.
5.  **Run Analysis:** Click the **"Run Analysis"** button.
6.  **Pause & Save:** You can pause the simulation at any time. When paused, the "Save Data" button is enabled, allowing you to save the current state.
7.  **Create Animation:** After a run is complete, use the "Create Wake Animation" button to generate a video or GIF from a saved `.mat` file.

---

## Adding New Propellers

VortexBlade is designed for flexibility. To analyze your own propeller, create a new folder inside the `Propeller Packages` directory. This folder must contain:

1.  **`Prop_sections.xlsx`:** An Excel file defining the blade geometry. The solver reads the file according to the following structure:
    * **Row 2 (Orange):** Non-dimensional span location for each section (`r/R`).
    * **Row 3 (Orange):** Chord length (`c`) in meters for each section.
    * **Row 4 (Orange):** Twist angle (`β`) in degrees for each section.
    * **Row 5 (Yellow):** The name of the corresponding airfoil `.dat` file (without the extension).
    * **Row 8, Col B (Orange):** The cuff/hub radius in meters.

2.  **`foils` (folder):** A sub-folder containing the airfoil `.dat` coordinate files for each section used in the propeller design.

### Required Folder Structure for propellers:

Propeller Packages/
└── Your_Propeller_Name/
├── Prop_sections.xlsx
└── foils/
├── airfoil1.dat
├── airfoil2.dat
└── ...
