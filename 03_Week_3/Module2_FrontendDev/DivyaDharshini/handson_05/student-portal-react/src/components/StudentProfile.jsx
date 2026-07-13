import { useState, useEffect } from "react";

function StudentProfile() {

    const [name, setName] = useState("");
    const [email, setEmail] = useState("");
    const [semester, setSemester] = useState("");

    const [loading, setLoading] = useState(true);

    useEffect(() => {

        // Simulate API Call
        setTimeout(() => {

            setName("Divya Dharshini");
            setEmail("divya@example.com");
            setSemester("6");

            setLoading(false);

        }, 1000);

    }, []);

    if (loading) {

        return <h2>Loading Student Profile...</h2>;

    }

    return (

        <div
            style={{
                border: "1px solid #ddd",
                padding: "20px",
                borderRadius: "10px",
                marginTop: "30px"
            }}
        >

            <h2>Student Profile</h2>

            <br />

            <label>Name</label>

            <br />

            <input
                type="text"
                value={name}
                onChange={(e) => setName(e.target.value)}
            />

            <br /><br />

            <label>Email</label>

            <br />

            <input
                type="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
            />

            <br /><br />

            <label>Semester</label>

            <br />

            <input
                type="number"
                value={semester}
                onChange={(e) => setSemester(e.target.value)}
            />

            <hr />

            <h3>Preview</h3>

            <p>Name : {name}</p>

            <p>Email : {email}</p>

            <p>Semester : {semester}</p>

        </div>

    );

}

export default StudentProfile;











/*
import { useState } from "react";

function StudentProfile() {

    const [name, setName] = useState("");

    const [email, setEmail] = useState("");

    const [semester, setSemester] = useState("");

    return (

        <div
            style={{
                border: "1px solid #ddd",
                padding: "20px",
                borderRadius: "10px",
                marginTop: "30px"
            }}
        >

            <h2>Student Profile</h2>

            <br />

            <label>Name</label>

            <br />

            <input
                type="text"
                value={name}
                onChange={(event) => setName(event.target.value)}
                placeholder="Enter Name"
            />

            <br /><br />

            <label>Email</label>

            <br />

            <input
                type="email"
                value={email}
                onChange={(event) => setEmail(event.target.value)}
                placeholder="Enter Email"
            />

            <br /><br />

            <label>Semester</label>

            <br />

            <input
                type="number"
                value={semester}
                onChange={(event) => setSemester(event.target.value)}
                placeholder="Enter Semester"
            />

            <hr />

            <h3>Preview</h3>

            <p>Name : {name}</p>

            <p>Email : {email}</p>

            <p>Semester : {semester}</p>

        </div>

    );

}

export default StudentProfile;
*/