# 🚀 Canadian University of Bangladesh Hackathon 2024

*Empowering Innovation, Building the Future of Bangladesh*

## 🗓️ Important Dates

- **Registration Opens**: September 1, 2024
- **Registration Deadline**: October 15, 2024
- **Hackathon Kickoff**: November 1, 2024 (Opening Ceremony)
- **Submission Deadline**: November 3, 2024 (11:59 PM BST)
- **Final Presentations**: November 4, 2024
- **Award Ceremony**: November 5, 2024

## 🏆 Prizes & Opportunities

Winning teams will receive more than just cash prizes. Here's what's in store:

### Prize Pool (Total: ৳400,000+)
- **1st Place**: ৳200,000 + Internship Opportunities + Trophy
- **2nd Place**: ৳100,000 + Tech Gadgets
- **3rd Place**: ৳50,000 + Tech Swag
- **Best Local Solution**: ৳30,000
- **People's Choice Award**: ৳20,000

### Additional Benefits
- **Incubation Support**: Top projects may receive support from CUB's Innovation Lab
- **Mentorship**: Access to industry experts and entrepreneurs
- **Networking**: Connect with potential employers and investors
- **Media Coverage**: Feature in leading tech publications

- **1st Place**: ৳200,000 + Internship Opportunities + Trophy
- **2nd Place**: ৳100,000 + Tech Gadgets
- **3rd Place**: ৳50,000 + Tech Swag
- **Best Local Solution**: ৳30,000
- **People's Choice Award**: ৳20,000
- **Special Prizes**: Additional awards for innovation, design, and social impact

## 🤝 Partners & Sponsors

We're proud to collaborate with industry leaders who are committed to fostering innovation in Bangladesh's tech ecosystem.

### Title Sponsor
- **Robi Axiata Limited**

### Innovation Partners
- **a2i (Aspire to Innovate)**
- **Bangladesh Computer Council**

### Technology Partners
- **Google Developers Group (GDG) Bangladesh**
- **Bangladesh Open Source Network (BdOSN)**
- **Bangladesh Association of Software and Information Services (BASIS)**

### Community Partners
- **Tech for Good Bangladesh**
- **Women in Tech Bangladesh**
- **Bangladesh Open Source Network (BdOSN)**

*Interested in sponsoring? Contact us at sponsorship@cubhack2024.edu.bd*

### Platinum Sponsors
- **Grameenphone**
- **bKash**

### Gold Sponsors
- **Pathao**
- **Shohoz**

### Technology Partners
- **Google Developers Group (GDG) Bangladesh**
- **Bangladesh Open Source Network (BdOSN)**

## Challenge Questions

## Easy Level

### 1. FizzBuzz
**Problem:** Write a program that prints numbers from 1 to 100. But for multiples of 3, print "Fizz" instead of the number, and for multiples of 5, print "Buzz". For numbers that are multiples of both 3 and 5, print "FizzBuzz".

**Solution:**
```python
def fizzbuzz():
    for i in range(1, 101):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
```

### 2. Palindrome Checker
**Problem:** Write a function that checks if a given string is a palindrome (reads the same backward as forward).

**Solution:**
```python
def is_palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]
```

## Medium Level

### 3. URL Shortener
**Problem:** Design a URL shortening service. Implement a class that can convert a long URL to a short URL and back.

**Solution:**
```python
import hashlib

class URLShortener:
    def __init__(self):
        self.url_map = {}
        self.prefix = "https://short.url/"
    
    def shorten(self, long_url):
        # Create a hash of the URL
        hash_object = hashlib.md5(long_url.encode())
        short_hash = hash_object.hexdigest()[:6]
        short_url = self.prefix + short_hash
        self.url_map[short_url] = long_url
        return short_url
    
    def expand(self, short_url):
        return self.url_map.get(short_url, "URL not found")
```

### 4. Task Scheduler
**Problem:** Given a list of tasks and a cooldown period, find the minimum time required to complete all tasks with the given cooldown between identical tasks.

**Solution:**
```python
def least_interval(tasks, cooldown):
    from collections import Counter
    
    task_counts = Counter(tasks).values()
    max_count = max(task_counts)
    max_tasks = sum(1 for count in task_counts if count == max_count)
    
    return max(len(tasks), (max_count - 1) * (cooldown + 1) + max_tasks)
```

## Hard Level

### 5. Distributed Key-Value Store
**Problem:** Design a simple distributed key-value store that can handle multiple read/write operations with consistency guarantees.

