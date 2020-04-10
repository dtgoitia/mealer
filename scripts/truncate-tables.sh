# pqsl options:
# -t only tuple
# -A output not unaligned
# -q quiet
# Source: https://stackoverflow.com/questions/28451598/how-to-return-a-value-from-psql-to-bash-and-use-it

table_indexes="ingredients|recipes"

sql_get_table_names="\
SELECT table_name \
FROM information_schema.tables \
WHERE table_name SIMILAR TO '%(${table_indexes})%' \
    AND table_schema NOT IN ('information_schema', 'pg_catalog') \
    AND table_type = 'BASE TABLE'\
ORDER BY table_name, table_schema;\
"
table_names=$(echo $sql_get_table_names | psql -U postgres -d ${POSTGRES_DB} -tA)

# Store default delimiter to restore it later
default_ifs=$IFS
IFS=$'\n' # set new line as delimiter
read -rd '' -ra ADDR <<< "$table_names" # read table_names into an array as tokens separated by IFS

# Build SQL query to truncate all the tables in table_names
sql_truncate_tables=""
for i in "${ADDR[@]}"; do # access each element of array
    sql_truncate_tables+="TRUNCATE TABLE \"$i\" CASCADE;"
done

# Truncate tables
echo $sql_truncate_tables | psql -U postgres -d ${POSTGRES_DB} -tAq

# IFS=' ' # reset to default value after usage
IFS=$default_ifs # reset to default value after usage