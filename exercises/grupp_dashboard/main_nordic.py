import taipy.gui.builder as tgb
from taipy.gui import Gui
import pandas as pd
import plotly.express as px
from utils.constants import DATA_DIRECTORY

# -----------------------------------------------------------------------
# -----------------------------------------------------------------------

# Load into DataFrame
df = pd.read_csv(DATA_DIRECTORY / "nordic_company_rankings.csv")

# Split Rank into Main Rank and Sub Rank
df['Rank in Scandinavia'] = df['Rank'].str.extract(r'(\d+)').astype(int)
df['Rank in Forbes 2000'] = df['Rank'].str.extract(r'\((\d+)\)').astype(int)

# Split Headquarters into City and Country
df[['City', 'Country']] = df['Headquarters'].str.split(',', n=1, expand=True)
df['City'] = df['City'].str.strip()
df['Country'] = df['Country'].str.strip()

# Clean 'Market value (billion $)' column:
# Keep only the numeric part before any '['
df['Market value (billion $)'] = df['Market value (billion $)'].str.extract(r'([\d.]+)').astype(float)

# Create a new DataFrame, dropping 'Headquarters' and 'Rank'
df_new = df.drop(columns=['Headquarters', 'Rank'])

# Rename columns
df_new.rename(columns={'City': 'City Headquarters', 'Country': 'Country Headquarters'}, inplace=True)

# -----------------------------------------------------------------------
# -----------------------------------------------------------------------

# sort per financial metric

def select_from_df(df, type_of_industry = "Banking", financial_metric = "Profits (billion $)"):
    # Select relevant columns
    df_selected = df.query("Industry == @type_of_industry")[["Company", financial_metric]]

    # Sort by financial metric in descending order
    df_selected = df_selected.sort_values(by=financial_metric, ascending=False).reset_index(drop=True)

    return df_selected



def filter_data(state):
    #try:
    # Get full sorted df for max limit
    full_df = select_from_df(df = state.df_new, type_of_industry = state.selected_industry, financial_metric = state.selected_metric)
    state.max_companies = len(full_df)
    print(f"State max companies = {state.max_companies}")
    # Apply filtering by number of companies
    df_filtered = full_df.head(state.number_companies)

    state.bar_chart = px.bar(
        df_filtered,
        x=state.selected_metric,
        y="Company",
        title=f"{state.selected_metric.capitalize()} for companies in {state.selected_industry} industry",
    )
    
    #except Exception as e:
    #    print(f"Error updating chart: {e}")
    #    state.bar_chart = None

selected_metric = "Profits (billion $)"
selected_industry = "Banking"

number_companies = 1  # Starting value 
#min_companies = 1 # Temporary value, will be updated dynamically
#max_companies = len(select_from_df(df_new, selected_industry, selected_metric)) 

#try:
df_filtered = select_from_df(df_new, selected_industry, selected_metric)
max_companies = len(df_filtered)
bar_chart = px.bar(
    df_filtered,
    x=selected_metric,
    y="Company",
    title=f"{selected_metric.capitalize()} for companies in {selected_industry} industry",
)
#except Exception as e:
#    print(f"Error creating initial chart: {e}")
#    bar_chart = None


# --------------------------------------------------------------
# --------------------------------------------------------------

with tgb.Page() as page:
    with tgb.part(class_name="container card"):
        tgb.text("# List of largest Nordic companies", mode="md")

        with tgb.layout(columns="2 1"):
            with tgb.part(class_name="card"):
                #tgb.text("Graph")
                tgb.chart(figure="{bar_chart}")

            with tgb.part(class_name="card"):
                tgb.text("## Filtrer data", mode="md")
                tgb.text("Select type of industry", mode="md")
                tgb.selector(
                    "{selected_industry}",
                    lov = df_new["Industry"].unique(),
                    dropdown = True,
                    continuous=False,
                )

                tgb.text("Select financial metric", mode="md")
                tgb.selector(
                    "{selected_metric}",
                    lov = [
                        "Revenue (billion $)",
                        "Profits (billion $)", 
                        "Assets (billion $)",
                        "Market value (billion $)"],
                    dropdown = True,
                    continuous=False,
                )

                tgb.slider(
                    value="{number_companies}",
                    min=1,
                    max="{max_companies}",
                    continuous=False,
                )

                
                tgb.button("FILTRER DATA", class_name="plain", on_action=filter_data)

        with tgb.part(class_name="card"):
            tgb.text("Raw data")
            tgb.table("{df_new}")


# --------------------------------------------------------------
# --------------------------------------------------------------

if __name__ == "__main__":
    Gui(page).run(dark_mode=False, use_reloader=False, port=8080)