**Solution Architecture:**
```python
class DistributedKVStore:
    def __init__(self, nodes):
        self.nodes = nodes  # List of node addresses
        self.data = {node: {} for node in nodes}
        self.version = 0
    
    def put(self, key, value):
        self.version += 1
        # Write to all nodes (synchronous for strong consistency)
        for node in self.nodes:
            if key not in self.data[node]:
                self.data[node][key] = {}
            self.data[node][key]['value'] = value
            self.data[node][key]['version'] = self.version
        return self.version
    
    def get(self, key):
        # Read from all nodes and return the latest version
        latest = None
        for node in self.nodes:
            if key in self.data[node]:
                if latest is None or self.data[node][key]['version'] > latest['version']:
                    latest = self.data[node][key]
        return latest['value'] if latest else None
```

### 6. Real-time Analytics Dashboard
**Problem:** Design a system that processes a stream of user events and displays real-time analytics on a dashboard.

**Solution Components:**
1. **Data Ingestion Layer**: Kafka/PubSub for event streaming
2. **Stream Processing**: Apache Flink/Spark Streaming
3. **Storage**: Time-series database (InfluxDB/TimescaleDB)
4. **API Layer**: FastAPI/Node.js for serving analytics
5. **Frontend**: React/Vue.js with WebSockets for real-time updates

**Example Implementation (Simplified):**
```python
# API Endpoint for analytics
@app.get("/api/analytics")
async def get_analytics(time_window: str = "1h"):
    # Query time-series database for metrics
    # Return aggregated data for the dashboard
    return {
        "active_users": get_active_users(time_window),
        "popular_events": get_popular_events(time_window),
        "conversion_rate": get_conversion_rate(time_window)
    }
```

## Bonus: System Design

### 7. Design Twitter
**Key Components:**
1. **Tweets Service**: Handle tweet creation, reading, and deletion
2. **User Service**: User profiles and authentication
3. **Social Graph**: Followers/following relationships
4. **News Feed**: Generate and serve timeline
5. **Media Service**: Handle image/video uploads
6. **Search**: Enable searching tweets and users

**Scaling Considerations:**
- Sharding databases by user_id
- Caching with Redis/Memcached
- CDN for static content
- Asynchronous processing for non-critical tasks

### 8. Rate Limiter
**Problem:** Implement a rate limiter that allows 100 requests per minute per user.

**Solution (Token Bucket Algorithm):**
```python
import time
from collections import defaultdict

class RateLimiter:
    def __init__(self, capacity, refill_rate):
        self.capacity = capacity  # Max tokens
        self.refill_rate = refill_rate  # tokens per second
        self.tokens = defaultdict(lambda: capacity)
        self.last_refill = defaultdict(time.time)
    
    def is_allowed(self, user_id):
        current_time = time.time()
        time_passed = current_time - self.last_refill[user_id]
        self.tokens[user_id] = min(
            self.capacity,
            self.tokens[user_id] + time_passed * self.refill_rate
        )
        self.last_refill[user_id] = current_time
        
        if self.tokens[user_id] >= 1:
            self.tokens[user_id] -= 1
            return True
        return False
```

## 🚀 About Canadian University of Bangladesh Hackathon

Welcome to the Canadian University of Bangladesh Hackathon 2024! This premier event brings together the brightest minds from across Bangladesh to solve pressing local and global challenges through innovative technology solutions. Whether you're a beginner or an experienced coder, this is your platform to innovate, collaborate, and make a real impact.

## 🎯 Local Challenges

### 1. Smart Traffic Management for Dhaka City
**Problem**: Develop an AI-powered traffic management system to reduce congestion in Dhaka.
**Focus Areas**: Real-time traffic analysis, route optimization, emergency vehicle prioritization

### 2. Flood Prediction and Early Warning System
**Problem**: Create a solution that predicts flood risks and sends early warnings to vulnerable communities.
**Focus Areas**: IoT sensors, data analytics, mobile notifications

### 3. Digital Healthcare for Rural Bangladesh
**Problem**: Build a telemedicine platform connecting rural patients with doctors in urban areas.
**Focus Areas**: Low-bandwidth optimization, multilingual support, offline functionality

### 4. Waste Management Solution
**Problem**: Develop a smart waste collection system for urban areas in Bangladesh.
**Focus Areas**: Route optimization, IoT sensors, community engagement

### 5. Agricultural Tech for Farmers
**Problem**: Create a mobile app that helps farmers with crop selection, weather predictions, and market prices.
**Focus Areas**: Local language support, offline functionality, SMS integration

