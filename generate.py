#!/bin/env python3

"""Generate a set of typical bins"""

from subprocess import run

# length x width x height / divisions
wanted=[ 
    "1x1x6/1",
    "1x1x9/1", # allen keys
    "2x1x2/1",
    "2x1x2/5",
    "2x1x3/5",
    "2x1x6/3",
    "2x2x3/4",
    "2x2x6/1",
    "2x4x3/4",
    "3x1x6/5",
    "3x2x6/1",
    "4x1x6/1",
    "4x2x3/4",
    "4x2x6/1",
    "5x1x7/1", # pencils
    ]

file_extension = "3mf" # I usually set this to 3mf or stl

extra_args=""
for i in wanted:
    size, chambers = i.split("/")
    length, width, height = size.split("x")
    shortlabel="true"
    if int(chambers) > 1:
        shortlabel="false"
    filename = f"Renders/bin-{length}x{width}x{height}-{chambers}divs.{file_extension}"
    if "stl" in file_extension:
        extra_args = "--export-format binstl"
    run(f"openscad gridfinity_basic_cup.scad -D length={length} -D width={width} -D height={height} -D numbchambers={chambers} -D fingerslide=true -D withLabel=true -D shortLabel={shortlabel} -o {filename} {extra_args}", shell=True)
    if "stl" in file_extension:
        run(f"python canonicalize.py {filename}", shell=True)

