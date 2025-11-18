## [CellImageBuilder](https://developers.google.com/apps-script/reference/spreadsheet/cell-image-builder)

### Properties

|   Property    |                                          Type                                           |                           Description                           |
|---------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| `value``Type` | [ValueType](https://developers.google.com/apps-script/reference/spreadsheet/value-type) | The value type of the cell image, which is `Value``Type.IMAGE`. |

### Methods

|                                                                         Method                                                                         |                                              Return type                                               |                          Brief description                          |
|--------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| [build()](https://developers.google.com/apps-script/reference/spreadsheet/cell-image-builder#build())                                                  | [CellImage](https://developers.google.com/apps-script/reference/spreadsheet/cell-image)                | Creates the image value type needed to add an image to a cell.      |
| [getAltTextDescription()](https://developers.google.com/apps-script/reference/spreadsheet/cell-image-builder#getAltTextDescription())                  | `String`                                                                                               | Returns the alt text description for this image.                    |
| [getAltTextTitle()](https://developers.google.com/apps-script/reference/spreadsheet/cell-image-builder#getAltTextTitle())                              | `String`                                                                                               | Returns the alt text title for this image.                          |
| [getContentUrl()](https://developers.google.com/apps-script/reference/spreadsheet/cell-image-builder#getContentUrl())                                  | `String`                                                                                               | Returns a Google-hosted URL to the image.                           |
| [setAltTextDescription(description)](https://developers.google.com/apps-script/reference/spreadsheet/cell-image-builder#setAltTextDescription(String)) | [CellImage](https://developers.google.com/apps-script/reference/spreadsheet/cell-image)                | Sets the alt-text description for this image.                       |
| [setAltTextTitle(title)](https://developers.google.com/apps-script/reference/spreadsheet/cell-image-builder#setAltTextTitle(String))                   | [CellImage](https://developers.google.com/apps-script/reference/spreadsheet/cell-image)                | Sets the alt text title for this image.                             |
| [setSourceUrl(url)](https://developers.google.com/apps-script/reference/spreadsheet/cell-image-builder#setSourceUrl(String))                           | [CellImageBuilder](https://developers.google.com/apps-script/reference/spreadsheet/cell-image-builder) | Sets the image source URL.                                          |
| [toBuilder()](https://developers.google.com/apps-script/reference/spreadsheet/cell-image-builder#toBuilder())                                          | [CellImageBuilder](https://developers.google.com/apps-script/reference/spreadsheet/cell-image-builder) | Creates a cell image builder based on the current image properties. |
