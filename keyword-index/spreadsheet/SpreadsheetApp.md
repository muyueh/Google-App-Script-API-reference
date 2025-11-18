## SpreadsheetApp

### Properties

- AutoFillSeries — AutoFillSeries
- BandingTheme — BandingTheme
- BooleanCriteria — BooleanCriteria
- BorderStyle — BorderStyle
- ColorType — ColorType
- CopyPasteType — CopyPasteType
- DataExecutionErrorCode — DataExecutionErrorCode
- DataExecutionState — DataExecutionState
- DataSourceParameterType — DataSourceParameterType
- DataSourceRefreshScope — DataSourceRefreshScope
- DataSourceType — DataSourceType
- DataValidationCriteria — DataValidationCriteria
- DateTimeGroupingRuleType — DateTimeGroupingRuleType
- DeveloperMetadataLocationType — DeveloperMetadataLocationType
- DeveloperMetadataVisibility — DeveloperMetadataVisibility
- Dimension — Dimension
- Direction — Direction
- FrequencyType — FrequencyType
- GroupControlTogglePosition — GroupControlTogglePosition
- InterpolationType — InterpolationType
- PivotTableSummarizeFunction — PivotTableSummarizeFunction
- PivotValueDisplayType — PivotValueDisplayType
- ProtectionType — ProtectionType
- RecalculationInterval — RecalculationInterval
- RelativeDate — RelativeDate
- SheetType — SheetType
- SortOrder — SortOrder
- TextDirection — TextDirection
- TextToColumnsDelimiter — TextToColumnsDelimiter
- ThemeColorType — ThemeColorType
- ValueType — ValueType
- WrapStrategy — WrapStrategy

### Methods

- create(name) — Spreadsheet
- create(name, rows, columns) — Spreadsheet
- enableAllDataSourcesExecution() — void
- enableBigQueryExecution() — void
- enableLookerExecution() — void
- flush() — void
- getActive() — Spreadsheet
- getActiveRange() — Range
- getActiveRangeList() — RangeList
- getActiveSheet() — Sheet
- getActiveSpreadsheet() — Spreadsheet
- getCurrentCell() — Range
- getSelection() — Selection
- getUi() — Ui
- newCellImage() — CellImageBuilder
- newColor() — ColorBuilder
- newConditionalFormatRule() — ConditionalFormatRuleBuilder
- newDataSourceSpec() — DataSourceSpecBuilder
- newDataValidation() — DataValidationBuilder
- newFilterCriteria() — FilterCriteriaBuilder
- newRichTextValue() — RichTextValueBuilder
- newTextStyle() — TextStyleBuilder
- open(file) — Spreadsheet
- openById(id) — Spreadsheet
- openByUrl(url) — Spreadsheet
- setActiveRange(range) — Range
- setActiveRangeList(rangeList) — RangeList
- setActiveSheet(sheet) — Sheet
- setActiveSheet(sheet, restoreSelection) — Sheet
- setActiveSpreadsheet(newActiveSpreadsheet) — void
- setCurrentCell(cell) — Range
