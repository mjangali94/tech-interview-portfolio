import React from "react"
import UserInfo from './UserInfo'
import GetProgram from './GetProgram'
export default function Main(){
    const [info, setInfo] =React.useState()
    const [infoEntered, setInfoEntered] =React.useState(false)
    function setUserInfo(formData){
        const gender = formData.get("gender")
        const calories = formData.get("calories")
        const exerciseInterests = formData.getAll("exercise_interests")

        setInfo({
                gender:gender,
                calories:calories,
                exerciseInterests:exerciseInterests
            })
        console.log(info)
        setInfoEntered(true)
        }
    return (
        <>
            <form action={setUserInfo}>
                <select name="gender" id="gender">
                    <option>male</option>
                    <option>female</option>
                </select>
                <input name="calories" id="calories" placeholder="enter your calories received"/>

                <label><input type="checkbox" name="exercise_interests" value="running" /> Running</label><br/>
                <label><input type="checkbox" name="exercise_interests" value="swimming" /> Swimming</label><br/>
                <label><input type="checkbox" name="exercise_interests" value="cycling" /> Cycling</label><br/>

                <input type="submit" name="submit" />
            </form>

            {infoEntered && <UserInfo info={info}/>}
            {infoEntered && <GetProgram info={info}/>}

        </>
        );
    }