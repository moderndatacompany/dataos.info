# Query Dataset for Job in Progress

## Overview

This use case describes that **Read & Write** operations work in isolation for Iceberg formats, not affecting the live table. So when you run a Flare job to write data in Iceberg format, the dataset is available for query while data is being written. Using the snapshot pattern, it will perform a metadata swap only when the Write operation is complete. The use of snapshots also enables time-travel operations as you can perform query operations on different versions of the table by specifying the snapshot to use.

## Implementation Details

While a Flare job is running for writing in Iceberg, we can run the query with the previous snapshot- metadata location set before the job run. If we update the snapshot id during a job run, it picks data from that snapshot.

Same as done in [Concurrent writes and parallel processing use case](concurrent.md).

## Outcomes

This scenario was tested by querying the data while parallel write operation was in progress. Data from the previous snapshot was available to query. 

## Code files

Refer code file in [Concurrent writes and parallel processing use case](concurrent.md).