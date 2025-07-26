# VortexBlade: A High-Fidelity Free-Wake Solver for Propeller Aerodynamics

<p align="center">
<img width="512" height="512" alt="VortexBlade Logo" src="https://github.com/user-attachments/assets/77bc0471-584e-447a-8ddc-cbee6d75a04d" />
</p>

**VortexBlade is an advanced aerodynamic analysis tool that implements a three-dimensional, unsteady free-wake vortex method to deliver high-fidelity performance predictions for propellers and rotors. By simulating the full wake development, it overcomes the inherent limitations of traditional BEMT-based approaches, especially in complex flow conditions.**

---

## Core Aerodynamic Theory

VortexBlade is built on a first-principles approach to fluid dynamics. Unlike simplified models that rely on momentum balance, this solver directly simulates the behavior of the wake as it is shed from the propeller blades.

* **Free-Wake Method:** The core of the solver is its "free-wake" methodology. At each time step, vortex filaments representing the vorticity shed from the trailing edge of the blades are introduced into the flow field. These filaments are then convected downstream with the local velocity, which is a sum of the freestream velocity and the velocity induced by all other vortex elements in the wake. This allows the wake to develop its shape freely and realistically, capturing complex phenomena like wake contraction and interaction.

* **Biot-Savart Law:** The velocity induced by each straight-line vortex segment on every other point in the flow field (both on the blades and in the wake) is calculated using the Biot-Savart law. This fundamental law of electromagnetism, applied to fluid dynamics, relates the strength and geometry of a vortex element to the velocity it induces.

* **Vortex Core Growth Model:** To avoid the physical and mathematical singularity at the center of a vortex filament (where induced velocity would be infinite), a vortex core model is implemented. The solver uses a viscous core growth model where each filament is given an initial core radius based on the blade's zero-lift drag. As the vortex filament ages, its core grows based on the effects of turbulent viscosity, realistically diffusing the vorticity over time and ensuring a stable, physical solution.

---

## Key Features

* **High-Fidelity Free-Wake Model:** Accurately simulates the convection and interaction of shed vortex filaments, providing a precise calculation of the non-uniform induced velocity field.
* **Interactive GUI:** A comprehensive and user-friendly interface allows for easy setup of simulation parameters, flight conditions, and wake model settings without touching a line of code.
* **Parallelized Solution:** Leverages MATLAB's `parfor` to significantly accelerate the most demanding parts of the calculation, such as wake convection and induced velocity updates, making high-fidelity analysis faster than ever.
* **Advanced 3D Visualization:** The GUI provides a live, interactive 3D plot showing the fully rendered propeller geometry and the developing wake structure, with filaments colored by vortex strength. An accompanying 2D contour plot shows the induced velocity field for immediate physical insight.
* **Post-Processing & Animation:** Save complete simulation states and use the built-in animation tool to create high-quality videos (`.mp4`) or GIFs (`.gif`) of the full wake evolution from the saved data.
* **Modular Propeller Library:** Easily add, manage, and visualize different propeller geometries through a simple folder structure. Requires a `Prop_sections.xlsx` file and associated airfoil `.dat` files.
* **Integrated XFOIL Workflow:** Includes tools to automatically call XFOIL for generating airfoil polar data or use existing data files.

---

## Analysis Models & Capabilities

* **Extended Airfoil Polars:** To handle high angles of incidence and stalled conditions, the solver incorporates the **Viterna method** to extrapolate airfoil polar data up to **±180°**. This provides a more robust and physically realistic representation of lift and drag well beyond the normal operating range.
* **Solid Hub Obstacle:** The propeller hub or cuff is modeled as a solid cylindrical obstacle. Any vortex filament that drifts inside this volume is pushed to the cylinder's surface, preventing non-physical behavior and more accurately modeling the flow redirection around the hub.

---

## Showcase

### Main Application Interface

The intuitive GUI gives you full control over every aspect of the simulation, from propeller selection and flight conditions (velocity, angle of incidence) to the numerical details of the wake discretization and vortex core model.

<img width="2560" height="1380" alt="image" src="https://github.com/user-attachments/assets/78fb9c1d-7ce0-40a8-b46c-02b4f6378441" />

### Live Wake Visualization

https://github.com/user-attachments/assets/9059d387-2025-40d8-8dd0-6631dacbcbb5

Gain a deep understanding of the propeller's aerodynamic environment by observing the wake structure evolve in real-time. The interface displays the 3D vortex filaments trailing from the blades, the solid propeller geometry, and a 2D slice of the induced velocity field simultaneously.



---

## Future Development

VortexBlade is an actively developed platform. Key features planned for future releases include:

* **Blade-Vortex Interaction (BVI) Model:** Integration of a higher-fidelity panel source code to accurately capture the sharp airload fluctuations caused by close blade-vortex encounters, a critical component for noise prediction.
* **Wake-Motor Interaction Modeling:** The ability to account for the blockage and acceleration effects of nacelles or motor bodies, enabling more accurate comparisons with wind tunnel and real-world test setups.
* **Source Code Release:** While currently distributed as an executable, a fully-documented source code version is planned for a future release to support academic and community development.

---

## Getting Started

### Prerequisites

* A computer capable of running the provided VortexBlade executable.
* **XFOIL:** The executable (`xfoil.exe` for Windows) must be included in the `XFOIL` folder within the application directory.
* **Propeller Packages:** Propeller geometries must be placed in the `Propeller Packages` folder.

### Installation & Running

At this time, VortexBlade is being distributed as a standalone executable.

1.  **Download:** Obtain the application package.
2.  **Unzip:** Extract the contents to a folder on your computer.
3.  **Run:** Execute the `VortexBlade_GUI_FWM.exe` file.

---

## How to Use

1.  **Select a Propeller:** Choose a propeller from the "Propeller" dropdown. Use the "Visualize" button to inspect its 3D geometry.
2.  **Set Flight Conditions:** Input the velocity, angle of incidence, altitude, and RPM.
3.  **Configure Wake Model:** Adjust parameters like the number of wake revolutions and the azimuthal step size to balance fidelity and computational time.
4.  **Run Analysis:** Click the **"Run Analysis"** button. The simulation will begin, and the plots will update live.
5.  **Pause & Save:** You can pause the simulation at any time, which automatically saves the current state. This data can be used later to generate animations.
6.  **Create Animation:** After a run is complete (or paused), run the separate `create_wake_animation` tool to generate a video or GIF from the saved data file.

---

## Adding New Propellers

VortexBlade is designed for flexibility. To analyze your own propeller, create a new folder inside the `Propeller Packages` directory. This folder must contain:

1.  **`Prop_sections.xlsx`:** An Excel file defining the blade geometry. The solver reads the file according to the following structure:
    * **Row 2:** Non-dimensional span location for each section (`x/R`).
    * **Row 3:** Chord length (`c`) in meters for each section.
    * **Row 4:** Twist angle (`β`) in degrees for each section.
    * **Row 5:** The name of the corresponding airfoil `.dat` file (without the extension).

2.  **`foils` (folder):** A sub-folder containing the airfoil `.dat` coordinate files for each section used in the propeller design.

Restart the GUI, and your new propeller will automatically appear in the dropdown menu.
