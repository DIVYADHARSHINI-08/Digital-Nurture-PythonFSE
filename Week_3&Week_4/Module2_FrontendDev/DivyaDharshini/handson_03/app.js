import { courses } from "./data.js";

const courseGrid = document.querySelector(".course-grid");
const totalCredits = document.getElementById("total-credits");

const searchInput = document.getElementById("search-courses");
const sortButton = document.getElementById("sort-btn");
const selectedCourse = document.getElementById("selected-course");

// Render Function
function renderCourses(courseArray){

    courseGrid.innerHTML = "";

    courseArray.forEach(course => {

        const article = document.createElement("article");

        article.className = "course-card";

        // Store id for event delegation
        article.dataset.id = course.id;

        article.innerHTML = `
            <h3>${course.name}</h3>
            <p>Course Code : ${course.code}</p>
            <p>Credits : ${course.credits}</p>
            <span>Grade : ${course.grade}</span>
        `;

        courseGrid.appendChild(article);

    });

    // Update total credits
    const total = courseArray.reduce(
        (sum, course) => sum + course.credits,
        0
    );

    totalCredits.textContent = `Total Credits : ${total}`;
}

// Initial Render
renderCourses(courses);



// Search Courses

searchInput.addEventListener("input", () => {

    const value = searchInput.value.toLowerCase();

    const filteredCourses = courses.filter(course =>

        course.name.toLowerCase().includes(value)

    );

    renderCourses(filteredCourses);

});



// Sort by Credits

sortButton.addEventListener("click", () => {

    const sortedCourses = [...courses].sort(

        (a, b) => b.credits - a.credits

    );

    renderCourses(sortedCourses);

});



// Event Delegation

courseGrid.addEventListener("click", (event) => {

    const card = event.target.closest(".course-card");

    if(!card) return;

    const id = Number(card.dataset.id);

    const course = courses.find(c => c.id === id);

    selectedCourse.innerHTML = `
        <h3>Selected Course</h3>

        <p><strong>Name:</strong> ${course.name}</p>

        <p><strong>Code:</strong> ${course.code}</p>

        <p><strong>Credits:</strong> ${course.credits}</p>

        <p><strong>Grade:</strong> ${course.grade}</p>
    `;

});