import { Button } from 'react-bootstrap';

const JobsList = (props) => {

    return (
        <div className="mt-2">
        {/* Display the article details if article is not None */}
        {props.jobs && props.jobs.map(job =>{
        return (

        <div key={job.job_id} >
        <Button className="text-primary"> { job.site } </Button>
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