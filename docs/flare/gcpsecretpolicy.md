# GCP Service Account Permissions

## Overview

This use case describes the strategy for getting **Required** permissions from the client on the  Google service account to access the data from their cloud storage. This service account will enable data processing Flare job to access data from the client's Google cloud storage account.  

## Solution approach

A service account is a special type of Google account that can be authorized to access data in Cloud Storage. This service account is created and configured during the install process of DataOS on Google cloud. Please note that this service account is a resource with IAM policies attached to it, and these policies determine who can use the service account.

We create a Depot definition providing credentials of this service account to enable data access. Flare workflow that will run the data processing job will use this Depot to access data from the cloud storage.

In the case of GCP cloud, while creating a Depot, we can not configure credentials per bucket as access to GCP services is enabled on a per-project/account basis. So, when we need to read data from the client's storage(bigquery, big table/storage location), we need to ask for **Read** permissions on this service account, allowing it to access a client's data resources.   In this case, the service account is the identity that is granted permissions for another resource (client's Cloud Storage bucket).

Depending on the data processing job, we need to have all the required permissions on the service account to access the data from the client's storage, such as:

- BigQuery Data Viewer

- BigQuery Job User

- BigQuery Metadata Viewer

- BigQuery Read Session User

- Storage Admin (For Read & Write access)

- Storage Object Viewer

