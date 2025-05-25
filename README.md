# Tabby

A small implementation of pyarrow/pandas to better understand how they work and how they can be optimized.
The goal is to implement a subset of the functionalities and explore performance optimizations such as data oriented design (DOD),
concurrency and parallelism, SIMD, and maybe even CUDA.

## Background

I recently got my first data science job (Yay!) and we operate on LARGE datasets.
Dataframes can approach the 100s of GBs.
At this scale, performance matters a lot.
It quickly became obvious too that how the data is saved in a dataframe matters a lot too.
For example, one extra byte per row over hundreds of millions of rows just became hundreds of megabytes.
Therefore, the type used but also the memory overhead are extremely important.
I wanted to explore how such libraries represent data.
Some of the questions I have is how are millions of rows layed out in memory and how do the frameworks make it easy and efficient to add millions of rows more?
How do common operations like subset selection, filters, joins, concatenations, group by, and drop duplicates work?
How can these common operations be optimized on modern server hardware?

## Goal

In light of this, I want to implement the following operations:

- Reading from a file (I'll use CSVs for simplicity even though it's not the best format)
- Filter based on a boolean condition
- Join (left and inner) based on specified columns
- Concat (Append rows)
- Group by
- Drop duplicates

I'll implement the operations mentionned above in C++ with a Python wrapper.
I'll use Pybind11 for the wrapper because both a Reddit user and DeepSeek said so.
First, I'll implement all the operations in single-threaded, "basic" code.
Then, I'll explore multithreading, SIMD, and perhaps CUDA to see how much more speed⚡🚀💨 I can get.

## Implementation Notes

In Python:

- Dataframe, Schema
- concat, join, read_csv, Dataframe.filter, Dataframe.group_by, Dataframe.drop_duplicates
