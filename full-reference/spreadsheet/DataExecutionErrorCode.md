## [DataExecutionErrorCode](https://developers.google.com/apps-script/reference/spreadsheet/data-execution-error-code)

### Properties

|                Property                 |  Type  |                                          Description                                           |
|-----------------------------------------|--------|------------------------------------------------------------------------------------------------|
| `DATA_EXECUTION_ERROR_CODE_UNSUPPORTED` | `Enum` | A data execution error code that is not supported in Apps Script.                              |
| `NONE`                                  | `Enum` | The data execution has no error.                                                               |
| `TIME_OUT`                              | `Enum` | The data execution timed out.                                                                  |
| `TOO_MANY_ROWS`                         | `Enum` | The data execution returns more rows than the limit.                                           |
| `TOO_MANY_COLUMNS`                      | `Enum` | The data execution returns more columns than the limit.                                        |
| `TOO_MANY_CELLS`                        | `Enum` | The data execution returns more cells than the limit.                                          |
| `ENGINE`                                | `Enum` | Data execution engine error.                                                                   |
| `PARAMETER_INVALID`                     | `Enum` | Invalid data execution parameter.                                                              |
| `UNSUPPORTED_DATA_TYPE`                 | `Enum` | The data execution returns unsupported data type.                                              |
| `DUPLICATE_COLUMN_NAMES`                | `Enum` | The data execution returns duplicate column names.                                             |
| `INTERRUPTED`                           | `Enum` | The data execution is interrupted.                                                             |
| `OTHER`                                 | `Enum` | Other errors.                                                                                  |
| `TOO_MANY_CHARS_PER_CELL`               | `Enum` | The data execution returns values that exceed the maximum characters allowed in a single cell. |
| `DATA_NOT_FOUND`                        | `Enum` | The database referenced by the data source is not found.                                       |
| `PERMISSION_DENIED`                     | `Enum` | The user does not have access to the database referenced by the data source.                   |
