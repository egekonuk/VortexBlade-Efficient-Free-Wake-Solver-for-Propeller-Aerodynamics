import neuralfoil as nf
import numpy as np
import json

# MODIFIED: Removed the default value for model_size
def get_neuralfoil_aero(dat_file, alpha_deg, reynolds_number, model_size):
    """
    Computes airfoil aerodynamics using NeuralFoil and returns a JSON string.
    """
    try:
        aero = nf.get_aero_from_dat_file(
            dat_file,
            alpha=alpha_deg,
            Re=reynolds_number,
            model_size=model_size,
        )
        # Convert numpy types to native Python types for JSON serialization
        for key, value in aero.items():
            if isinstance(value, np.ndarray):
                aero[key] = value.tolist()
            elif isinstance(value, (np.float32, np.float64, np.int32, np.int64)):
                aero[key] = float(value) # Use standard float
        
        # Return the final dictionary as a JSON formatted string
        return json.dumps(aero)

    except Exception as e:
        # Return error as a JSON string
        return json.dumps({"error": str(e)})