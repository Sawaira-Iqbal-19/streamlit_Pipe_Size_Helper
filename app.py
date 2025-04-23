import streamlit as st
import math

def calculate_diameter(flow_rate, velocity):
    """
    Calculate the internal diameter of a pipe based on flow rate and velocity.
    Parameters:
    - flow_rate (float): Volumetric flow rate in cubic meters per second (m³/s).
    - velocity (float): Flow velocity in meters per second (m/s).
    Returns:
    - float: Internal diameter in meters.
    """
    if flow_rate <= 0 or velocity <= 0:
        return None
    area = flow_rate / velocity
    diameter = math.sqrt((4 * area) / math.pi)
    return diameter

def main():
    st.title("🛠️ Pipe Size Helper")
    st.write("Calculate the required pipe diameter based on flow rate and velocity.")

    # Input fields
    flow_rate = st.number_input("Enter the flow rate (m³/s):", min_value=0.0, format="%.6f")
    velocity = st.number_input("Enter the velocity (m/s):", min_value=0.0, format="%.6f")

    if st.button("Calculate Diameter"):
        diameter = calculate_diameter(flow_rate, velocity)
        if diameter:
            st.success(f"Required Internal Pipe Diameter: {diameter:.4f} meters")
            st.info(f"Equivalent to {diameter * 1000:.2f} millimeters")
        else:
            st.error("Please enter positive values for flow rate and velocity.")

if __name__ == "__main__":
    main()
