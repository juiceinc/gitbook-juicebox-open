# User Roles and Management

Users must be logged in to the apps page with a Juicebox user account. What users can do once logged in depends on their user role.  There are four user roles: viewer, editor, admin, and owner. 

## User Roles

Here's an overview of what each role can do. 

<table>
  <thead>
    <tr>
      <th style="text-align:left">Action</th>
      <th style="text-align:left">Viewer</th>
      <th style="text-align:center">Editor</th>
      <th style="text-align:center">Admin</th>
      <th style="text-align:center">Owner</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">View specific apps that they&apos;ve been invited to</td>
      <td style="text-align:left">&#x2714;&#xFE0F;</td>
      <td style="text-align:center">N/A</td>
      <td style="text-align:center">N/A</td>
      <td style="text-align:center">N/A</td>
    </tr>
    <tr>
      <td style="text-align:left">Invite viewers to specific
        <br />apps</td>
      <td style="text-align:left"></td>
      <td style="text-align:center">&#x2714;&#xFE0F;</td>
      <td style="text-align:center">&#x2714;&#xFE0F;</td>
      <td style="text-align:center">&#x2714;&#xFE0F;</td>
    </tr>
    <tr>
      <td style="text-align:left">View all apps</td>
      <td style="text-align:left"></td>
      <td style="text-align:center">&#x2714;&#xFE0F;</td>
      <td style="text-align:center">&#x2714;&#xFE0F;</td>
      <td style="text-align:center">&#x2714;&#xFE0F;</td>
    </tr>
    <tr>
      <td style="text-align:left">Edit all apps</td>
      <td style="text-align:left"></td>
      <td style="text-align:center">&#x2714;&#xFE0F;</td>
      <td style="text-align:center">&#x2714;&#xFE0F;</td>
      <td style="text-align:center">&#x2714;&#xFE0F;</td>
    </tr>
    <tr>
      <td style="text-align:left">Create new apps</td>
      <td style="text-align:left"></td>
      <td style="text-align:center">&#x2714;&#xFE0F;</td>
      <td style="text-align:center">&#x2714;&#xFE0F;</td>
      <td style="text-align:center">&#x2714;&#xFE0F;</td>
    </tr>
    <tr>
      <td style="text-align:left">Manage users</td>
      <td style="text-align:left"></td>
      <td style="text-align:center"></td>
      <td style="text-align:center">&#x2714;&#xFE0F;</td>
      <td style="text-align:center">&#x2714;&#xFE0F;</td>
    </tr>
    <tr>
      <td style="text-align:left">Manage workspace settings &#x1F51C;</td>
      <td style="text-align:left"></td>
      <td style="text-align:center"></td>
      <td style="text-align:center">&#x2714;&#xFE0F;</td>
      <td style="text-align:center">&#x2714;&#xFE0F;</td>
    </tr>
    <tr>
      <td style="text-align:left">
        <p>Change subscription</p>
        <p>and payment info (future release)</p>
      </td>
      <td style="text-align:left"></td>
      <td style="text-align:center"></td>
      <td style="text-align:center"></td>
      <td style="text-align:center">&#x2714;&#xFE0F;</td>
    </tr>
  </tbody>
</table>

### Viewer

**Viewers** can view the apps they've been given access to through an access link. They cannot see apps they have not been given access to and they can not create new apps or edit apps. 

### Editor

**Editors** can view all apps, edit all apps, and create new apps. 

### Admin

**Admins** can view all apps, edit all apps, create new apps, and manage user roles and app access in the [People view](user-management-and-roles.md#managing-users).

### Owner

Each workspace has at least one **owner**. Owners can do everything admins ****can do. \(In a future release, owners ****will be able to adjust the subscription and payment information.\) 

## Managing Users

Workspace owners and admins can manage users through the People view. At the top of the apps page, owners and admins will see two buttons: **Apps** and **People**. 

![The People button will display on the apps page if you are an owner or admin](../.gitbook/assets/image%20%28117%29.png)

Clicking the **People** button will open the People view. 

![The People view](../.gitbook/assets/image%20%28123%29.png)

The People view lists each workspace user as well as the number of apps the user has access to, the user's role, when the user last logged in, and when the user first signed up. You can search for users using the search bar at the top of the People view. You can sort the values in a column by clicking the column header.

### Changing a user's role

To change a user's role, click on the user's name in the list of users. A modal will open where you can select a different role for the user from a dropdown. 

![Select a new role for the user](../.gitbook/assets/image%20%28120%29.png)

{% hint style="info" %}
There must be at least one workspace owner. If a user is the only owner for the workspace, the user's role cannot be changed. 
{% endhint %}

### Changing a viewer's apps

While owners, admins, and editors can access all apps in a workspace, viewers can only view the apps they have been given access to. To modify a viewer's apps, click on the viewer's name from the list of users. A modal will open where you can modify the viewers app access.  

![Modify the viewer&apos;s app access](../.gitbook/assets/image%20%28116%29.png)

To give the viewer access to all apps in the workspace, select **All Apps**. To give the user access to specific apps in the workspace, select **Customized** and then tick the boxes for each app the viewer should have access to. 

### Deleting a user

To delete a user, hover over the user you wish to delete and select the trash can icon \(![](../.gitbook/assets/trash-alt-regular-1-.svg)\). 

![Click the trash can icon to delete the user](../.gitbook/assets/image%20%28114%29.png)

