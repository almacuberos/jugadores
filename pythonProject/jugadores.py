import streamlit as st
import pandas as pd

# Load and display the logo
logo_path = './imagenes/PineTools.com_Soluc.png'
st.image(logo_path, use_column_width=True)

# Load the CSV file from a local path
csv_file_path = './informacion/jugadores.csv'
df = pd.read_csv(csv_file_path)

# Ensure "Cotización (USD)" column is numeric
df["Cotización (USD)"] = df["Cotización (USD)"].str.replace(',', '')
df["Cotización (USD)"] = pd.to_numeric(df["Cotización (USD)"], errors='coerce')

# Handle non-finite values in "Edad" column and convert to integers
df["Edad"] = pd.to_numeric(df["Edad"], errors='coerce').fillna(0).astype(int)

# Data filtering
st.sidebar.header("Filtros")

# Filter by specific columns
columns_to_filter = st.sidebar.multiselect("Selecciona las columnas que quieras filtrar:", df.columns)

filtered_df = df.copy()

for column in columns_to_filter:
    if column == "Cotización (USD)":
        min_value = 0
        max_value = 18000000
        step_value = 100000
        selected_range = st.sidebar.slider(f"Selecciona el rango para {column}:", min_value, max_value, (min_value, max_value), step=step_value)
        filtered_df = filtered_df[(df[column] >= selected_range[0]) & (df[column] <= selected_range[1])]
    elif column == "Edad":
        min_value = 16
        max_value = 50
        selected_range = st.sidebar.slider(f"Selecciona el rango para {column}:", min_value, max_value, (min_value, max_value))
        filtered_df = filtered_df[(df[column] >= selected_range[0]) & (df[column] <= selected_range[1])]
    else:
        unique_values = df[column].unique()
        selected_values = st.sidebar.multiselect(f"Selecciona el rango para {column}:", unique_values)
        if selected_values:
            filtered_df = filtered_df[filtered_df[column].isin(selected_values)]

# Add description text
st.write("Toca el nombre de la columna para organizar sus datos de mayor a menor.")

# Display the filtered DataFrame with all columns and dynamic height
num_rows = len(filtered_df)
st.dataframe(filtered_df, height=num_rows * 35 + 35)
