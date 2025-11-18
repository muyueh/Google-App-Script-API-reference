## DriveApp

### Properties

- Access — Access
- Permission — Permission

### Methods

- continueFileIterator(continuationToken) — FileIterator
- continueFolderIterator(continuationToken) — FolderIterator
- createFile(blob) — File
- createFile(name, content) — File
- createFile(name, content, mimeType) — File
- createFolder(name) — Folder
- createShortcut(targetId) — File
- createShortcutForTargetIdAndResourceKey(targetId, targetResourceKey) — File
- enforceSingleParent(value) — void
- getFileById(id) — File
- getFileByIdAndResourceKey(id, resourceKey) — File
- getFiles() — FileIterator
- getFilesByName(name) — FileIterator
- getFilesByType(mimeType) — FileIterator
- getFolderById(id) — Folder
- getFolderByIdAndResourceKey(id, resourceKey) — Folder
- getFolders() — FolderIterator
- getFoldersByName(name) — FolderIterator
- getRootFolder() — Folder
- getStorageLimit() — Integer
- getStorageUsed() — Integer
- getTrashedFiles() — FileIterator
- getTrashedFolders() — FolderIterator
- searchFiles(params) — FileIterator
- searchFolders(params) — FolderIterator
