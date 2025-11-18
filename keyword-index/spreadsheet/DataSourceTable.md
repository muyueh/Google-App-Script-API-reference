## DataSourceTable

### Methods

- addColumns(columnNames) — DataSourceTable
- addFilter(columnName, filterCriteria) — DataSourceTable
- addSortSpec(columnName, ascending) — DataSourceTable
- addSortSpec(columnName, sortOrder) — DataSourceTable
- cancelDataRefresh() — DataSourceTable
- forceRefreshData() — DataSourceTable
- getColumns() — DataSourceTableColumn[]
- getDataSource() — DataSource
- getFilters() — DataSourceTableFilter[]
- getRange() — Range
- getRowLimit() — Integer
- getSortSpecs() — SortSpec[]
- getStatus() — DataExecutionStatus
- isSyncingAllColumns() — Boolean
- refreshData() — DataSourceTable
- removeAllColumns() — DataSourceTable
- removeAllSortSpecs() — DataSourceTable
- setRowLimit(rowLimit) — DataSourceTable
- syncAllColumns() — DataSourceTable
- waitForCompletion(timeoutInSeconds) — DataExecutionStatus
