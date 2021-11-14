const JobsList = (props) => {

    return (
        <div className="mt-2">
        {/* Display the article details if article is not None */}
        {props.jobs && props.jobs.map(job =>{
        return (

        <div >
        <h2 > { job.site } </h2>
        <p> { job.location } </p>
        <p> { job.start } </p>
        <hr/>
        </div>
    )

        })}
    </div>
    )
}

export default JobsList;