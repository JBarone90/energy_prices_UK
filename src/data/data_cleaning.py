import pandas as pd


def clean_cpih(file_path):
    """
    Preprocesses the Consumer Price Index including owner occupiers' housing costs (CPIH) data.

    Parameters:
        file_path (str): Path to the Excel file containing the CPIH data.

    Returns:
        pd.DataFrame: A cleaned and processed DataFrame suitable for analysis.
    """
    cpih_data = pd.read_excel(file_path, sheet_name=0, skiprows=2, engine="openpyxl")
    date_columns = cpih_data.columns[3:].tolist()
    cpih_data = cpih_data[["Aggregate"] + date_columns]

    categories_to_include = [
        "Overall Index",
        "Gas",
        "Electricity",
        "Liquid fuels",
        "Transport",
    ]
    category_mask = cpih_data["Aggregate"].str.contains("|".join(categories_to_include))
    transport_mask = cpih_data["Aggregate"].str.contains("07")
    cpih_data = cpih_data[category_mask | transport_mask].reset_index(drop=True)

    reshaped_cpih = cpih_data.melt(
        id_vars=["Aggregate"], var_name="Date", value_name="Value"
    ).pivot(index="Date", columns="Aggregate", values="Value")

    similar_columns_mapping = [
        (("07.1.1 New Cars", "07.1.1.1 New motor cars"), "07.1.1 New motor cars"),
        (
            ("07.1.1.2 Second-hand motor cars", "07.1.1b Second Hand Cars"),
            "07.1.2 Second-hand motor cars",
        ),
        (
            ("07.1.2/3 Motocycles and bicycles", "07.1.2/3 Motorcycles and bicycles"),
            "07.1.3 Motorcycles and bicycles",
        ),
    ]

    for old_columns, new_column in similar_columns_mapping:
        reshaped_cpih[new_column] = reshaped_cpih[list(old_columns)].sum(axis=1)
        reshaped_cpih.drop(list(old_columns), axis=1, inplace=True)

    reshaped_cpih.index = pd.to_datetime(reshaped_cpih.index, format="%b-%y")
    reshaped_cpih.sort_index(inplace=True)
    reshaped_cpih = reshaped_cpih[reshaped_cpih.index.year >= 2010]

    return reshaped_cpih


def clean_passenger_journeys_by_ticket_type(file_path):
    """
    Preprocesses the "Passenger journeys by ticket type" table (Table 1222b)
    from Table 1222: Passenger journeys by ticket type, Great Britain, April 1986 to March 2023.

    Parameters:
        file_path (str): The path to the ODS file containing the data.

    Returns:
        pd.DataFrame: A cleaned DataFrame containing the data from Table 1222b.
    """

    def is_table_row(row):
        """Identify if a row contains 'Table 1222b'."""
        return row.astype(str).str.contains("Table 1222b").any()

    sheet_data = pd.read_excel(file_path, sheet_name=2, header=None)
    start_row_index = sheet_data[sheet_data.apply(is_table_row, axis=1)].index[0]
    data_start_row_index = start_row_index + 2

    passenger_data = pd.read_excel(
        file_path, sheet_name=2, header=None, skiprows=range(0, data_start_row_index)
    )

    column_names = [
        "Date",
        "Ordinary Advance",
        "Ordinary Anytime or Peak",
        "Ordinary Off Peak",
        "Ordinary Other",
        "Ordinary Total",
        "Season",
        "Open access",
        "Total",
    ]
    passenger_data.columns = column_names

    date_data = passenger_data["Date"].str.extract(r"(\w{3}) to (\w{3}) (\d{4})")
    passenger_data["Date"] = pd.to_datetime(
        date_data[2] + "-" + date_data[0].str[:3] + "-01"
    )

    passenger_data.set_index("Date", inplace=True)
    passenger_data = passenger_data[passenger_data.index >= "2010-01-01"]
    passenger_data = passenger_data.replace(["[x]", "[z]"], [None, None]).dropna()

    return passenger_data
