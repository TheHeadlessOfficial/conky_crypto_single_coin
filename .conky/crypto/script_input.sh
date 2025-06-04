#!/bin/bash

path_default="/home/hiro/.conky/crypto"

# Ask user to enter limit price UP
echo "Type limit UP price (with 2 decimals, using the point (.) example: 20570.51):"
read inputup

# Ask user to enter DOWN limit price
echo "Type limit DOWN price (with 2 decimals, using the point (.) example: 20570.51):"
read inputdown

# Save the data to a file, for example "data.txt"
data_path="$path_default/usertargets.txt"
echo "$inputup" > "$data_path"
echo "$inputdown" >> "$data_path"

# Create a flag file indicating that the data has been saved
flag_path="$path_default/_conky_user_data.flag"
echo "OK" > "$flag_path"

# Once the data has been saved and the flag file created, close the script
echo "Data saved successfully."

#echo "done" > /tmp/input_ready

exit 0
