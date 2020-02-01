
dir="data/poultry1"
amp_file="csv_amp_names.txt"
water_file="csv_water_names.txt"

> $amp_file
> $water_file

for csv in "$dir"/*
do
	if [[ $csv == *"amp"* ]]; then
		echo "$csv" >> $amp_file
	elif [[ $csv == *"water"* ]]; then
			echo "$csv" >> $water_file
	fi
done

