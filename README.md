# Dataframe Engine

The goal of this project is to explore how a tabular dataframe library can optimize processing to the fullest.
Lazy evaluation libraries like Apache Spark or Polars typically use a Directed Acyclic Graph (DAG) to determine dependencies between operations and allow pruning of useless operations.
It also allows reordering operations logically.
I want to explore how can such a library plan operations efficiently given:

- CPU resources
- Memory resources
- I/O bound tasks
- CPU bound tasks
- Algorithm requirements

One important topic that I want to explore that I heard much about before is efficiently using I/O.
When dealing with large amounts of data, this is a big bottleneck.
Some optimizations that I think could be interesting to explore are:

- Pre-Fetching Data: Some data used later in a pipeline would be fetched earlier while the CPU is busy doing intensive computations.
- Reorganizing Dodes: In many pipelines that I have seen at my day job, all data extractions are done, then all processing is done. I think there it could potentially be beneficial to reorganize steps (nodes in the DAG) so that I/O does not stall the CPU.
- Database Extractions: In SAS, database tables can be used as a libname and are used just like any other table. This is very cool and useful, so I think a good framework should allow to use a database table in a query containing a dataframe and know automatically what to fetch in the database. It could also use schema information and table statistics to optimize queries.
- Data Distribution: Libraries like Spark will run a distribute the results of a SQL query on multiple executors and each executors will do computations on a subset of the data to speed things up. A performance-focused framework should be able to efficiently allocate data.
- Memory Management: Long chains of operations cause data to be accumulated which slows processing down. This is something that I have experienced professionally with Spark. The optimization engine should know when things are not needed anymore and free things up.
