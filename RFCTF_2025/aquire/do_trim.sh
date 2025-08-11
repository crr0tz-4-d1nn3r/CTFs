infile="../POCSAG/pocsog_msg.bin"
outfile="../POCSAG/pocsag_msg_trim.bin"
start_seconds=5
end_seconds=14
sample_rate=96000
sample_size=8

python3 trim.py -i "$infile" -o "$outfile" -t0 "$start_seconds" -t1 "$end_seconds" -sr "$sample_rate" -ss "$sample_size"

