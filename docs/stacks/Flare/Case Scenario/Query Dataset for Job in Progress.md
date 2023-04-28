# **Query Dataset for Job in Progress**

This case scenario describes that Read & Write operations work in isolation for Iceberg formats, not affecting the live table. So when you run a Flare job to write data in Iceberg format, the dataset is available for query while data is being written. Using the snapshot pattern, it will perform a metadata swap only when the Write operation is complete. The use of snapshots also enables time-travel operations as you can perform query operations on different versions of the table by specifying the snapshot to use.

# **Implementation Details**

While a Flare job is running for writing in Icebase, we can run the query with the previous snapshot- metadata location set before the job run. If we update the snapshot ID during a job run, it picks data from that snapshot.

The code snippet will be the same as [Concurrent Writes](Concurrent%20Writes.md).

# **Outcomes**

This scenario was tested by querying the data while a parallel write operation was in progress. Data from the previous snapshot was available to query.