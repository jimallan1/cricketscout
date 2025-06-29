def get_filter_options(batting, bowling):
    # Collect all unique values for advanced filters
    options = {
        "player": sorted(list(set(batting['player']).union(bowling['player']))),
        "team": sorted(list(set(batting['team']).union(bowling['team']))),
        "opposition": sorted(list(set(batting['opposition']).union(bowling['opposition']))),
        "venue": sorted(list(set(batting['venue']).union(bowling['venue']))),
        "year": sorted(list(set(batting['year']).union(bowling['year']))),
        # Add more as needed
    }
    return options

def apply_filters(df, filters):
    df_filtered = df.copy()
    for key, values in filters.items():
        if key in df.columns and values:
            df_filtered = df_filtered[df_filtered[key].isin(values)]
    return df_filtered