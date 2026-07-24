// Import courses array using ES6 module import
import { courses } from './data.js';

console.log("=== Student Portal Dashboard - ES6+ Syntax Exercises ===");

// 30. Use destructuring to extract name and credits from each course in a loop
console.log("\n--- Step 30: Loop Destructuring ---");
for (const course of courses) {
    const { name, credits } = course;
    console.log(`Course: "${name}" has ${credits} credits.`);
}

// 31. Use Array.map() to format course details as a string array
console.log("\n--- Step 31: Array.map() Formatted Courses ---");
const formattedCourses = courses.map(course => `${course.code} — ${course.name} (${course.credits} credits)`);
console.log(formattedCourses);

// 32. Use Array.filter() to get courses with credits >= 4 and log the count
console.log("\n--- Step 32: Array.filter() High Credits ---");
const highCreditCourses = courses.filter(course => course.credits >= 4);
console.log(`Count of courses with credits >= 4: ${highCreditCourses.length}`);
console.log(highCreditCourses);

// 33. Use Array.reduce() to calculate total credits enrolled
console.log("\n--- Step 33: Array.reduce() Total Credits ---");
const totalCredits = courses.reduce((accumulator, course) => accumulator + course.credits, 0);
console.log(`Total credits enrolled: ${totalCredits}`);

// 34. Rewrite an existing loop as an arrow function using a template literal for string interpolation
console.log("\n--- Step 34: Arrow Function & Template Literal ---");
const displayCourseSummary = (courseList) => {
    courseList.forEach(({ code, name, grade }) => {
        // Log formatted details using a template literal
        console.log(`Course [${code}] - ${name} - Final Grade: ${grade}`);
    });
};
displayCourseSummary(courses);

// ==========================================================================
// Task 2: DOM Selection & Dynamic Rendering
// ==========================================================================

console.log("\n--- Task 2: DOM Selection & Dynamic Rendering ---");

const courseGrid = document.querySelector('.course-grid');

// Refactored helper function to dynamically render cards
const renderCourses = (coursesToRender) => {
    if (!courseGrid) return;
    
    // Clear container to avoid duplicate cards
    courseGrid.innerHTML = '';
    
    const fragment = document.createDocumentFragment();
    
    coursesToRender.forEach(course => {
        const { id, name, code, credits, description } = course;
        
        const article = document.createElement('article');
        article.className = 'course-card';
        // Set data-id attribute for event delegation
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
    console.log(`Rendered ${coursesToRender.length} course cards.`);
};

// Initial rendering of all courses
if (courseGrid) {
    renderCourses(courses);
}

// 39. Select total-credits element and update its textContent
const totalCreditsEl = document.getElementById('total-credits');
if (totalCreditsEl) {
    totalCreditsEl.textContent = `Total Enrolled Credits: ${totalCredits}`;
    console.log(`Updated dynamic total credits display to: ${totalCredits}`);
}

// ==========================================================================
// Task 3: Event Listeners & Interactivity
// ==========================================================================

console.log("\n--- Task 3: Event Listeners & Interactivity ---");

// 41. Search Input: filter courses by name on input event
const searchInput = document.getElementById('search-courses');
if (searchInput) {
    searchInput.addEventListener('input', (event) => {
        const query = event.target.value.toLowerCase().trim();
        const filtered = courses.filter(course => course.name.toLowerCase().includes(query));
        renderCourses(filtered);
    });
    console.log("Registered course search filter event listener.");
}

// 42. Sort Button: sort courses by credits descending
const sortButton = document.getElementById('sort-credits');
if (sortButton) {
    sortButton.addEventListener('click', () => {
        // Sort course array descending (creating a copy to preserve main array sequence)
        const sorted = [...courses].sort((a, b) => b.credits - a.credits);
        renderCourses(sorted);
    });
    console.log("Registered course sorting event listener.");
}

// 44. Event Delegation: single click listener on courseGrid
if (courseGrid) {
    courseGrid.addEventListener('click', (event) => {
        // Locate closest .course-card node
        const card = event.target.closest('.course-card');
        
        if (card) {
            // Retrieve course ID from dataset
            const courseId = parseInt(card.dataset.id, 10);
            const course = courses.find(c => c.id === courseId);
            
            if (course) {
                // 43. Update the selectedcourse details display container
                const selectedDiv = document.getElementById('selectedcourse');
                if (selectedDiv) {
                    selectedDiv.innerHTML = `<strong>Selected:</strong> ${course.name} (${course.code}) — Grade Earned: <strong>${course.grade}</strong>`;
                    selectedDiv.style.display = 'block';
                    console.log(`User selected course: ${course.name} (Grade: ${course.grade})`);
                }
            }
        }
    });
    console.log("Registered click delegation handler on course-grid.");
}

