const WorkPackagesList = (props) => {

    return (
        <div className="mt-2">
        {/* Display the article details if article is not None */}
        {props.WORK_PACKAGE && props.WORK_PACKAGE.map(work_package =>{
        return (

        <div key= {work_package.id}>
        <Button variant="text-primary" size="lg">
        { work_package.work_package_name}
         </Button>{' '}
        <p> { work_package.price_of_work } </p>
        <p> { work_package.hours_alloted } </p>
        <p> { work_package.hours_used } </p>
        <hr/>
        </div>
    )

        })}
    </div>
    )
}

export default WorkPackagesList;