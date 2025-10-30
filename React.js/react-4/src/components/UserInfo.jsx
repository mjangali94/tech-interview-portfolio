function exerciseList(exercises){
    console.log(exercises)
    return(
        exercises.map(e => (
             <li key={e}>{e}</li>
            ))
        );
    }

export default function UserInfo(props){
    return(
            <div>
                 <ul>
                     <li>gender : {props.info.gender}
                         </li>
                     <li>calories received : {props.info.calories}
                         </li>
                     <li><ul>exercise type : {exerciseList(props.info.exerciseInterests)}
                                                          </ul></li>
                     </ul>
             </div>
        );
    }