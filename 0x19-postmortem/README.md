### **Issue Summary:** 

#### **Duration:** 
The outage lasted 4 hours, from 10:00 PM to 2:00 AM (UTC-5) on March 5th, 2024. 
 
#### **Impact:** 
The outage mainly affected our mobile app, resulting in a significant decrease of 70% in user activity during that time. 

#### **Root Cause:**
The outage was caused by a mistake in setting up the load balancer, which caused an overload on one of the servers that handle the app's requests.

### **Incident Timeline:** 

     10:00 PM ────────────────── Automated alerts detected a sharp increase in server response times.
         │
         │
    10:15 PM ────────────────── Engineering investigated, suspecting network issues. 
         │
         │
    11:00 PM ────────────────── Potential DDoS attack considered, security team notified. 
         │
         │
    11:30 PM ────────────────── Investigation revealed excessive traffic being routed to a specific backend server.
         │
         │
    12:00 AM ────────────────── Senior engineers and DevOps intervened for urgent resolution. 
         │
         │
    1:30 AM ─────────────────── Load balancer settings adjusted to distribute traffic more evenly.
         │
         │
    2:00 AM ─────────────────── Service fully restored


### **Root Cause and Fix:** 

The issue was caused by a misconfiguration in the load balancer settings, resulting in traffic being unevenly distributed to backend servers. 

This led to overload on one server, disrupting service functionality. 

The issue was resolved by correcting the load balancer settings to evenly distribute traffic, restoring normal service operation.
   
### **Corrective and Preventative Steps:** 
   
#### **Improvements:** 

The load balancer monitoring system will be improved to detect misconfigurations more quickly. 
    
#### **Tasks:** 
     
Implement automated validation of load balancer configurations. 
      
Perform regular audits of the load balancer to ensure optimal performance. 
       
Provide additional training on best practices for managing load balancers to the operations team.

