# Adding users to Azure Active Directory

## Scenario 

You have been tasked with adding a new user to your organisation's Azure Active Directory so that they can access the resources in your organisation.

## Prerequisites

To complete this scenario, you need the following:

- A role that allows you to create users in your tenant directory, such as the Global Administrator role or a limited administrator directory role (for example, Guest inviter or User administrator).

- Access to a valid email address outside of your Azure Active Directory tenant, such as a separate work, school, or social email address. You will use this email to create the guest account in your tenant directory and to access the invitation.

## Add a new guest user in Azure Active Directory

1. Sign in to the [Azure portal](https://portal.azure.com/) with an account that's been assigned the Global administrator, Guest, Inviter, or User administrator role.

2. Under Azure services, select Azure Active Directory (or use the search box to find and select Azure Active Directory).
    
    ![Azure AD]( /learn/operator_learn_track/access_control/authentication/adding_user_in_azure_ad/azure_ad.png)
    
3. Under Manage, select Users.
    
    ![Azure AD User](/learn/operator_learn_track/access_control/authentication/adding_user_in_azure_ad/users.png)
    
4. Under New user, select Invite external user.
    
    ![External User](/learn/operator_learn_track/access_control/authentication/adding_user_in_azure_ad/external_users.png)
    
5. On the New user page, select Invite user and then add the guest user's information.
    - **Name**: The first and last name of the guest user.
    - **Email address (required)**: The email address of the guest user.
    - **Personal message (optional)**: Include a personal welcome message to the guest user.
    - **Groups**: You can add the guest user to one or more existing groups, or you can do it later.
    - **Roles**: If you require Azure Active Directory administrative permissions for the user, you can add them to an Azure AD role.
    
    ![User Form](/learn/operator_learn_track/access_control/authentication/adding_user_in_azure_ad/new_user_form.png)
    
6. Select Invite to automatically send the invitation to the guest user. A notification appears in the upper-right corner with the message 'Successfully invited user'.

7. After you send the invitation, the user account is automatically added to the directory as a guest.
    
    ![User Added](/learn/operator_learn_track/access_control/authentication/adding_user_in_azure_ad/user_added.png)
    

## Accept the invitation

<aside class="callout">
🗣️ This needs to be done by The Modern Data Company representative.
</aside>

Now sign in as the guest user to see the invitation.

1. Sign in to your test guest user's email account.
2. In your inbox, open the email from 'Microsoft Invitations on behalf of Contoso'.
    
    ![User Added](/learn/operator_learn_track/access_control/authentication/adding_user_in_azure_ad/email_invite.png) 
    
3. In the email body, select 'Accept Invitation'. A Review permissions page opens in the browser.
    
    ![Consent Screen](/learn/operator_learn_track/access_control/authentication/adding_user_in_azure_ad/email_invite.png) 

4. Select Accept.

5. The My Apps page opens. Because we haven't assigned any apps to this guest user, you'll see the message 'There are no apps to show'.. In a real-life scenario, you would [add the guest user to an app](https://learn.microsoft.com/en-us/azure/active-directory/external-identities/add-users-administrator#add-guest-users-to-an-application), which would then appear here."
