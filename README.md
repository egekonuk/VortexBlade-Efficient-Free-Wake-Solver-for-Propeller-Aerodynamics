# VortexBlade: A Mid-Fidelity Free-Wake Solver for Propeller Aerodynamics

<p align="center">
<img width="512" height="512" alt="VortexBlade Logo" src="https://github.com/user-attachments/assets/77bc0471-584e-447a-8ddc-cbee6d75a04d" />
</p>

**VortexBlade is an advanced aerodynamic analysis tool that implements a three-dimensional, unsteady free-wake vortex method and combines with the intrinsic loads from BEM Method to deliver Mid-fidelity performance predictions for propellers and rotors. By simulating the full wake development, it overcomes the inherent limitations of standalone BEMT-based approaches, especially in complex flow conditions.**

---

## Core Aerodynamic Theory

VortexBlade is built on a first-principles approach to fluid dynamics. Unlike simplified models that rely on momentum balance, this solver directly simulates the behavior of the wake as it is shed from the propeller blades.

* **Free-Wake Method:** The core of the solver is its "free-wake" methodology. At each time step, vortex filaments representing the vorticity shed from the trailing edge of the blades are introduced into the flow field. These filaments are then convected downstream with the local velocity, which is a sum of the freestream velocity and the velocity induced by all other vortex elements in the wake. This allows the wake to develop its shape freely and realistically, capturing complex phenomena like wake contraction and interaction.

* **Biot-Savart Law:** The velocity induced by each straight-line vortex segment on every other point in the flow field (both on the blades and in the wake) is calculated using the Biot-Savart law. This fundamental law of electromagnetism, applied to fluid dynamics, relates the strength and geometry of a vortex element to the velocity it induces.

* **Vortex Core Growth Model:** To avoid the physical and mathematical singularity at the center of a vortex filament, a viscous core model is implemented. The core radius of each filament evolves at every time step according to a turbulent viscosity model. Critically, the turbulent viscosity coefficient is calculated based on the local strain rate of the filament. This allows the core to grow dynamically in response to physical vortex stretching, realistically diffusing the vorticity over time and ensuring a stable, physical solution.

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

V1.2 Axial Flow
<img width="1780" height="1324" alt="image" src="https://github.com/user-attachments/assets/e6db4046-dfad-4c0f-b475-432378ad5225" />

<img width="2996" height="1874" alt="CleanShot 2025-07-27 at 02 02 13@2x" src="https://github.com/user-attachments/assets/ea51b1a1-17a9-4bca-893b-969c69f5213a" />

### Live Wake Visualization

https://github.com/user-attachments/assets/63215b23-d7e6-47ff-94d0-5ae12465593d

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
* **XFOIL:** The executable (`xfoil.exe` for Windows) is included in the inside the application.
* **Propeller Packages:** Propeller geometries must be placed in the `Propeller Packages` folder, following the structure defined above.

### Installation & Running

At this time, VortexBlade is being distributed as a standalone executable.

1.  **Download:** Obtain the application package.
2.  **Unzip:** Extract the contents to a folder on your computer.
3.  **Run:** Execute the `VortexBlade.exe` file.

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
    * **Row 2 (Orange):** Non-dimensional span location for each section (`x/R`).
    * **Row 3 (Orange):** Chord length (`c`) in meters for each section.
    * **Row 4 (Orange):** Twist angle (`β`) in degrees for each section.
    * **Row 5 (Yellow):** The name of the corresponding airfoil `.dat` file (without the extension).

2.  **`foils` (folder):** A sub-folder containing the airfoil `.dat` coordinate files for each section used in the propeller design.

### Required Folder Structure:

For the solver to correctly load your propeller, your folder inside `Propeller Packages` must look like this:


Propeller Packages/

└── Your_Propeller_Name/

├── Prop_sections.xlsx

└── foils/
├── airfoil1.dat
├── airfoil2.dat
└── ...



