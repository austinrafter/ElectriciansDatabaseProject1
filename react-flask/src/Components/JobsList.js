const JobsList = (props) => {

    return (
        <div className="mt-2">
        {/* Display the article details if article is not None */}
        {props.jobs && props.jobs.map(job =>{
        return (

        <div key= {job.id}>
        <Button variant="text-primary" size="lg"> { job.site_name} </Button>{' '}
        <p> { job.location } </p>
        <p> { job.start_date } </p>
        <hr/>
        </div>
    )

        })}
    </div>
    )
}

export default JobsList;