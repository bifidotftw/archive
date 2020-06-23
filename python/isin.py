# Compares items in df with list

# Print rows that contain an item in list in $COLUMN
df[df['$COLUMN'].isin(list)]


# Print rows that do NOT contain an item in list in $COLUMN
df[~df['$COLUMN'].isin(list)]
