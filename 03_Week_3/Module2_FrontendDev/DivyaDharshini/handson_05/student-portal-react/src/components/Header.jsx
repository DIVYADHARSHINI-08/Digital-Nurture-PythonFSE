function Header(props) {

    return (

        <header
            style={{
                background: "#1e3a8a",
                color: "white",
                padding: "20px",
                display: "flex",
                justifyContent: "space-between",
                alignItems: "center",
            }}
        >

            <div>

                <h2>{props.siteName}</h2>

                <p>
                    Enrolled Courses : {props.enrolledCount}
                </p>

            </div>

            <nav>

                <a
                    href="#"
                    style={{ color: "white", marginRight: "20px" }}
                >
                    Home
                </a>

                <a
                    href="#"
                    style={{ color: "white", marginRight: "20px" }}
                >
                    Courses
                </a>

                <a
                    href="#"
                    style={{ color: "white", marginRight: "20px" }}
                >
                    Profile
                </a>

                <a
                    href="#"
                    style={{ color: "white" }}
                >
                    Grades
                </a>

            </nav>

        </header>

    );

}

export default Header;