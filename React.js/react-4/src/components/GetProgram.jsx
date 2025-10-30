export default function GetProgram(props){

    function getProgram(){
        console.log(props)
        }
    return(
            <>
            <h3>Click the button to get your program from AI!</h3>
            <button onClick={getProgram} name="getProgram" >Get your program</button>
            <div>
                here is your program:

                </div>
            </>
        );
    }