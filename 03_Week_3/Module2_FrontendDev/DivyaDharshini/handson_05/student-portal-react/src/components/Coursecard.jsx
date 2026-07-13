function CourseCard(props){

    return(

        <div style={{
            border:"1px solid #ddd",
            borderRadius:"10px",
            padding:"20px",
            width:"300px",
            margin:"20px auto",
            boxShadow:"0 4px 8px rgba(0,0,0,0.1)"
        }}>

            <h2>{props.name}</h2>

            <p>Course Code : {props.code}</p>

            <p>Credits : {props.credits}</p>

            <p>Grade : {props.grade}</p>

            <button
                onClick={() => props.onEnroll(props)}>
                Enroll
            </button>

        </div>

    );

}

export default CourseCard;