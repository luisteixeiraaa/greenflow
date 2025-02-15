# Key functions for data processing and analysis that are used in the API endpoints.

def top_consumers(df, resource, top_n=5, order="desc"):
    """Returns the top N companies consuming the most of a given resource."""
    if order == "asc":
        return df.groupby("empresa")[resource].sum().nsmallest(int(top_n)).round(2).to_dict()
    else:
        return df.groupby("empresa")[resource].sum().nlargest(int(top_n)).round(2).to_dict()

def least_consumers(df, resource, top_n=5):
    """Returns the lowest N companies consuming the most of a given resource."""
    return df.groupby("empresa")[resource].sum().nlowest(int(top_n)).round(2).to_dict()

def sector_comparison(df, resource):
    """Aggregates resource consumption by sector."""
    return df.groupby("setor")[resource].mean().round(2).to_dict()

def company_info(df, id):
    """Selects the records available for a specific company."""
    return df[df["empresa"] == f"Empresa_{id}"].round(2).to_dict()