import argparse
import os

"""
Example usage:
infile="out.bin"
outfile="out_trim.bin"
start_seconds=10
end_seconds=12
samp_rate=96000
# for complex 32-bit, sample size is 4 * 2 = 8
# for others - look at https://wiki.gnuradio.org/index.php/File_Sink
samp_size=8

python3 trim.py -i $infile -o $outfile -t0 $start_seconds -t1 $end_seconds -sr $sample_rate -ss $sample_size
"""


def main():
    # add args
    parser = argparse.ArgumentParser(description="trim binary collections to just the signal")
    parser.add_argument("-i", "--infile", type=str, help="The name of the file to process.")
    parser.add_argument("-o", "--outfile", type=str, help="The name of the trimmed file to write.")
    parser.add_argument("-t0", "--starttime", type=float,help="time(s) where signal starts")
    parser.add_argument("-t1", "--endtime", type=float, help="time(s) where signal stops")
    parser.add_argument("-sr", "--sample_rate", type=int, default=96000, help="sample rate for collection")
    parser.add_argument("-ss", "--sample_size", type=int, default=4, help="size of sample, in bytes")
    

    # parse the arguments
    args = parser.parse_args()
    infile = os.path.abspath(args.infile)
    outfile = os.path.abspath(args.outfile)
    endtime = args.endtime
    starttime = args.starttime
    sample_rate = args.sample_rate
    sample_size = args.sample_size
    print(f"collection {infile}, start {starttime} s, end {endtime} s")
    print(f"Sample Rate {sample_rate} kHz, Size of a sample: {sample_size} bytes")

    # some math
    len_seconds = endtime - starttime
    skip = int(starttime * sample_rate * sample_size)
    count = int(len_seconds * sample_rate * sample_size)

    # do it
    print(f"writing file {outfile}")
    with open(outfile, 'wb') as fo:
        with open(infile, 'rb') as fi:
            fi.seek(skip, 0)
            fo.write(fi.read(count))


if __name__ == "__main__":
    print("Collection Trimmer Starting")
    main()
    print("Done!")
