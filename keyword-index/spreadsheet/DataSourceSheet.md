## DataSourceSheet

### Methods

- addFilter(columnName, filterCriteria) — DataSourceSheet
- asSheet() — Sheet
- autoResizeColumn(columnName) — DataSourceSheet
- autoResizeColumns(columnNames) — DataSourceSheet
- cancelDataRefresh() — DataSourceSheet
- forceRefreshData() — DataSourceSheet
- getColumnWidth(columnName) — Integer
- getDataSource() — DataSource
- getFilters() — DataSourceSheetFilter[]
- getSheetValues(columnName) — Object[]
- getSheetValues(columnName, startRow, numRows) — Object[]
- getSortSpecs() — SortSpec[]
- getStatus() — DataExecutionStatus
- refreshData() — DataSourceSheet
- removeFilters(columnName) — DataSourceSheet
- removeSortSpec(columnName) — DataSourceSheet
- setColumnWidth(columnName, width) — DataSourceSheet
- setColumnWidths(columnNames, width) — DataSourceSheet
- setSortSpec(columnName, ascending) — DataSourceSheet
- setSortSpec(columnName, sortOrder) — DataSourceSheet
- waitForCompletion(timeoutInSeconds) — DataExecutionStatus
