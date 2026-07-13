import { courses } from "./data.js";

const courseGrid = document.querySelector(".course-grid");

const totalCredits = document.getElementById("total-credits");

const loading = document.getElementById("loading");

const spinner = document.getElementById("spinner");

const postsDiv = document.getElementById("posts");

const retryBtn = document.getElementById("retryBtn");



// Render Courses

function renderCourses(courseArray){

    courseGrid.innerHTML="";

    courseArray.forEach(course=>{

        const article=document.createElement("article");

        article.className="course-card";

        article.innerHTML=`

            <h3>${course.name}</h3>

            <p>Course Code : ${course.code}</p>

            <p>Credits : ${course.credits}</p>

            <span>Grade : ${course.grade}</span>

        `;

        courseGrid.appendChild(article);

    });

    const total=courseArray.reduce(

        (sum,course)=>sum+course.credits,

        0

    );

    totalCredits.textContent=`Total Credits : ${total}`;

}



// Promise Chaining

function fetchUser(id){

    return fetch(

        `https://jsonplaceholder.typicode.com/users/${id}`

    )

    .then(response=>response.json())

    .then(user=>{

        console.log("Promise User :",user.name);

        return user;

    });

}

fetchUser(1);



// Async Await

async function fetchUserAsync(id){

    try{

        const response=await fetch(

            `https://jsonplaceholder.typicode.com/users/${id}`

        );

        const user=await response.json();

        console.log("Async User :",user.name);

    }

    catch(error){

        console.log(error);

    }

}

fetchUserAsync(2);



// Fake Delay

function fetchAllCourses(){

    return new Promise(resolve=>{

        setTimeout(()=>{

            resolve(courses);

        },1000);

    });

}



// Loading Message


loading.style.display="block";

fetchAllCourses()

.then(data=>{

    loading.style.display="none";

    renderCourses(data);

});



// Promise.all()

Promise.all([

    fetchUser(1),

    fetchUser(2)

])

.then(users=>{

    console.log(

        "Promise.all Users:",

        users[0].name,

        users[1].name

    );

});

async function apiFetch(url){

    const response = await fetch(url);

    if(!response.ok){

        throw new Error("Unable to fetch notifications.");

    }

    return response.json();

}

async function loadNotifications(){

    spinner.style.display = "block";

    postsDiv.innerHTML = "";

    retryBtn.style.display = "none";

    try{

        const posts = await apiFetch(

            "https://jsonplaceholder.typicode.com/posts?_limit=5"

        );

        spinner.style.display = "none";

        posts.forEach(post=>{

            const div = document.createElement("div");

            div.className = "notification-card";

            div.innerHTML = `
                <h3>${post.title}</h3>
                <p>${post.body}</p>
            `;

            postsDiv.appendChild(div);

        });

    }

    catch(error){

        spinner.style.display = "none";

        postsDiv.innerHTML = `
            <p class="error">${error.message}</p>
        `;

        retryBtn.style.display = "inline-block";

    }

}

loadNotifications();

retryBtn.addEventListener("click", () => {

    loadNotifications();

});

axios.interceptors.request.use(

    config => {

        console.log("API call started:", config.url);

        return config;

    }

);

async function fetchUserPosts(){

    try{

        const response = await axios.get(

            "https://jsonplaceholder.typicode.com/posts",

            {

                params:{

                    userId:1

                }

            }

        );

        console.log("User 1 Posts");

        console.log(response.data);

    }

    catch(error){

        console.log(error);

    }

}

fetchUserPosts();

/*

NOTES :

FETCH -

1. Browser API

2. Need response.json()

3. Need response.ok

AXIOS -

1. External Library

2. JSON parsed automatically

3. Throws errors automatically

*/