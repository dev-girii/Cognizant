// Import courses array using ES6 module import
import { courses } from './data.js';

console.log("=== Student Portal Dashboard - Async JS & Fetch API ===");

// --------------------------------------------------------------------------
// Step 45: Promise Chaining (.then)
// --------------------------------------------------------------------------
const fetchUserThen = (id) => {
    return fetch(`https://jsonplaceholder.typicode.com/users/${id}`)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(user => {
            console.log(`[Promise Chaining] Fetched User ID ${id} Name: ${user.name}`);
            return user;
        })
        .catch(error => {
            console.error(`[Promise Chaining] Error fetching user ID ${id}:`, error);
        });
};

// --------------------------------------------------------------------------
// Step 46: Async/Await with try/catch
// --------------------------------------------------------------------------
const fetchUser = async (id) => {
    try {
        const response = await fetch(`https://jsonplaceholder.typicode.com/users/${id}`);
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        const user = await response.json();
        console.log(`[Async/Await] Fetched User ID ${id} Name: ${user.name}`);
        return user;
    } catch (error) {
        console.error(`[Async/Await] Error fetching user ID ${id}:`, error);
        throw error;
    }
};

// ==========================================================================
// Task 2: Fetch API with Error Handling (Notifications Section)
// ==========================================================================

// 58. Add a request interceptor using axios.interceptors.request.use()
axios.interceptors.request.use(config => {
    console.log(`API call started: ${config.url}`);
    return config;
}, error => {
    return Promise.reject(error);
});

// 50. Rewrite the apiFetch function using axios.get(url)
const apiFetch = async (url) => {
    // Axios automatically checks status codes and throws, and parses JSON automatically
    const response = await axios.get(url);
    return response.data; // Axios returns parsed data in response.data
};

const notificationsContainer = document.querySelector('.notifications-container');

// Load notifications function with loading state, error display, and retry logic
const loadNotifications = async (url) => {
    if (!notificationsContainer) return;
    
    // 52. Display loading state
    notificationsContainer.innerHTML = '<div class="loading-state">Loading notifications...</div>';
    
    try {
        let posts;
        if (url.includes('/posts')) {
            // 57. Use axios.get with a params object to fetch user 1's posts
            const response = await axios.get('https://jsonplaceholder.typicode.com/posts', {
                params: { userId: 1 }
            });
            posts = response.data;
        } else {
            posts = await apiFetch(url);
        }
        // Limit to 3 notifications for clean dashboard presentation
        const displayPosts = posts.slice(0, 3);
        
        notificationsContainer.innerHTML = '';
        const fragment = document.createDocumentFragment();
        
        // Realistic academic alert templates
        const notificationTemplates = [
            {
                title: "🏆 Annual Campus Hackathon 2026",
                body: "Register now for the 48-hour coding sprint! Exciting cash prizes, internships, and mentorship opportunities await all participants."
            },
            {
                title: "📅 Upcoming Cultural Festival",
                body: "Join us for the annual spring fest this Friday! Live music, food stalls, art exhibitions, and interactive games await."
            },
            {
                title: "📝 Mid-Term Exam Schedule Released",
                body: "The official mid-term exam schedule is now live. Please review your student dashboard for exam dates, times, and assigned rooms."
            }
        ];
        
        // 51. Render dynamically from API data mapped to realistic templates
        displayPosts.forEach((post, index) => {
            const template = notificationTemplates[index] || { title: post.title, body: post.body };
            const card = document.createElement('div');
            card.className = 'notification-card';
            card.innerHTML = `
                <h4>${template.title}</h4>
                <p>${template.body}</p>
            `;
            fragment.appendChild(card);
        });
        
        notificationsContainer.appendChild(fragment);
        console.log("Successfully rendered notifications from API.");
    } catch (error) {
        console.error("Error loading notifications:", error);
        
        // 53. Display user-friendly error message
        // 54. Add a Retry button to recovery flow
        notificationsContainer.innerHTML = `
            <div class="error-container">
                <span class="error-message">⚠️ Error: Unable to fetch campus notifications. (${error.message})</span>
                <button type="button" class="btn-retry" id="retry-notifications">Retry Loading</button>
            </div>
        `;
        
        const retryBtn = document.getElementById('retry-notifications');
        if (retryBtn) {
            retryBtn.addEventListener('click', () => {
                console.log("Retrying fetch with valid URL...");
                // Retry loads successfully from correct endpoint
                loadNotifications('https://jsonplaceholder.typicode.com/posts');
            });
        }
    }
};

// Initial run: trigger simulated 404 error using nonexistent URL
loadNotifications('https://jsonplaceholder.typicode.com/nonexistent');


