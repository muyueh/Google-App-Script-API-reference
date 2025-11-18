# Drive Service

Drive

This service lets scripts create, find, and modify files and folders in
Google Drive. Although the built-in Drive service is easier to use, it has some limitations.
For the most
up-to-date features and support, and to access files or folders in shared drives, use the
[advanced Drive service](https://developers.google.com/apps-script/advanced/drive).

If your script uses a
[standard Cloud project](https://developers.google.com/apps-script/guides/cloud-platform-projects#standard)
instead of a default Cloud project, you must
manually turn on the Drive API. In your standard Cloud project, turn on the Drive API:

[Turn on the Drive API](https://console.cloud.google.com/apis/enableflow?apiid=drive.googleapis.com)
The following code sample shows how to log the names of each file in the user's My Drive folder:  

    // Logs the name of every file in the user's Drive.
    var files = DriveApp.getFiles();
    while (files.hasNext()) {
      var file = files.next();
      console.log(file.getName());
    }

| **Note:** Google Workspace Administrators
| can turn off the [Drive SDK](https://developers.google.com/drive)
| for their domain, which prevents their users from installing and using Google
| Drive apps. This setting also prevents users from using
| Apps Script scripts, web apps and add-ons that use the [Drive
| service](https://developers.google.com/apps-script/reference/drive) or [Advanced Drive Service](https://developers.google.com/apps-script/advanced/drive)
| (even if the add-on or web app was installed before the admin turned off the
| [Drive SDK](https://developers.google.com/drive)).
|
| However, if an add-on using the Drive service is published for domain-wide installation
| and is installed by the administrator for some or all users in the domain, or any script that
| has its [OAuth client allowlisted](https://support.google.com/a/answer/162106)
| by the domain administrator, the add-on functions for those users even if the
| [Drive SDK](https://developers.google.com/drive) is turned off in the domain.

## Classes

|                                            Name                                             |                                                                     Brief description                                                                      |
|---------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Access](https://developers.google.com/apps-script/reference/drive/access)                  | An enum representing classes of users who can access a file or folder, besides any individual users who have been explicitly given access.                 |
| [DriveApp](https://developers.google.com/apps-script/reference/drive/drive-app)             | Allows scripts to create, find, and modify files and folders in Google Drive.                                                                              |
| [File](https://developers.google.com/apps-script/reference/drive/file)                      | A file in Google Drive.                                                                                                                                    |
| [FileIterator](https://developers.google.com/apps-script/reference/drive/file-iterator)     | An iterator that allows scripts to iterate over a potentially large collection of files.                                                                   |
| [Folder](https://developers.google.com/apps-script/reference/drive/folder)                  | A folder in Google Drive.                                                                                                                                  |
| [FolderIterator](https://developers.google.com/apps-script/reference/drive/folder-iterator) | An object that allows scripts to iterate over a potentially large collection of folders.                                                                   |
| [Permission](https://developers.google.com/apps-script/reference/drive/permission)          | An enum representing the permissions granted to users who can access a file or folder, besides any individual users who have been explicitly given access. |
| [User](https://developers.google.com/apps-script/reference/drive/user)                      | A user associated with a file in Google Drive.                                                                                                             |
