# Auto session renewal failure

Katalon Studio sessions are authenticated using refresh tokens that periodically expire for security reasons. When a refresh token expires, your session ends automatically, and you are required to relogin. This ensures account security and prevents unauthorized long-term access.

## Cause
- The refresh token used for maintaining your login session has expired.
- Tokens have a limited lifetime, after which Katalon Studio invalidates them to enforce secure authentication.
- This behavior is expected and ensures that credentials are revalidated periodically.

## Remedy

1. Acknowledge the Logout. Click **Acknowledge** on the Katalon Studio notification dialog.

    <img src= "https://tw-cdn.katalon.com/katalon-studio/troubleshooting/troubleshoot-common-exceptions/Auto_session_renewal_failure_notification.png" alt="Auto session renewal failure" width="300" />

2.  When the Relogin dialog appears, you may select either **Login with another account** and enter new credentials, or **Relogin** with your current account.

    <img src= "https://tw-cdn.katalon.com/katalon-studio/troubleshooting/troubleshoot-common-exceptions/License_expired_login_with_another_account.png" alt="Login with another account" width="300" />