## 🏅 Judging Criteria

1. **Innovation** (25%): Originality and creativity of the solution
2. **Technical Implementation** (25%): Quality of code, architecture, and technical complexity
3. **Impact** (20%): Potential real-world impact on Bangladesh
4. **User Experience** (15%): Design, usability, and accessibility
5. **Presentation** (15%): Clarity and effectiveness of the pitch

## 📝 Submission Guidelines

1. **Team Size**: 2-4 members
2. **Submission Deadline**: November 3, 2024 (11:59 PM BST)
3. **Required Materials**:
   - Source code (GitHub repository)
   - 3-minute demo video
   - Presentation slides (max 5 slides)
   - Team information
4. **Code Requirements**:
   - Must include a README with setup instructions
   - Should be well-documented
   - Must be original work created during the hackathon

## 👥 Who Can Participate?

### Eligible Participants
- University students from any discipline (undergraduate/graduate)
- Recent graduates (within 1 year of graduation)
- Professionals (as mentors or judges)

### Team Formation
- Teams of 2-4 members
- At least one team member must be from a Bangladeshi institution
- Cross-university teams are encouraged
- Teams can include members from different disciplines (e.g., developers, designers, business students)

### What to Bring
- Laptop and charger
- Valid student ID
- Any hardware you plan to use (we'll provide basic equipment)
- Your creativity and enthusiasm!

## 📍 Venue & Accommodation

### Hackathon Location
**Canadian University of Bangladesh**  
Panthapath, Dhaka 1205, Bangladesh  
[View on Google Maps](https://maps.google.com)

### Getting Here
- **By Bus**: Take any bus that goes to Panthapath or Green Road
- **By Metro**: Nearest station at Farmgate (10-minute rickshaw ride)
- **Ride-sharing**: Recommended apps: Pathao, Uber, Shohoz

### Accommodation (for outstation participants)
Special rates available at partner hotels:
- Hotel Lake Castle (5 minutes walk)
- Green House Hotel (10 minutes by rickshaw)
- Hotel Grand Park (15 minutes by car)

*Contact us for accommodation assistance at logistics@cubhack2024.edu.bd*

## 📞 Contact Us

### General Inquiries
📧 Email: hackathon2024@cub.edu.bd  
📞 Phone: +880 2-2222-64060 (10 AM - 6 PM)

### Social Media
- **Facebook**: [CUB Hackathon](https://facebook.com/cubhack)  
- **LinkedIn**: [CUB Hackathon](https://linkedin.com/company/cubhack)  
- **Instagram**: [@cubhack2024](https://instagram.com/cubhack2024)

### Office Hours
Sunday-Thursday: 9:00 AM - 5:00 PM  
Friday-Saturday: Closed

### Visit Us
Canadian University of Bangladesh  
Panthapath, Dhaka 1205  
Ground Floor, Academic Building

## 💡 Tips for Participants

1. **Understand the Problem**: Research the local context thoroughly
2. **Think Local, Build Global**: Focus on solutions that can scale beyond Bangladesh
3. **User-Centric Design**: Consider the needs of your target users
4. **Test Early, Test Often**: Get feedback from potential users
5. **Document Everything**: Keep track of your development process
6. **Prepare Your Pitch**: Practice explaining your solution clearly and concisely

## 🌟 Why Participate?

### For Students
- Solve real-world problems affecting Bangladesh
- Build your portfolio with practical projects
- Network with industry professionals
- Win exciting prizes and opportunities
- Gain hands-on experience with cutting-edge technologies

### For Sponsors
- Access to Bangladesh's brightest tech talent
- Early exposure to innovative solutions
- Brand visibility among future tech leaders
- Opportunity to recruit top performers
- Corporate social responsibility impact

### For Mentors & Judges
- Shape the future of tech in Bangladesh
- Share your expertise with passionate students
- Discover emerging talent
- Contribute to meaningful projects

## 🎉 Final Words

This is more than just a hackathon – it's a platform to transform your ideas into reality and make a lasting impact on Bangladesh's future. Whether you're a coder, designer, or entrepreneur, there's a place for you here.

**Join us in building the future of Bangladesh, one line of code at a time!**

**#CUBHack2024 #InnovateForBangladesh #TechForGood #DigitalBangladesh**

*May your code be bug-free and your dreams limitless. See you at the hackathon!* 🚀🔥

---
*Organized by Canadian University of Bangladesh in partnership with leading tech organizations across Bangladesh.*
