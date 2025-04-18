# User Roles and Management

Users must be logged in to the workspace with a Juicebox user account. User permissions (i.e., what users can do once logged in) depends on the user role.  There are four user roles: viewer, editor, admin, and owner.&#x20;

## User Roles

Here's an overview of what each role can do.&#x20;

<table><thead><tr><th width="206">Action</th><th width="150" align="center">Viewer</th><th width="150" align="center">Editor </th><th width="150" align="center">Admin </th><th align="center">Owner</th></tr></thead><tbody><tr><td>Action</td><td align="center">Viewer</td><td align="center">Editor </td><td align="center">Admin </td><td align="center">Owner</td></tr><tr><td>View specific reports that they've been invited to</td><td align="center">✔️</td><td align="center">N/A</td><td align="center">N/A</td><td align="center">N/A</td></tr><tr><td>Invite viewers to specific reports</td><td align="center"></td><td align="center">✔️</td><td align="center">✔️</td><td align="center">✔️</td></tr><tr><td>View all reports</td><td align="center"></td><td align="center">✔️</td><td align="center">✔️</td><td align="center">✔️</td></tr><tr><td>Edit all reports</td><td align="center"></td><td align="center">✔️</td><td align="center">✔️</td><td align="center">✔️</td></tr><tr><td>Create new reports</td><td align="center"></td><td align="center">✔️</td><td align="center">✔️</td><td align="center">✔️</td></tr><tr><td>Manage users</td><td align="center"></td><td align="center"></td><td align="center">✔️</td><td align="center">✔️</td></tr><tr><td>Manage workspace settings</td><td align="center"></td><td align="center"></td><td align="center">✔️</td><td align="center">✔️</td></tr><tr><td><p>Change subscription</p><p>and payment info </p></td><td align="center"></td><td align="center"></td><td align="center"></td><td align="center">✔️</td></tr></tbody></table>

### Viewer

**Viewers** can view the reports they've been given access to through an access link. They cannot see reports they have not been given access to and they cannot create new reports or edit reports.&#x20;

### Editor

**Editors** can view all reports, edit all reports, and create new reports.&#x20;

### Admin

**Admins** can view all reports, edit all reports, create new reports, and manage user roles and report access in the [People page](user-management-and-roles.md#managing-users).

### Owner

Each workspace has at least one **owner**. Owners can do everything admins can do. In addition, owners can adjust workspace settings and subscription and payment information.

## Managing Users

Workspace owners and admins can manage users through the People page. At the top of the workspace home page, owners and admins will see a **People** button.&#x20;

<figure><img src="../.gitbook/assets/image (20).png" alt=""><figcaption><p>The People button will display on the home page if you are an owner or admin</p></figcaption></figure>

Clicking the **People** button will open the People page.&#x20;

<figure><img src="../.gitbook/assets/image (21).png" alt=""><figcaption><p>The People page</p></figcaption></figure>

The People page lists each workspace user as well as the number of reports the user has access to, the user's role, when the user last logged in, and when the user first signed up. You can search for users using the search bar at the top of the People page. You can sort the values in a column by clicking the column header.

### Changing a user's role

To change a user's role, click on the user's name in the list of users. A modal will open where you can select a different role for the user from a dropdown.&#x20;

<figure><img src="../.gitbook/assets/image (23).png" alt=""><figcaption><p>Modify the user's role</p></figcaption></figure>

{% hint style="info" %}
There must be at least one workspace owner. If a user is the only owner for the workspace, the user's role cannot be changed.&#x20;
{% endhint %}

### Changing a viewer's reports

While owners, admins, and editors can access all reports in a workspace, viewers can only view the reports they have been given access to. To modify a viewer's reports, click on the viewer's name from the list of users. A modal will open where you can modify the viewers report access. &#x20;

<figure><img src="../.gitbook/assets/image (22).png" alt=""><figcaption><p>Modify the viewer's report access</p></figcaption></figure>

To give the viewer access to all reports in the workspace, select **All Reports**. To give the user access to specific reports in the workspace, select **Customized** and then tick the boxes for each report the viewer should have access to.&#x20;

### Changing a user's data permissions

To limit the data that a user can see, you can set data permissions. By default, data permissions are set to `{}`, which gives the user access to all records. If a permissions object is added for the user, then the data will be filtered to show only the permitted records. For example, the permissions object below will only display records `where customer_id = "30005"`. Information about setting up data permissions can be found [here](limiting-what-data-users-can-see.md).&#x20;

<figure><img src="../.gitbook/assets/image (24).png" alt=""><figcaption><p>This user can only see records where customer_id = "30005"</p></figcaption></figure>

### Deleting a user

To delete a user, hover over the user you wish to delete and select the trash can icon (<img src="../.gitbook/assets/trash-alt-regular (1).svg" alt="" data-size="line">).&#x20;

<figure><img src="../.gitbook/assets/image (25).png" alt=""><figcaption><p>Click the trash can icon to delete the user</p></figcaption></figure>