// --------------------------------------------------------------------------
// Step 47: Simulate 1-second Network Delay
// --------------------------------------------------------------------------
const fetchAllCourses = () => {
    return new Promise(resolve => {
        setTimeout(() => {
            resolve(courses);
        }, 1000);
    });
};

// --------------------------------------------------------------------------
// Step 49: Demonstrate Promise.all()
// --------------------------------------------------------------------------
const fetchUsersSimultaneously = () => {
    console.log("[Promise.all] Starting simultaneous fetches for User 1 and User 2...");
    Promise.all([
        fetch('https://jsonplaceholder.typicode.com/users/1').then(r => r.json()),
        fetch('https://jsonplaceholder.typicode.com/users/2').then(r => r.json())
    ])
    .then(([user1, user2]) => {
        console.log(`[Promise.all] Completed. User 1: "${user1.name}", User 2: "${user2.name}"`);
    })
    .catch(error => {
        console.error("[Promise.all] Error fetching users:", error);
    });
};

// --------------------------------------------------------------------------
// DOM Rendering & Setup (Interactivity from Hands-On 3)
// --------------------------------------------------------------------------
const courseGrid = document.querySelector('.course-grid');
const totalCreditsEl = document.getElementById('total-credits');
const selectedDiv = document.getElementById('selectedcourse');

const renderCourses = (coursesToRender) => {
    if (!courseGrid) return;
    courseGrid.innerHTML = '';
    const fragment = document.createDocumentFragment();
    
    coursesToRender.forEach(course => {
        const { id, name, code, credits, description } = course;
        const article = document.createElement('article');
        article.className = 'course-card';
        article.dataset.id = id;
        
        article.innerHTML = `
            <div class="course-header">
                <h3>${name}</h3>
                <span class="course-tag">${code}</span>
            </div>
            <p>${description}</p>
            <div class="course-footer">
                <span class="credits">${credits} Credits</span>
            </div>
        `;
        fragment.appendChild(article);
    });
    courseGrid.appendChild(fragment);
};

// --------------------------------------------------------------------------
// Step 48: Call fetchAllCourses() and Manage Loading State
// --------------------------------------------------------------------------
const initializeCourses = () => {
    if (courseGrid) {
        // Show Loading message
        courseGrid.innerHTML = '<div class="loading-state">Loading courses...</div>';
    }
    
    fetchAllCourses().then(data => {
        // Render dynamically after 1-second delay resolves
        renderCourses(data);
        
        // Calculate and update dynamic total credits
        const total = data.reduce((acc, c) => acc + c.credits, 0);
        if (totalCreditsEl) {
            totalCreditsEl.textContent = `Total Enrolled Credits: ${total}`;
        }
    });
};

// Run initialization triggers
initializeCourses();

// Trigger user fetch demonstrations
fetchUserThen(1);
fetchUser(2);
fetchUsersSimultaneously();

// Register Interactivity Event Listeners
const searchInput = document.getElementById('search-courses');
if (searchInput) {
    searchInput.addEventListener('input', (event) => {
        const query = event.target.value.toLowerCase().trim();
        const filtered = courses.filter(course => course.name.toLowerCase().includes(query));
        renderCourses(filtered);
    });
}

const sortButton = document.getElementById('sort-credits');
if (sortButton) {
    sortButton.addEventListener('click', () => {
        const sorted = [...courses].sort((a, b) => b.credits - a.credits);
        renderCourses(sorted);
    });
}

if (courseGrid) {
    courseGrid.addEventListener('click', (event) => {
        const card = event.target.closest('.course-card');
        if (card) {
            const courseId = parseInt(card.dataset.id, 10);
            const course = courses.find(c => c.id === courseId);
            if (course && selectedDiv) {
                selectedDiv.innerHTML = `<strong>Selected:</strong> ${course.name} (${course.code}) — Grade Earned: <strong>${course.grade}</strong>`;
                selectedDiv.style.display = 'block';
            }
        }
    });
}

/*
==========================================================================
Step 59: Comparison - Fetch API vs Axios (Side-by-Side differences)
==========================================================================
1. JSON Parsing:
   - Fetch: Requires manual parsing of the response body via `response.json()`.
   - Axios: Automatically parses the response JSON and returns it in the `.data` property.

2. Error Handling (HTTP Status Codes):
   - Fetch: Resolves the promise even on HTTP error status codes (like 404 or 500) and only rejects on network errors. You must check `response.ok` manually.
   - Axios: Rejects the promise automatically for any status code outside the 2xx range (e.g. 404, 500), making error handling more straightforward.

3. Interceptors & Request Cancellation:
   - Fetch: Does not have built-in request/response interceptors or easy request timeout features out of the box (requires AbortController).
   - Axios: Provides built-in request/response interceptors (`axios.interceptors`) and simple timeout options (`{ timeout: 5000 }`).
==========================================================================
*/
