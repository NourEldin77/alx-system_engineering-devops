## Postmortem Report

### Issue Summary

**Duration of the Outage:**  
Start: June 23, 2024, 14:00 UTC  
End: June 23, 2024, 18:00 UTC  

**Impact:**  
The website was completely down, with 100% of users unable to access the service. Users encountered 500 Internal Server Error messages. Approximately 80% of our user base reported issues via support channels.

**Root Cause:**  
A critical PHP file was mistakenly saved with the wrong extension (.phpp instead of .php), causing the server to fail in loading a key component of the application.

### Timeline

- **14:00 UTC:** Issue detected by monitoring alert indicating 500 Internal Server Error messages.
- **14:05 UTC:** On-call engineer notified and began investigation.
- **14:15 UTC:** Suspected recent deployment issue; initiated rollback.
- **14:30 UTC:** Rollback completed; issue persisted; escalated to backend engineering team.
- **16:00 UTC:** Identified wrong file extension (.phpp); corrected to .php and redeployed.
- **16:30 UTC:** Monitoring confirmed web service restored.
- **18:00 UTC:** Continuous monitoring showed stable operations; declared issue resolved.

### Root Cause and Resolution

**Root Cause:**  
A key PHP file essential for the authentication service was mistakenly saved with a .phpp extension instead of .php. This typo caused the server to fail in loading this critical component, resulting in 500 Internal Server Error messages across the site.

**Resolution:**  
The issue was resolved by identifying the incorrect file extension during a detailed file system inspection. The file extension was corrected from .phpp to .php. The corrected file was then redeployed to the server, restoring the web service functionality.

### Corrective and Preventative Measures

**Improvements/Fixes:**

1. **Code Review Process:** Strengthen the code review process to catch such errors before deployment.
2. **Pre-Deployment Checks:** Implement automated pre-deployment checks to verify file extensions and configurations.
3. **Enhanced Monitoring:** Improve monitoring to detect specific issues related to file loading errors.

