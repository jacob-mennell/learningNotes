import polars as pl
import duckdb
import time

# Generate dummy data
data = {
    'ID': range(1, 1000001),
    'Value': [i * 2 for i in range(1, 1000001)]
}
df = pl.DataFrame(data)

# Transformation using polars (lazy evaluation)
start_time_polars_lazy = time.time()
df_lazy = df.lazy()
df_lazy = df_lazy.with_column(pl.col("Value").alias("Value_Squared"), pl.col("Value") ** 2)
end_time_polars_lazy = time.time()

# Transformation using polars (eager evaluation)
start_time_polars_eager = time.time()
df_eager = df.with_column(pl.col("Value").alias("Value_Squared"), pl.col("Value") ** 2)
end_time_polars_eager = time.time()

# Transformation using duckdb
con = duckdb.connect()
con.register('df', df.to_pandas())
start_time_duckdb = time.time()
con.execute('SELECT ID, Value, Value * Value AS Value_Squared FROM df')
end_time_duckdb = time.time()

# Calculate time taken for transformations
time_taken_polars_lazy = end_time_polars_lazy - start_time_polars_lazy
time_taken_polars_eager = end_time_polars_eager - start_time_polars_eager
time_taken_duckdb = end_time_duckdb - start_time_duckdb

# Print the time taken for transformations
print(f"Time taken for lazy evaluation using polars: {time_taken_polars_lazy} seconds")
print(f"Time taken for eager evaluation using polars: {time_taken_polars_eager} seconds")
print(f"Time taken for transformation using duckdb: {time_taken_duckdb} seconds")
