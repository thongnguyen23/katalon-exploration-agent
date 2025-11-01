# Session has been terminated: Your account has been logged in on another machine

When you log in to Katalon Studio using a license on one machine and then attempt to use the same license on another machine, the first session is automatically terminated. This prevents simultaneous use of the same license across multiple environments.

## Cause
- Katalon Studio licenses are designed for one active session at a time.
- If the same account and license are used to log in from another machine, the current session is logged out automatically.
- This behavior ensures compliance with license agreements and prevents license conflicts.

## Remedy
1. Acknowledge the Logout. Click **Acknowledge** on the Katalon Studio notification dialog.

    <img src= "https://tw-cdn.katalon.com/katalon-studio/troubleshooting/troubleshoot-common-exceptions/Acknowledge_logout_due_to_login_in_another_machine.png" alt="New Katalon Studio Onboarding" width="300" />

2. When the Relogin dialog appears, you may select one of the following options:
    - **Login with another account** and enter new credentials.

    <img src= "https://tw-cdn.katalon.com/katalon-studio/troubleshooting/troubleshoot-common-exceptions/License_expired_login_with_another_account.png" alt="Login with another account" width="300" />

    - **Relogin** signs you back in using the same method as your initial login (either Login with Browser or License Server) to restore your session.

    <img src= "https://tw-cdn.katalon.com/katalon-studio/troubleshooting/troubleshoot-common-exceptions/License_expired_relogin.png" alt="Relogin" width="300" />
